# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric6/Preferences/ConfigurationPages/HelpDocumentationPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HelpDocumentationPage(object):
    def setupUi(self, HelpDocumentationPage):
        HelpDocumentationPage.setObjectName("HelpDocumentationPage")
        HelpDocumentationPage.resize(526, 894)
        self.verticalLayout = QtWidgets.QVBoxLayout(HelpDocumentationPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headerLabel = QtWidgets.QLabel(HelpDocumentationPage)
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout.addWidget(self.headerLabel)
        self.line17 = QtWidgets.QFrame(HelpDocumentationPage)
        self.line17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line17.setObjectName("line17")
        self.verticalLayout.addWidget(self.line17)
        self.groupBox_9 = QtWidgets.QGroupBox(HelpDocumentationPage)
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.ericDocDirPicker = E5PathPicker(self.groupBox_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ericDocDirPicker.sizePolicy().hasHeightForWidth())
        self.ericDocDirPicker.setSizePolicy(sizePolicy)
        self.ericDocDirPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ericDocDirPicker.setObjectName("ericDocDirPicker")
        self.verticalLayout_9.addWidget(self.ericDocDirPicker)
        self.textLabel1_8_2_2_6 = QtWidgets.QLabel(self.groupBox_9)
        self.textLabel1_8_2_2_6.setWordWrap(True)
        self.textLabel1_8_2_2_6.setObjectName("textLabel1_8_2_2_6")
        self.verticalLayout_9.addWidget(self.textLabel1_8_2_2_6)
        self.verticalLayout.addWidget(self.groupBox_9)
        self.groupBox_4 = QtWidgets.QGroupBox(HelpDocumentationPage)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pythonDocDirPicker = E5PathPicker(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pythonDocDirPicker.sizePolicy().hasHeightForWidth())
        self.pythonDocDirPicker.setSizePolicy(sizePolicy)
        self.pythonDocDirPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pythonDocDirPicker.setObjectName("pythonDocDirPicker")
        self.verticalLayout_3.addWidget(self.pythonDocDirPicker)
        self.textLabel1_8_2 = QtWidgets.QLabel(self.groupBox_4)
        self.textLabel1_8_2.setWordWrap(True)
        self.textLabel1_8_2.setObjectName("textLabel1_8_2")
        self.verticalLayout_3.addWidget(self.textLabel1_8_2)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_8 = QtWidgets.QGroupBox(HelpDocumentationPage)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.qt5DocDirPicker = E5PathPicker(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qt5DocDirPicker.sizePolicy().hasHeightForWidth())
        self.qt5DocDirPicker.setSizePolicy(sizePolicy)
        self.qt5DocDirPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.qt5DocDirPicker.setObjectName("qt5DocDirPicker")
        self.verticalLayout_5.addWidget(self.qt5DocDirPicker)
        self.textLabel1_8_2_2_4 = QtWidgets.QLabel(self.groupBox_8)
        self.textLabel1_8_2_2_4.setWordWrap(True)
        self.textLabel1_8_2_2_4.setObjectName("textLabel1_8_2_2_4")
        self.verticalLayout_5.addWidget(self.textLabel1_8_2_2_4)
        self.verticalLayout.addWidget(self.groupBox_8)
        self.pyqt5Group = QtWidgets.QGroupBox(HelpDocumentationPage)
        self.pyqt5Group.setObjectName("pyqt5Group")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.pyqt5Group)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pyqt5DocDirPicker = E5PathPicker(self.pyqt5Group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pyqt5DocDirPicker.sizePolicy().hasHeightForWidth())
        self.pyqt5DocDirPicker.setSizePolicy(sizePolicy)
        self.pyqt5DocDirPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pyqt5DocDirPicker.setObjectName("pyqt5DocDirPicker")
        self.verticalLayout_7.addWidget(self.pyqt5DocDirPicker)
        self.textLabel1_8_2_2_5 = QtWidgets.QLabel(self.pyqt5Group)
        self.textLabel1_8_2_2_5.setWordWrap(True)
        self.textLabel1_8_2_2_5.setObjectName("textLabel1_8_2_2_5")
        self.verticalLayout_7.addWidget(self.textLabel1_8_2_2_5)
        self.verticalLayout.addWidget(self.pyqt5Group)
        self.pyside2Group = QtWidgets.QGroupBox(HelpDocumentationPage)
        self.pyside2Group.setObjectName("pyside2Group")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.pyside2Group)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pyside2DocDirPicker = E5PathPicker(self.pyside2Group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pyside2DocDirPicker.sizePolicy().hasHeightForWidth())
        self.pyside2DocDirPicker.setSizePolicy(sizePolicy)
        self.pyside2DocDirPicker.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pyside2DocDirPicker.setObjectName("pyside2DocDirPicker")
        self.verticalLayout_10.addWidget(self.pyside2DocDirPicker)
        self.textLabel1_8_2_3 = QtWidgets.QLabel(self.pyside2Group)
        self.textLabel1_8_2_3.setWordWrap(True)
        self.textLabel1_8_2_3.setObjectName("textLabel1_8_2_3")
        self.verticalLayout_10.addWidget(self.textLabel1_8_2_3)
        self.verticalLayout.addWidget(self.pyside2Group)
        spacerItem = QtWidgets.QSpacerItem(479, 41, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(HelpDocumentationPage)
        QtCore.QMetaObject.connectSlotsByName(HelpDocumentationPage)
        HelpDocumentationPage.setTabOrder(self.ericDocDirPicker, self.pythonDocDirPicker)
        HelpDocumentationPage.setTabOrder(self.pythonDocDirPicker, self.qt5DocDirPicker)
        HelpDocumentationPage.setTabOrder(self.qt5DocDirPicker, self.pyqt5DocDirPicker)

    def retranslateUi(self, HelpDocumentationPage):
        _translate = QtCore.QCoreApplication.translate
        self.headerLabel.setText(_translate("HelpDocumentationPage", "<b>Configure help documentation</b>"))
        self.groupBox_9.setTitle(_translate("HelpDocumentationPage", "eric API Documentation"))
        self.ericDocDirPicker.setToolTip(_translate("HelpDocumentationPage", "Enter the eric documentation directory"))
        self.textLabel1_8_2_2_6.setText(_translate("HelpDocumentationPage", "<b>Note</b>: Leave empty to use the default location."))
        self.groupBox_4.setTitle(_translate("HelpDocumentationPage", "Python 3 Documentation"))
        self.pythonDocDirPicker.setToolTip(_translate("HelpDocumentationPage", "Enter the Python 3 documentation directory"))
        self.textLabel1_8_2.setText(_translate("HelpDocumentationPage", "<b>Note</b>: Leave empty to use the PYTHON3DOCDIR environment variable, if set."))
        self.groupBox_8.setTitle(_translate("HelpDocumentationPage", "Qt5 Documentation"))
        self.qt5DocDirPicker.setToolTip(_translate("HelpDocumentationPage", "Enter the Qt5 documentation directory"))
        self.textLabel1_8_2_2_4.setText(_translate("HelpDocumentationPage", "<b>Note</b>: Leave empty to use the QT5DOCDIR environment variable, if set."))
        self.pyqt5Group.setTitle(_translate("HelpDocumentationPage", "PyQt5 Documentation"))
        self.pyqt5DocDirPicker.setToolTip(_translate("HelpDocumentationPage", "Enter the PyQt5 documentation directory"))
        self.textLabel1_8_2_2_5.setText(_translate("HelpDocumentationPage", "<b>Note</b>: Leave empty to use the PYQT5DOCDIR environment variable, if set."))
        self.pyside2Group.setTitle(_translate("HelpDocumentationPage", "PySide2 Documentation"))
        self.pyside2DocDirPicker.setToolTip(_translate("HelpDocumentationPage", "Enter the PySide2 documentation directory"))
        self.textLabel1_8_2_3.setText(_translate("HelpDocumentationPage", "<b>Note</b>: Leave empty to use the PYSIDE2DOCDIR environment variable, if set."))
from E5Gui.E5PathPicker import E5PathPicker
