# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HDLHelper_UI.ui'
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
        self.ticks_calculator_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.ticks_calculator_button.setObjectName("ticks_calculator_button")
        self.horizontalLayout_2.addWidget(self.ticks_calculator_button)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.hdl_translator_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.hdl_translator_button.setObjectName("hdl_translator_button")
        self.horizontalLayout_2.addWidget(self.hdl_translator_button)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.hdl_generator_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.hdl_generator_button.setObjectName("hdl_generator_button")
        self.horizontalLayout_2.addWidget(self.hdl_generator_button)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(HDLHelper)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 240, 541, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.visualizer = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.visualizer.setObjectName("visualizer")
        self.horizontalLayout_3.addWidget(self.visualizer)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.documentation_generator_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.documentation_generator_button.setObjectName("documentation_generator_button")
        self.horizontalLayout_3.addWidget(self.documentation_generator_button)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.analize_dependencies_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.analize_dependencies_button.setObjectName("analize_dependencies_button")
        self.horizontalLayout_3.addWidget(self.analize_dependencies_button)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(HDLHelper)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(50, 340, 541, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.generate_state_machine_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.generate_state_machine_button.setObjectName("generate_state_machine_button")
        self.horizontalLayout_4.addWidget(self.generate_state_machine_button)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.empty_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.empty_2.setEnabled(False)
        self.empty_2.setText("")
        self.empty_2.setObjectName("empty_2")
        self.horizontalLayout_4.addWidget(self.empty_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.empty = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.empty.setEnabled(False)
        self.empty.setText("")
        self.empty.setObjectName("empty")
        self.horizontalLayout_4.addWidget(self.empty)

        self.retranslateUi(HDLHelper)
        QtCore.QMetaObject.connectSlotsByName(HDLHelper)

    def retranslateUi(self, HDLHelper):
        _translate = QtCore.QCoreApplication.translate
        HDLHelper.setWindowTitle(_translate("HDLHelper", "Dialog"))
        self.testbench_generator_button.setText(_translate("HDLHelper", "Testbench generator"))
        self.calculator_button.setText(_translate("HDLHelper", "Calculator"))
        self.top_file_generator_button.setText(_translate("HDLHelper", "Top file generator"))
        self.ticks_calculator_button.setText(_translate("HDLHelper", "Ticks calculator"))
        self.hdl_translator_button.setText(_translate("HDLHelper", ".v <-> .vhd"))
        self.hdl_generator_button.setText(_translate("HDLHelper", "HDL generator"))
        self.visualizer.setText(_translate("HDLHelper", "Visualizer"))
        self.documentation_generator_button.setText(_translate("HDLHelper", "Documentation generator"))
        self.analize_dependencies_button.setText(_translate("HDLHelper", "Analize dependencies"))
        self.generate_state_machine_button.setText(_translate("HDLHelper", "Gen. State Machine"))
