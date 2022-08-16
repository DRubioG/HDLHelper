# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/HDLHelper_UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HDLHelper(object):
    def setupUi(self, HDLHelper):
        HDLHelper.setObjectName("HDLHelper")
        HDLHelper.resize(639, 462)
        self.horizontalLayoutWidget = QtWidgets.QWidget(HDLHelper)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 40, 541, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.testbench_generator_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.testbench_generator_button.setObjectName("testbench_generator_button")
        self.horizontalLayout.addWidget(self.testbench_generator_button)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.calculator_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.calculator_button.setObjectName("calculator_button")
        self.horizontalLayout.addWidget(self.calculator_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.top_file_generator_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.top_file_generator_button.setObjectName("top_file_generator_button")
        self.horizontalLayout.addWidget(self.top_file_generator_button)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(HDLHelper)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 140, 541, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.retranslateUi(HDLHelper)
        QtCore.QMetaObject.connectSlotsByName(HDLHelper)

    def retranslateUi(self, HDLHelper):
        _translate = QtCore.QCoreApplication.translate
        HDLHelper.setWindowTitle(_translate("HDLHelper", "Dialog"))
        self.testbench_generator_button.setText(_translate("HDLHelper", "Testbench generator"))
        self.calculator_button.setText(_translate("HDLHelper", "Calculator"))
        self.top_file_generator_button.setText(_translate("HDLHelper", "Top file generator"))
