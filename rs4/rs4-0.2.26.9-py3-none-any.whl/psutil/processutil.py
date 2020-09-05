import os, sys

#Throws OSError exception (it will be thrown when the process is not allowed
#to switch its effective UID or GID):

def drop_privileges (uid_name = None, group_name = None, umask = 0o22):
    if os.name == "nt":
        return
    if os.getuid() != 0:
        return

    import pwd, grp
    user_name = uid_name or os.getenv("SUDO_USER") or 'nobody'
    pwnam = pwd.getpwnam(user_name)
    uid = pwnam.pw_uid
    if group_name is None:
        gid = pwnam.pw_gid
    else:
        try:
            gid = [grp.getgrgid(g).gr_gid for g in os.getgroups() if grp.getgrgid(g).gr_name == group_name][0]
        except IndexError:
            raise ValueError ('unknown group')
    os.setgroups([])
    os.setgid(gid)
    os.setuid(uid)

    old_umask = os.umask (umask)

def set_process_name (name):
    if os.name == "posix":
        from setproctitle import setproctitle
        setproctitle (name)

def is_running (pid, cmd = None):
    if cmd is None:
        cmd = os.path.split (sys.argv [0])[1]

    if os.name == "nt":
        import win32process, win32api, win32con, pywintypes
        HAS_WMI = True
        try: import wmi
        except ImportError: HAS_WMI = False

        if pid not in win32process.EnumProcesses ():
            return False

        if HAS_WMI:
            cl = [p.CommandLine for p in wmi.WMI ().Win32_Process () if p.ProcessID == pid]
            if cl and cl [0].find (cmd) != -1:
                return True
            return False

        else:
            try:
                handle = win32api.OpenProcess (win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, 0, int (pid))
                exefilename = win32process.GetModuleFileNameEx (handle, 0)
                win32process.GetStartupInfo()
                if exefilename.lower ().find ("python.exe") != -1 or exefilename.lower ().find ("cmd.exe") != -1:
                    return True
            except pywintypes.error:
                # Windows service, Access is denied
                return False

    else:
        proc = "/proc/%s/cmdline" % pid
        if not os.path.isfile (proc):
            return False

        with open (proc) as f:
            exefilename = f.read ()
        if exefilename.find (cmd) != -1:
            return True

    return False

if os.name == "nt":
    import win32pdh
    import win32process
    import win32event
    import pywintypes

    def timeout_execute (cmd, timeout = 0):
        if timeout == 0:
            timeout = win32event.INFINITE

        info  = win32process.CreateProcess(None, cmd, None, None, 0, 0, None, None, win32process.STARTUPINFO())
        subprocess = info [0]

        rc = win32event.WaitForSingleObject (subprocess, timeout)

        if rc == win32event.WAIT_FAILED:
            return -1

        if rc == win32event.WAIT_TIMEOUT:
            try:
                win32process.TerminateProcess (subprocess, 0)
            except pywintypes.error:
                return -3
            return -2

        if rc == win32event.WAIT_OBJECT_0:
            return win32process.GetExitCodeProcess(subprocess)


    def get_child_pid (cpid):
        object = 'Process'
        items, instances = win32pdh.EnumObjectItems(None, None, object,
                                                   win32pdh.PERF_DETAIL_WIZARD)
        instance_dict = {}
        for instance in instances:
            try:
                instance_dict[instance] = instance_dict[instance] + 1
            except KeyError:
                instance_dict[instance] = 0

        processinfos = []
        for instance, max_instances in list(instance_dict.items()):
            for inum in range(max_instances+1):
                processinfo = []
                hq = win32pdh.OpenQuery()
                hcs = []
                for item in ['ID Process', 'Creating Process ID']:
                    path = win32pdh.MakeCounterPath((None,object,instance,None,inum,item))
                    hcs.append(win32pdh.AddCounter(hq,path))
                win32pdh.CollectQueryData(hq)
                processinfo.append (instance[:15].strip ())
                #print "%-15s\t" % (instance[:15]),
                for hc in hcs:
                    type,val=win32pdh.GetFormattedCounterValue(hc,win32pdh.PDH_FMT_LONG)
                    processinfo.append (int (val))
                    #print "%5d" % (val),
                    win32pdh.RemoveCounter(hc)
                #print
                win32pdh.CloseQuery(hq)
                processinfos.append (tuple (processinfo))

        def recusive (cpid):
            pids = []
            for name, pid, ppid in processinfos:
                if ppid == cpid:
                    pids.append (pid)
            for pid in pids:
                pids += recusive (pid)
            return pids

        pids = recusive (cpid)
        return pids

if __name__ == "__main__":
    print(get_child_pid (3172))


