# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'File_generator_UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_File_generator_ui(object):
    def setupUi(self, File_generator_ui):
        File_generator_ui.setObjectName("File_generator_ui")
        File_generator_ui.resize(526, 635)
        self.textEdit_text = QtWidgets.QTextEdit(File_generator_ui)
        self.textEdit_text.setGeometry(QtCore.QRect(20, 20, 491, 251))
        self.textEdit_text.setObjectName("textEdit_text")
        self.tableView_content = QtWidgets.QTableView(File_generator_ui)
        self.tableView_content.setGeometry(QtCore.QRect(20, 310, 491, 201))
        self.tableView_content.setObjectName("tableView_content")
        self.comboBox_port_generic = QtWidgets.QComboBox(File_generator_ui)
        self.comboBox_port_generic.setGeometry(QtCore.QRect(20, 540, 79, 25))
        self.comboBox_port_generic.setObjectName("comboBox_port_generic")
        self.comboBox_port_generic.addItem("")
        self.comboBox_port_generic.addItem("")
        self.lineEdit_name = QtWidgets.QLineEdit(File_generator_ui)
        self.lineEdit_name.setGeometry(QtCore.QRect(110, 540, 141, 25))
        self.lineEdit_name.setText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.comboBox_type = QtWidgets.QComboBox(File_generator_ui)
        self.comboBox_type.setGeometry(QtCore.QRect(260, 540, 101, 25))
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.lineEdit_bits = QtWidgets.QLineEdit(File_generator_ui)
        self.lineEdit_bits.setGeometry(QtCore.QRect(372, 540, 61, 25))
        self.lineEdit_bits.setText("")
        self.lineEdit_bits.setObjectName("lineEdit_bits")
        self.pushButton_add = QtWidgets.QPushButton(File_generator_ui)
        self.pushButton_add.setGeometry(QtCore.QRect(440, 540, 80, 25))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_create = QtWidgets.QPushButton(File_generator_ui)
        self.pushButton_create.setGeometry(QtCore.QRect(340, 600, 80, 25))
        self.pushButton_create.setObjectName("pushButton_create")
        self.pushButton_cancel = QtWidgets.QPushButton(File_generator_ui)
        self.pushButton_cancel.setGeometry(QtCore.QRect(430, 600, 80, 25))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_config = QtWidgets.QPushButton(File_generator_ui)
        self.pushButton_config.setGeometry(QtCore.QRect(250, 600, 80, 25))
        self.pushButton_config.setObjectName("pushButton_config")
        self.lineEdit_entity = QtWidgets.QLineEdit(File_generator_ui)
        self.lineEdit_entity.setGeometry(QtCore.QRect(20, 280, 151, 25))
        self.lineEdit_entity.setText("")
        self.lineEdit_entity.setObjectName("lineEdit_entity")
        self.lineEdit_architecture = QtWidgets.QLineEdit(File_generator_ui)
        self.lineEdit_architecture.setGeometry(QtCore.QRect(180, 280, 191, 25))
        self.lineEdit_architecture.setText("")
        self.lineEdit_architecture.setObjectName("lineEdit_architecture")
        self.radioButton_sort = QtWidgets.QRadioButton(File_generator_ui)
        self.radioButton_sort.setGeometry(QtCore.QRect(400, 280, 101, 23))
        self.radioButton_sort.setObjectName("radioButton_sort")

        self.retranslateUi(File_generator_ui)
        QtCore.QMetaObject.connectSlotsByName(File_generator_ui)

    def retranslateUi(self, File_generator_ui):
        _translate = QtCore.QCoreApplication.translate
        File_generator_ui.setWindowTitle(_translate("File_generator_ui", "Dialog"))
        self.comboBox_port_generic.setItemText(0, _translate("File_generator_ui", "port"))
        self.comboBox_port_generic.setItemText(1, _translate("File_generator_ui", "generic"))
        self.comboBox_type.setItemText(0, _translate("File_generator_ui", "std_logic"))
        self.comboBox_type.setItemText(1, _translate("File_generator_ui", "unsigned"))
        self.comboBox_type.setItemText(2, _translate("File_generator_ui", "integer"))
        self.comboBox_type.setItemText(3, _translate("File_generator_ui", "std_ulogic"))
        self.pushButton_add.setText(_translate("File_generator_ui", "Add"))
        self.pushButton_create.setText(_translate("File_generator_ui", "Create"))
        self.pushButton_cancel.setText(_translate("File_generator_ui", "Cancel"))
        self.pushButton_config.setText(_translate("File_generator_ui", "Config"))
        self.radioButton_sort.setText(_translate("File_generator_ui", "Sort"))
