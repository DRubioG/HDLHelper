# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Top_file_generator_UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(589, 298)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 90, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 180, 91, 17))
        self.label_2.setObjectName("label_2")
        self.comboBox_files = QtWidgets.QComboBox(Dialog)
        self.comboBox_files.setGeometry(QtCore.QRect(140, 80, 301, 36))
        self.comboBox_files.setObjectName("comboBox_files")
        self.lineEdit_name_file = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_name_file.setGeometry(QtCore.QRect(140, 170, 301, 36))
        self.lineEdit_name_file.setObjectName("lineEdit_name_file")
        self.pushButton_search = QtWidgets.QPushButton(Dialog)
        self.pushButton_search.setGeometry(QtCore.QRect(480, 80, 95, 36))
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(470, 240, 95, 36))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_create = QtWidgets.QPushButton(Dialog)
        self.pushButton_create.setGeometry(QtCore.QRect(350, 240, 95, 36))
        self.pushButton_create.setObjectName("pushButton_create")
        self.pushButton_config = QtWidgets.QPushButton(Dialog)
        self.pushButton_config.setGeometry(QtCore.QRect(240, 240, 95, 36))
        self.pushButton_config.setObjectName("pushButton_config")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Input files"))
        self.label_2.setText(_translate("Dialog", "Top file name"))
        self.pushButton_search.setText(_translate("Dialog", "search"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))
        self.pushButton_create.setText(_translate("Dialog", "Create"))
        self.pushButton_config.setText(_translate("Dialog", "Config"))
