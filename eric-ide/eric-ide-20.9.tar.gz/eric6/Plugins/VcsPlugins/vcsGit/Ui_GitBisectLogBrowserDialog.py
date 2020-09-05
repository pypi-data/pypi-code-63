# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric6/Plugins/VcsPlugins/vcsGit/GitBisectLogBrowserDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GitBisectLogBrowserDialog(object):
    def setupUi(self, GitBisectLogBrowserDialog):
        GitBisectLogBrowserDialog.setObjectName("GitBisectLogBrowserDialog")
        GitBisectLogBrowserDialog.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(GitBisectLogBrowserDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logTree = QtWidgets.QTreeWidget(GitBisectLogBrowserDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.logTree.sizePolicy().hasHeightForWidth())
        self.logTree.setSizePolicy(sizePolicy)
        self.logTree.setAlternatingRowColors(True)
        self.logTree.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.logTree.setRootIsDecorated(False)
        self.logTree.setItemsExpandable(False)
        self.logTree.setAllColumnsShowFocus(True)
        self.logTree.setObjectName("logTree")
        self.verticalLayout.addWidget(self.logTree)
        self.errorGroup = QtWidgets.QGroupBox(GitBisectLogBrowserDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorGroup.sizePolicy().hasHeightForWidth())
        self.errorGroup.setSizePolicy(sizePolicy)
        self.errorGroup.setObjectName("errorGroup")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.errorGroup)
        self.vboxlayout.setObjectName("vboxlayout")
        self.errors = QtWidgets.QTextEdit(self.errorGroup)
        self.errors.setReadOnly(True)
        self.errors.setAcceptRichText(False)
        self.errors.setObjectName("errors")
        self.vboxlayout.addWidget(self.errors)
        self.verticalLayout.addWidget(self.errorGroup)
        self.inputGroup = QtWidgets.QGroupBox(GitBisectLogBrowserDialog)
        self.inputGroup.setObjectName("inputGroup")
        self.gridlayout = QtWidgets.QGridLayout(self.inputGroup)
        self.gridlayout.setObjectName("gridlayout")
        spacerItem = QtWidgets.QSpacerItem(327, 29, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 1, 1, 1, 1)
        self.sendButton = QtWidgets.QPushButton(self.inputGroup)
        self.sendButton.setObjectName("sendButton")
        self.gridlayout.addWidget(self.sendButton, 1, 2, 1, 1)
        self.input = QtWidgets.QLineEdit(self.inputGroup)
        self.input.setObjectName("input")
        self.gridlayout.addWidget(self.input, 0, 0, 1, 3)
        self.passwordCheckBox = QtWidgets.QCheckBox(self.inputGroup)
        self.passwordCheckBox.setObjectName("passwordCheckBox")
        self.gridlayout.addWidget(self.passwordCheckBox, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.inputGroup)
        self.buttonBox = QtWidgets.QDialogButtonBox(GitBisectLogBrowserDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(GitBisectLogBrowserDialog)
        QtCore.QMetaObject.connectSlotsByName(GitBisectLogBrowserDialog)
        GitBisectLogBrowserDialog.setTabOrder(self.logTree, self.errors)
        GitBisectLogBrowserDialog.setTabOrder(self.errors, self.input)
        GitBisectLogBrowserDialog.setTabOrder(self.input, self.passwordCheckBox)
        GitBisectLogBrowserDialog.setTabOrder(self.passwordCheckBox, self.sendButton)

    def retranslateUi(self, GitBisectLogBrowserDialog):
        _translate = QtCore.QCoreApplication.translate
        GitBisectLogBrowserDialog.setWindowTitle(_translate("GitBisectLogBrowserDialog", "Git Bisect Log"))
        self.logTree.headerItem().setText(0, _translate("GitBisectLogBrowserDialog", "Commit"))
        self.logTree.headerItem().setText(1, _translate("GitBisectLogBrowserDialog", "Operation"))
        self.logTree.headerItem().setText(2, _translate("GitBisectLogBrowserDialog", "Subject"))
        self.errorGroup.setTitle(_translate("GitBisectLogBrowserDialog", "Errors"))
        self.errors.setWhatsThis(_translate("GitBisectLogBrowserDialog", "<b>Git log errors</b><p>This shows possible error messages of the git log command.</p>"))
        self.inputGroup.setTitle(_translate("GitBisectLogBrowserDialog", "Input"))
        self.sendButton.setToolTip(_translate("GitBisectLogBrowserDialog", "Press to send the input to the git process"))
        self.sendButton.setText(_translate("GitBisectLogBrowserDialog", "&Send"))
        self.sendButton.setShortcut(_translate("GitBisectLogBrowserDialog", "Alt+S"))
        self.input.setToolTip(_translate("GitBisectLogBrowserDialog", "Enter data to be sent to the git process"))
        self.passwordCheckBox.setToolTip(_translate("GitBisectLogBrowserDialog", "Select to switch the input field to password mode"))
        self.passwordCheckBox.setText(_translate("GitBisectLogBrowserDialog", "&Password Mode"))
        self.passwordCheckBox.setShortcut(_translate("GitBisectLogBrowserDialog", "Alt+P"))
