import os
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore

from UI.HDLHelper_preferences_UI import *
from UI.StyleSheet.StyleSheet_testbench_generator import testbench_generator_gui

class HDLHelper_preferences_gui(QWidget):
    def __init__(self):
        # self.setStyleSheet(testbench_generator_gui)
        self.ui = Ui_HDLHelper_preferences()
        self.ui.setupUi(self)
        self.open_config()
        self.load_config()
        self.connections()
        self.show()

    def connections(self):
        self.ui.pushButton_cancel.clicked.connect(self.cancel)
        self.ui.pushButton_Ok.clicked.connect(self.ok)


    def ok(self):
        self.save_file()

    def cancel(self):
        self.close()
    
    def open_config(self):
        pass

    def load_config():
        pass