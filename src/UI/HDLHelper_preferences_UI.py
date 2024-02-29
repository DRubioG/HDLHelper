# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HDLHelper_preferences_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_HDLHelper_preferences(object):
    def setupUi(self, HDLHelper_preferences):
        if not HDLHelper_preferences.objectName():
            HDLHelper_preferences.setObjectName(u"HDLHelper_preferences")
        HDLHelper_preferences.resize(404, 476)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HDLHelper_preferences.sizePolicy().hasHeightForWidth())
        HDLHelper_preferences.setSizePolicy(sizePolicy)
        HDLHelper_preferences.setMaximumSize(QSize(404, 476))
        icon = QIcon()
        icon.addFile(u"../../../img/logo/icon2.png", QSize(), QIcon.Normal, QIcon.Off)
        HDLHelper_preferences.setWindowIcon(icon)
        self.groupBox = QGroupBox(HDLHelper_preferences)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 30, 331, 281))
        self.lineEdit_user = QLineEdit(self.groupBox)
        self.lineEdit_user.setObjectName(u"lineEdit_user")
        self.lineEdit_user.setGeometry(QRect(120, 40, 201, 25))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 51, 17))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 80, 101, 17))
        self.lineEdit_corpation = QLineEdit(self.groupBox)
        self.lineEdit_corpation.setObjectName(u"lineEdit_corpation")
        self.lineEdit_corpation.setGeometry(QRect(120, 80, 201, 25))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 120, 91, 17))
        self.lineEdit_contact = QLineEdit(self.groupBox)
        self.lineEdit_contact.setObjectName(u"lineEdit_contact")
        self.lineEdit_contact.setGeometry(QRect(120, 120, 201, 25))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 160, 91, 17))
        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(120, 160, 201, 25))
        self.checkBox_version_fl = QCheckBox(self.groupBox)
        self.checkBox_version_fl.setObjectName(u"checkBox_version_fl")
        self.checkBox_version_fl.setGeometry(QRect(10, 200, 201, 23))
        self.checkBox_version_fl.setChecked(True)
        self.checkBox_date = QCheckBox(self.groupBox)
        self.checkBox_date.setObjectName(u"checkBox_date")
        self.checkBox_date.setGeometry(QRect(10, 230, 201, 23))
        self.checkBox_date.setChecked(True)
        self.pushButton_cancel = QPushButton(HDLHelper_preferences)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setGeometry(QRect(279, 420, 101, 27))
        self.pushButton_save = QPushButton(HDLHelper_preferences)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(170, 420, 100, 27))

        self.retranslateUi(HDLHelper_preferences)

        QMetaObject.connectSlotsByName(HDLHelper_preferences)
    # setupUi

    def retranslateUi(self, HDLHelper_preferences):
        HDLHelper_preferences.setWindowTitle(QCoreApplication.translate("HDLHelper_preferences", u"Preferences", None))
        self.groupBox.setTitle(QCoreApplication.translate("HDLHelper_preferences", u"Comments", None))
        self.lineEdit_user.setInputMask("")
        self.lineEdit_user.setText("")
        self.label_2.setText(QCoreApplication.translate("HDLHelper_preferences", u"User", None))
        self.label_3.setText(QCoreApplication.translate("HDLHelper_preferences", u"Corporation", None))
        self.lineEdit_corpation.setInputMask("")
        self.lineEdit_corpation.setText("")
        self.label_4.setText(QCoreApplication.translate("HDLHelper_preferences", u"Contact", None))
        self.lineEdit_contact.setInputMask("")
        self.lineEdit_contact.setText("")
        self.label_5.setText(QCoreApplication.translate("HDLHelper_preferences", u"Version", None))
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setText("")
        self.checkBox_version_fl.setText(QCoreApplication.translate("HDLHelper_preferences", u"Version of HDLHelper", None))
        self.checkBox_date.setText(QCoreApplication.translate("HDLHelper_preferences", u"Add date", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("HDLHelper_preferences", u"Cancel", None))
        self.pushButton_save.setText(QCoreApplication.translate("HDLHelper_preferences", u"Save", None))
    # retranslateUi

