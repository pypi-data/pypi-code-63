# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric6/Plugins/AboutPlugin/AboutDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(580, 450)
        self.vboxlayout = QtWidgets.QVBoxLayout(AboutDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.ericPixmap = QtWidgets.QLabel(AboutDialog)
        self.ericPixmap.setScaledContents(False)
        self.ericPixmap.setObjectName("ericPixmap")
        self.hboxlayout.addWidget(self.ericPixmap)
        self.ericLabel = QtWidgets.QLabel(AboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ericLabel.sizePolicy().hasHeightForWidth())
        self.ericLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.ericLabel.setFont(font)
        self.ericLabel.setObjectName("ericLabel")
        self.hboxlayout.addWidget(self.ericLabel)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.aboutTabWidget = QtWidgets.QTabWidget(AboutDialog)
        self.aboutTabWidget.setObjectName("aboutTabWidget")
        self.about = QtWidgets.QWidget()
        self.about.setObjectName("about")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.about)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.aboutEdit = QtWidgets.QTextBrowser(self.about)
        self.aboutEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aboutEdit.setOpenExternalLinks(True)
        self.aboutEdit.setObjectName("aboutEdit")
        self.vboxlayout1.addWidget(self.aboutEdit)
        self.aboutTabWidget.addTab(self.about, "")
        self.authors = QtWidgets.QWidget()
        self.authors.setObjectName("authors")
        self.vboxlayout2 = QtWidgets.QVBoxLayout(self.authors)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.authorsEdit = QtWidgets.QTextEdit(self.authors)
        self.authorsEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.authorsEdit.setReadOnly(True)
        self.authorsEdit.setObjectName("authorsEdit")
        self.vboxlayout2.addWidget(self.authorsEdit)
        self.aboutTabWidget.addTab(self.authors, "")
        self.thanks = QtWidgets.QWidget()
        self.thanks.setObjectName("thanks")
        self.vboxlayout3 = QtWidgets.QVBoxLayout(self.thanks)
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.thanksEdit = QtWidgets.QTextEdit(self.thanks)
        self.thanksEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.thanksEdit.setReadOnly(True)
        self.thanksEdit.setObjectName("thanksEdit")
        self.vboxlayout3.addWidget(self.thanksEdit)
        self.aboutTabWidget.addTab(self.thanks, "")
        self.license = QtWidgets.QWidget()
        self.license.setObjectName("license")
        self.vboxlayout4 = QtWidgets.QVBoxLayout(self.license)
        self.vboxlayout4.setObjectName("vboxlayout4")
        self.licenseEdit = QtWidgets.QTextEdit(self.license)
        self.licenseEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.licenseEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.licenseEdit.setReadOnly(True)
        self.licenseEdit.setAcceptRichText(False)
        self.licenseEdit.setObjectName("licenseEdit")
        self.vboxlayout4.addWidget(self.licenseEdit)
        self.aboutTabWidget.addTab(self.license, "")
        self.vboxlayout.addWidget(self.aboutTabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(AboutDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(AboutDialog)
        self.aboutTabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(AboutDialog.accept)
        self.buttonBox.rejected.connect(AboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)
        AboutDialog.setTabOrder(self.aboutTabWidget, self.aboutEdit)
        AboutDialog.setTabOrder(self.aboutEdit, self.authorsEdit)
        AboutDialog.setTabOrder(self.authorsEdit, self.thanksEdit)
        AboutDialog.setTabOrder(self.thanksEdit, self.licenseEdit)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About Eric"))
        self.aboutTabWidget.setTabText(self.aboutTabWidget.indexOf(self.about), _translate("AboutDialog", "&About"))
        self.aboutTabWidget.setTabText(self.aboutTabWidget.indexOf(self.authors), _translate("AboutDialog", "A&uthors"))
        self.aboutTabWidget.setTabText(self.aboutTabWidget.indexOf(self.thanks), _translate("AboutDialog", "&Thanks To"))
        self.aboutTabWidget.setTabText(self.aboutTabWidget.indexOf(self.license), _translate("AboutDialog", "&License Agreement"))
