# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric6/Plugins/CheckerPlugins/CodeStyleChecker/CodeStyleCodeSelectionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CodeStyleCodeSelectionDialog(object):
    def setupUi(self, CodeStyleCodeSelectionDialog):
        CodeStyleCodeSelectionDialog.setObjectName("CodeStyleCodeSelectionDialog")
        CodeStyleCodeSelectionDialog.resize(500, 400)
        CodeStyleCodeSelectionDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(CodeStyleCodeSelectionDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(CodeStyleCodeSelectionDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.codeTable = QtWidgets.QTreeWidget(CodeStyleCodeSelectionDialog)
        self.codeTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.codeTable.setAlternatingRowColors(True)
        self.codeTable.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.codeTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.codeTable.setRootIsDecorated(False)
        self.codeTable.setAllColumnsShowFocus(True)
        self.codeTable.setWordWrap(True)
        self.codeTable.setObjectName("codeTable")
        self.verticalLayout.addWidget(self.codeTable)
        self.buttonBox = QtWidgets.QDialogButtonBox(CodeStyleCodeSelectionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CodeStyleCodeSelectionDialog)
        self.buttonBox.accepted.connect(CodeStyleCodeSelectionDialog.accept)
        self.buttonBox.rejected.connect(CodeStyleCodeSelectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CodeStyleCodeSelectionDialog)
        CodeStyleCodeSelectionDialog.setTabOrder(self.codeTable, self.buttonBox)

    def retranslateUi(self, CodeStyleCodeSelectionDialog):
        _translate = QtCore.QCoreApplication.translate
        CodeStyleCodeSelectionDialog.setWindowTitle(_translate("CodeStyleCodeSelectionDialog", "Code Style Message Codes"))
        self.label.setText(_translate("CodeStyleCodeSelectionDialog", "Select the message codes from the list:"))
        self.codeTable.setToolTip(_translate("CodeStyleCodeSelectionDialog", "Select the message codes from this table"))
        self.codeTable.headerItem().setText(0, _translate("CodeStyleCodeSelectionDialog", "Code"))
        self.codeTable.headerItem().setText(1, _translate("CodeStyleCodeSelectionDialog", "Message"))
