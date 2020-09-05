# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric6/Preferences/ConfigurationPages/EditorCalltipsPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditorCalltipsPage(object):
    def setupUi(self, EditorCalltipsPage):
        EditorCalltipsPage.setObjectName("EditorCalltipsPage")
        EditorCalltipsPage.resize(408, 556)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(EditorCalltipsPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.headerLabel = QtWidgets.QLabel(EditorCalltipsPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_3.addWidget(self.headerLabel)
        self.line18 = QtWidgets.QFrame(EditorCalltipsPage)
        self.line18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line18.setObjectName("line18")
        self.verticalLayout_3.addWidget(self.line18)
        self.ctEnabledCheckBox = QtWidgets.QCheckBox(EditorCalltipsPage)
        self.ctEnabledCheckBox.setObjectName("ctEnabledCheckBox")
        self.verticalLayout_3.addWidget(self.ctEnabledCheckBox)
        self.frame = QtWidgets.QFrame(EditorCalltipsPage)
        self.frame.setEnabled(False)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3.addWidget(self.frame)
        self.groupBox_4 = QtWidgets.QGroupBox(EditorCalltipsPage)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ctVisibleSlider = QtWidgets.QSlider(self.groupBox_4)
        self.ctVisibleSlider.setMaximum(20)
        self.ctVisibleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ctVisibleSlider.setTickInterval(1)
        self.ctVisibleSlider.setObjectName("ctVisibleSlider")
        self.horizontalLayout_2.addWidget(self.ctVisibleSlider)
        self.lCDNumber5 = QtWidgets.QLCDNumber(self.groupBox_4)
        self.lCDNumber5.setDigitCount(2)
        self.lCDNumber5.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lCDNumber5.setObjectName("lCDNumber5")
        self.horizontalLayout_2.addWidget(self.lCDNumber5)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.calltipsPositionBox = QtWidgets.QGroupBox(EditorCalltipsPage)
        self.calltipsPositionBox.setObjectName("calltipsPositionBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.calltipsPositionBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.positionComboBox = QtWidgets.QComboBox(self.calltipsPositionBox)
        self.positionComboBox.setObjectName("positionComboBox")
        self.verticalLayout_2.addWidget(self.positionComboBox)
        self.verticalLayout_3.addWidget(self.calltipsPositionBox)
        self.groupBox_2 = QtWidgets.QGroupBox(EditorCalltipsPage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.TextLabel2_2_2_2 = QtWidgets.QLabel(self.groupBox_2)
        self.TextLabel2_2_2_2.setObjectName("TextLabel2_2_2_2")
        self.gridLayout.addWidget(self.TextLabel2_2_2_2, 0, 0, 1, 1)
        self.calltipsBackgroundButton = QtWidgets.QPushButton(self.groupBox_2)
        self.calltipsBackgroundButton.setMinimumSize(QtCore.QSize(100, 0))
        self.calltipsBackgroundButton.setText("")
        self.calltipsBackgroundButton.setObjectName("calltipsBackgroundButton")
        self.gridLayout.addWidget(self.calltipsBackgroundButton, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.TextLabel2_2_2_3 = QtWidgets.QLabel(self.groupBox_2)
        self.TextLabel2_2_2_3.setObjectName("TextLabel2_2_2_3")
        self.gridLayout.addWidget(self.TextLabel2_2_2_3, 1, 0, 1, 1)
        self.calltipsForegroundButton = QtWidgets.QPushButton(self.groupBox_2)
        self.calltipsForegroundButton.setMinimumSize(QtCore.QSize(100, 0))
        self.calltipsForegroundButton.setText("")
        self.calltipsForegroundButton.setObjectName("calltipsForegroundButton")
        self.gridLayout.addWidget(self.calltipsForegroundButton, 1, 1, 1, 1)
        self.TextLabel2_2_2_4 = QtWidgets.QLabel(self.groupBox_2)
        self.TextLabel2_2_2_4.setObjectName("TextLabel2_2_2_4")
        self.gridLayout.addWidget(self.TextLabel2_2_2_4, 2, 0, 1, 1)
        self.calltipsHighlightButton = QtWidgets.QPushButton(self.groupBox_2)
        self.calltipsHighlightButton.setMinimumSize(QtCore.QSize(100, 0))
        self.calltipsHighlightButton.setText("")
        self.calltipsHighlightButton.setObjectName("calltipsHighlightButton")
        self.gridLayout.addWidget(self.calltipsHighlightButton, 2, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(EditorCalltipsPage)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ctScintillaCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.ctScintillaCheckBox.setObjectName("ctScintillaCheckBox")
        self.verticalLayout.addWidget(self.ctScintillaCheckBox)
        self.verticalLayout_3.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)

        self.retranslateUi(EditorCalltipsPage)
        self.ctVisibleSlider.valueChanged['int'].connect(self.lCDNumber5.display)
        QtCore.QMetaObject.connectSlotsByName(EditorCalltipsPage)
        EditorCalltipsPage.setTabOrder(self.ctEnabledCheckBox, self.ctVisibleSlider)
        EditorCalltipsPage.setTabOrder(self.ctVisibleSlider, self.positionComboBox)
        EditorCalltipsPage.setTabOrder(self.positionComboBox, self.calltipsBackgroundButton)
        EditorCalltipsPage.setTabOrder(self.calltipsBackgroundButton, self.calltipsForegroundButton)
        EditorCalltipsPage.setTabOrder(self.calltipsForegroundButton, self.calltipsHighlightButton)
        EditorCalltipsPage.setTabOrder(self.calltipsHighlightButton, self.ctScintillaCheckBox)

    def retranslateUi(self, EditorCalltipsPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("EditorCalltipsPage", "<b>Configure Calltips</b>"))
        self.ctEnabledCheckBox.setToolTip(_translate("EditorCalltipsPage", "Select this to enable calltips"))
        self.ctEnabledCheckBox.setText(_translate("EditorCalltipsPage", "Automatic Calltips Enabled"))
        self.groupBox_4.setTitle(_translate("EditorCalltipsPage", "Visible Calltips"))
        self.ctVisibleSlider.setToolTip(_translate("EditorCalltipsPage", "Move to set the maximum number of calltips shown (0 = all available)"))
        self.lCDNumber5.setToolTip(_translate("EditorCalltipsPage", "Displays the maximum number of calltips to be shown"))
        self.calltipsPositionBox.setTitle(_translate("EditorCalltipsPage", "Calltips Position"))
        self.positionComboBox.setToolTip(_translate("EditorCalltipsPage", "Select the position for the calltips"))
        self.groupBox_2.setTitle(_translate("EditorCalltipsPage", "Colors"))
        self.TextLabel2_2_2_2.setText(_translate("EditorCalltipsPage", "Background color:"))
        self.calltipsBackgroundButton.setToolTip(_translate("EditorCalltipsPage", "Select the background color for calltips."))
        self.TextLabel2_2_2_3.setText(_translate("EditorCalltipsPage", "Foreground color:"))
        self.calltipsForegroundButton.setToolTip(_translate("EditorCalltipsPage", "Select the foreground color for calltips."))
        self.TextLabel2_2_2_4.setText(_translate("EditorCalltipsPage", "Highlight color:"))
        self.calltipsHighlightButton.setToolTip(_translate("EditorCalltipsPage", "Select the highlight color for calltips."))
        self.groupBox.setTitle(_translate("EditorCalltipsPage", "Plug-In Behavior"))
        self.ctScintillaCheckBox.setToolTip(_translate("EditorCalltipsPage", "Select to show QScintilla provided calltips, if the selected plug-ins fail"))
        self.ctScintillaCheckBox.setWhatsThis(_translate("EditorCalltipsPage", "Qscintilla provided calltips are shown, if this option is enabled and calltips shall be provided by plug-ins (see calltips sub-page of the plug-in) and the plugin-ins don\'t deliver any calltips."))
        self.ctScintillaCheckBox.setText(_translate("EditorCalltipsPage", "Show QScintilla calltips, if plug-ins fail"))
