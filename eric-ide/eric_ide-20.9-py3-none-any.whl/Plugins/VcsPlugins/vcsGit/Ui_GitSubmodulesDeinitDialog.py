# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric6/Plugins/VcsPlugins/vcsGit/GitSubmodulesDeinitDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GitSubmodulesDeinitDialog(object):
    def setupUi(self, GitSubmodulesDeinitDialog):
        GitSubmodulesDeinitDialog.setObjectName("GitSubmodulesDeinitDialog")
        GitSubmodulesDeinitDialog.resize(400, 300)
        GitSubmodulesDeinitDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(GitSubmodulesDeinitDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.allCheckBox = QtWidgets.QCheckBox(GitSubmodulesDeinitDialog)
        self.allCheckBox.setObjectName("allCheckBox")
        self.verticalLayout.addWidget(self.allCheckBox)
        self.label = QtWidgets.QLabel(GitSubmodulesDeinitDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.submodulesList = QtWidgets.QListWidget(GitSubmodulesDeinitDialog)
        self.submodulesList.setAlternatingRowColors(True)
        self.submodulesList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.submodulesList.setObjectName("submodulesList")
        self.verticalLayout.addWidget(self.submodulesList)
        self.forceCheckBox = QtWidgets.QCheckBox(GitSubmodulesDeinitDialog)
        self.forceCheckBox.setObjectName("forceCheckBox")
        self.verticalLayout.addWidget(self.forceCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(GitSubmodulesDeinitDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(GitSubmodulesDeinitDialog)
        self.buttonBox.accepted.connect(GitSubmodulesDeinitDialog.accept)
        self.buttonBox.rejected.connect(GitSubmodulesDeinitDialog.reject)
        self.allCheckBox.toggled['bool'].connect(self.label.setDisabled)
        self.allCheckBox.toggled['bool'].connect(self.submodulesList.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(GitSubmodulesDeinitDialog)
        GitSubmodulesDeinitDialog.setTabOrder(self.allCheckBox, self.submodulesList)
        GitSubmodulesDeinitDialog.setTabOrder(self.submodulesList, self.forceCheckBox)

    def retranslateUi(self, GitSubmodulesDeinitDialog):
        _translate = QtCore.QCoreApplication.translate
        GitSubmodulesDeinitDialog.setWindowTitle(_translate("GitSubmodulesDeinitDialog", "Unregister Submodules"))
        self.allCheckBox.setToolTip(_translate("GitSubmodulesDeinitDialog", "Select to unregister all submodules"))
        self.allCheckBox.setText(_translate("GitSubmodulesDeinitDialog", "Unregister All Submodules"))
        self.label.setText(_translate("GitSubmodulesDeinitDialog", "Selected Submodules:"))
        self.submodulesList.setToolTip(_translate("GitSubmodulesDeinitDialog", "Select the submodules to be unregistered"))
        self.forceCheckBox.setToolTip(_translate("GitSubmodulesDeinitDialog", "Select to enforce unregistering"))
        self.forceCheckBox.setText(_translate("GitSubmodulesDeinitDialog", "Enforce Operation"))
