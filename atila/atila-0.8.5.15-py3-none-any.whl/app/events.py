from functools import wraps
import os
from skitai import was as the_was
from event_bus.exceptions import EventDoesntExist
from rs4 import evbus

class Events:
    def __init__ (self):
        self.bus = evbus.EventBus ()
        self.subscribers = []
        self.events = {}

    # Events ----------------------------------------------
    def on (self, *events):
        def decorator(f):
            self.save_function_spec (f)
            for e in events:
                if self._reloading:
                    try: self.bus.remove_event (f.__name__, e)
                    except EventDoesntExist: pass
                self.bus.add_event (f, e)

            @wraps(f)
            def wrapper(*args, **kwargs):
                return f (*args, **kwargs)
            return wrapper
        return decorator

    def emit_after (self, event):
        def outer (f):
            self.save_function_spec (f)
            @wraps (f)
            def wrapper(*args, **kwargs):
                returned = f (*args, **kwargs)
                self.emit (event)
                return returned
            return wrapper
        return outer

    def emit (self, event, *args, **kargs):
        self.bus.emit (event, the_was._get (), *args, **kargs)
        [s.emit (event, the_was._get (), *args, **kargs) for s in self.subscribers]

    # Broadcating ----------------------------------------
    def on_broadcast (self, *events):
        def decorator(f):
            self.save_function_spec (f)
            for e in events:
                self.add_event (e, f)
            @wraps(f)
            def wrapper(*args, **kwargs):
                return f (*args, **kwargs)
            return wrapper
        return decorator
    # this is for model signal
    on_signal = on_broadcast

    def broadcast_after (self, event):
        def decorator (f):
            self.save_function_spec (f)
            @wraps (f)
            def wrapper(*args, **kwargs):
                returned = f (*args, **kwargs)
                the_was._get ().apps.emit (event)
                return returned
            return wrapper
        return decorator

    def add_event (self, event, f):
        try:
            del self.events [(f.__name__, event)]
        except KeyError:
            pass
        self.events [(f.__name__, event)] = f

    def commit_events_to (self, broad_bus):
        for (fname, event), f in self.events.items ():
            broad_bus.add_event (f, event)

    def remove_events (self, broad_bus):
        for (fname, event), f in self.events.items ():
            try:
                broad_bus.remove_event (fname, event)
            except EventDoesntExist:
                pass

        if self.target_bus:
            for (fname, event), f in self.events.items ():
                try:
                    self.target_bus.remove_event (fname, event)
                except EventDoesntExist:
                    pass

    def add_subscriber (self, subscriber):
        self.subscribers.append (subscriber)
