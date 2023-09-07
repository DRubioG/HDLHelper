# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Testbench_overwrite_UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Testbench_overwrite(object):
    def setupUi(self, Testbench_overwrite):
        Testbench_overwrite.setObjectName("Testbench_overwrite")
        Testbench_overwrite.resize(497, 156)
        self.label = QtWidgets.QLabel(Testbench_overwrite)
        self.label.setGeometry(QtCore.QRect(50, 50, 431, 21))
        self.label.setObjectName("label")
        self.pushButton_accept = QtWidgets.QPushButton(Testbench_overwrite)
        self.pushButton_accept.setGeometry(QtCore.QRect(360, 110, 100, 27))
        self.pushButton_accept.setObjectName("pushButton_accept")
        self.checkBox = QtWidgets.QCheckBox(Testbench_overwrite)
        self.checkBox.setGeometry(QtCore.QRect(50, 110, 141, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Testbench_overwrite)
        QtCore.QMetaObject.connectSlotsByName(Testbench_overwrite)

    def retranslateUi(self, Testbench_overwrite):
        _translate = QtCore.QCoreApplication.translate
        Testbench_overwrite.setWindowTitle(_translate("Testbench_overwrite", "Dialog"))
        self.label.setText(_translate("Testbench_overwrite", "You are going to overwrite the previous testbench."))
        self.pushButton_accept.setText(_translate("Testbench_overwrite", "Accept"))
        self.checkBox.setText(_translate("Testbench_overwrite", "Do not show again"))
