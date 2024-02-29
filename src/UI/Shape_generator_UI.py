# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Shape_generator_UI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QTabWidget,
    QWidget)

class Ui_Shape_generator(object):
    def setupUi(self, Shape_generator):
        if not Shape_generator.objectName():
            Shape_generator.setObjectName(u"Shape_generator")
        Shape_generator.resize(673, 513)
        self.tabWidget = QTabWidget(Shape_generator)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(9, 9, 651, 488))
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_triangle = QWidget()
        self.tab_triangle.setObjectName(u"tab_triangle")
        self.tabWidget.addTab(self.tab_triangle, "")
        self.tab_positive_saw = QWidget()
        self.tab_positive_saw.setObjectName(u"tab_positive_saw")
        self.tabWidget.addTab(self.tab_positive_saw, "")

        self.retranslateUi(Shape_generator)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Shape_generator)
    # setupUi

    def retranslateUi(self, Shape_generator):
        Shape_generator.setWindowTitle(QCoreApplication.translate("Shape_generator", u"Shape Generator", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_triangle), QCoreApplication.translate("Shape_generator", u"Triangle", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_positive_saw), QCoreApplication.translate("Shape_generator", u"Positive saw", None))
    # retranslateUi

