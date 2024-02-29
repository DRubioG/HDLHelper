# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Top_file_generator_UI.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Top_file_generator(object):
    def setupUi(self, Top_file_generator):
        if not Top_file_generator.objectName():
            Top_file_generator.setObjectName(u"Top_file_generator")
        Top_file_generator.resize(589, 298)
        self.label = QLabel(Top_file_generator)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 90, 81, 17))
        self.label_2 = QLabel(Top_file_generator)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 180, 111, 17))
        self.comboBox_files = QComboBox(Top_file_generator)
        self.comboBox_files.setObjectName(u"comboBox_files")
        self.comboBox_files.setGeometry(QRect(140, 80, 301, 36))
        self.lineEdit_name_file = QLineEdit(Top_file_generator)
        self.lineEdit_name_file.setObjectName(u"lineEdit_name_file")
        self.lineEdit_name_file.setGeometry(QRect(140, 170, 301, 36))
        self.pushButton_search = QPushButton(Top_file_generator)
        self.pushButton_search.setObjectName(u"pushButton_search")
        self.pushButton_search.setGeometry(QRect(480, 80, 95, 36))
        self.pushButton_cancel = QPushButton(Top_file_generator)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setGeometry(QRect(470, 240, 95, 36))
        self.pushButton_create = QPushButton(Top_file_generator)
        self.pushButton_create.setObjectName(u"pushButton_create")
        self.pushButton_create.setGeometry(QRect(360, 240, 95, 36))
        self.pushButton_config = QPushButton(Top_file_generator)
        self.pushButton_config.setObjectName(u"pushButton_config")
        self.pushButton_config.setGeometry(QRect(250, 240, 95, 36))
        self.label_type = QLabel(Top_file_generator)
        self.label_type.setObjectName(u"label_type")
        self.label_type.setGeometry(QRect(470, 180, 80, 19))

        self.retranslateUi(Top_file_generator)

        QMetaObject.connectSlotsByName(Top_file_generator)
    # setupUi

    def retranslateUi(self, Top_file_generator):
        Top_file_generator.setWindowTitle(QCoreApplication.translate("Top_file_generator", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Top_file_generator", u"Input files", None))
        self.label_2.setText(QCoreApplication.translate("Top_file_generator", u"Top file name", None))
        self.pushButton_search.setText(QCoreApplication.translate("Top_file_generator", u"search", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Top_file_generator", u"Cancel", None))
        self.pushButton_create.setText(QCoreApplication.translate("Top_file_generator", u"Create", None))
        self.pushButton_config.setText(QCoreApplication.translate("Top_file_generator", u"Config", None))
        self.label_type.setText("")
    # retranslateUi

