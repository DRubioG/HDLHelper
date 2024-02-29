# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Documentation_generator_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Documentation_generator(object):
    def setupUi(self, Documentation_generator):
        if not Documentation_generator.objectName():
            Documentation_generator.setObjectName(u"Documentation_generator")
        Documentation_generator.resize(366, 429)
        self.pushButton_input = QPushButton(Documentation_generator)
        self.pushButton_input.setObjectName(u"pushButton_input")
        self.pushButton_input.setGeometry(QRect(240, 60, 100, 27))
        self.pushButton_cancel = QPushButton(Documentation_generator)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setGeometry(QRect(130, 390, 100, 27))
        self.pushButton_accept = QPushButton(Documentation_generator)
        self.pushButton_accept.setObjectName(u"pushButton_accept")
        self.pushButton_accept.setGeometry(QRect(240, 390, 100, 27))
        self.comboBox_templates = QComboBox(Documentation_generator)
        self.comboBox_templates.setObjectName(u"comboBox_templates")
        self.comboBox_templates.setGeometry(QRect(140, 120, 161, 27))
        self.label_2 = QLabel(Documentation_generator)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 120, 79, 19))
        self.checkBox = QCheckBox(Documentation_generator)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(40, 170, 181, 25))
        self.groupBox = QGroupBox(Documentation_generator)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 20, 341, 80))
        self.lineEdit_file = QLineEdit(self.groupBox)
        self.lineEdit_file.setObjectName(u"lineEdit_file")
        self.lineEdit_file.setGeometry(QRect(10, 40, 201, 27))
        self.groupBox_2 = QGroupBox(Documentation_generator)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 290, 341, 80))
        self.lineEdit_output = QLineEdit(self.groupBox_2)
        self.lineEdit_output.setObjectName(u"lineEdit_output")
        self.lineEdit_output.setGeometry(QRect(10, 40, 201, 27))
        self.pushButton_output = QPushButton(self.groupBox_2)
        self.pushButton_output.setObjectName(u"pushButton_output")
        self.pushButton_output.setGeometry(QRect(230, 40, 100, 27))
        self.groupBox_3 = QGroupBox(Documentation_generator)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 200, 341, 80))
        self.lineEdit_logo = QLineEdit(self.groupBox_3)
        self.lineEdit_logo.setObjectName(u"lineEdit_logo")
        self.lineEdit_logo.setGeometry(QRect(10, 40, 201, 27))
        self.pushButton_logo = QPushButton(self.groupBox_3)
        self.pushButton_logo.setObjectName(u"pushButton_logo")
        self.pushButton_logo.setGeometry(QRect(230, 40, 100, 27))
        self.checkBox_logo = QCheckBox(self.groupBox_3)
        self.checkBox_logo.setObjectName(u"checkBox_logo")
        self.checkBox_logo.setGeometry(QRect(10, 0, 181, 25))
        self.groupBox.raise_()
        self.pushButton_input.raise_()
        self.pushButton_cancel.raise_()
        self.pushButton_accept.raise_()
        self.comboBox_templates.raise_()
        self.label_2.raise_()
        self.checkBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()

        self.retranslateUi(Documentation_generator)

        QMetaObject.connectSlotsByName(Documentation_generator)
    # setupUi

    def retranslateUi(self, Documentation_generator):
        Documentation_generator.setWindowTitle(QCoreApplication.translate("Documentation_generator", u"Documentation generator", None))
        self.pushButton_input.setText(QCoreApplication.translate("Documentation_generator", u"Search", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Documentation_generator", u"Cancel", None))
        self.pushButton_accept.setText(QCoreApplication.translate("Documentation_generator", u"Accept", None))
        self.label_2.setText(QCoreApplication.translate("Documentation_generator", u"Template", None))
        self.checkBox.setText(QCoreApplication.translate("Documentation_generator", u"Add source code", None))
        self.groupBox.setTitle(QCoreApplication.translate("Documentation_generator", u"File", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Documentation_generator", u"Output", None))
        self.pushButton_output.setText(QCoreApplication.translate("Documentation_generator", u"Search", None))
        self.groupBox_3.setTitle("")
        self.pushButton_logo.setText(QCoreApplication.translate("Documentation_generator", u"Search", None))
        self.checkBox_logo.setText(QCoreApplication.translate("Documentation_generator", u"Logo", None))
    # retranslateUi

