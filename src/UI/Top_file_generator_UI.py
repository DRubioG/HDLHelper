# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Top_file_generator_UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Top_file_generator(object):
    def setupUi(self, Top_file_generator):
        Top_file_generator.setObjectName("Top_file_generator")
        Top_file_generator.resize(589, 298)
        self.label = QtWidgets.QLabel(Top_file_generator)
        self.label.setGeometry(QtCore.QRect(20, 90, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Top_file_generator)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 111, 17))
        self.label_2.setObjectName("label_2")
        self.comboBox_files = QtWidgets.QComboBox(Top_file_generator)
        self.comboBox_files.setGeometry(QtCore.QRect(140, 80, 301, 36))
        self.comboBox_files.setObjectName("comboBox_files")
        self.lineEdit_name_file = QtWidgets.QLineEdit(Top_file_generator)
        self.lineEdit_name_file.setGeometry(QtCore.QRect(140, 170, 301, 36))
        self.lineEdit_name_file.setObjectName("lineEdit_name_file")
        self.pushButton_search = QtWidgets.QPushButton(Top_file_generator)
        self.pushButton_search.setGeometry(QtCore.QRect(480, 80, 95, 36))
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_cancel = QtWidgets.QPushButton(Top_file_generator)
        self.pushButton_cancel.setGeometry(QtCore.QRect(470, 240, 95, 36))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_create = QtWidgets.QPushButton(Top_file_generator)
        self.pushButton_create.setGeometry(QtCore.QRect(360, 240, 95, 36))
        self.pushButton_create.setObjectName("pushButton_create")
        self.pushButton_config = QtWidgets.QPushButton(Top_file_generator)
        self.pushButton_config.setGeometry(QtCore.QRect(250, 240, 95, 36))
        self.pushButton_config.setObjectName("pushButton_config")
        self.label_type = QtWidgets.QLabel(Top_file_generator)
        self.label_type.setGeometry(QtCore.QRect(470, 180, 80, 19))
        self.label_type.setText("")
        self.label_type.setObjectName("label_type")

        self.retranslateUi(Top_file_generator)
        QtCore.QMetaObject.connectSlotsByName(Top_file_generator)

    def retranslateUi(self, Top_file_generator):
        _translate = QtCore.QCoreApplication.translate
        Top_file_generator.setWindowTitle(_translate("Top_file_generator", "Dialog"))
        self.label.setText(_translate("Top_file_generator", "Input files"))
        self.label_2.setText(_translate("Top_file_generator", "Top file name"))
        self.pushButton_search.setText(_translate("Top_file_generator", "search"))
        self.pushButton_cancel.setText(_translate("Top_file_generator", "Cancel"))
        self.pushButton_create.setText(_translate("Top_file_generator", "Create"))
        self.pushButton_config.setText(_translate("Top_file_generator", "Config"))
