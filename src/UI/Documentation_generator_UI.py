# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Documentation_generator_UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Documentation_generator(object):
    def setupUi(self, Documentation_generator):
        Documentation_generator.setObjectName("Documentation_generator")
        Documentation_generator.resize(366, 357)
        self.pushButton_input = QtWidgets.QPushButton(Documentation_generator)
        self.pushButton_input.setGeometry(QtCore.QRect(240, 60, 100, 27))
        self.pushButton_input.setObjectName("pushButton_input")
        self.pushButton_cancel = QtWidgets.QPushButton(Documentation_generator)
        self.pushButton_cancel.setGeometry(QtCore.QRect(130, 310, 100, 27))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_accept = QtWidgets.QPushButton(Documentation_generator)
        self.pushButton_accept.setGeometry(QtCore.QRect(240, 310, 100, 27))
        self.pushButton_accept.setObjectName("pushButton_accept")
        self.comboBox_templates = QtWidgets.QComboBox(Documentation_generator)
        self.comboBox_templates.setGeometry(QtCore.QRect(140, 120, 161, 27))
        self.comboBox_templates.setObjectName("comboBox_templates")
        self.label_2 = QtWidgets.QLabel(Documentation_generator)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 79, 19))
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(Documentation_generator)
        self.checkBox.setGeometry(QtCore.QRect(40, 170, 181, 25))
        self.checkBox.setObjectName("checkBox")
        self.groupBox = QtWidgets.QGroupBox(Documentation_generator)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 341, 80))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_file = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_file.setGeometry(QtCore.QRect(10, 40, 201, 27))
        self.lineEdit_file.setObjectName("lineEdit_file")
        self.groupBox_2 = QtWidgets.QGroupBox(Documentation_generator)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 210, 341, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_output = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_output.setGeometry(QtCore.QRect(10, 40, 201, 27))
        self.lineEdit_output.setObjectName("lineEdit_output")
        self.pushButton_output = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_output.setGeometry(QtCore.QRect(230, 40, 100, 27))
        self.pushButton_output.setObjectName("pushButton_output")
        self.groupBox.raise_()
        self.pushButton_input.raise_()
        self.pushButton_cancel.raise_()
        self.pushButton_accept.raise_()
        self.comboBox_templates.raise_()
        self.label_2.raise_()
        self.checkBox.raise_()
        self.groupBox_2.raise_()

        self.retranslateUi(Documentation_generator)
        QtCore.QMetaObject.connectSlotsByName(Documentation_generator)

    def retranslateUi(self, Documentation_generator):
        _translate = QtCore.QCoreApplication.translate
        Documentation_generator.setWindowTitle(_translate("Documentation_generator", "Documentation generator"))
        self.pushButton_input.setText(_translate("Documentation_generator", "Search"))
        self.pushButton_cancel.setText(_translate("Documentation_generator", "Cancel"))
        self.pushButton_accept.setText(_translate("Documentation_generator", "Accept"))
        self.label_2.setText(_translate("Documentation_generator", "Template"))
        self.checkBox.setText(_translate("Documentation_generator", "Add source code"))
        self.groupBox.setTitle(_translate("Documentation_generator", "File"))
        self.groupBox_2.setTitle(_translate("Documentation_generator", "Output"))
        self.pushButton_output.setText(_translate("Documentation_generator", "Search"))
