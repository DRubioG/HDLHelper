# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pulse_calculator_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_Pulses_calculator(object):
    def setupUi(self, Pulses_calculator):
        if not Pulses_calculator.objectName():
            Pulses_calculator.setObjectName(u"Pulses_calculator")
        Pulses_calculator.resize(589, 350)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Pulses_calculator.sizePolicy().hasHeightForWidth())
        Pulses_calculator.setSizePolicy(sizePolicy)
        self.lineEdit_f_p_global = QLineEdit(Pulses_calculator)
        self.lineEdit_f_p_global.setObjectName(u"lineEdit_f_p_global")
        self.lineEdit_f_p_global.setGeometry(QRect(70, 110, 91, 36))
        self.lineEdit_f_p_global.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_f_p_local = QLineEdit(Pulses_calculator)
        self.lineEdit_f_p_local.setObjectName(u"lineEdit_f_p_local")
        self.lineEdit_f_p_local.setGeometry(QRect(70, 180, 91, 36))
        self.lineEdit_f_p_local.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.comboBox_f_p_general = QComboBox(Pulses_calculator)
        self.comboBox_f_p_general.addItem("")
        self.comboBox_f_p_general.addItem("")
        self.comboBox_f_p_general.addItem("")
        self.comboBox_f_p_general.addItem("")
        self.comboBox_f_p_general.setObjectName(u"comboBox_f_p_general")
        self.comboBox_f_p_general.setGeometry(QRect(180, 110, 81, 36))
        self.label = QLabel(Pulses_calculator)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 120, 41, 17))
        self.label_2 = QLabel(Pulses_calculator)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 190, 41, 17))
        self.pushButton_calculate = QPushButton(Pulses_calculator)
        self.pushButton_calculate.setObjectName(u"pushButton_calculate")
        self.pushButton_calculate.setGeometry(QRect(470, 290, 95, 36))
        self.pushButton_cancel = QPushButton(Pulses_calculator)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setGeometry(QRect(350, 290, 95, 36))
        self.label_4 = QLabel(Pulses_calculator)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 40, 71, 17))
        self.radioButton_frequency = QRadioButton(Pulses_calculator)
        self.radioButton_frequency.setObjectName(u"radioButton_frequency")
        self.radioButton_frequency.setGeometry(QRect(120, 30, 104, 23))
        self.radioButton_frequency.setChecked(True)
        self.radioButton_pulses = QRadioButton(Pulses_calculator)
        self.radioButton_pulses.setObjectName(u"radioButton_pulses")
        self.radioButton_pulses.setGeometry(QRect(120, 60, 104, 23))
        self.comboBox_f_p_local = QComboBox(Pulses_calculator)
        self.comboBox_f_p_local.addItem("")
        self.comboBox_f_p_local.addItem("")
        self.comboBox_f_p_local.addItem("")
        self.comboBox_f_p_local.addItem("")
        self.comboBox_f_p_local.setObjectName(u"comboBox_f_p_local")
        self.comboBox_f_p_local.setGeometry(QRect(180, 180, 81, 36))
        self.comboBox_seconds_general = QComboBox(Pulses_calculator)
        self.comboBox_seconds_general.addItem("")
        self.comboBox_seconds_general.addItem("")
        self.comboBox_seconds_general.addItem("")
        self.comboBox_seconds_general.addItem("")
        self.comboBox_seconds_general.setObjectName(u"comboBox_seconds_general")
        self.comboBox_seconds_general.setGeometry(QRect(440, 110, 81, 36))
        self.lineEdit_seconds_local = QLineEdit(Pulses_calculator)
        self.lineEdit_seconds_local.setObjectName(u"lineEdit_seconds_local")
        self.lineEdit_seconds_local.setGeometry(QRect(330, 180, 91, 36))
        self.lineEdit_seconds_local.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_seconds_general = QLineEdit(Pulses_calculator)
        self.lineEdit_seconds_general.setObjectName(u"lineEdit_seconds_general")
        self.lineEdit_seconds_general.setGeometry(QRect(330, 110, 91, 36))
        self.lineEdit_seconds_general.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.comboBox_seconds_local = QComboBox(Pulses_calculator)
        self.comboBox_seconds_local.addItem("")
        self.comboBox_seconds_local.addItem("")
        self.comboBox_seconds_local.addItem("")
        self.comboBox_seconds_local.addItem("")
        self.comboBox_seconds_local.setObjectName(u"comboBox_seconds_local")
        self.comboBox_seconds_local.setGeometry(QRect(440, 180, 81, 36))
        self.label_5 = QLabel(Pulses_calculator)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 230, 31, 17))
        self.label_6 = QLabel(Pulses_calculator)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 260, 41, 17))
        self.binary_result = QLabel(Pulses_calculator)
        self.binary_result.setObjectName(u"binary_result")
        self.binary_result.setGeometry(QRect(70, 230, 141, 17))
        self.hexadecimal_result = QLabel(Pulses_calculator)
        self.hexadecimal_result.setObjectName(u"hexadecimal_result")
        self.hexadecimal_result.setGeometry(QRect(70, 260, 141, 17))

        self.retranslateUi(Pulses_calculator)

        QMetaObject.connectSlotsByName(Pulses_calculator)
    # setupUi

    def retranslateUi(self, Pulses_calculator):
        Pulses_calculator.setWindowTitle(QCoreApplication.translate("Pulses_calculator", u"Pulses_calculator", None))
        self.comboBox_f_p_general.setItemText(0, QCoreApplication.translate("Pulses_calculator", u"MHz", None))
        self.comboBox_f_p_general.setItemText(1, QCoreApplication.translate("Pulses_calculator", u"Hz", None))
        self.comboBox_f_p_general.setItemText(2, QCoreApplication.translate("Pulses_calculator", u"kHz", None))
        self.comboBox_f_p_general.setItemText(3, QCoreApplication.translate("Pulses_calculator", u"GHz", None))

        self.comboBox_f_p_general.setCurrentText(QCoreApplication.translate("Pulses_calculator", u"MHz", None))
        self.label.setText(QCoreApplication.translate("Pulses_calculator", u"<-->", None))
        self.label_2.setText(QCoreApplication.translate("Pulses_calculator", u"<-->", None))
        self.pushButton_calculate.setText(QCoreApplication.translate("Pulses_calculator", u"Calculate", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Pulses_calculator", u"Cancel", None))
        self.label_4.setText(QCoreApplication.translate("Pulses_calculator", u"Seconds", None))
        self.radioButton_frequency.setText(QCoreApplication.translate("Pulses_calculator", u"Frequency", None))
        self.radioButton_pulses.setText(QCoreApplication.translate("Pulses_calculator", u"Pulses", None))
        self.comboBox_f_p_local.setItemText(0, QCoreApplication.translate("Pulses_calculator", u"Hz", None))
        self.comboBox_f_p_local.setItemText(1, QCoreApplication.translate("Pulses_calculator", u"kHz", None))
        self.comboBox_f_p_local.setItemText(2, QCoreApplication.translate("Pulses_calculator", u"MHz", None))
        self.comboBox_f_p_local.setItemText(3, QCoreApplication.translate("Pulses_calculator", u"GHz", None))

        self.comboBox_seconds_general.setItemText(0, QCoreApplication.translate("Pulses_calculator", u"sec", None))
        self.comboBox_seconds_general.setItemText(1, QCoreApplication.translate("Pulses_calculator", u"msec", None))
        self.comboBox_seconds_general.setItemText(2, QCoreApplication.translate("Pulses_calculator", u"usec", None))
        self.comboBox_seconds_general.setItemText(3, QCoreApplication.translate("Pulses_calculator", u"nsec", None))

        self.comboBox_seconds_local.setItemText(0, QCoreApplication.translate("Pulses_calculator", u"sec", None))
        self.comboBox_seconds_local.setItemText(1, QCoreApplication.translate("Pulses_calculator", u"msec", None))
        self.comboBox_seconds_local.setItemText(2, QCoreApplication.translate("Pulses_calculator", u"usec", None))
        self.comboBox_seconds_local.setItemText(3, QCoreApplication.translate("Pulses_calculator", u"nsec", None))

        self.label_5.setText(QCoreApplication.translate("Pulses_calculator", u"Bin:", None))
        self.label_6.setText(QCoreApplication.translate("Pulses_calculator", u"Hex:", None))
        self.binary_result.setText("")
        self.hexadecimal_result.setText("")
    # retranslateUi

