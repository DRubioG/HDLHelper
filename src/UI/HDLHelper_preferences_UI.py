# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HDLHelper_preferences_UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HDLHelper_preferences(object):
    def setupUi(self, HDLHelper_preferences):
        HDLHelper_preferences.setObjectName("HDLHelper_preferences")
        HDLHelper_preferences.resize(404, 476)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HDLHelper_preferences.sizePolicy().hasHeightForWidth())
        HDLHelper_preferences.setSizePolicy(sizePolicy)
        HDLHelper_preferences.setMaximumSize(QtCore.QSize(404, 476))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../img/logo/icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HDLHelper_preferences.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(HDLHelper_preferences)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 331, 281))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_user = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_user.setGeometry(QtCore.QRect(120, 40, 201, 25))
        self.lineEdit_user.setInputMask("")
        self.lineEdit_user.setText("")
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 51, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 101, 17))
        self.label_3.setObjectName("label_3")
        self.lineEdit_corpation = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_corpation.setGeometry(QtCore.QRect(120, 80, 201, 25))
        self.lineEdit_corpation.setInputMask("")
        self.lineEdit_corpation.setText("")
        self.lineEdit_corpation.setObjectName("lineEdit_corpation")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 91, 17))
        self.label_4.setObjectName("label_4")
        self.lineEdit_contact = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_contact.setGeometry(QtCore.QRect(120, 120, 201, 25))
        self.lineEdit_contact.setInputMask("")
        self.lineEdit_contact.setText("")
        self.lineEdit_contact.setObjectName("lineEdit_contact")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 91, 17))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 160, 201, 25))
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.checkBox_version_fl = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_version_fl.setGeometry(QtCore.QRect(10, 200, 201, 23))
        self.checkBox_version_fl.setChecked(True)
        self.checkBox_version_fl.setObjectName("checkBox_version_fl")
        self.checkBox_date = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_date.setGeometry(QtCore.QRect(10, 230, 201, 23))
        self.checkBox_date.setChecked(True)
        self.checkBox_date.setObjectName("checkBox_date")
        self.pushButton_cancel = QtWidgets.QPushButton(HDLHelper_preferences)
        self.pushButton_cancel.setGeometry(QtCore.QRect(279, 420, 101, 27))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_save = QtWidgets.QPushButton(HDLHelper_preferences)
        self.pushButton_save.setGeometry(QtCore.QRect(170, 420, 100, 27))
        self.pushButton_save.setObjectName("pushButton_save")

        self.retranslateUi(HDLHelper_preferences)
        QtCore.QMetaObject.connectSlotsByName(HDLHelper_preferences)

    def retranslateUi(self, HDLHelper_preferences):
        _translate = QtCore.QCoreApplication.translate
        HDLHelper_preferences.setWindowTitle(_translate("HDLHelper_preferences", "Preferences"))
        self.groupBox.setTitle(_translate("HDLHelper_preferences", "Comments"))
        self.label_2.setText(_translate("HDLHelper_preferences", "User"))
        self.label_3.setText(_translate("HDLHelper_preferences", "Corporation"))
        self.label_4.setText(_translate("HDLHelper_preferences", "Contact"))
        self.label_5.setText(_translate("HDLHelper_preferences", "Version"))
        self.checkBox_version_fl.setText(_translate("HDLHelper_preferences", "Version of HDLHelper"))
        self.checkBox_date.setText(_translate("HDLHelper_preferences", "Add date"))
        self.pushButton_cancel.setText(_translate("HDLHelper_preferences", "Cancel"))
        self.pushButton_save.setText(_translate("HDLHelper_preferences", "Save"))
