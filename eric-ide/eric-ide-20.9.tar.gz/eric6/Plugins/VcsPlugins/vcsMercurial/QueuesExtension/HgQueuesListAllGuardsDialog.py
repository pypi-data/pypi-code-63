# -*- coding: utf-8 -*-

# Copyright (c) 2011 - 2020 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to show all guards for all patches.
"""

import os

from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QDialog, QTreeWidgetItem

from .Ui_HgQueuesListAllGuardsDialog import Ui_HgQueuesListAllGuardsDialog

import UI.PixmapCache


class HgQueuesListAllGuardsDialog(QDialog, Ui_HgQueuesListAllGuardsDialog):
    """
    Class implementing a dialog to show all guards for all patches.
    """
    def __init__(self, vcs, parent=None):
        """
        Constructor
        
        @param vcs reference to the VCS object (Hg)
        @param parent reference to the parent widget (QWidget)
        """
        super(HgQueuesListAllGuardsDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.Window)
        
        self.vcs = vcs
        self.__hgClient = vcs.getClient()
        
        self.show()
        QCoreApplication.processEvents()
    
    def start(self, path):
        """
        Public slot to start the list command.
        
        @param path name of directory to be listed (string)
        """
        dname, fname = self.vcs.splitPath(path)
        
        # find the root of the repo
        repodir = dname
        while not os.path.isdir(os.path.join(repodir, self.vcs.adminDir)):
            repodir = os.path.dirname(repodir)
            if os.path.splitdrive(repodir)[1] == os.sep:
                return
        
        args = self.vcs.initCommand("qguard")
        args.append("--list")
        
        output = self.__hgClient.runcommand(args)[0]
        
        if output:
            guardsDict = {}
            for line in output.splitlines():
                if line:
                    patchName, guards = line.strip().split(":", 1)
                    guardsDict[patchName] = guards.strip().split()
            for patchName in sorted(guardsDict.keys()):
                patchItm = QTreeWidgetItem(self.guardsTree, [patchName])
                patchItm.setExpanded(True)
                for guard in guardsDict[patchName]:
                    if guard.startswith("+"):
                        icon = UI.PixmapCache.getIcon("plus")
                        guard = guard[1:]
                    elif guard.startswith("-"):
                        icon = UI.PixmapCache.getIcon("minus")
                        guard = guard[1:]
                    else:
                        icon = None
                        guard = self.tr("Unguarded")
                    itm = QTreeWidgetItem(patchItm, [guard])
                    if icon:
                        itm.setIcon(0, icon)
        else:
            QTreeWidgetItem(self.guardsTree, [self.tr("no patches found")])
