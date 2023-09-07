# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_version_advise_UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_new_version(object):
    def setupUi(self, Dialog_new_version):
        Dialog_new_version.setObjectName("Dialog_new_version")
        Dialog_new_version.resize(509, 187)
        self.label = QtWidgets.QLabel(Dialog_new_version)
        self.label.setGeometry(QtCore.QRect(40, 40, 301, 19))
        self.label.setObjectName("label")
        self.pushButton_ok = QtWidgets.QPushButton(Dialog_new_version)
        self.pushButton_ok.setGeometry(QtCore.QRect(370, 140, 100, 27))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.checkBox_show_again = QtWidgets.QCheckBox(Dialog_new_version)
        self.checkBox_show_again.setGeometry(QtCore.QRect(40, 140, 181, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_show_again.setFont(font)
        self.checkBox_show_again.setObjectName("checkBox_show_again")
        self.label_2 = QtWidgets.QLabel(Dialog_new_version)
        self.label_2.setGeometry(QtCore.QRect(140, 80, 111, 19))
        self.label_2.setObjectName("label_2")
        self.pushButton_web = QtWidgets.QPushButton(Dialog_new_version)
        self.pushButton_web.setGeometry(QtCore.QRect(250, 140, 100, 27))
        self.pushButton_web.setObjectName("pushButton_web")
        self.label_previous_version = QtWidgets.QLabel(Dialog_new_version)
        self.label_previous_version.setGeometry(QtCore.QRect(260, 80, 41, 19))
        self.label_previous_version.setText("")
        self.label_previous_version.setObjectName("label_previous_version")
        self.label_4 = QtWidgets.QLabel(Dialog_new_version)
        self.label_4.setGeometry(QtCore.QRect(300, 80, 31, 19))
        self.label_4.setObjectName("label_4")
        self.label_new_version = QtWidgets.QLabel(Dialog_new_version)
        self.label_new_version.setGeometry(QtCore.QRect(340, 80, 41, 19))
        self.label_new_version.setText("")
        self.label_new_version.setObjectName("label_new_version")

        self.retranslateUi(Dialog_new_version)
        QtCore.QMetaObject.connectSlotsByName(Dialog_new_version)

    def retranslateUi(self, Dialog_new_version):
        _translate = QtCore.QCoreApplication.translate
        Dialog_new_version.setWindowTitle(_translate("Dialog_new_version", "Dialog"))
        self.label.setText(_translate("Dialog_new_version", "New version of HDLHelper"))
        self.pushButton_ok.setText(_translate("Dialog_new_version", "Ok"))
        self.checkBox_show_again.setText(_translate("Dialog_new_version", "Do not show again"))
        self.label_2.setText(_translate("Dialog_new_version", "Your version:"))
        self.pushButton_web.setText(_translate("Dialog_new_version", "Web"))
        self.label_4.setText(_translate("Dialog_new_version", "-> "))
