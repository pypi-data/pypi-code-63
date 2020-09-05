# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric6/Network/IRC/IrcIdentitiesEditDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IrcIdentitiesEditDialog(object):
    def setupUi(self, IrcIdentitiesEditDialog):
        IrcIdentitiesEditDialog.setObjectName("IrcIdentitiesEditDialog")
        IrcIdentitiesEditDialog.resize(650, 510)
        IrcIdentitiesEditDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(IrcIdentitiesEditDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(IrcIdentitiesEditDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.identitiesCombo = QtWidgets.QComboBox(IrcIdentitiesEditDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.identitiesCombo.sizePolicy().hasHeightForWidth())
        self.identitiesCombo.setSizePolicy(sizePolicy)
        self.identitiesCombo.setObjectName("identitiesCombo")
        self.horizontalLayout.addWidget(self.identitiesCombo)
        self.addButton = QtWidgets.QToolButton(IrcIdentitiesEditDialog)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.copyButton = QtWidgets.QToolButton(IrcIdentitiesEditDialog)
        self.copyButton.setObjectName("copyButton")
        self.horizontalLayout.addWidget(self.copyButton)
        self.renameButton = QtWidgets.QToolButton(IrcIdentitiesEditDialog)
        self.renameButton.setObjectName("renameButton")
        self.horizontalLayout.addWidget(self.renameButton)
        self.deleteButton = QtWidgets.QToolButton(IrcIdentitiesEditDialog)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.identityTabWidget = QtWidgets.QTabWidget(IrcIdentitiesEditDialog)
        self.identityTabWidget.setObjectName("identityTabWidget")
        self.generalTab = QtWidgets.QWidget()
        self.generalTab.setObjectName("generalTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.generalTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.generalTab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.realnameEdit = QtWidgets.QLineEdit(self.generalTab)
        self.realnameEdit.setObjectName("realnameEdit")
        self.gridLayout_2.addWidget(self.realnameEdit, 0, 1, 1, 1)
        self.nickNameGroup = QtWidgets.QGroupBox(self.generalTab)
        self.nickNameGroup.setObjectName("nickNameGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.nickNameGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.nicknameEdit = QtWidgets.QLineEdit(self.nickNameGroup)
        self.nicknameEdit.setObjectName("nicknameEdit")
        self.gridLayout.addWidget(self.nicknameEdit, 0, 0, 1, 2)
        self.nicknamesList = QtWidgets.QListWidget(self.nickNameGroup)
        self.nicknamesList.setAlternatingRowColors(True)
        self.nicknamesList.setObjectName("nicknamesList")
        self.gridLayout.addWidget(self.nicknamesList, 1, 0, 5, 1)
        self.nicknameAddButton = QtWidgets.QToolButton(self.nickNameGroup)
        self.nicknameAddButton.setObjectName("nicknameAddButton")
        self.gridLayout.addWidget(self.nicknameAddButton, 1, 1, 1, 1)
        self.nicknameDeleteButton = QtWidgets.QToolButton(self.nickNameGroup)
        self.nicknameDeleteButton.setText("")
        self.nicknameDeleteButton.setObjectName("nicknameDeleteButton")
        self.gridLayout.addWidget(self.nicknameDeleteButton, 2, 1, 1, 1)
        self.nicknameUpButton = QtWidgets.QToolButton(self.nickNameGroup)
        self.nicknameUpButton.setObjectName("nicknameUpButton")
        self.gridLayout.addWidget(self.nicknameUpButton, 3, 1, 1, 1)
        self.nicknameDownButton = QtWidgets.QToolButton(self.nickNameGroup)
        self.nicknameDownButton.setObjectName("nicknameDownButton")
        self.gridLayout.addWidget(self.nicknameDownButton, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 87, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.gridLayout_2.addWidget(self.nickNameGroup, 1, 0, 1, 2)
        self.autoIdentifyGroup = QtWidgets.QGroupBox(self.generalTab)
        self.autoIdentifyGroup.setObjectName("autoIdentifyGroup")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.autoIdentifyGroup)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.autoIdentifyGroup)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.serviceEdit = QtWidgets.QLineEdit(self.autoIdentifyGroup)
        self.serviceEdit.setObjectName("serviceEdit")
        self.horizontalLayout_2.addWidget(self.serviceEdit)
        self.label_4 = QtWidgets.QLabel(self.autoIdentifyGroup)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.passwordEdit = QtWidgets.QLineEdit(self.autoIdentifyGroup)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.horizontalLayout_2.addWidget(self.passwordEdit)
        self.showPasswordButton = QtWidgets.QToolButton(self.autoIdentifyGroup)
        self.showPasswordButton.setCheckable(True)
        self.showPasswordButton.setObjectName("showPasswordButton")
        self.horizontalLayout_2.addWidget(self.showPasswordButton)
        self.gridLayout_2.addWidget(self.autoIdentifyGroup, 2, 0, 1, 2)
        self.identityTabWidget.addTab(self.generalTab, "")
        self.awayTab = QtWidgets.QWidget()
        self.awayTab.setObjectName("awayTab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.awayTab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.rememberPosOnAwayCheckBox = QtWidgets.QCheckBox(self.awayTab)
        self.rememberPosOnAwayCheckBox.setWhatsThis("")
        self.rememberPosOnAwayCheckBox.setObjectName("rememberPosOnAwayCheckBox")
        self.gridLayout_5.addWidget(self.rememberPosOnAwayCheckBox, 0, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.awayTab)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)
        self.awayEdit = QtWidgets.QLineEdit(self.awayTab)
        self.awayEdit.setObjectName("awayEdit")
        self.gridLayout_5.addWidget(self.awayEdit, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 219, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 2, 1, 1, 1)
        self.identityTabWidget.addTab(self.awayTab, "")
        self.advancedTab = QtWidgets.QWidget()
        self.advancedTab.setObjectName("advancedTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.advancedTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.advancedTab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.identEdit = QtWidgets.QLineEdit(self.advancedTab)
        self.identEdit.setObjectName("identEdit")
        self.gridLayout_3.addWidget(self.identEdit, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.advancedTab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.quitEdit = QtWidgets.QLineEdit(self.advancedTab)
        self.quitEdit.setObjectName("quitEdit")
        self.gridLayout_3.addWidget(self.quitEdit, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.advancedTab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.partEdit = QtWidgets.QLineEdit(self.advancedTab)
        self.partEdit.setObjectName("partEdit")
        self.gridLayout_3.addWidget(self.partEdit, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 291, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 3, 1, 1, 1)
        self.identityTabWidget.addTab(self.advancedTab, "")
        self.verticalLayout.addWidget(self.identityTabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(IrcIdentitiesEditDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(IrcIdentitiesEditDialog)
        self.identityTabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(IrcIdentitiesEditDialog.accept)
        self.buttonBox.rejected.connect(IrcIdentitiesEditDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(IrcIdentitiesEditDialog)
        IrcIdentitiesEditDialog.setTabOrder(self.identitiesCombo, self.addButton)
        IrcIdentitiesEditDialog.setTabOrder(self.addButton, self.copyButton)
        IrcIdentitiesEditDialog.setTabOrder(self.copyButton, self.renameButton)
        IrcIdentitiesEditDialog.setTabOrder(self.renameButton, self.deleteButton)
        IrcIdentitiesEditDialog.setTabOrder(self.deleteButton, self.identityTabWidget)
        IrcIdentitiesEditDialog.setTabOrder(self.identityTabWidget, self.realnameEdit)
        IrcIdentitiesEditDialog.setTabOrder(self.realnameEdit, self.nicknameEdit)
        IrcIdentitiesEditDialog.setTabOrder(self.nicknameEdit, self.nicknamesList)
        IrcIdentitiesEditDialog.setTabOrder(self.nicknamesList, self.nicknameAddButton)
        IrcIdentitiesEditDialog.setTabOrder(self.nicknameAddButton, self.nicknameDeleteButton)
        IrcIdentitiesEditDialog.setTabOrder(self.nicknameDeleteButton, self.nicknameUpButton)
        IrcIdentitiesEditDialog.setTabOrder(self.nicknameUpButton, self.nicknameDownButton)
        IrcIdentitiesEditDialog.setTabOrder(self.nicknameDownButton, self.serviceEdit)
        IrcIdentitiesEditDialog.setTabOrder(self.serviceEdit, self.passwordEdit)
        IrcIdentitiesEditDialog.setTabOrder(self.passwordEdit, self.showPasswordButton)
        IrcIdentitiesEditDialog.setTabOrder(self.showPasswordButton, self.rememberPosOnAwayCheckBox)
        IrcIdentitiesEditDialog.setTabOrder(self.rememberPosOnAwayCheckBox, self.awayEdit)
        IrcIdentitiesEditDialog.setTabOrder(self.awayEdit, self.identEdit)
        IrcIdentitiesEditDialog.setTabOrder(self.identEdit, self.quitEdit)
        IrcIdentitiesEditDialog.setTabOrder(self.quitEdit, self.partEdit)

    def retranslateUi(self, IrcIdentitiesEditDialog):
        _translate = QtCore.QCoreApplication.translate
        IrcIdentitiesEditDialog.setWindowTitle(_translate("IrcIdentitiesEditDialog", "IRC Identities"))
        self.label.setText(_translate("IrcIdentitiesEditDialog", "Identity:"))
        self.identitiesCombo.setToolTip(_translate("IrcIdentitiesEditDialog", "Select the identity to work on"))
        self.addButton.setToolTip(_translate("IrcIdentitiesEditDialog", "Press to add a new identity"))
        self.copyButton.setToolTip(_translate("IrcIdentitiesEditDialog", "Press to copy the selected identity"))
        self.renameButton.setToolTip(_translate("IrcIdentitiesEditDialog", "Press to rename the selected identity"))
        self.deleteButton.setToolTip(_translate("IrcIdentitiesEditDialog", "Press to delete the selected identity"))
        self.label_2.setText(_translate("IrcIdentitiesEditDialog", "Real Name:"))
        self.realnameEdit.setToolTip(_translate("IrcIdentitiesEditDialog", "Enter the real name"))
        self.nickNameGroup.setTitle(_translate("IrcIdentitiesEditDialog", "Nick Names"))
        self.nicknameEdit.setToolTip(_translate("IrcIdentitiesEditDialog", "Enter a nick name to add"))
        self.nicknameAddButton.setToolTip(_translate("IrcIdentitiesEditDialog", "Press to add the entered nick name"))
        self.nicknameDeleteButton.setToolTip(_translate("IrcIdentitiesEditDialog", "Press to delete the selected nick name"))
        self.nicknameUpButton.setToolTip(_translate("IrcIdentitiesEditDialog", "Press to move the selected nick name up"))
        self.nicknameDownButton.setToolTip(_translate("IrcIdentitiesEditDialog", "Press to move the selected nick name down"))
        self.autoIdentifyGroup.setTitle(_translate("IrcIdentitiesEditDialog", "Auto Identify"))
        self.label_3.setText(_translate("IrcIdentitiesEditDialog", "Service:"))
        self.serviceEdit.setToolTip(_translate("IrcIdentitiesEditDialog", "Enter the name of the service to identify against"))
        self.serviceEdit.setWhatsThis(_translate("IrcIdentitiesEditDialog", "Service name can be <b><i>nickserv</i></b> or a network-dependent name such as <b><i>nickserv@services.dal.net</i></b>"))
        self.label_4.setText(_translate("IrcIdentitiesEditDialog", "Password:"))
        self.passwordEdit.setToolTip(_translate("IrcIdentitiesEditDialog", "Enter the password"))
        self.showPasswordButton.setToolTip(_translate("IrcIdentitiesEditDialog", "Press to show the password"))
        self.identityTabWidget.setTabText(self.identityTabWidget.indexOf(self.generalTab), _translate("IrcIdentitiesEditDialog", "General"))
        self.rememberPosOnAwayCheckBox.setToolTip(_translate("IrcIdentitiesEditDialog", "Select to mark the current position in the chat, when you send an AWAY command."))
        self.rememberPosOnAwayCheckBox.setText(_translate("IrcIdentitiesEditDialog", "Mark the current position in chat windows when going away"))
        self.label_8.setText(_translate("IrcIdentitiesEditDialog", "Away Message:"))
        self.awayEdit.setToolTip(_translate("IrcIdentitiesEditDialog", "Enter the message to be sent when going away"))
        self.identityTabWidget.setTabText(self.identityTabWidget.indexOf(self.awayTab), _translate("IrcIdentitiesEditDialog", "Away"))
        self.label_5.setText(_translate("IrcIdentitiesEditDialog", "Ident:"))
        self.identEdit.setToolTip(_translate("IrcIdentitiesEditDialog", "Enter the identity to be used to log-on to the server"))
        self.label_6.setText(_translate("IrcIdentitiesEditDialog", "Reason for Quit:"))
        self.quitEdit.setToolTip(_translate("IrcIdentitiesEditDialog", "Enter a message to be sent when quitting"))
        self.label_7.setText(_translate("IrcIdentitiesEditDialog", "Reason for Part:"))
        self.partEdit.setToolTip(_translate("IrcIdentitiesEditDialog", "Enter message to be sent when leaving a channel"))
        self.identityTabWidget.setTabText(self.identityTabWidget.indexOf(self.advancedTab), _translate("IrcIdentitiesEditDialog", "Advanced"))
