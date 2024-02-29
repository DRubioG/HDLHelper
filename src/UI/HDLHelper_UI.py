# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HDLHelper_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_HDLHelper(object):
    def setupUi(self, HDLHelper):
        if not HDLHelper.objectName():
            HDLHelper.setObjectName(u"HDLHelper")
        HDLHelper.resize(639, 757)
        self.horizontalLayoutWidget = QWidget(HDLHelper)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(50, 40, 541, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.testbench_generator_button = QPushButton(self.horizontalLayoutWidget)
        self.testbench_generator_button.setObjectName(u"testbench_generator_button")

        self.horizontalLayout.addWidget(self.testbench_generator_button)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.calculator_button = QPushButton(self.horizontalLayoutWidget)
        self.calculator_button.setObjectName(u"calculator_button")

        self.horizontalLayout.addWidget(self.calculator_button)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.top_file_generator_button = QPushButton(self.horizontalLayoutWidget)
        self.top_file_generator_button.setObjectName(u"top_file_generator_button")

        self.horizontalLayout.addWidget(self.top_file_generator_button)

        self.horizontalLayoutWidget_2 = QWidget(HDLHelper)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(50, 140, 541, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ticks_calculator_button = QPushButton(self.horizontalLayoutWidget_2)
        self.ticks_calculator_button.setObjectName(u"ticks_calculator_button")

        self.horizontalLayout_2.addWidget(self.ticks_calculator_button)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.hdl_translator_button = QPushButton(self.horizontalLayoutWidget_2)
        self.hdl_translator_button.setObjectName(u"hdl_translator_button")

        self.horizontalLayout_2.addWidget(self.hdl_translator_button)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.hdl_generator_button = QPushButton(self.horizontalLayoutWidget_2)
        self.hdl_generator_button.setObjectName(u"hdl_generator_button")

        self.horizontalLayout_2.addWidget(self.hdl_generator_button)

        self.horizontalLayoutWidget_3 = QWidget(HDLHelper)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(50, 240, 546, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.editor_button = QPushButton(self.horizontalLayoutWidget_3)
        self.editor_button.setObjectName(u"editor_button")

        self.horizontalLayout_3.addWidget(self.editor_button)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.documentation_generator_button = QPushButton(self.horizontalLayoutWidget_3)
        self.documentation_generator_button.setObjectName(u"documentation_generator_button")

        self.horizontalLayout_3.addWidget(self.documentation_generator_button)

        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.analize_dependencies_button = QPushButton(self.horizontalLayoutWidget_3)
        self.analize_dependencies_button.setObjectName(u"analize_dependencies_button")

        self.horizontalLayout_3.addWidget(self.analize_dependencies_button)

        self.horizontalLayoutWidget_4 = QWidget(HDLHelper)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(50, 340, 541, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.generate_state_machine_button = QPushButton(self.horizontalLayoutWidget_4)
        self.generate_state_machine_button.setObjectName(u"generate_state_machine_button")

        self.horizontalLayout_4.addWidget(self.generate_state_machine_button)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.ascii_conversor_button = QPushButton(self.horizontalLayoutWidget_4)
        self.ascii_conversor_button.setObjectName(u"ascii_conversor_button")
        self.ascii_conversor_button.setEnabled(True)

        self.horizontalLayout_4.addWidget(self.ascii_conversor_button)

        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.auto_improve_button = QPushButton(self.horizontalLayoutWidget_4)
        self.auto_improve_button.setObjectName(u"auto_improve_button")
        self.auto_improve_button.setEnabled(True)

        self.horizontalLayout_4.addWidget(self.auto_improve_button)

        self.horizontalLayoutWidget_5 = QWidget(HDLHelper)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(50, 440, 541, 80))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.axi_generator_button = QPushButton(self.horizontalLayoutWidget_5)
        self.axi_generator_button.setObjectName(u"axi_generator_button")

        self.horizontalLayout_5.addWidget(self.axi_generator_button)

        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.shape_generator_button = QPushButton(self.horizontalLayoutWidget_5)
        self.shape_generator_button.setObjectName(u"shape_generator_button")
        self.shape_generator_button.setEnabled(True)

        self.horizontalLayout_5.addWidget(self.shape_generator_button)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.antirrebotes_button = QPushButton(self.horizontalLayoutWidget_5)
        self.antirrebotes_button.setObjectName(u"antirrebotes_button")
        self.antirrebotes_button.setEnabled(True)

        self.horizontalLayout_5.addWidget(self.antirrebotes_button)

        self.horizontalLayoutWidget_6 = QWidget(HDLHelper)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(50, 540, 541, 80))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.clock_divisor_button = QPushButton(self.horizontalLayoutWidget_6)
        self.clock_divisor_button.setObjectName(u"clock_divisor_button")

        self.horizontalLayout_6.addWidget(self.clock_divisor_button)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_11)

        self.filter_generator_button = QPushButton(self.horizontalLayoutWidget_6)
        self.filter_generator_button.setObjectName(u"filter_generator_button")
        self.filter_generator_button.setEnabled(True)

        self.horizontalLayout_6.addWidget(self.filter_generator_button)

        self.horizontalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)

        self.auto_improve_button_3 = QPushButton(self.horizontalLayoutWidget_6)
        self.auto_improve_button_3.setObjectName(u"auto_improve_button_3")
        self.auto_improve_button_3.setEnabled(True)

        self.horizontalLayout_6.addWidget(self.auto_improve_button_3)

        self.horizontalLayoutWidget_7 = QWidget(HDLHelper)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(50, 640, 541, 80))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.clock_divisor_button_2 = QPushButton(self.horizontalLayoutWidget_7)
        self.clock_divisor_button_2.setObjectName(u"clock_divisor_button_2")

        self.horizontalLayout_7.addWidget(self.clock_divisor_button_2)

        self.horizontalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)

        self.filter_generator_button_2 = QPushButton(self.horizontalLayoutWidget_7)
        self.filter_generator_button_2.setObjectName(u"filter_generator_button_2")
        self.filter_generator_button_2.setEnabled(True)

        self.horizontalLayout_7.addWidget(self.filter_generator_button_2)

        self.horizontalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_14)

        self.auto_improve_button_4 = QPushButton(self.horizontalLayoutWidget_7)
        self.auto_improve_button_4.setObjectName(u"auto_improve_button_4")
        self.auto_improve_button_4.setEnabled(True)

        self.horizontalLayout_7.addWidget(self.auto_improve_button_4)

        self.label = QLabel(HDLHelper)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 630, 131, 17))
        font = QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.label.setFont(font)

        self.retranslateUi(HDLHelper)

        QMetaObject.connectSlotsByName(HDLHelper)
    # setupUi

    def retranslateUi(self, HDLHelper):
        HDLHelper.setWindowTitle(QCoreApplication.translate("HDLHelper", u"Dialog", None))
        self.testbench_generator_button.setText(QCoreApplication.translate("HDLHelper", u"Testbench generator", None))
        self.calculator_button.setText(QCoreApplication.translate("HDLHelper", u"Calculator", None))
        self.top_file_generator_button.setText(QCoreApplication.translate("HDLHelper", u"Top file generator", None))
        self.ticks_calculator_button.setText(QCoreApplication.translate("HDLHelper", u"Ticks calculator", None))
        self.hdl_translator_button.setText(QCoreApplication.translate("HDLHelper", u".v <-> .vhd", None))
        self.hdl_generator_button.setText(QCoreApplication.translate("HDLHelper", u"HDL generator", None))
        self.editor_button.setText(QCoreApplication.translate("HDLHelper", u"Editor", None))
        self.documentation_generator_button.setText(QCoreApplication.translate("HDLHelper", u"Documentation generator", None))
        self.analize_dependencies_button.setText(QCoreApplication.translate("HDLHelper", u"Analize dependencies", None))
        self.generate_state_machine_button.setText(QCoreApplication.translate("HDLHelper", u"Gen. State Machine", None))
        self.ascii_conversor_button.setText(QCoreApplication.translate("HDLHelper", u"ASCII Conversor", None))
        self.auto_improve_button.setText(QCoreApplication.translate("HDLHelper", u"Reshape code", None))
        self.axi_generator_button.setText(QCoreApplication.translate("HDLHelper", u"AXI generator", None))
        self.shape_generator_button.setText(QCoreApplication.translate("HDLHelper", u"Shapes generator", None))
        self.antirrebotes_button.setText(QCoreApplication.translate("HDLHelper", u"Debounce", None))
        self.clock_divisor_button.setText(QCoreApplication.translate("HDLHelper", u"Prescaler clock", None))
        self.filter_generator_button.setText(QCoreApplication.translate("HDLHelper", u"Filter generator", None))
        self.auto_improve_button_3.setText(QCoreApplication.translate("HDLHelper", u"VHDL type conversor", None))
        self.clock_divisor_button_2.setText(QCoreApplication.translate("HDLHelper", u"Control Engineering", None))
        self.filter_generator_button_2.setText(QCoreApplication.translate("HDLHelper", u"Power Control", None))
        self.auto_improve_button_4.setText(QCoreApplication.translate("HDLHelper", u"Communication", None))
        self.label.setText(QCoreApplication.translate("HDLHelper", u"Specific fields", None))
    # retranslateUi

