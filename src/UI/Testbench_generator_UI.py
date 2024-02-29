# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Testbench_generator_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Testbench_generator(object):
    def setupUi(self, Testbench_generator):
        if not Testbench_generator.objectName():
            Testbench_generator.setObjectName(u"Testbench_generator")
        Testbench_generator.resize(523, 250)
        self.label_input = QLabel(Testbench_generator)
        self.label_input.setObjectName(u"label_input")
        self.label_input.setGeometry(QRect(30, 80, 60, 17))
        font = QFont()
        font.setPointSize(10)
        self.label_input.setFont(font)
        self.label_output = QLabel(Testbench_generator)
        self.label_output.setObjectName(u"label_output")
        self.label_output.setGeometry(QRect(30, 140, 81, 17))
        self.label_output.setFont(font)
        self.lineEdit_input = QLineEdit(Testbench_generator)
        self.lineEdit_input.setObjectName(u"lineEdit_input")
        self.lineEdit_input.setGeometry(QRect(110, 80, 261, 21))
        self.lineEdit_output = QLineEdit(Testbench_generator)
        self.lineEdit_output.setObjectName(u"lineEdit_output")
        self.lineEdit_output.setGeometry(QRect(110, 140, 261, 21))
        self.pushButton_input = QPushButton(Testbench_generator)
        self.pushButton_input.setObjectName(u"pushButton_input")
        self.pushButton_input.setGeometry(QRect(400, 70, 95, 36))
        self.pushButton_input.setFont(font)
        self.pushButton_output = QPushButton(Testbench_generator)
        self.pushButton_output.setObjectName(u"pushButton_output")
        self.pushButton_output.setGeometry(QRect(400, 130, 95, 36))
        self.pushButton_output.setFont(font)
        self.pushButton_cancel = QPushButton(Testbench_generator)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setGeometry(QRect(400, 190, 95, 36))
        self.pushButton_cancel.setFont(font)
        self.pushButton_create = QPushButton(Testbench_generator)
        self.pushButton_create.setObjectName(u"pushButton_create")
        self.pushButton_create.setGeometry(QRect(290, 190, 95, 36))
        self.pushButton_create.setFont(font)
        self.pushButton_config = QPushButton(Testbench_generator)
        self.pushButton_config.setObjectName(u"pushButton_config")
        self.pushButton_config.setGeometry(QRect(180, 190, 95, 36))
        self.pushButton_config.setFont(font)

        self.retranslateUi(Testbench_generator)

        QMetaObject.connectSlotsByName(Testbench_generator)
    # setupUi

    def retranslateUi(self, Testbench_generator):
        Testbench_generator.setWindowTitle(QCoreApplication.translate("Testbench_generator", u"Testbench Generator", None))
        self.label_input.setText(QCoreApplication.translate("Testbench_generator", u"Input File", None))
        self.label_output.setText(QCoreApplication.translate("Testbench_generator", u"Output File", None))
        self.pushButton_input.setText(QCoreApplication.translate("Testbench_generator", u"search", None))
        self.pushButton_output.setText(QCoreApplication.translate("Testbench_generator", u"search", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Testbench_generator", u"Cancel", None))
        self.pushButton_create.setText(QCoreApplication.translate("Testbench_generator", u"Create", None))
        self.pushButton_config.setText(QCoreApplication.translate("Testbench_generator", u"Config", None))
    # retranslateUi

