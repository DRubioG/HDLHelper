# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Testbench_generator_UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Testbench_generator(object):
    def setupUi(self, Testbench_generator):
        Testbench_generator.setObjectName("Testbench_generator")
        Testbench_generator.resize(523, 250)
        self.label_input = QtWidgets.QLabel(Testbench_generator)
        self.label_input.setGeometry(QtCore.QRect(30, 80, 60, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_input.setFont(font)
        self.label_input.setObjectName("label_input")
        self.label_output = QtWidgets.QLabel(Testbench_generator)
        self.label_output.setGeometry(QtCore.QRect(30, 140, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_output.setFont(font)
        self.label_output.setObjectName("label_output")
        self.lineEdit_input = QtWidgets.QLineEdit(Testbench_generator)
        self.lineEdit_input.setGeometry(QtCore.QRect(110, 80, 261, 21))
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.lineEdit_output = QtWidgets.QLineEdit(Testbench_generator)
        self.lineEdit_output.setGeometry(QtCore.QRect(110, 140, 261, 21))
        self.lineEdit_output.setObjectName("lineEdit_output")
        self.pushButton_input = QtWidgets.QPushButton(Testbench_generator)
        self.pushButton_input.setGeometry(QtCore.QRect(400, 70, 95, 36))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_input.setFont(font)
        self.pushButton_input.setObjectName("pushButton_input")
        self.pushButton_output = QtWidgets.QPushButton(Testbench_generator)
        self.pushButton_output.setGeometry(QtCore.QRect(400, 130, 95, 36))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_output.setFont(font)
        self.pushButton_output.setObjectName("pushButton_output")
        self.pushButton_cancel = QtWidgets.QPushButton(Testbench_generator)
        self.pushButton_cancel.setGeometry(QtCore.QRect(400, 190, 95, 36))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_create = QtWidgets.QPushButton(Testbench_generator)
        self.pushButton_create.setGeometry(QtCore.QRect(290, 190, 95, 36))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setObjectName("pushButton_create")
        self.pushButton_config = QtWidgets.QPushButton(Testbench_generator)
        self.pushButton_config.setGeometry(QtCore.QRect(180, 190, 95, 36))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_config.setFont(font)
        self.pushButton_config.setObjectName("pushButton_config")

        self.retranslateUi(Testbench_generator)
        QtCore.QMetaObject.connectSlotsByName(Testbench_generator)

    def retranslateUi(self, Testbench_generator):
        _translate = QtCore.QCoreApplication.translate
        Testbench_generator.setWindowTitle(_translate("Testbench_generator", "Testbench Generator"))
        self.label_input.setText(_translate("Testbench_generator", "Input File"))
        self.label_output.setText(_translate("Testbench_generator", "Output File"))
        self.pushButton_input.setText(_translate("Testbench_generator", "search"))
        self.pushButton_output.setText(_translate("Testbench_generator", "search"))
        self.pushButton_cancel.setText(_translate("Testbench_generator", "Cancel"))
        self.pushButton_create.setText(_translate("Testbench_generator", "Create"))
        self.pushButton_config.setText(_translate("Testbench_generator", "Config"))
