# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eric6/Plugins/VcsPlugins/vcsGit/GitSubmodulesSummaryOptionsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GitSubmodulesSummaryOptionsDialog(object):
    def setupUi(self, GitSubmodulesSummaryOptionsDialog):
        GitSubmodulesSummaryOptionsDialog.setObjectName("GitSubmodulesSummaryOptionsDialog")
        GitSubmodulesSummaryOptionsDialog.resize(400, 350)
        GitSubmodulesSummaryOptionsDialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(GitSubmodulesSummaryOptionsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(GitSubmodulesSummaryOptionsDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.submodulesList = QtWidgets.QListWidget(GitSubmodulesSummaryOptionsDialog)
        self.submodulesList.setAlternatingRowColors(True)
        self.submodulesList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.submodulesList.setObjectName("submodulesList")
        self.gridLayout.addWidget(self.submodulesList, 1, 0, 1, 3)
        self.filesCheckBox = QtWidgets.QCheckBox(GitSubmodulesSummaryOptionsDialog)
        self.filesCheckBox.setObjectName("filesCheckBox")
        self.gridLayout.addWidget(self.filesCheckBox, 2, 0, 1, 3)
        self.indexCheckBox = QtWidgets.QCheckBox(GitSubmodulesSummaryOptionsDialog)
        self.indexCheckBox.setObjectName("indexCheckBox")
        self.gridLayout.addWidget(self.indexCheckBox, 3, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(GitSubmodulesSummaryOptionsDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.commitEdit = QtWidgets.QLineEdit(GitSubmodulesSummaryOptionsDialog)
        self.commitEdit.setObjectName("commitEdit")
        self.gridLayout.addWidget(self.commitEdit, 4, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(GitSubmodulesSummaryOptionsDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.limitSpinBox = QtWidgets.QSpinBox(GitSubmodulesSummaryOptionsDialog)
        self.limitSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.limitSpinBox.setMaximum(9999)
        self.limitSpinBox.setSingleStep(5)
        self.limitSpinBox.setObjectName("limitSpinBox")
        self.gridLayout.addWidget(self.limitSpinBox, 5, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(269, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(GitSubmodulesSummaryOptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 3)

        self.retranslateUi(GitSubmodulesSummaryOptionsDialog)
        self.buttonBox.accepted.connect(GitSubmodulesSummaryOptionsDialog.accept)
        self.buttonBox.rejected.connect(GitSubmodulesSummaryOptionsDialog.reject)
        self.filesCheckBox.toggled['bool'].connect(self.indexCheckBox.setDisabled)
        self.filesCheckBox.toggled['bool'].connect(self.commitEdit.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(GitSubmodulesSummaryOptionsDialog)
        GitSubmodulesSummaryOptionsDialog.setTabOrder(self.submodulesList, self.filesCheckBox)
        GitSubmodulesSummaryOptionsDialog.setTabOrder(self.filesCheckBox, self.indexCheckBox)
        GitSubmodulesSummaryOptionsDialog.setTabOrder(self.indexCheckBox, self.commitEdit)
        GitSubmodulesSummaryOptionsDialog.setTabOrder(self.commitEdit, self.limitSpinBox)

    def retranslateUi(self, GitSubmodulesSummaryOptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        GitSubmodulesSummaryOptionsDialog.setWindowTitle(_translate("GitSubmodulesSummaryOptionsDialog", "Submodule Summary Options"))
        self.label.setText(_translate("GitSubmodulesSummaryOptionsDialog", "Selected Submodules:"))
        self.submodulesList.setToolTip(_translate("GitSubmodulesSummaryOptionsDialog", "Select the submodules to show the summary for"))
        self.filesCheckBox.setToolTip(_translate("GitSubmodulesSummaryOptionsDialog", "Select to show summary information for the index of the superproject"))
        self.filesCheckBox.setText(_translate("GitSubmodulesSummaryOptionsDialog", "Show Summary for Superproject Index"))
        self.indexCheckBox.setToolTip(_translate("GitSubmodulesSummaryOptionsDialog", "Select to show summary information for the index"))
        self.indexCheckBox.setText(_translate("GitSubmodulesSummaryOptionsDialog", "Show Summary for Index"))
        self.label_2.setText(_translate("GitSubmodulesSummaryOptionsDialog", "Commit:"))
        self.commitEdit.setToolTip(_translate("GitSubmodulesSummaryOptionsDialog", "Enter a commit ID to show summary information for"))
        self.commitEdit.setPlaceholderText(_translate("GitSubmodulesSummaryOptionsDialog", "Enter Commit ID"))
        self.label_3.setText(_translate("GitSubmodulesSummaryOptionsDialog", "Limit:"))
        self.limitSpinBox.setToolTip(_translate("GitSubmodulesSummaryOptionsDialog", "Enter the maximum number of entries to be shown per submodule"))
        self.limitSpinBox.setSpecialValueText(_translate("GitSubmodulesSummaryOptionsDialog", "No Limit"))
