# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric6/CondaInterface/CondaPackagesWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CondaPackagesWidget(object):
    def setupUi(self, CondaPackagesWidget):
        CondaPackagesWidget.setObjectName("CondaPackagesWidget")
        CondaPackagesWidget.resize(600, 600)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(CondaPackagesWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.notAvailableWidget = QtWidgets.QWidget(CondaPackagesWidget)
        self.notAvailableWidget.setObjectName("notAvailableWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.notAvailableWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.notAvailableLabel = QtWidgets.QLabel(self.notAvailableWidget)
        self.notAvailableLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.notAvailableLabel.setObjectName("notAvailableLabel")
        self.verticalLayout_4.addWidget(self.notAvailableLabel)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.recheckButton = QtWidgets.QPushButton(self.notAvailableWidget)
        self.recheckButton.setObjectName("recheckButton")
        self.horizontalLayout_6.addWidget(self.recheckButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.verticalLayout_5.addWidget(self.notAvailableWidget)
        self.baseWidget = QtWidgets.QWidget(CondaPackagesWidget)
        self.baseWidget.setObjectName("baseWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.baseWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.environmentsComboBox = QtWidgets.QComboBox(self.baseWidget)
        self.environmentsComboBox.setObjectName("environmentsComboBox")
        self.horizontalLayout.addWidget(self.environmentsComboBox)
        self.condaMenuButton = E5ToolButton(self.baseWidget)
        self.condaMenuButton.setObjectName("condaMenuButton")
        self.horizontalLayout.addWidget(self.condaMenuButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.statusLabel = QtWidgets.QLabel(self.baseWidget)
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout_3.addWidget(self.statusLabel)
        self.packagesList = QtWidgets.QTreeWidget(self.baseWidget)
        self.packagesList.setAlternatingRowColors(True)
        self.packagesList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.packagesList.setRootIsDecorated(False)
        self.packagesList.setItemsExpandable(False)
        self.packagesList.setObjectName("packagesList")
        self.packagesList.header().setDefaultSectionSize(150)
        self.verticalLayout_3.addWidget(self.packagesList)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.refreshButton = QtWidgets.QToolButton(self.baseWidget)
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout_2.addWidget(self.refreshButton)
        self.upgradeButton = QtWidgets.QToolButton(self.baseWidget)
        self.upgradeButton.setObjectName("upgradeButton")
        self.horizontalLayout_2.addWidget(self.upgradeButton)
        self.upgradeAllButton = QtWidgets.QToolButton(self.baseWidget)
        self.upgradeAllButton.setObjectName("upgradeAllButton")
        self.horizontalLayout_2.addWidget(self.upgradeAllButton)
        self.uninstallButton = QtWidgets.QToolButton(self.baseWidget)
        self.uninstallButton.setObjectName("uninstallButton")
        self.horizontalLayout_2.addWidget(self.uninstallButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.searchToggleButton = QtWidgets.QToolButton(self.baseWidget)
        self.searchToggleButton.setCheckable(True)
        self.searchToggleButton.setObjectName("searchToggleButton")
        self.horizontalLayout_2.addWidget(self.searchToggleButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addWidget(self.baseWidget)
        self.searchWidget = QtWidgets.QWidget(CondaPackagesWidget)
        self.searchWidget.setObjectName("searchWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.searchWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.searchEdit = QtWidgets.QLineEdit(self.searchWidget)
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout_4.addWidget(self.searchEdit)
        self.searchButton = QtWidgets.QToolButton(self.searchWidget)
        self.searchButton.setEnabled(False)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_4.addWidget(self.searchButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.searchOptionsWidget = QtWidgets.QWidget(self.searchWidget)
        self.searchOptionsWidget.setObjectName("searchOptionsWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.searchOptionsWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.patternButton = QtWidgets.QRadioButton(self.searchOptionsWidget)
        self.patternButton.setChecked(True)
        self.patternButton.setObjectName("patternButton")
        self.horizontalLayout_5.addWidget(self.patternButton)
        self.fullNameButton = QtWidgets.QRadioButton(self.searchOptionsWidget)
        self.fullNameButton.setObjectName("fullNameButton")
        self.horizontalLayout_5.addWidget(self.fullNameButton)
        self.packageSpecButton = QtWidgets.QRadioButton(self.searchOptionsWidget)
        self.packageSpecButton.setObjectName("packageSpecButton")
        self.horizontalLayout_5.addWidget(self.packageSpecButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.searchOptionsWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.platformComboBox = QtWidgets.QComboBox(self.searchOptionsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.platformComboBox.sizePolicy().hasHeightForWidth())
        self.platformComboBox.setSizePolicy(sizePolicy)
        self.platformComboBox.setObjectName("platformComboBox")
        self.horizontalLayout_7.addWidget(self.platformComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addWidget(self.searchOptionsWidget)
        self.searchResultList = QtWidgets.QTreeWidget(self.searchWidget)
        self.searchResultList.setAlternatingRowColors(True)
        self.searchResultList.setObjectName("searchResultList")
        self.verticalLayout_2.addWidget(self.searchResultList)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.installButton = QtWidgets.QToolButton(self.searchWidget)
        self.installButton.setObjectName("installButton")
        self.horizontalLayout_3.addWidget(self.installButton)
        self.showDetailsButton = QtWidgets.QToolButton(self.searchWidget)
        self.showDetailsButton.setObjectName("showDetailsButton")
        self.horizontalLayout_3.addWidget(self.showDetailsButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addWidget(self.searchWidget)

        self.retranslateUi(CondaPackagesWidget)
        QtCore.QMetaObject.connectSlotsByName(CondaPackagesWidget)
        CondaPackagesWidget.setTabOrder(self.environmentsComboBox, self.condaMenuButton)
        CondaPackagesWidget.setTabOrder(self.condaMenuButton, self.packagesList)
        CondaPackagesWidget.setTabOrder(self.packagesList, self.refreshButton)
        CondaPackagesWidget.setTabOrder(self.refreshButton, self.upgradeButton)
        CondaPackagesWidget.setTabOrder(self.upgradeButton, self.upgradeAllButton)
        CondaPackagesWidget.setTabOrder(self.upgradeAllButton, self.uninstallButton)
        CondaPackagesWidget.setTabOrder(self.uninstallButton, self.searchToggleButton)
        CondaPackagesWidget.setTabOrder(self.searchToggleButton, self.searchEdit)
        CondaPackagesWidget.setTabOrder(self.searchEdit, self.searchButton)
        CondaPackagesWidget.setTabOrder(self.searchButton, self.patternButton)
        CondaPackagesWidget.setTabOrder(self.patternButton, self.fullNameButton)
        CondaPackagesWidget.setTabOrder(self.fullNameButton, self.packageSpecButton)
        CondaPackagesWidget.setTabOrder(self.packageSpecButton, self.searchResultList)
        CondaPackagesWidget.setTabOrder(self.searchResultList, self.installButton)
        CondaPackagesWidget.setTabOrder(self.installButton, self.showDetailsButton)

    def retranslateUi(self, CondaPackagesWidget):
        _translate = QtCore.QCoreApplication.translate
        self.notAvailableLabel.setText(_translate("CondaPackagesWidget", "<h2>conda is not available</h2>"))
        self.recheckButton.setToolTip(_translate("CondaPackagesWidget", "Press to re-check the availability of conda"))
        self.recheckButton.setText(_translate("CondaPackagesWidget", "Re-Check"))
        self.packagesList.headerItem().setText(0, _translate("CondaPackagesWidget", "Package"))
        self.packagesList.headerItem().setText(1, _translate("CondaPackagesWidget", "Installed Version"))
        self.packagesList.headerItem().setText(2, _translate("CondaPackagesWidget", "Available Version"))
        self.refreshButton.setToolTip(_translate("CondaPackagesWidget", "Press to refresh the lists"))
        self.upgradeButton.setToolTip(_translate("CondaPackagesWidget", "Press to upgrade the selected packages"))
        self.upgradeAllButton.setToolTip(_translate("CondaPackagesWidget", "Press to upgrade all listed packages"))
        self.uninstallButton.setToolTip(_translate("CondaPackagesWidget", "Press to uninstall the selected package"))
        self.searchToggleButton.setToolTip(_translate("CondaPackagesWidget", "Toggle to show or hide the search window"))
        self.searchEdit.setPlaceholderText(_translate("CondaPackagesWidget", "Enter search specification"))
        self.searchButton.setToolTip(_translate("CondaPackagesWidget", "Press to start the search"))
        self.patternButton.setToolTip(_translate("CondaPackagesWidget", "Search string is a pattern (default)"))
        self.patternButton.setText(_translate("CondaPackagesWidget", "Search Pattern"))
        self.fullNameButton.setToolTip(_translate("CondaPackagesWidget", "Search string is a full name"))
        self.fullNameButton.setText(_translate("CondaPackagesWidget", "Full Name"))
        self.packageSpecButton.setToolTip(_translate("CondaPackagesWidget", "Search string is a package specification"))
        self.packageSpecButton.setText(_translate("CondaPackagesWidget", "Package Specification"))
        self.label.setText(_translate("CondaPackagesWidget", "Platform:"))
        self.platformComboBox.setToolTip(_translate("CondaPackagesWidget", "Select the platform"))
        self.searchResultList.headerItem().setText(0, _translate("CondaPackagesWidget", "Package"))
        self.searchResultList.headerItem().setText(1, _translate("CondaPackagesWidget", "Version"))
        self.searchResultList.headerItem().setText(2, _translate("CondaPackagesWidget", "Build"))
        self.searchResultList.headerItem().setText(3, _translate("CondaPackagesWidget", "Platform"))
        self.installButton.setToolTip(_translate("CondaPackagesWidget", "Press to install the selected package (by name or package specification)"))
        self.showDetailsButton.setToolTip(_translate("CondaPackagesWidget", "Press to show details for the selected entry"))
from E5Gui.E5ToolButton import E5ToolButton
