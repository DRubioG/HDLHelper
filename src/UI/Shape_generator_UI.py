# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Shape_generator_UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Shape_generator(object):
    def setupUi(self, Shape_generator):
        Shape_generator.setObjectName("Shape_generator")
        Shape_generator.resize(673, 513)
        self.tabWidget = QtWidgets.QTabWidget(Shape_generator)
        self.tabWidget.setGeometry(QtCore.QRect(9, 9, 651, 488))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_triangle = QtWidgets.QWidget()
        self.tab_triangle.setObjectName("tab_triangle")
        self.tabWidget.addTab(self.tab_triangle, "")
        self.tab_positive_saw = QtWidgets.QWidget()
        self.tab_positive_saw.setObjectName("tab_positive_saw")
        self.tabWidget.addTab(self.tab_positive_saw, "")

        self.retranslateUi(Shape_generator)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Shape_generator)

    def retranslateUi(self, Shape_generator):
        _translate = QtCore.QCoreApplication.translate
        Shape_generator.setWindowTitle(_translate("Shape_generator", "Shape Generator"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_triangle), _translate("Shape_generator", "Triangle"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_positive_saw), _translate("Shape_generator", "Positive saw"))
