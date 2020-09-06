#!/usr/bin/env python3
#
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
# Built on top of Unicorn emulator (www.unicorn-engine.org)

import struct
import time
from qiling.os.windows.const import *
from qiling.os.const import *
from qiling.os.windows.fncc import *
from qiling.os.windows.utils import *
from qiling.os.windows.thread import *
from qiling.os.windows.handle import *
from qiling.exception import *

dllname = 'kernel32_dll'

# BOOL GetModuleInformation(
#   HANDLE       hProcess,
#   HMODULE      hModule,
#   LPMODULEINFO lpmodinfo,
#   DWORD        cb
# );
@winsdkapi(cc=STDCALL, dllname=dllname)
def hook_K32GetModuleInformation(self, address, params):
    # TODO
    return 0
