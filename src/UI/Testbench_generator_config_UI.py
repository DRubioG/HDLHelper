# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Testbench_generator_config_UI.ui'
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
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_testbench_generator_config(object):
    def setupUi(self, testbench_generator_config):
        if not testbench_generator_config.objectName():
            testbench_generator_config.setObjectName(u"testbench_generator_config")
        testbench_generator_config.resize(476, 660)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(testbench_generator_config.sizePolicy().hasHeightForWidth())
        testbench_generator_config.setSizePolicy(sizePolicy)
        self.groupBox_version = QGroupBox(testbench_generator_config)
        self.groupBox_version.setObjectName(u"groupBox_version")
        self.groupBox_version.setGeometry(QRect(20, 40, 391, 71))
        self.horizontalLayoutWidget = QWidget(self.groupBox_version)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 30, 321, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton_87 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_87.setObjectName(u"radioButton_87")

        self.horizontalLayout.addWidget(self.radioButton_87)

        self.radioButton_93 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_93.setObjectName(u"radioButton_93")

        self.horizontalLayout.addWidget(self.radioButton_93)

        self.radioButton_08 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_08.setObjectName(u"radioButton_08")

        self.horizontalLayout.addWidget(self.radioButton_08)

        self.radioButton_mixed = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_mixed.setObjectName(u"radioButton_mixed")

        self.horizontalLayout.addWidget(self.radioButton_mixed)

        self.groupBox_tab_space = QGroupBox(testbench_generator_config)
        self.groupBox_tab_space.setObjectName(u"groupBox_tab_space")
        self.groupBox_tab_space.setGeometry(QRect(20, 130, 301, 71))
        self.horizontalLayoutWidget_2 = QWidget(self.groupBox_tab_space)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 30, 241, 38))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton_tab = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_tab.setObjectName(u"radioButton_tab")

        self.horizontalLayout_2.addWidget(self.radioButton_tab)

        self.radioButton_spaces = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_spaces.setObjectName(u"radioButton_spaces")

        self.horizontalLayout_2.addWidget(self.radioButton_spaces)

        self.lineEdit_number_spaces = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_number_spaces.setObjectName(u"lineEdit_number_spaces")

        self.horizontalLayout_2.addWidget(self.lineEdit_number_spaces)

        self.comboBox_language = QComboBox(testbench_generator_config)
        self.comboBox_language.addItem("")
        self.comboBox_language.addItem("")
        self.comboBox_language.setObjectName(u"comboBox_language")
        self.comboBox_language.setGeometry(QRect(330, 10, 100, 30))
        self.groupBox_3 = QGroupBox(testbench_generator_config)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 220, 301, 71))
        self.horizontalLayoutWidget_3 = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(20, 30, 263, 38))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_begin = QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_begin.setObjectName(u"lineEdit_begin")
        self.lineEdit_begin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_begin)

        self.label = QLabel(self.horizontalLayoutWidget_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit_end = QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_end.setObjectName(u"lineEdit_end")

        self.horizontalLayout_3.addWidget(self.lineEdit_end)

        self.pushButton_save = QPushButton(testbench_generator_config)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(340, 610, 91, 31))
        self.pushButton_cancel = QPushButton(testbench_generator_config)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setGeometry(QRect(230, 610, 91, 31))
        self.textEdit_default_config = QTextEdit(testbench_generator_config)
        self.textEdit_default_config.setObjectName(u"textEdit_default_config")
        self.textEdit_default_config.setGeometry(QRect(20, 480, 411, 111))
        self.label_2 = QLabel(testbench_generator_config)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 460, 211, 17))
        self.label_config_file = QLabel(testbench_generator_config)
        self.label_config_file.setObjectName(u"label_config_file")
        self.label_config_file.setGeometry(QRect(60, 500, 361, 31))
        font = QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.label_config_file.setFont(font)
        self.groupBox = QGroupBox(testbench_generator_config)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 310, 301, 101))
        self.checkBox_uppercase_generics = QCheckBox(self.groupBox)
        self.checkBox_uppercase_generics.setObjectName(u"checkBox_uppercase_generics")
        self.checkBox_uppercase_generics.setGeometry(QRect(10, 30, 281, 23))
        self.checkBox_uppercase_ports = QCheckBox(self.groupBox)
        self.checkBox_uppercase_ports.setObjectName(u"checkBox_uppercase_ports")
        self.checkBox_uppercase_ports.setGeometry(QRect(10, 50, 291, 23))
        self.checkBox_comments = QCheckBox(self.groupBox)
        self.checkBox_comments.setObjectName(u"checkBox_comments")
        self.checkBox_comments.setGeometry(QRect(10, 70, 291, 23))
        self.radioButton_regenerate = QRadioButton(self.groupBox)
        self.radioButton_regenerate.setObjectName(u"radioButton_regenerate")
        self.radioButton_regenerate.setGeometry(QRect(10, 0, 131, 23))
        self.radioButton_copy = QRadioButton(self.groupBox)
        self.radioButton_copy.setObjectName(u"radioButton_copy")
        self.radioButton_copy.setGeometry(QRect(210, 0, 101, 23))
        self.checkBox_tool_coments = QCheckBox(testbench_generator_config)
        self.checkBox_tool_coments.setObjectName(u"checkBox_tool_coments")
        self.checkBox_tool_coments.setGeometry(QRect(20, 610, 181, 23))
        self.checkBox_signal_constant = QCheckBox(testbench_generator_config)
        self.checkBox_signal_constant.setObjectName(u"checkBox_signal_constant")
        self.checkBox_signal_constant.setGeometry(QRect(30, 420, 241, 25))
        self.groupBox.raise_()
        self.groupBox_version.raise_()
        self.groupBox_tab_space.raise_()
        self.comboBox_language.raise_()
        self.groupBox_3.raise_()
        self.pushButton_save.raise_()
        self.pushButton_cancel.raise_()
        self.textEdit_default_config.raise_()
        self.label_2.raise_()
        self.label_config_file.raise_()
        self.checkBox_tool_coments.raise_()
        self.checkBox_signal_constant.raise_()

        self.retranslateUi(testbench_generator_config)

        QMetaObject.connectSlotsByName(testbench_generator_config)
    # setupUi

    def retranslateUi(self, testbench_generator_config):
        testbench_generator_config.setWindowTitle(QCoreApplication.translate("testbench_generator_config", u"Testbench Generator Config", None))
        self.groupBox_version.setTitle(QCoreApplication.translate("testbench_generator_config", u"Version", None))
        self.radioButton_87.setText(QCoreApplication.translate("testbench_generator_config", u"'87", None))
        self.radioButton_93.setText(QCoreApplication.translate("testbench_generator_config", u"'93", None))
        self.radioButton_08.setText(QCoreApplication.translate("testbench_generator_config", u"'08", None))
        self.radioButton_mixed.setText(QCoreApplication.translate("testbench_generator_config", u"Mixed", None))
        self.groupBox_tab_space.setTitle(QCoreApplication.translate("testbench_generator_config", u"Tab/space", None))
        self.radioButton_tab.setText(QCoreApplication.translate("testbench_generator_config", u"tab", None))
        self.radioButton_spaces.setText(QCoreApplication.translate("testbench_generator_config", u"spaces", None))
        self.comboBox_language.setItemText(0, QCoreApplication.translate("testbench_generator_config", u"VHDL", None))
        self.comboBox_language.setItemText(1, QCoreApplication.translate("testbench_generator_config", u"Verilog", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("testbench_generator_config", u"Testbench port names", None))
        self.label.setText(QCoreApplication.translate("testbench_generator_config", u"<port name>", None))
        self.pushButton_save.setText(QCoreApplication.translate("testbench_generator_config", u"Save", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("testbench_generator_config", u"Cancel", None))
        self.label_2.setText(QCoreApplication.translate("testbench_generator_config", u"Default configuration ", None))
        self.label_config_file.setText("")
        self.groupBox.setTitle("")
        self.checkBox_uppercase_generics.setText(QCoreApplication.translate("testbench_generator_config", u"Capital letters for generics", None))
        self.checkBox_uppercase_ports.setText(QCoreApplication.translate("testbench_generator_config", u"Capital letters for ports", None))
        self.checkBox_comments.setText(QCoreApplication.translate("testbench_generator_config", u"Regenerate with comments", None))
        self.radioButton_regenerate.setText(QCoreApplication.translate("testbench_generator_config", u"Regenerate", None))
        self.radioButton_copy.setText(QCoreApplication.translate("testbench_generator_config", u"Copy", None))
        self.checkBox_tool_coments.setText(QCoreApplication.translate("testbench_generator_config", u"Tool comments", None))
        self.checkBox_signal_constant.setText(QCoreApplication.translate("testbench_generator_config", u"Split generics and ports", None))
    # retranslateUi

