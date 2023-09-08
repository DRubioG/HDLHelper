import os
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore

from UI.HDLHelper_preferences_UI import *
from UI.StyleSheet.StyleSheet_testbench_generator import testbench_generator_gui

class HDLHelper_preferences_gui(QWidget):
    """
    This class configures the GUI of the preferences options. Preferences option 
    takes every options of the tools and put together
    """
    def __init__(self):
        # self.setStyleSheet(testbench_generator_gui)
        self.ui = Ui_HDLHelper_preferences()
        self.ui.setupUi(self)
        self.open_config()
        self.load_config()
        self.connections()
        self.show()

    def connections(self):
        """
        This option connects the UI with the operational methods
        """
        self.ui.pushButton_cancel.clicked.connect(self.cancel)
        self.ui.pushButton_Ok.clicked.connect(self.ok)


    def ok(self):
        """
        This method configures ok button
        """
        # self.save_file()
        pass

    def cancel(self):
        """
        This method configures cancel button
        """
        self.close()
    
    def open_config(self):
        """
        This method configures opening of config file
        """
        pass

    def load_config():
        """
        This method configures the interface with options in json file
        """
        pass