import sys
from tkinter import X
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLineEdit, QFileDialog,
QLabel, QAction, QCheckBox, QDialog, QVBoxLayout)
from PyQt5 import QtCore, Qt, QtWidgets, QtGui
from StyleSheet import style_sheet


class Testbench_gui(QDialog):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.show()


    def initializeUI(self):
        
        self.resize(523,250)

        self.setWindowTitle('Testbench Generator')
        #self.main_label = QLabel(self)
       # self.main_label.setText("TESTBENCH GENERATOR")
       # self.main_label.setGeometry(QtCore.QRect(150, 10, 400, 20))#   10,100, 150, 150))
        #self.setCentralWidget(self.main_label)

        x, y, w, h  = 10, 50, 60, 70
        dist = 65
    
    # Label
        self.label_input = QLabel(self)
        self.label_input.setText("Input File")
        self.label_input.setGeometry(QtCore.QRect(30, 80, 60, 17))

        self.label_output = QLabel(self)
        self.label_output.setText("Output File")
        self.label_output.setGeometry(QtCore.QRect(30, 140, 70, 17))

    #QLineEdit
        x, y, w, h  = x+70, y+15, 330, 21
        self.lineEdit_input = QLineEdit(self)
        self.lineEdit_input.setGeometry(QtCore.QRect(110, 80, 261, 21))

        self.lineEdit_output = QLineEdit(self)
        self.lineEdit_output.setGeometry(QtCore.QRect(110, 140, 261, 21))

    # Buttons
        x, y, w, h = x+w+10, y, 60, 36
        self.pushButton_input = QPushButton("search", self)
        self.pushButton_input.setGeometry(QtCore.QRect(400, 70, 95, 36))
        self.pushButton_input.setObjectName("pushButton_input")
        self.pushButton_input.setToolTip('Input file')

        self.pushButton_output = QPushButton("search", self)
        self.pushButton_output.setGeometry(QtCore.QRect(400, 130, 95, 36))
        self.pushButton_output.setObjectName("pushButton_output")
        

        self.pushButton_create = QPushButton("Create", self)
        self.pushButton_create.setGeometry(QtCore.QRect(300, y+dist*2, 95, 36))
        self.pushButton_create.setObjectName("pushButton_create")
        
        self.pushButton_cancel = QPushButton("Cancel", self)
        self.pushButton_cancel.setGeometry(QtCore.QRect(409, y+dist*2, 95, 36))
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.pushButton_config = QPushButton("Config", self)
        self.pushButton_config.setGeometry(QtCore.QRect(190, y+dist*2, 95, 36))
        self.pushButton_config.setObjectName("pushButton_config")

    
if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    w = Testbench_gui()
    w.show()
    sys.exit(app.exec_())