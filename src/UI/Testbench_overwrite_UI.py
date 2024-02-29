# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Testbench_overwrite_UI.ui'
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

class Ui_Testbench_overwrite(object):
    def setupUi(self, Testbench_overwrite):
        if not Testbench_overwrite.objectName():
            Testbench_overwrite.setObjectName(u"Testbench_overwrite")
        Testbench_overwrite.resize(497, 156)
        self.label = QLabel(Testbench_overwrite)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 50, 431, 21))
        self.pushButton_accept = QPushButton(Testbench_overwrite)
        self.pushButton_accept.setObjectName(u"pushButton_accept")
        self.pushButton_accept.setGeometry(QRect(360, 110, 100, 27))
        self.checkBox = QCheckBox(Testbench_overwrite)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(50, 110, 141, 25))
        font = QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)

        self.retranslateUi(Testbench_overwrite)

        QMetaObject.connectSlotsByName(Testbench_overwrite)
    # setupUi

    def retranslateUi(self, Testbench_overwrite):
        Testbench_overwrite.setWindowTitle(QCoreApplication.translate("Testbench_overwrite", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Testbench_overwrite", u"You are going to overwrite the previous testbench.", None))
        self.pushButton_accept.setText(QCoreApplication.translate("Testbench_overwrite", u"Accept", None))
        self.checkBox.setText(QCoreApplication.translate("Testbench_overwrite", u"Do not show again", None))
    # retranslateUi

