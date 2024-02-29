# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'New_version_advise_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog_new_version(object):
    def setupUi(self, Dialog_new_version):
        if not Dialog_new_version.objectName():
            Dialog_new_version.setObjectName(u"Dialog_new_version")
        Dialog_new_version.resize(509, 187)
        self.label = QLabel(Dialog_new_version)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 40, 301, 19))
        self.pushButton_ok = QPushButton(Dialog_new_version)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        self.pushButton_ok.setGeometry(QRect(370, 140, 100, 27))
        self.checkBox_show_again = QCheckBox(Dialog_new_version)
        self.checkBox_show_again.setObjectName(u"checkBox_show_again")
        self.checkBox_show_again.setGeometry(QRect(40, 140, 181, 25))
        font = QFont()
        font.setPointSize(10)
        self.checkBox_show_again.setFont(font)
        self.label_2 = QLabel(Dialog_new_version)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 80, 111, 19))
        self.pushButton_web = QPushButton(Dialog_new_version)
        self.pushButton_web.setObjectName(u"pushButton_web")
        self.pushButton_web.setGeometry(QRect(250, 140, 100, 27))
        self.label_previous_version = QLabel(Dialog_new_version)
        self.label_previous_version.setObjectName(u"label_previous_version")
        self.label_previous_version.setGeometry(QRect(260, 80, 41, 19))
        self.label_4 = QLabel(Dialog_new_version)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(300, 80, 31, 19))
        self.label_new_version = QLabel(Dialog_new_version)
        self.label_new_version.setObjectName(u"label_new_version")
        self.label_new_version.setGeometry(QRect(340, 80, 41, 19))

        self.retranslateUi(Dialog_new_version)

        QMetaObject.connectSlotsByName(Dialog_new_version)
    # setupUi

    def retranslateUi(self, Dialog_new_version):
        Dialog_new_version.setWindowTitle(QCoreApplication.translate("Dialog_new_version", u"New version", None))
        self.label.setText(QCoreApplication.translate("Dialog_new_version", u"New version of HDLHelper", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog_new_version", u"Ok", None))
        self.checkBox_show_again.setText(QCoreApplication.translate("Dialog_new_version", u"Do not show again", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_new_version", u"Your version:", None))
        self.pushButton_web.setText(QCoreApplication.translate("Dialog_new_version", u"Web", None))
        self.label_previous_version.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog_new_version", u"-> ", None))
        self.label_new_version.setText("")
    # retranslateUi

