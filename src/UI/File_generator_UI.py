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
        self.textEdit_text.setReadOnly(True)
        self.textEdit_text.setObjectName("textEdit_text")
        self.comboBox_port_generic = QtWidgets.QComboBox(File_generator_ui)
        self.comboBox_port_generic.setGeometry(QtCore.QRect(10, 540, 91, 25))
        self.comboBox_port_generic.setObjectName("comboBox_port_generic")
        self.comboBox_port_generic.addItem("")
        self.comboBox_port_generic.addItem("")
        self.lineEdit_name = QtWidgets.QLineEdit(File_generator_ui)
        self.lineEdit_name.setGeometry(QtCore.QRect(110, 540, 91, 25))
        self.lineEdit_name.setText("")
        self.lineEdit_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.comboBox_type = QtWidgets.QComboBox(File_generator_ui)
        self.comboBox_type.setGeometry(QtCore.QRect(290, 540, 101, 25))
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.lineEdit_bits = QtWidgets.QLineEdit(File_generator_ui)
        self.lineEdit_bits.setGeometry(QtCore.QRect(402, 540, 31, 25))
        self.lineEdit_bits.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_bits.setAutoFillBackground(False)
        self.lineEdit_bits.setText("")
        self.lineEdit_bits.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
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
        self.lineEdit_entity.setGeometry(QtCore.QRect(100, 280, 91, 25))
        self.lineEdit_entity.setText("")
        self.lineEdit_entity.setObjectName("lineEdit_entity")
        self.lineEdit_architecture = QtWidgets.QLineEdit(File_generator_ui)
        self.lineEdit_architecture.setGeometry(QtCore.QRect(320, 280, 131, 25))
        self.lineEdit_architecture.setText("")
        self.lineEdit_architecture.setReadOnly(True)
        self.lineEdit_architecture.setObjectName("lineEdit_architecture")
        self.radioButton_sort = QtWidgets.QRadioButton(File_generator_ui)
        self.radioButton_sort.setGeometry(QtCore.QRect(460, 280, 61, 23))
        self.radioButton_sort.setObjectName("radioButton_sort")
        self.comboBox_inout = QtWidgets.QComboBox(File_generator_ui)
        self.comboBox_inout.setGeometry(QtCore.QRect(210, 540, 71, 25))
        self.comboBox_inout.setObjectName("comboBox_inout")
        self.comboBox_inout.addItem("")
        self.comboBox_inout.addItem("")
        self.comboBox_inout.addItem("")
        self.tableWidget_content = QtWidgets.QTableWidget(File_generator_ui)
        self.tableWidget_content.setGeometry(QtCore.QRect(20, 310, 491, 201))
        self.tableWidget_content.setObjectName("tableWidget_content")
        self.tableWidget_content.setColumnCount(0)
        self.tableWidget_content.setRowCount(0)
        self.label = QtWidgets.QLabel(File_generator_ui)
        self.label.setGeometry(QtCore.QRect(20, 520, 71, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(File_generator_ui)
        self.label_2.setGeometry(QtCore.QRect(140, 520, 41, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_inout = QtWidgets.QLabel(File_generator_ui)
        self.label_inout.setGeometry(QtCore.QRect(210, 520, 71, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_inout.setFont(font)
        self.label_inout.setObjectName("label_inout")
        self.label_4 = QtWidgets.QLabel(File_generator_ui)
        self.label_4.setGeometry(QtCore.QRect(330, 520, 71, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(File_generator_ui)
        self.label_5.setGeometry(QtCore.QRect(400, 520, 71, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_comment = QtWidgets.QLineEdit(File_generator_ui)
        self.lineEdit_comment.setGeometry(QtCore.QRect(110, 570, 321, 25))
        self.lineEdit_comment.setText("")
        self.lineEdit_comment.setObjectName("lineEdit_comment")
        self.label_3 = QtWidgets.QLabel(File_generator_ui)
        self.label_3.setGeometry(QtCore.QRect(50, 570, 61, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(File_generator_ui)
        self.label_6.setGeometry(QtCore.QRect(20, 280, 81, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(File_generator_ui)
        self.label_7.setGeometry(QtCore.QRect(200, 280, 111, 19))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tableWidget_content.raise_()
        self.textEdit_text.raise_()
        self.comboBox_port_generic.raise_()
        self.lineEdit_name.raise_()
        self.comboBox_type.raise_()
        self.lineEdit_bits.raise_()
        self.pushButton_add.raise_()
        self.pushButton_create.raise_()
        self.pushButton_cancel.raise_()
        self.pushButton_config.raise_()
        self.lineEdit_entity.raise_()
        self.lineEdit_architecture.raise_()
        self.radioButton_sort.raise_()
        self.comboBox_inout.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_inout.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.lineEdit_comment.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.label_7.raise_()

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
        self.comboBox_inout.setItemText(0, _translate("File_generator_ui", "in"))
        self.comboBox_inout.setItemText(1, _translate("File_generator_ui", "out"))
        self.comboBox_inout.setItemText(2, _translate("File_generator_ui", "inout"))
        self.label.setText(_translate("File_generator_ui", "port/generic"))
        self.label_2.setText(_translate("File_generator_ui", "name"))
        self.label_inout.setText(_translate("File_generator_ui", "in/out/inout"))
        self.label_4.setText(_translate("File_generator_ui", "type"))
        self.label_5.setText(_translate("File_generator_ui", "Nº bits"))
        self.label_3.setText(_translate("File_generator_ui", "comment"))
        self.label_6.setText(_translate("File_generator_ui", "entity name:"))
        self.label_7.setText(_translate("File_generator_ui", "architecture name:"))
