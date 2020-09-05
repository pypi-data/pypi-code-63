# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric6/VirtualEnv/VirtualenvConfigurationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VirtualenvConfigurationDialog(object):
    def setupUi(self, VirtualenvConfigurationDialog):
        VirtualenvConfigurationDialog.setObjectName("VirtualenvConfigurationDialog")
        VirtualenvConfigurationDialog.resize(700, 654)
        VirtualenvConfigurationDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(VirtualenvConfigurationDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(VirtualenvConfigurationDialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.virtualenvButton = QtWidgets.QRadioButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.virtualenvButton.setFont(font)
        self.virtualenvButton.setText("0.0")
        self.virtualenvButton.setObjectName("virtualenvButton")
        self.gridLayout_3.addWidget(self.virtualenvButton, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.pyvenvButton = QtWidgets.QRadioButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pyvenvButton.setFont(font)
        self.pyvenvButton.setText("0.0")
        self.pyvenvButton.setObjectName("pyvenvButton")
        self.gridLayout_3.addWidget(self.pyvenvButton, 1, 0, 1, 1)
        self.condaButton = QtWidgets.QRadioButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.condaButton.setFont(font)
        self.condaButton.setText("0.0")
        self.condaButton.setObjectName("condaButton")
        self.gridLayout_3.addWidget(self.condaButton, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(VirtualenvConfigurationDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.nameEdit = E5ClearableLineEdit(VirtualenvConfigurationDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout_2.addWidget(self.nameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.venvStack = QtWidgets.QStackedWidget(VirtualenvConfigurationDialog)
        self.venvStack.setObjectName("venvStack")
        self.venvPage = QtWidgets.QWidget()
        self.venvPage.setObjectName("venvPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.venvPage)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.venvPage)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.targetDirectoryPicker = E5PathPicker(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetDirectoryPicker.sizePolicy().hasHeightForWidth())
        self.targetDirectoryPicker.setSizePolicy(sizePolicy)
        self.targetDirectoryPicker.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.targetDirectoryPicker.setObjectName("targetDirectoryPicker")
        self.gridLayout.addWidget(self.targetDirectoryPicker, 0, 1, 1, 1)
        self.extraSearchPathLabel = QtWidgets.QLabel(self.groupBox)
        self.extraSearchPathLabel.setObjectName("extraSearchPathLabel")
        self.gridLayout.addWidget(self.extraSearchPathLabel, 1, 0, 1, 1)
        self.extraSearchPathPicker = E5PathPicker(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extraSearchPathPicker.sizePolicy().hasHeightForWidth())
        self.extraSearchPathPicker.setSizePolicy(sizePolicy)
        self.extraSearchPathPicker.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.extraSearchPathPicker.setObjectName("extraSearchPathPicker")
        self.gridLayout.addWidget(self.extraSearchPathPicker, 1, 1, 1, 1)
        self.promptPrefixLabel = QtWidgets.QLabel(self.groupBox)
        self.promptPrefixLabel.setObjectName("promptPrefixLabel")
        self.gridLayout.addWidget(self.promptPrefixLabel, 2, 0, 1, 1)
        self.promptPrefixEdit = E5ClearableLineEdit(self.groupBox)
        self.promptPrefixEdit.setObjectName("promptPrefixEdit")
        self.gridLayout.addWidget(self.promptPrefixEdit, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.pythonExecPicker = E5PathPicker(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pythonExecPicker.sizePolicy().hasHeightForWidth())
        self.pythonExecPicker.setSizePolicy(sizePolicy)
        self.pythonExecPicker.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pythonExecPicker.setObjectName("pythonExecPicker")
        self.gridLayout.addWidget(self.pythonExecPicker, 3, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.venvPage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verbosityLabel = QtWidgets.QLabel(self.groupBox_2)
        self.verbosityLabel.setObjectName("verbosityLabel")
        self.horizontalLayout_3.addWidget(self.verbosityLabel)
        self.verbositySpinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.verbositySpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.verbositySpinBox.setMinimum(-1)
        self.verbositySpinBox.setMaximum(1)
        self.verbositySpinBox.setObjectName("verbositySpinBox")
        self.horizontalLayout_3.addWidget(self.verbositySpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.versionLabel = QtWidgets.QLabel(self.groupBox_2)
        self.versionLabel.setObjectName("versionLabel")
        self.horizontalLayout.addWidget(self.versionLabel)
        self.versionComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.versionComboBox.setObjectName("versionComboBox")
        self.versionComboBox.addItem("")
        self.versionComboBox.setItemText(0, "")
        self.versionComboBox.addItem("")
        self.versionComboBox.setItemText(1, "3.4")
        self.versionComboBox.addItem("")
        self.versionComboBox.setItemText(2, "3.5")
        self.versionComboBox.addItem("")
        self.versionComboBox.setItemText(3, "3.6")
        self.versionComboBox.addItem("")
        self.versionComboBox.setItemText(4, "3.7")
        self.versionComboBox.addItem("")
        self.versionComboBox.setItemText(5, "3.8")
        self.versionComboBox.addItem("")
        self.versionComboBox.setItemText(6, "3.9")
        self.horizontalLayout.addWidget(self.versionComboBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.systemCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.systemCheckBox.setObjectName("systemCheckBox")
        self.gridLayout_2.addWidget(self.systemCheckBox, 1, 0, 1, 1)
        self.unzipCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.unzipCheckBox.setChecked(True)
        self.unzipCheckBox.setObjectName("unzipCheckBox")
        self.gridLayout_2.addWidget(self.unzipCheckBox, 1, 1, 1, 1)
        self.noSetuptoolsCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.noSetuptoolsCheckBox.setObjectName("noSetuptoolsCheckBox")
        self.gridLayout_2.addWidget(self.noSetuptoolsCheckBox, 2, 0, 1, 1)
        self.noPipCcheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.noPipCcheckBox.setObjectName("noPipCcheckBox")
        self.gridLayout_2.addWidget(self.noPipCcheckBox, 2, 1, 1, 1)
        self.clearCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.clearCheckBox.setObjectName("clearCheckBox")
        self.gridLayout_2.addWidget(self.clearCheckBox, 3, 0, 1, 1)
        self.copyCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.copyCheckBox.setObjectName("copyCheckBox")
        self.gridLayout_2.addWidget(self.copyCheckBox, 3, 1, 1, 1)
        self.symlinkCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.symlinkCheckBox.setObjectName("symlinkCheckBox")
        self.gridLayout_2.addWidget(self.symlinkCheckBox, 4, 0, 1, 1)
        self.upgradeCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.upgradeCheckBox.setObjectName("upgradeCheckBox")
        self.gridLayout_2.addWidget(self.upgradeCheckBox, 4, 1, 1, 1)
        self.logCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.logCheckBox.setChecked(True)
        self.logCheckBox.setObjectName("logCheckBox")
        self.gridLayout_2.addWidget(self.logCheckBox, 5, 0, 1, 1)
        self.scriptCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.scriptCheckBox.setChecked(True)
        self.scriptCheckBox.setObjectName("scriptCheckBox")
        self.gridLayout_2.addWidget(self.scriptCheckBox, 5, 1, 1, 1)
        self.openCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.openCheckBox.setObjectName("openCheckBox")
        self.gridLayout_2.addWidget(self.openCheckBox, 6, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.venvStack.addWidget(self.venvPage)
        self.condaPage = QtWidgets.QWidget()
        self.condaPage.setObjectName("condaPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.condaPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.condaPage)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.condaNameEdit = E5ClearableLineEdit(self.groupBox_4)
        self.condaNameEdit.setObjectName("condaNameEdit")
        self.gridLayout_4.addWidget(self.condaNameEdit, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.condaTargetDirectoryPicker = E5PathPicker(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.condaTargetDirectoryPicker.sizePolicy().hasHeightForWidth())
        self.condaTargetDirectoryPicker.setSizePolicy(sizePolicy)
        self.condaTargetDirectoryPicker.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.condaTargetDirectoryPicker.setObjectName("condaTargetDirectoryPicker")
        self.gridLayout_4.addWidget(self.condaTargetDirectoryPicker, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 2, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.condaSpecialsGroup = QtWidgets.QGroupBox(self.condaPage)
        self.condaSpecialsGroup.setCheckable(True)
        self.condaSpecialsGroup.setChecked(False)
        self.condaSpecialsGroup.setObjectName("condaSpecialsGroup")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.condaSpecialsGroup)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.condaCloneButton = QtWidgets.QRadioButton(self.condaSpecialsGroup)
        self.condaCloneButton.setChecked(True)
        self.condaCloneButton.setObjectName("condaCloneButton")
        self.gridLayout_5.addWidget(self.condaCloneButton, 0, 0, 1, 1)
        self.condaRequirementsButton = QtWidgets.QRadioButton(self.condaSpecialsGroup)
        self.condaRequirementsButton.setObjectName("condaRequirementsButton")
        self.gridLayout_5.addWidget(self.condaRequirementsButton, 0, 1, 1, 1)
        self.condaCloneFrame = QtWidgets.QFrame(self.condaSpecialsGroup)
        self.condaCloneFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.condaCloneFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.condaCloneFrame.setObjectName("condaCloneFrame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.condaCloneFrame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_8 = QtWidgets.QLabel(self.condaCloneFrame)
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)
        self.condaCloneNameEdit = E5ClearableLineEdit(self.condaCloneFrame)
        self.condaCloneNameEdit.setObjectName("condaCloneNameEdit")
        self.gridLayout_7.addWidget(self.condaCloneNameEdit, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.condaCloneFrame)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 1, 0, 1, 1)
        self.condaCloneDirectoryPicker = E5PathPicker(self.condaCloneFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.condaCloneDirectoryPicker.sizePolicy().hasHeightForWidth())
        self.condaCloneDirectoryPicker.setSizePolicy(sizePolicy)
        self.condaCloneDirectoryPicker.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.condaCloneDirectoryPicker.setObjectName("condaCloneDirectoryPicker")
        self.gridLayout_7.addWidget(self.condaCloneDirectoryPicker, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.condaCloneFrame, 1, 0, 1, 1)
        self.condaRequirementsFrame = QtWidgets.QFrame(self.condaSpecialsGroup)
        self.condaRequirementsFrame.setEnabled(False)
        self.condaRequirementsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.condaRequirementsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.condaRequirementsFrame.setObjectName("condaRequirementsFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.condaRequirementsFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.condaRequirementsFilePicker = E5PathPicker(self.condaRequirementsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.condaRequirementsFilePicker.sizePolicy().hasHeightForWidth())
        self.condaRequirementsFilePicker.setSizePolicy(sizePolicy)
        self.condaRequirementsFilePicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.condaRequirementsFilePicker.setObjectName("condaRequirementsFilePicker")
        self.verticalLayout_4.addWidget(self.condaRequirementsFilePicker)
        spacerItem3 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.gridLayout_5.addWidget(self.condaRequirementsFrame, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.condaSpecialsGroup)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.condaPage)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.condaPackagesEdit = E5ClearableLineEdit(self.condaPage)
        self.condaPackagesEdit.setObjectName("condaPackagesEdit")
        self.horizontalLayout_4.addWidget(self.condaPackagesEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.condaPage)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.versionLabel_2 = QtWidgets.QLabel(self.groupBox_5)
        self.versionLabel_2.setObjectName("versionLabel_2")
        self.gridLayout_6.addWidget(self.versionLabel_2, 0, 0, 1, 1)
        self.condaPythonEdit = E5ClearableLineEdit(self.groupBox_5)
        self.condaPythonEdit.setObjectName("condaPythonEdit")
        self.gridLayout_6.addWidget(self.condaPythonEdit, 0, 1, 1, 1)
        self.condaInsecureCheckBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.condaInsecureCheckBox.setObjectName("condaInsecureCheckBox")
        self.gridLayout_6.addWidget(self.condaInsecureCheckBox, 1, 0, 1, 2)
        self.condaDryrunCheckBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.condaDryrunCheckBox.setObjectName("condaDryrunCheckBox")
        self.gridLayout_6.addWidget(self.condaDryrunCheckBox, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.venvStack.addWidget(self.condaPage)
        self.verticalLayout.addWidget(self.venvStack)
        self.buttonBox = QtWidgets.QDialogButtonBox(VirtualenvConfigurationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(VirtualenvConfigurationDialog)
        self.venvStack.setCurrentIndex(0)
        self.buttonBox.accepted.connect(VirtualenvConfigurationDialog.accept)
        self.buttonBox.rejected.connect(VirtualenvConfigurationDialog.reject)
        self.condaCloneButton.toggled['bool'].connect(self.condaCloneFrame.setEnabled)
        self.condaRequirementsButton.toggled['bool'].connect(self.condaRequirementsFrame.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(VirtualenvConfigurationDialog)
        VirtualenvConfigurationDialog.setTabOrder(self.virtualenvButton, self.pyvenvButton)
        VirtualenvConfigurationDialog.setTabOrder(self.pyvenvButton, self.condaButton)
        VirtualenvConfigurationDialog.setTabOrder(self.condaButton, self.nameEdit)
        VirtualenvConfigurationDialog.setTabOrder(self.nameEdit, self.targetDirectoryPicker)
        VirtualenvConfigurationDialog.setTabOrder(self.targetDirectoryPicker, self.extraSearchPathPicker)
        VirtualenvConfigurationDialog.setTabOrder(self.extraSearchPathPicker, self.promptPrefixEdit)
        VirtualenvConfigurationDialog.setTabOrder(self.promptPrefixEdit, self.pythonExecPicker)
        VirtualenvConfigurationDialog.setTabOrder(self.pythonExecPicker, self.verbositySpinBox)
        VirtualenvConfigurationDialog.setTabOrder(self.verbositySpinBox, self.versionComboBox)
        VirtualenvConfigurationDialog.setTabOrder(self.versionComboBox, self.systemCheckBox)
        VirtualenvConfigurationDialog.setTabOrder(self.systemCheckBox, self.unzipCheckBox)
        VirtualenvConfigurationDialog.setTabOrder(self.unzipCheckBox, self.noSetuptoolsCheckBox)
        VirtualenvConfigurationDialog.setTabOrder(self.noSetuptoolsCheckBox, self.noPipCcheckBox)
        VirtualenvConfigurationDialog.setTabOrder(self.noPipCcheckBox, self.clearCheckBox)
        VirtualenvConfigurationDialog.setTabOrder(self.clearCheckBox, self.copyCheckBox)
        VirtualenvConfigurationDialog.setTabOrder(self.copyCheckBox, self.symlinkCheckBox)
        VirtualenvConfigurationDialog.setTabOrder(self.symlinkCheckBox, self.upgradeCheckBox)
        VirtualenvConfigurationDialog.setTabOrder(self.upgradeCheckBox, self.logCheckBox)
        VirtualenvConfigurationDialog.setTabOrder(self.logCheckBox, self.scriptCheckBox)
        VirtualenvConfigurationDialog.setTabOrder(self.scriptCheckBox, self.openCheckBox)
        VirtualenvConfigurationDialog.setTabOrder(self.openCheckBox, self.condaNameEdit)
        VirtualenvConfigurationDialog.setTabOrder(self.condaNameEdit, self.condaTargetDirectoryPicker)
        VirtualenvConfigurationDialog.setTabOrder(self.condaTargetDirectoryPicker, self.condaSpecialsGroup)
        VirtualenvConfigurationDialog.setTabOrder(self.condaSpecialsGroup, self.condaCloneButton)
        VirtualenvConfigurationDialog.setTabOrder(self.condaCloneButton, self.condaCloneNameEdit)
        VirtualenvConfigurationDialog.setTabOrder(self.condaCloneNameEdit, self.condaCloneDirectoryPicker)
        VirtualenvConfigurationDialog.setTabOrder(self.condaCloneDirectoryPicker, self.condaRequirementsButton)
        VirtualenvConfigurationDialog.setTabOrder(self.condaRequirementsButton, self.condaRequirementsFilePicker)
        VirtualenvConfigurationDialog.setTabOrder(self.condaRequirementsFilePicker, self.condaPackagesEdit)
        VirtualenvConfigurationDialog.setTabOrder(self.condaPackagesEdit, self.condaPythonEdit)
        VirtualenvConfigurationDialog.setTabOrder(self.condaPythonEdit, self.condaInsecureCheckBox)
        VirtualenvConfigurationDialog.setTabOrder(self.condaInsecureCheckBox, self.condaDryrunCheckBox)

    def retranslateUi(self, VirtualenvConfigurationDialog):
        _translate = QtCore.QCoreApplication.translate
        VirtualenvConfigurationDialog.setWindowTitle(_translate("VirtualenvConfigurationDialog", "Virtual Environment Configuration"))
        self.groupBox_3.setTitle(_translate("VirtualenvConfigurationDialog", "Environment Creator"))
        self.virtualenvButton.setToolTip(_translate("VirtualenvConfigurationDialog", "Select to use \'virtualenv\'"))
        self.pyvenvButton.setToolTip(_translate("VirtualenvConfigurationDialog", "Select to use \'pyvenv\'"))
        self.condaButton.setToolTip(_translate("VirtualenvConfigurationDialog", "Select to use \'conda\'"))
        self.label_2.setText(_translate("VirtualenvConfigurationDialog", "Logical Name:"))
        self.nameEdit.setToolTip(_translate("VirtualenvConfigurationDialog", "Enter a unique name for the virtual environment"))
        self.nameEdit.setPlaceholderText(_translate("VirtualenvConfigurationDialog", "Name for the virtual environment"))
        self.groupBox.setTitle(_translate("VirtualenvConfigurationDialog", "Paths"))
        self.label.setText(_translate("VirtualenvConfigurationDialog", "Target Directory:"))
        self.targetDirectoryPicker.setToolTip(_translate("VirtualenvConfigurationDialog", "Enter the target directory for the virtual environment"))
        self.extraSearchPathLabel.setText(_translate("VirtualenvConfigurationDialog", "Extra Search Path:"))
        self.extraSearchPathPicker.setToolTip(_translate("VirtualenvConfigurationDialog", "Enter the extra search path to look for setuptools/pip"))
        self.promptPrefixLabel.setText(_translate("VirtualenvConfigurationDialog", "Prompt Prefix:"))
        self.promptPrefixEdit.setToolTip(_translate("VirtualenvConfigurationDialog", "Enter the prompt prefix for the virtual environment"))
        self.promptPrefixEdit.setPlaceholderText(_translate("VirtualenvConfigurationDialog", "Prompt prefix for the virtual environment"))
        self.label_5.setText(_translate("VirtualenvConfigurationDialog", "Python Executable:"))
        self.pythonExecPicker.setToolTip(_translate("VirtualenvConfigurationDialog", "Enter the Python interpreter for the virtual environment"))
        self.groupBox_2.setTitle(_translate("VirtualenvConfigurationDialog", "Options"))
        self.verbosityLabel.setText(_translate("VirtualenvConfigurationDialog", "Verbosity:"))
        self.verbositySpinBox.setToolTip(_translate("VirtualenvConfigurationDialog", "Select the verbosity (-1: quiet, 0: normal, 1: verbose)"))
        self.versionLabel.setText(_translate("VirtualenvConfigurationDialog", "Python Version:"))
        self.versionComboBox.setToolTip(_translate("VirtualenvConfigurationDialog", "Select the Python version (empty for current)"))
        self.systemCheckBox.setToolTip(_translate("VirtualenvConfigurationDialog", "Select to give the virtualenv access to the global site-packages"))
        self.systemCheckBox.setText(_translate("VirtualenvConfigurationDialog", "System-wide Python Packages"))
        self.unzipCheckBox.setToolTip(_translate("VirtualenvConfigurationDialog", "Select to unzip setuptools when installing it"))
        self.unzipCheckBox.setText(_translate("VirtualenvConfigurationDialog", "Unzip Setuptool to virtualenv"))
        self.noSetuptoolsCheckBox.setToolTip(_translate("VirtualenvConfigurationDialog", "Select to not install setuptools (or pip) in the new virtualenv"))
        self.noSetuptoolsCheckBox.setText(_translate("VirtualenvConfigurationDialog", "Don\'t install \'setuptool\' (or pip) in the virtualenv"))
        self.noPipCcheckBox.setToolTip(_translate("VirtualenvConfigurationDialog", "Select to not install pip in the new virtualenv"))
        self.noPipCcheckBox.setText(_translate("VirtualenvConfigurationDialog", "Don\'t install \'pip\' in the virtualenv"))
        self.clearCheckBox.setToolTip(_translate("VirtualenvConfigurationDialog", "Select to clear the target first"))
        self.clearCheckBox.setText(_translate("VirtualenvConfigurationDialog", "Clear out the target directory"))
        self.copyCheckBox.setToolTip(_translate("VirtualenvConfigurationDialog", "Select to always copy files rather than symlinking"))
        self.copyCheckBox.setText(_translate("VirtualenvConfigurationDialog", "Always copy files"))
        self.symlinkCheckBox.setToolTip(_translate("VirtualenvConfigurationDialog", "Select to use symlinks instead of copies"))
        self.symlinkCheckBox.setText(_translate("VirtualenvConfigurationDialog", "Use Symbolic Links"))
        self.upgradeCheckBox.setToolTip(_translate("VirtualenvConfigurationDialog", "Select to upgrade a virtual environment"))
        self.upgradeCheckBox.setText(_translate("VirtualenvConfigurationDialog", "Upgrade"))
        self.logCheckBox.setToolTip(_translate("VirtualenvConfigurationDialog", "Select to generate a log file in the target directory"))
        self.logCheckBox.setText(_translate("VirtualenvConfigurationDialog", "Save a log file in the target directory after creation"))
        self.scriptCheckBox.setToolTip(_translate("VirtualenvConfigurationDialog", "Select to write a shell script/batch file to regenerate the virtualenv"))
        self.scriptCheckBox.setText(_translate("VirtualenvConfigurationDialog", "Save virtualenv generation script"))
        self.openCheckBox.setToolTip(_translate("VirtualenvConfigurationDialog", "Open the newly created virtualenv in a file manager window"))
        self.openCheckBox.setText(_translate("VirtualenvConfigurationDialog", "Open target directory after creation"))
        self.groupBox_4.setTitle(_translate("VirtualenvConfigurationDialog", "Target Environment Specification"))
        self.label_3.setText(_translate("VirtualenvConfigurationDialog", "Name:"))
        self.condaNameEdit.setToolTip(_translate("VirtualenvConfigurationDialog", "Enter the name for the environment"))
        self.label_4.setText(_translate("VirtualenvConfigurationDialog", "Path:"))
        self.condaTargetDirectoryPicker.setToolTip(_translate("VirtualenvConfigurationDialog", "Enter the target directory for the conda environment"))
        self.label_6.setText(_translate("VirtualenvConfigurationDialog", "<b>Note:</b> Only one of the above entries is mandatory."))
        self.condaSpecialsGroup.setTitle(_translate("VirtualenvConfigurationDialog", "Special Operations"))
        self.condaCloneButton.setToolTip(_translate("VirtualenvConfigurationDialog", "Select to clone an environment"))
        self.condaCloneButton.setText(_translate("VirtualenvConfigurationDialog", "Clone Environment"))
        self.condaRequirementsButton.setStatusTip(_translate("VirtualenvConfigurationDialog", "Select to create the environment from a requirements file"))
        self.condaRequirementsButton.setText(_translate("VirtualenvConfigurationDialog", "from Requirements"))
        self.label_8.setText(_translate("VirtualenvConfigurationDialog", "Name:"))
        self.condaCloneNameEdit.setToolTip(_translate("VirtualenvConfigurationDialog", "Enter the name of the environment to be cloned"))
        self.label_7.setText(_translate("VirtualenvConfigurationDialog", "Path:"))
        self.condaCloneDirectoryPicker.setToolTip(_translate("VirtualenvConfigurationDialog", "Enter the directory of the environment to be cloned"))
        self.label_9.setText(_translate("VirtualenvConfigurationDialog", "Package Specs:"))
        self.condaPackagesEdit.setToolTip(_translate("VirtualenvConfigurationDialog", "Enter the package specifications for the environment"))
        self.groupBox_5.setTitle(_translate("VirtualenvConfigurationDialog", "Options"))
        self.versionLabel_2.setText(_translate("VirtualenvConfigurationDialog", "Python Version:"))
        self.condaPythonEdit.setToolTip(_translate("VirtualenvConfigurationDialog", "Enter the Python version for the environment"))
        self.condaInsecureCheckBox.setText(_translate("VirtualenvConfigurationDialog", "Allow insecure SSL connections"))
        self.condaDryrunCheckBox.setToolTip(_translate("VirtualenvConfigurationDialog", "Select to perform just a dry-run"))
        self.condaDryrunCheckBox.setText(_translate("VirtualenvConfigurationDialog", "Perform dry-run"))
from E5Gui.E5LineEdit import E5ClearableLineEdit
from E5Gui.E5PathPicker import E5PathPicker
