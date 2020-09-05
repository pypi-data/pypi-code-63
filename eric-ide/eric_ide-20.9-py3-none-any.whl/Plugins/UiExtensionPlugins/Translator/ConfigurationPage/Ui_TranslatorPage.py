# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric6/Plugins/UiExtensionPlugins/Translator/ConfigurationPage/TranslatorPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TranslatorPage(object):
    def setupUi(self, TranslatorPage):
        TranslatorPage.setObjectName("TranslatorPage")
        TranslatorPage.resize(500, 1125)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(TranslatorPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.headerLabel = QtWidgets.QLabel(TranslatorPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_3.addWidget(self.headerLabel)
        self.line15 = QtWidgets.QFrame(TranslatorPage)
        self.line15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line15.setObjectName("line15")
        self.verticalLayout_3.addWidget(self.line15)
        self.groupBox = QtWidgets.QGroupBox(TranslatorPage)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.languagesList = QtWidgets.QListWidget(self.groupBox)
        self.languagesList.setMinimumSize(QtCore.QSize(0, 250))
        self.languagesList.setIconSize(QtCore.QSize(22, 22))
        self.languagesList.setProperty("isWrapping", True)
        self.languagesList.setObjectName("languagesList")
        self.verticalLayout.addWidget(self.languagesList)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.setButton = QtWidgets.QPushButton(self.groupBox)
        self.setButton.setObjectName("setButton")
        self.horizontalLayout.addWidget(self.setButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.defaultButton = QtWidgets.QPushButton(self.groupBox)
        self.defaultButton.setObjectName("defaultButton")
        self.horizontalLayout.addWidget(self.defaultButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_8 = QtWidgets.QGroupBox(TranslatorPage)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox_8)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)
        self.deeplKeyEdit = QtWidgets.QLineEdit(self.groupBox_8)
        self.deeplKeyEdit.setObjectName("deeplKeyEdit")
        self.gridLayout_6.addWidget(self.deeplKeyEdit, 0, 1, 1, 1)
        self.deeplLabel = QtWidgets.QLabel(self.groupBox_8)
        self.deeplLabel.setText("")
        self.deeplLabel.setWordWrap(True)
        self.deeplLabel.setOpenExternalLinks(True)
        self.deeplLabel.setObjectName("deeplLabel")
        self.gridLayout_6.addWidget(self.deeplLabel, 1, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.groupBox_8)
        self.groupBox_2 = QtWidgets.QGroupBox(TranslatorPage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dictionaryCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.dictionaryCheckBox.setObjectName("dictionaryCheckBox")
        self.verticalLayout_2.addWidget(self.dictionaryCheckBox)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_5 = QtWidgets.QGroupBox(TranslatorPage)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.googlev2KeyEdit = QtWidgets.QLineEdit(self.groupBox_5)
        self.googlev2KeyEdit.setObjectName("googlev2KeyEdit")
        self.gridLayout_3.addWidget(self.googlev2KeyEdit, 0, 1, 1, 1)
        self.googlev2Label = QtWidgets.QLabel(self.groupBox_5)
        self.googlev2Label.setText("")
        self.googlev2Label.setWordWrap(True)
        self.googlev2Label.setOpenExternalLinks(True)
        self.googlev2Label.setObjectName("googlev2Label")
        self.gridLayout_3.addWidget(self.googlev2Label, 1, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.groupBox_7 = QtWidgets.QGroupBox(TranslatorPage)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_7)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.ibmUrlEdit = QtWidgets.QLineEdit(self.groupBox_7)
        self.ibmUrlEdit.setObjectName("ibmUrlEdit")
        self.gridLayout_5.addWidget(self.ibmUrlEdit, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_7)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 1, 0, 1, 1)
        self.ibmKeyEdit = QtWidgets.QLineEdit(self.groupBox_7)
        self.ibmKeyEdit.setObjectName("ibmKeyEdit")
        self.gridLayout_5.addWidget(self.ibmKeyEdit, 1, 1, 1, 1)
        self.ibmLabel = QtWidgets.QLabel(self.groupBox_7)
        self.ibmLabel.setText("")
        self.ibmLabel.setWordWrap(True)
        self.ibmLabel.setOpenExternalLinks(True)
        self.ibmLabel.setObjectName("ibmLabel")
        self.gridLayout_5.addWidget(self.ibmLabel, 2, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.groupBox_7)
        self.groupBox_6 = QtWidgets.QGroupBox(TranslatorPage)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_6)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.msSubscriptionKeyEdit = QtWidgets.QLineEdit(self.groupBox_6)
        self.msSubscriptionKeyEdit.setObjectName("msSubscriptionKeyEdit")
        self.gridLayout_4.addWidget(self.msSubscriptionKeyEdit, 0, 1, 1, 1)
        self.msLabel = QtWidgets.QLabel(self.groupBox_6)
        self.msLabel.setWordWrap(True)
        self.msLabel.setOpenExternalLinks(True)
        self.msLabel.setObjectName("msLabel")
        self.gridLayout_4.addWidget(self.msLabel, 1, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.groupBox_4 = QtWidgets.QGroupBox(TranslatorPage)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.mymemoryEmailEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.mymemoryEmailEdit.setObjectName("mymemoryEmailEdit")
        self.gridLayout_2.addWidget(self.mymemoryEmailEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.mymemoryKeyEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.mymemoryKeyEdit.setObjectName("mymemoryKeyEdit")
        self.gridLayout_2.addWidget(self.mymemoryKeyEdit, 1, 1, 1, 1)
        self.mymemoryLabel = QtWidgets.QLabel(self.groupBox_4)
        self.mymemoryLabel.setText("")
        self.mymemoryLabel.setWordWrap(True)
        self.mymemoryLabel.setOpenExternalLinks(True)
        self.mymemoryLabel.setObjectName("mymemoryLabel")
        self.gridLayout_2.addWidget(self.mymemoryLabel, 2, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(TranslatorPage)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.yandexKeyEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.yandexKeyEdit.setObjectName("yandexKeyEdit")
        self.gridLayout.addWidget(self.yandexKeyEdit, 0, 1, 1, 1)
        self.yandexLabel = QtWidgets.QLabel(self.groupBox_3)
        self.yandexLabel.setText("")
        self.yandexLabel.setWordWrap(True)
        self.yandexLabel.setOpenExternalLinks(True)
        self.yandexLabel.setObjectName("yandexLabel")
        self.gridLayout.addWidget(self.yandexLabel, 1, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.retranslateUi(TranslatorPage)
        QtCore.QMetaObject.connectSlotsByName(TranslatorPage)
        TranslatorPage.setTabOrder(self.languagesList, self.setButton)
        TranslatorPage.setTabOrder(self.setButton, self.defaultButton)
        TranslatorPage.setTabOrder(self.defaultButton, self.deeplKeyEdit)
        TranslatorPage.setTabOrder(self.deeplKeyEdit, self.dictionaryCheckBox)
        TranslatorPage.setTabOrder(self.dictionaryCheckBox, self.googlev2KeyEdit)
        TranslatorPage.setTabOrder(self.googlev2KeyEdit, self.ibmUrlEdit)
        TranslatorPage.setTabOrder(self.ibmUrlEdit, self.ibmKeyEdit)
        TranslatorPage.setTabOrder(self.ibmKeyEdit, self.msSubscriptionKeyEdit)
        TranslatorPage.setTabOrder(self.msSubscriptionKeyEdit, self.mymemoryEmailEdit)
        TranslatorPage.setTabOrder(self.mymemoryEmailEdit, self.mymemoryKeyEdit)
        TranslatorPage.setTabOrder(self.mymemoryKeyEdit, self.yandexKeyEdit)

    def retranslateUi(self, TranslatorPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("TranslatorPage", "<b>Configure Translator</b>"))
        self.groupBox.setTitle(_translate("TranslatorPage", "Enabled Languages"))
        self.setButton.setToolTip(_translate("TranslatorPage", "Press to set or unset all entries"))
        self.setButton.setText(_translate("TranslatorPage", "Set/Unset All"))
        self.defaultButton.setToolTip(_translate("TranslatorPage", "Press to set the default list of enabled languages"))
        self.defaultButton.setText(_translate("TranslatorPage", "Set Default"))
        self.groupBox_8.setTitle(_translate("TranslatorPage", "DeepL Pro"))
        self.label_8.setText(_translate("TranslatorPage", "Key:"))
        self.deeplKeyEdit.setToolTip(_translate("TranslatorPage", "Enter your DeepL Pro key"))
        self.groupBox_2.setTitle(_translate("TranslatorPage", "Google V.1"))
        self.dictionaryCheckBox.setToolTip(_translate("TranslatorPage", "Select to show the results of the translation dictionary"))
        self.dictionaryCheckBox.setText(_translate("TranslatorPage", "Show dictionary results"))
        self.groupBox_5.setTitle(_translate("TranslatorPage", "Google V.2"))
        self.label_4.setText(_translate("TranslatorPage", "Key:"))
        self.googlev2KeyEdit.setToolTip(_translate("TranslatorPage", "Enter your Google Translate key"))
        self.groupBox_7.setTitle(_translate("TranslatorPage", "IBM Watson"))
        self.label_7.setText(_translate("TranslatorPage", "URL:"))
        self.ibmUrlEdit.setToolTip(_translate("TranslatorPage", "Enter your IBM Watson Translator URL"))
        self.label_6.setText(_translate("TranslatorPage", "API Key:"))
        self.ibmKeyEdit.setToolTip(_translate("TranslatorPage", "Enter your IBM Watson Translator API key"))
        self.groupBox_6.setTitle(_translate("TranslatorPage", "Microsoft Azure"))
        self.label_5.setText(_translate("TranslatorPage", "Subscription Key:"))
        self.msSubscriptionKeyEdit.setToolTip(_translate("TranslatorPage", "Enter the subscription key of the text translator service"))
        self.groupBox_4.setTitle(_translate("TranslatorPage", "MyMemory"))
        self.label.setText(_translate("TranslatorPage", "Email:"))
        self.mymemoryEmailEdit.setToolTip(_translate("TranslatorPage", "Enter email address to be sent with each request (optional)"))
        self.label_3.setText(_translate("TranslatorPage", "Key:"))
        self.mymemoryKeyEdit.setToolTip(_translate("TranslatorPage", "Enter your MyMemory key"))
        self.groupBox_3.setTitle(_translate("TranslatorPage", "Yandex"))
        self.label_2.setText(_translate("TranslatorPage", "Key:"))
        self.yandexKeyEdit.setToolTip(_translate("TranslatorPage", "Enter your Yandex key"))
