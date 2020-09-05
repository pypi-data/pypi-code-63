# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric6/PluginManager/PluginDetailsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PluginDetailsDialog(object):
    def setupUi(self, PluginDetailsDialog):
        PluginDetailsDialog.setObjectName("PluginDetailsDialog")
        PluginDetailsDialog.resize(563, 479)
        PluginDetailsDialog.setSizeGripEnabled(True)
        self.gridlayout = QtWidgets.QGridLayout(PluginDetailsDialog)
        self.gridlayout.setObjectName("gridlayout")
        self.label = QtWidgets.QLabel(PluginDetailsDialog)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.moduleNameEdit = QtWidgets.QLineEdit(PluginDetailsDialog)
        self.moduleNameEdit.setReadOnly(True)
        self.moduleNameEdit.setObjectName("moduleNameEdit")
        self.gridlayout.addWidget(self.moduleNameEdit, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(PluginDetailsDialog)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.moduleFileNameEdit = QtWidgets.QLineEdit(PluginDetailsDialog)
        self.moduleFileNameEdit.setReadOnly(True)
        self.moduleFileNameEdit.setObjectName("moduleFileNameEdit")
        self.gridlayout.addWidget(self.moduleFileNameEdit, 1, 1, 1, 2)
        self.autoactivateCheckBox = QtWidgets.QCheckBox(PluginDetailsDialog)
        self.autoactivateCheckBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.autoactivateCheckBox.setObjectName("autoactivateCheckBox")
        self.gridlayout.addWidget(self.autoactivateCheckBox, 2, 0, 1, 1)
        self.activeCheckBox = QtWidgets.QCheckBox(PluginDetailsDialog)
        self.activeCheckBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.activeCheckBox.setObjectName("activeCheckBox")
        self.gridlayout.addWidget(self.activeCheckBox, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(PluginDetailsDialog)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.pluginNameEdit = QtWidgets.QLineEdit(PluginDetailsDialog)
        self.pluginNameEdit.setReadOnly(True)
        self.pluginNameEdit.setObjectName("pluginNameEdit")
        self.gridlayout.addWidget(self.pluginNameEdit, 3, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(PluginDetailsDialog)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.versionEdit = QtWidgets.QLineEdit(PluginDetailsDialog)
        self.versionEdit.setReadOnly(True)
        self.versionEdit.setObjectName("versionEdit")
        self.gridlayout.addWidget(self.versionEdit, 4, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(PluginDetailsDialog)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.authorEdit = QtWidgets.QLineEdit(PluginDetailsDialog)
        self.authorEdit.setReadOnly(True)
        self.authorEdit.setObjectName("authorEdit")
        self.gridlayout.addWidget(self.authorEdit, 5, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(PluginDetailsDialog)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.gridlayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.descriptionEdit = QtWidgets.QTextEdit(PluginDetailsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.descriptionEdit.sizePolicy().hasHeightForWidth())
        self.descriptionEdit.setSizePolicy(sizePolicy)
        self.descriptionEdit.setReadOnly(True)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.gridlayout.addWidget(self.descriptionEdit, 6, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(PluginDetailsDialog)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.gridlayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.errorEdit = QtWidgets.QTextEdit(PluginDetailsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.errorEdit.sizePolicy().hasHeightForWidth())
        self.errorEdit.setSizePolicy(sizePolicy)
        self.errorEdit.setReadOnly(True)
        self.errorEdit.setObjectName("errorEdit")
        self.gridlayout.addWidget(self.errorEdit, 7, 1, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(PluginDetailsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 8, 0, 1, 3)

        self.retranslateUi(PluginDetailsDialog)
        self.buttonBox.accepted.connect(PluginDetailsDialog.accept)
        self.buttonBox.rejected.connect(PluginDetailsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PluginDetailsDialog)
        PluginDetailsDialog.setTabOrder(self.moduleNameEdit, self.moduleFileNameEdit)
        PluginDetailsDialog.setTabOrder(self.moduleFileNameEdit, self.pluginNameEdit)
        PluginDetailsDialog.setTabOrder(self.pluginNameEdit, self.versionEdit)
        PluginDetailsDialog.setTabOrder(self.versionEdit, self.authorEdit)
        PluginDetailsDialog.setTabOrder(self.authorEdit, self.descriptionEdit)
        PluginDetailsDialog.setTabOrder(self.descriptionEdit, self.errorEdit)
        PluginDetailsDialog.setTabOrder(self.errorEdit, self.buttonBox)

    def retranslateUi(self, PluginDetailsDialog):
        _translate = QtCore.QCoreApplication.translate
        PluginDetailsDialog.setWindowTitle(_translate("PluginDetailsDialog", "Plugin Details"))
        self.label.setText(_translate("PluginDetailsDialog", "Module name:"))
        self.label_2.setText(_translate("PluginDetailsDialog", "Module filename:"))
        self.autoactivateCheckBox.setText(_translate("PluginDetailsDialog", "Autoactivate"))
        self.activeCheckBox.setText(_translate("PluginDetailsDialog", "Active"))
        self.label_3.setText(_translate("PluginDetailsDialog", "Plugin name:"))
        self.label_4.setText(_translate("PluginDetailsDialog", "Version:"))
        self.label_5.setText(_translate("PluginDetailsDialog", "Author:"))
        self.label_6.setText(_translate("PluginDetailsDialog", "Description:"))
        self.label_7.setText(_translate("PluginDetailsDialog", "Error:"))
