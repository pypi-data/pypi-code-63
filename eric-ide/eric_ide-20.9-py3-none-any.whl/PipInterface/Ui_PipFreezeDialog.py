# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric6/PipInterface/PipFreezeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PipFreezeDialog(object):
    def setupUi(self, PipFreezeDialog):
        PipFreezeDialog.setObjectName("PipFreezeDialog")
        PipFreezeDialog.resize(600, 550)
        PipFreezeDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(PipFreezeDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.localCheckBox = QtWidgets.QCheckBox(PipFreezeDialog)
        self.localCheckBox.setChecked(True)
        self.localCheckBox.setObjectName("localCheckBox")
        self.verticalLayout.addWidget(self.localCheckBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(PipFreezeDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.requirementsFilePicker = E5PathPicker(PipFreezeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.requirementsFilePicker.sizePolicy().hasHeightForWidth())
        self.requirementsFilePicker.setSizePolicy(sizePolicy)
        self.requirementsFilePicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.requirementsFilePicker.setObjectName("requirementsFilePicker")
        self.horizontalLayout.addWidget(self.requirementsFilePicker)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.saveButton = QtWidgets.QPushButton(PipFreezeDialog)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 0, 1, 1, 1)
        self.saveToButton = QtWidgets.QPushButton(PipFreezeDialog)
        self.saveToButton.setObjectName("saveToButton")
        self.gridLayout.addWidget(self.saveToButton, 1, 1, 1, 1)
        self.copyButton = QtWidgets.QPushButton(PipFreezeDialog)
        self.copyButton.setObjectName("copyButton")
        self.gridLayout.addWidget(self.copyButton, 2, 1, 1, 1)
        self.insertButton = QtWidgets.QPushButton(PipFreezeDialog)
        self.insertButton.setObjectName("insertButton")
        self.gridLayout.addWidget(self.insertButton, 3, 1, 1, 1)
        self.replaceSelectionButton = QtWidgets.QPushButton(PipFreezeDialog)
        self.replaceSelectionButton.setObjectName("replaceSelectionButton")
        self.gridLayout.addWidget(self.replaceSelectionButton, 4, 1, 1, 1)
        self.replaceAllButton = QtWidgets.QPushButton(PipFreezeDialog)
        self.replaceAllButton.setObjectName("replaceAllButton")
        self.gridLayout.addWidget(self.replaceAllButton, 5, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.requirementsEdit = QtWidgets.QPlainTextEdit(PipFreezeDialog)
        self.requirementsEdit.setTabChangesFocus(True)
        self.requirementsEdit.setObjectName("requirementsEdit")
        self.gridLayout.addWidget(self.requirementsEdit, 0, 0, 7, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(PipFreezeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PipFreezeDialog)
        self.buttonBox.accepted.connect(PipFreezeDialog.accept)
        self.buttonBox.rejected.connect(PipFreezeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PipFreezeDialog)
        PipFreezeDialog.setTabOrder(self.localCheckBox, self.requirementsFilePicker)
        PipFreezeDialog.setTabOrder(self.requirementsFilePicker, self.requirementsEdit)
        PipFreezeDialog.setTabOrder(self.requirementsEdit, self.saveButton)
        PipFreezeDialog.setTabOrder(self.saveButton, self.saveToButton)
        PipFreezeDialog.setTabOrder(self.saveToButton, self.copyButton)
        PipFreezeDialog.setTabOrder(self.copyButton, self.insertButton)
        PipFreezeDialog.setTabOrder(self.insertButton, self.replaceSelectionButton)
        PipFreezeDialog.setTabOrder(self.replaceSelectionButton, self.replaceAllButton)

    def retranslateUi(self, PipFreezeDialog):
        _translate = QtCore.QCoreApplication.translate
        PipFreezeDialog.setWindowTitle(_translate("PipFreezeDialog", "Generate Requirements"))
        PipFreezeDialog.setToolTip(_translate("PipFreezeDialog", "Replace the current selection with the requirements text"))
        self.localCheckBox.setToolTip(_translate("PipFreezeDialog", "Select to show requirements for locally-installed packages only"))
        self.localCheckBox.setText(_translate("PipFreezeDialog", "Local packages only"))
        self.label.setText(_translate("PipFreezeDialog", "Requirements File:"))
        self.saveButton.setToolTip(_translate("PipFreezeDialog", "Press to save to the requirements file"))
        self.saveButton.setText(_translate("PipFreezeDialog", "Save"))
        self.saveToButton.setToolTip(_translate("PipFreezeDialog", "Save to a new file"))
        self.saveToButton.setText(_translate("PipFreezeDialog", "Save To"))
        self.copyButton.setToolTip(_translate("PipFreezeDialog", "Copy the requirements text to the clipboard"))
        self.copyButton.setText(_translate("PipFreezeDialog", "Copy"))
        self.insertButton.setToolTip(_translate("PipFreezeDialog", "Insert the requirements text at the cursor position"))
        self.insertButton.setText(_translate("PipFreezeDialog", "Insert"))
        self.replaceSelectionButton.setText(_translate("PipFreezeDialog", "Replace Selection"))
        self.replaceAllButton.setToolTip(_translate("PipFreezeDialog", "Replace all text with the requirements text"))
        self.replaceAllButton.setText(_translate("PipFreezeDialog", "Replace All"))
from E5Gui.E5PathPicker import E5PathPicker
