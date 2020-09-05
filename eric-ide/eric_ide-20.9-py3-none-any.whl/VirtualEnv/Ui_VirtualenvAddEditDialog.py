# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric6/VirtualEnv/VirtualenvAddEditDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VirtualenvAddEditDialog(object):
    def setupUi(self, VirtualenvAddEditDialog):
        VirtualenvAddEditDialog.setObjectName("VirtualenvAddEditDialog")
        VirtualenvAddEditDialog.resize(700, 188)
        VirtualenvAddEditDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(VirtualenvAddEditDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(VirtualenvAddEditDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.execPathEdit = E5ClearableLineEdit(VirtualenvAddEditDialog)
        self.execPathEdit.setObjectName("execPathEdit")
        self.gridLayout.addWidget(self.execPathEdit, 4, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.globalCheckBox = QtWidgets.QCheckBox(VirtualenvAddEditDialog)
        self.globalCheckBox.setObjectName("globalCheckBox")
        self.horizontalLayout.addWidget(self.globalCheckBox)
        self.anacondaCheckBox = QtWidgets.QCheckBox(VirtualenvAddEditDialog)
        self.anacondaCheckBox.setObjectName("anacondaCheckBox")
        self.horizontalLayout.addWidget(self.anacondaCheckBox)
        self.remoteCheckBox = QtWidgets.QCheckBox(VirtualenvAddEditDialog)
        self.remoteCheckBox.setObjectName("remoteCheckBox")
        self.horizontalLayout.addWidget(self.remoteCheckBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(VirtualenvAddEditDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 2)
        self.pythonExecPicker = E5PathPicker(VirtualenvAddEditDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pythonExecPicker.sizePolicy().hasHeightForWidth())
        self.pythonExecPicker.setSizePolicy(sizePolicy)
        self.pythonExecPicker.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pythonExecPicker.setObjectName("pythonExecPicker")
        self.gridLayout.addWidget(self.pythonExecPicker, 2, 1, 1, 1)
        self.targetDirectoryPicker = E5PathPicker(VirtualenvAddEditDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetDirectoryPicker.sizePolicy().hasHeightForWidth())
        self.targetDirectoryPicker.setSizePolicy(sizePolicy)
        self.targetDirectoryPicker.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.targetDirectoryPicker.setObjectName("targetDirectoryPicker")
        self.gridLayout.addWidget(self.targetDirectoryPicker, 1, 1, 1, 1)
        self.nameEdit = E5ClearableLineEdit(VirtualenvAddEditDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(VirtualenvAddEditDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(VirtualenvAddEditDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(VirtualenvAddEditDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.retranslateUi(VirtualenvAddEditDialog)
        self.buttonBox.accepted.connect(VirtualenvAddEditDialog.accept)
        self.buttonBox.rejected.connect(VirtualenvAddEditDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(VirtualenvAddEditDialog)
        VirtualenvAddEditDialog.setTabOrder(self.nameEdit, self.targetDirectoryPicker)
        VirtualenvAddEditDialog.setTabOrder(self.targetDirectoryPicker, self.pythonExecPicker)
        VirtualenvAddEditDialog.setTabOrder(self.pythonExecPicker, self.globalCheckBox)
        VirtualenvAddEditDialog.setTabOrder(self.globalCheckBox, self.anacondaCheckBox)
        VirtualenvAddEditDialog.setTabOrder(self.anacondaCheckBox, self.remoteCheckBox)
        VirtualenvAddEditDialog.setTabOrder(self.remoteCheckBox, self.execPathEdit)

    def retranslateUi(self, VirtualenvAddEditDialog):
        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("VirtualenvAddEditDialog", "PATH Prefix:"))
        self.globalCheckBox.setToolTip(_translate("VirtualenvAddEditDialog", "Select,if this is a global environment (i.e. no virtual environment directory to be given)"))
        self.globalCheckBox.setWhatsThis(_translate("VirtualenvAddEditDialog", "<b>Global Environment</b>\n"
"<p>Setting this indicates, that the environment is defined globally, i.e. not user specific. Usually such environments cannot be deleted by a standard user. The respective button of the Virtual Environment Manager dialog will be disabled for these entries.</p>"))
        self.globalCheckBox.setText(_translate("VirtualenvAddEditDialog", "Global Environment"))
        self.anacondaCheckBox.setToolTip(_translate("VirtualenvAddEditDialog", "Select, if this is a Conda environment"))
        self.anacondaCheckBox.setText(_translate("VirtualenvAddEditDialog", "Conda Environment"))
        self.remoteCheckBox.setToolTip(_translate("VirtualenvAddEditDialog", "Select, if this is a remotely accessed environment"))
        self.remoteCheckBox.setText(_translate("VirtualenvAddEditDialog", "Remote Environment"))
        self.pythonExecPicker.setToolTip(_translate("VirtualenvAddEditDialog", "Enter the Python interpreter of the virtual environment"))
        self.targetDirectoryPicker.setToolTip(_translate("VirtualenvAddEditDialog", "Enter the directory of the virtual environment"))
        self.nameEdit.setToolTip(_translate("VirtualenvAddEditDialog", "Enter a unique name for the virtual environment"))
        self.label_3.setText(_translate("VirtualenvAddEditDialog", "Python Interpreter:"))
        self.label.setText(_translate("VirtualenvAddEditDialog", "Logical Name:"))
        self.label_2.setText(_translate("VirtualenvAddEditDialog", "Directory:"))
from E5Gui.E5LineEdit import E5ClearableLineEdit
from E5Gui.E5PathPicker import E5PathPicker
