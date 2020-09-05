# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric6/Preferences/ConfigurationPages/ViewmanagerPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ViewmanagerPage(object):
    def setupUi(self, ViewmanagerPage):
        ViewmanagerPage.setObjectName("ViewmanagerPage")
        ViewmanagerPage.resize(406, 315)
        self.vboxlayout = QtWidgets.QVBoxLayout(ViewmanagerPage)
        self.vboxlayout.setObjectName("vboxlayout")
        self.headerLabel = QtWidgets.QLabel(ViewmanagerPage)
        self.headerLabel.setObjectName("headerLabel")
        self.vboxlayout.addWidget(self.headerLabel)
        self.line9_2 = QtWidgets.QFrame(ViewmanagerPage)
        self.line9_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line9_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line9_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line9_2.setObjectName("line9_2")
        self.vboxlayout.addWidget(self.line9_2)
        self.TextLabel1_2_2_2_3 = QtWidgets.QLabel(ViewmanagerPage)
        self.TextLabel1_2_2_2_3.setObjectName("TextLabel1_2_2_2_3")
        self.vboxlayout.addWidget(self.TextLabel1_2_2_2_3)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.windowLabel = QtWidgets.QLabel(ViewmanagerPage)
        self.windowLabel.setObjectName("windowLabel")
        self.hboxlayout.addWidget(self.windowLabel)
        self.windowComboBox = QtWidgets.QComboBox(ViewmanagerPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowComboBox.sizePolicy().hasHeightForWidth())
        self.windowComboBox.setSizePolicy(sizePolicy)
        self.windowComboBox.setObjectName("windowComboBox")
        self.hboxlayout.addWidget(self.windowComboBox)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.previewPixmap = QtWidgets.QLabel(ViewmanagerPage)
        self.previewPixmap.setScaledContents(False)
        self.previewPixmap.setAlignment(QtCore.Qt.AlignCenter)
        self.previewPixmap.setObjectName("previewPixmap")
        self.vboxlayout.addWidget(self.previewPixmap)
        self.line = QtWidgets.QFrame(ViewmanagerPage)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.vboxlayout.addWidget(self.line)
        self.tabViewGroupBox = QtWidgets.QGroupBox(ViewmanagerPage)
        self.tabViewGroupBox.setEnabled(False)
        self.tabViewGroupBox.setObjectName("tabViewGroupBox")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.tabViewGroupBox)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.filenameLengthLabel = QtWidgets.QLabel(self.tabViewGroupBox)
        self.filenameLengthLabel.setObjectName("filenameLengthLabel")
        self.hboxlayout1.addWidget(self.filenameLengthLabel)
        self.filenameLengthSpinBox = QtWidgets.QSpinBox(self.tabViewGroupBox)
        self.filenameLengthSpinBox.setMinimum(1)
        self.filenameLengthSpinBox.setMaximum(100)
        self.filenameLengthSpinBox.setProperty("value", 40)
        self.filenameLengthSpinBox.setObjectName("filenameLengthSpinBox")
        self.hboxlayout1.addWidget(self.filenameLengthSpinBox)
        spacerItem = QtWidgets.QSpacerItem(81, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.filenameOnlyCheckBox = QtWidgets.QCheckBox(self.tabViewGroupBox)
        self.filenameOnlyCheckBox.setObjectName("filenameOnlyCheckBox")
        self.vboxlayout1.addWidget(self.filenameOnlyCheckBox)
        self.vboxlayout.addWidget(self.tabViewGroupBox)
        self.groupBox_7 = QtWidgets.QGroupBox(ViewmanagerPage)
        self.groupBox_7.setObjectName("groupBox_7")
        self.hboxlayout2 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.label = QtWidgets.QLabel(self.groupBox_7)
        self.label.setObjectName("label")
        self.hboxlayout2.addWidget(self.label)
        self.recentFilesSpinBox = QtWidgets.QSpinBox(self.groupBox_7)
        self.recentFilesSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.recentFilesSpinBox.setMinimum(5)
        self.recentFilesSpinBox.setMaximum(50)
        self.recentFilesSpinBox.setObjectName("recentFilesSpinBox")
        self.hboxlayout2.addWidget(self.recentFilesSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem1)
        self.vboxlayout.addWidget(self.groupBox_7)
        spacerItem2 = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem2)
        self.windowLabel.setBuddy(self.windowComboBox)

        self.retranslateUi(ViewmanagerPage)
        QtCore.QMetaObject.connectSlotsByName(ViewmanagerPage)

    def retranslateUi(self, ViewmanagerPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("ViewmanagerPage", "<b>Configure viewmanager</b>"))
        self.TextLabel1_2_2_2_3.setText(_translate("ViewmanagerPage", "<font color=\"#FF0000\"><b>Note:</b> This setting is activated at the next startup of the application.</font>"))
        self.windowLabel.setText(_translate("ViewmanagerPage", "Window view:"))
        self.windowComboBox.setToolTip(_translate("ViewmanagerPage", "Select the window view type."))
        self.windowComboBox.setWhatsThis(_translate("ViewmanagerPage", "The kind of window view can be selected from this list. The picture below gives an example of the selected view type."))
        self.previewPixmap.setToolTip(_translate("ViewmanagerPage", "Preview of selected window view"))
        self.previewPixmap.setWhatsThis(_translate("ViewmanagerPage", "This displays a small preview of the selected window view. This is the way the source windows are displayed in the application."))
        self.tabViewGroupBox.setTitle(_translate("ViewmanagerPage", "Tabbed View"))
        self.filenameLengthLabel.setText(_translate("ViewmanagerPage", "Filename Length of Tab:"))
        self.filenameLengthSpinBox.setToolTip(_translate("ViewmanagerPage", "Enter the number of characters to be shown in the tab."))
        self.filenameOnlyCheckBox.setToolTip(_translate("ViewmanagerPage", "Select to display the filename only"))
        self.filenameOnlyCheckBox.setText(_translate("ViewmanagerPage", "Show filename only"))
        self.groupBox_7.setTitle(_translate("ViewmanagerPage", "Recent Files"))
        self.label.setText(_translate("ViewmanagerPage", "Number of recent files:"))
        self.recentFilesSpinBox.setToolTip(_translate("ViewmanagerPage", "Enter the number of recent files to remember"))
