# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric6/Plugins/VcsPlugins/vcsGit/GitChangeRemoteUrlDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GitChangeRemoteUrlDialog(object):
    def setupUi(self, GitChangeRemoteUrlDialog):
        GitChangeRemoteUrlDialog.setObjectName("GitChangeRemoteUrlDialog")
        GitChangeRemoteUrlDialog.resize(700, 140)
        GitChangeRemoteUrlDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(GitChangeRemoteUrlDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(GitChangeRemoteUrlDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(GitChangeRemoteUrlDialog)
        self.nameEdit.setToolTip("")
        self.nameEdit.setReadOnly(True)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(GitChangeRemoteUrlDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.urlEdit = QtWidgets.QLineEdit(GitChangeRemoteUrlDialog)
        self.urlEdit.setToolTip("")
        self.urlEdit.setReadOnly(True)
        self.urlEdit.setObjectName("urlEdit")
        self.gridLayout.addWidget(self.urlEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(GitChangeRemoteUrlDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.newUrlEdit = QtWidgets.QLineEdit(GitChangeRemoteUrlDialog)
        self.newUrlEdit.setObjectName("newUrlEdit")
        self.gridLayout.addWidget(self.newUrlEdit, 2, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(GitChangeRemoteUrlDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(GitChangeRemoteUrlDialog)
        self.buttonBox.accepted.connect(GitChangeRemoteUrlDialog.accept)
        self.buttonBox.rejected.connect(GitChangeRemoteUrlDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(GitChangeRemoteUrlDialog)

    def retranslateUi(self, GitChangeRemoteUrlDialog):
        _translate = QtCore.QCoreApplication.translate
        GitChangeRemoteUrlDialog.setWindowTitle(_translate("GitChangeRemoteUrlDialog", "Git Change Remote URL"))
        self.label.setText(_translate("GitChangeRemoteUrlDialog", "Name:"))
        self.label_2.setText(_translate("GitChangeRemoteUrlDialog", "URL:"))
        self.label_3.setText(_translate("GitChangeRemoteUrlDialog", "New URL:"))
        self.newUrlEdit.setToolTip(_translate("GitChangeRemoteUrlDialog", "Enter the new remote URL"))
