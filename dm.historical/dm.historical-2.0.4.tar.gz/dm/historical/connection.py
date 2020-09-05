# Copyright (C) 2007-2018 by Dr. Dieter Maurer, Eichendorffstr. 23, D-66386 St. Ingbert, Germany
# see "LICENSE.txt" for details
#       $Id: connection.py,v 1.4 2018/01/24 11:00:55 dieter Exp $
'''A historical connection.

It delivers state current at a given time or serial.
'''
from time import gmtime
from types import MethodType
from inspect import getargspec

from DateTime import DateTime
from ZODB.Connection import Connection
from ZODB.TimeStamp import TimeStamp
from ZODB.POSException import POSKeyError

class Connection(Connection):
  def __init__(self, baseConnection, timeOrSerial, before=False):
    '''creates a (historical) connection based on *baseConnection* that delivers state at or before *timeOrSerial*.

    *baseConnection* must be an (open) ZODB connection. Its 'db' is used
    as our 'db' as well.

    *timeOrSerial* is either a time ('DateTime' or float/int) or a serial/transactionid ('string').
    '''
    ts = None
    if isinstance(timeOrSerial, bytes): ts = TimeStamp(timeOrSerial)
    if isinstance(timeOrSerial, DateTime): timeOrSerial = timeOrSerial.timeTime()
    if isinstance(timeOrSerial, (int, float)):
      ts = TimeStamp(*(gmtime(timeOrSerial)[:5] + (timeOrSerial%60,)))
    db = baseConnection.db()
    c = super(Connection, self).__init__
    if "before" in getargspec(c).args:
      # this is a modern ZODB which directly supports historical connections
      if not before:
        # we must slightly increment "ts" as we need the state
        #   `at or before` while the connection gives us `before`.
        ts = ts.laterThan(ts)
      c(db, before=to_bytes(ts))
      self.open()
    else:
      try: super(Connection,self).__init__(); self._setDB(db)
      except TypeError:
        # maybe ZODB 3.6
        super(Connection,self).__init__(db); self._opened=True
      self._storage = _HistoricalStorageWrapper(to_bytes(ts), self._storage)


class _HistoricalStorageWrapper(object):
  '''ensure that we deliver state at or before a given serial.'''
  __base = None

  def __init__(self, serial, baseStorage, before):
    self.__base = baseStorage
    self.__serial = serial
    self.__before = before

  _is_read_only = True
  def isReadOnly(self): return True

  def load(self, oid, version):
    serial = self.__serial
    S = self.__base
    filter= before \
            and (lambda t, serial= serial: t['tid'] < serial)\
            or (lambda t, serial= serial: t['tid'] <= serial)
    if _hasSmartHistory(S):
      ts= hwrap(S.history)(oid, None, 1, filter= filter,)
    else:
      ts = HistoryFetcher(S, oid, None, last=1, filter=filter).next()
    if not ts: raise POSKeyError((oid, serial))
    oserial = ts[0]['tid']
    return S.loadSerial(oid, oserial), oserial

  def __getattr__(self, attr):
    av = getattr(self.__base, attr)
    if isinstance(av, MethodType):
      # rebind
      av = MethodType(av.im_func, self, _HistoricalStorageWrapper)
    return av
  

class HistoryFetcher:
  '''auxiliary class to incrementally fetch history.'''
  _curr= 0
  _inc= 1
  _complete= 0

  def __init__(self, storage, oid, version=None, first=0, last=None, filter=None):
    '''prepare fetching historical records for *oid* in *version*.

    Tries to find records satisfying *filter*. Records *first*
    through *last* are returned.
    '''
    S = storage
    history = hwrap(S.history)
    if _hasSmartHistory(S): self._smartHistory = history
    else: self._getRawHistory = history
    self._oid = oid
    self._version = version
    self._first = first
    self._last = last
    self._filter = _Filter(filter)

  def fetch(self):
    '''return the relevant history records.'''
    self.reset()
    n = self._last
    if n is None: n = maxint
    return self.next(n-self._first)

  def next(self,n=1):
    '''return up to n more relevant history records.'''
    l = []
    while n > 0:
      x= self._next()
      if x is None: break
      l.append(x); n -= 1
    return l

  def reset(self):
    self._bi = self._complete = self._filter.stopped = 0
    if self._buffer is None or self._last is not None or self._curr == self._first:
      return # just reset the buffer index
    del self._buffer # delete the buffer as well

  _buffer = None
  def _next(self):
    if self._complete: return
    buffer = self._buffer
    if buffer is None or self._bi >= len(buffer): buffer = self._prefetch()
    if not buffer: self._complete = 1; return
    x = buffer[self._bi]; self._bi += 1
    return x

  def _prefetch(self):
    '''prefetch history information.'''
    buffer = self._buffer
    self._bi = 0
    # if we know last, we fetch them in a single step
    last = self._last
    if last is not None:
      if buffer is not None: return # we already read everything
      self._buffer = buffer = self._fetchHistory(self._first,last)
      return buffer
    if buffer is None:
      # the first round
      curr = self._first
    else: curr = self._curr = self._curr + len(buffer)
    inc = self._inc
    buffer = self._fetchHistory(curr,curr+inc)
    self._inc <<= 1
    self._buffer = buffer
    return buffer

  def _fetchHistory(self,first,last):
    filter = self._filter
    if filter.stopped: return
    filter.setIgnore(first)
    inc = last-first
    r = self._smartHistory(self._oid, self._version,inc,filter)
    if len(r) != inc: filter.stopped= 1
    return r

  def _smartHistory(self,oid,version,size,filter):
    '''emulate a smart (i.e. filtered) history fetching for
    storages that provide only a simple one.'''
    r = [] # the result list
    if size <= 0: return r
    l = 0; h = size+filter._igncount # ATT: this is a very crude approximation -- we may do much better when we cache a bit.
    history = self._getRawHistory
    while 1:
      ts = history(oid,version,h)
      if len(ts) <= l: break
      for t in ts[l:h]:
        if filter(t):
          r.append(t)
          if len(r) >= size: return r # ATT: we may want to cache the remaining elements and how far we had to fetch ahead
      if len(ts) < h: break
      l = h; h <<= 1
    filter.stopped = 1
    return r


class _Filter:
  '''A filter ignoring an initial segment of a sequence accepted by a *baseFilter*.'''
  stopped = None
  _igncount = 0  # ignore that many events

  def __init__(self,baseFilter):
    self._base = baseFilter

  def setIgnore(self,no):
    self._igncount = no

  def __call__(self,obj):
    '''check whether *obj* should pass.'''
    base = self._base
    fd = base is None or base(obj)
    if fd:
      if self._igncount: self._igncount-= 1; return
    return fd


def _hasSmartHistory(storage):
  h = storage.history
  return "filter" in getargspec(h).args

## history wrapping
#    Modern ZODB versions have discarded the `version` parameter to `history`
#    For backward compatibility we still use it with this parameter
#    Wrap as appropriate

# Note: ZODB 3.10.5 is inconsistent with respect to this parameter
#  "BaseStorage.history" still has it. We look at "FileStorage"
#  to determine whether the parameter should be passed or not
from ZODB.FileStorage import FileStorage

if "version" in getargspec(FileStorage.history).args:
  def hwrap(history): return history
else:
  def hwrap(history):
    return lambda oid, version, *args, **kw: history(oid, *args, **kw)

def to_bytes(ts):
  """convert a `TimeStamp` to a byte string."""
  return ts.raw()
