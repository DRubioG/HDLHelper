# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Testbench_generator_config_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_testbench_generator_config(object):
    def setupUi(self, testbench_generator_config):
        testbench_generator_config.setObjectName("testbench_generator_config")
        testbench_generator_config.resize(476, 402)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(testbench_generator_config.sizePolicy().hasHeightForWidth())
        testbench_generator_config.setSizePolicy(sizePolicy)
        self.groupBox_version = QtWidgets.QGroupBox(testbench_generator_config)
        self.groupBox_version.setGeometry(QtCore.QRect(20, 40, 311, 71))
        self.groupBox_version.setObjectName("groupBox_version")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_version)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 261, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_87 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_87.setObjectName("radioButton_87")
        self.horizontalLayout.addWidget(self.radioButton_87)
        self.radioButton_93 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_93.setObjectName("radioButton_93")
        self.horizontalLayout.addWidget(self.radioButton_93)
        self.radioButton_mixed = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_mixed.setObjectName("radioButton_mixed")
        self.horizontalLayout.addWidget(self.radioButton_mixed)
        self.groupBox_tab_space = QtWidgets.QGroupBox(testbench_generator_config)
        self.groupBox_tab_space.setGeometry(QtCore.QRect(20, 130, 301, 71))
        self.groupBox_tab_space.setObjectName("groupBox_tab_space")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_tab_space)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 241, 38))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_tab = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_tab.setObjectName("radioButton_tab")
        self.horizontalLayout_2.addWidget(self.radioButton_tab)
        self.radioButton_spaces = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_spaces.setObjectName("radioButton_spaces")
        self.horizontalLayout_2.addWidget(self.radioButton_spaces)
        self.lineEdit_number_spaces = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_number_spaces.setObjectName("lineEdit_number_spaces")
        self.horizontalLayout_2.addWidget(self.lineEdit_number_spaces)
        self.comboBox_language = QtWidgets.QComboBox(testbench_generator_config)
        self.comboBox_language.setGeometry(QtCore.QRect(330, 10, 100, 30))
        self.comboBox_language.setObjectName("comboBox_language")
        self.comboBox_language.addItem("")
        self.comboBox_language.addItem("")
        self.groupBox_3 = QtWidgets.QGroupBox(testbench_generator_config)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 220, 301, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 30, 263, 38))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_begin = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_begin.setObjectName("lineEdit_begin")
        self.horizontalLayout_3.addWidget(self.lineEdit_begin)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit_end = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_end.setObjectName("lineEdit_end")
        self.horizontalLayout_3.addWidget(self.lineEdit_end)
        self.pushButton_save = QtWidgets.QPushButton(testbench_generator_config)
        self.pushButton_save.setGeometry(QtCore.QRect(370, 360, 91, 31))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_cancel = QtWidgets.QPushButton(testbench_generator_config)
        self.pushButton_cancel.setGeometry(QtCore.QRect(260, 360, 91, 31))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.checkBox_uppercase_generics = QtWidgets.QCheckBox(testbench_generator_config)
        self.checkBox_uppercase_generics.setGeometry(QtCore.QRect(30, 310, 181, 23))
        self.checkBox_uppercase_generics.setObjectName("checkBox_uppercase_generics")
        self.checkBox_uppercase_ports = QtWidgets.QCheckBox(testbench_generator_config)
        self.checkBox_uppercase_ports.setGeometry(QtCore.QRect(30, 340, 161, 23))
        self.checkBox_uppercase_ports.setObjectName("checkBox_uppercase_ports")

        self.retranslateUi(testbench_generator_config)
        QtCore.QMetaObject.connectSlotsByName(testbench_generator_config)

    def retranslateUi(self, testbench_generator_config):
        _translate = QtCore.QCoreApplication.translate
        testbench_generator_config.setWindowTitle(_translate("testbench_generator_config", "Testbench Generator Config"))
        self.groupBox_version.setTitle(_translate("testbench_generator_config", "Version"))
        self.radioButton_87.setText(_translate("testbench_generator_config", "\'87"))
        self.radioButton_93.setText(_translate("testbench_generator_config", "\'93"))
        self.radioButton_mixed.setText(_translate("testbench_generator_config", "Mixed"))
        self.groupBox_tab_space.setTitle(_translate("testbench_generator_config", "Tab/space"))
        self.radioButton_tab.setText(_translate("testbench_generator_config", "tab"))
        self.radioButton_spaces.setText(_translate("testbench_generator_config", "spaces"))
        self.comboBox_language.setItemText(0, _translate("testbench_generator_config", "VHDL"))
        self.comboBox_language.setItemText(1, _translate("testbench_generator_config", "Verilog"))
        self.groupBox_3.setTitle(_translate("testbench_generator_config", "Testbench ports name"))
        self.label.setText(_translate("testbench_generator_config", "<port name>"))
        self.pushButton_save.setText(_translate("testbench_generator_config", "Save"))
        self.pushButton_cancel.setText(_translate("testbench_generator_config", "Cancel"))
        self.checkBox_uppercase_generics.setText(_translate("testbench_generator_config", "Uppercase for generics"))
        self.checkBox_uppercase_ports.setText(_translate("testbench_generator_config", "Uppercase for ports"))
