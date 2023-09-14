import os
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore

from UI.HDLHelper_preferences_UI import *
from UI.StyleSheet.StyleSheet_testbench_generator import testbench_generator_gui

import json

class HDLHelper_preferences_gui(QWidget):
    """
    This class configures the GUI of the preferences options. Preferences option 
    takes every options of the tools and put together
    """
    def __init__(self):
        # self.setStyleSheet(testbench_generator_gui)
        super().__init__()
        self.ui = Ui_HDLHelper_preferences()
        self.ui.setupUi(self)
        self.read_config()
        self.load_config()
        self.connections()
        self.show()

    def connections(self):
        """
        This option connects the UI with the operational methods
        """
        self.ui.pushButton_cancel.clicked.connect(self.cancel_fn)
        self.ui.pushButton_save.clicked.connect(self.save_fn)


    def save_fn(self):
        """
        This method configures ok button
        """
        # self.save_file()
        pass

    def cancel_fn(self):
        """
        This method configures cancel button
        """
        self.close()
    
    def read_config(self):
        """
        This method configures opening of config file
        """
        try:
            file = open("./config/configuration.json", "r")
            self.data = json.load(file)

            self.tool_comments = self.data["preferences"][0]["tool_comments"]
            self.user = self.data["preferences"][0]["user"]
            self.corporation = self.data["preferences"][0]["corporation"]
            self.contact = self.data["preferences"][0]["contact"]
            self.user_version = self.data["preferences"][0]["user_version"]
            self.tool_version = self.data["preferences"][0]["tool_version"]
            self.date = self.data["preferences"][0]["date"]
        except:
            self.tool_comments = "False"
            self.user = ""
            self.corporation = ""
            self.contact = ""
            self.user_version = ""
            self.tool_version = "False"
            self.date = "False"
            

    def load_config(self):
        """
        This method configures the interface with options in json file
        """
        self.ui.lineEdit_user.setText(self.user)
        self.ui.lineEdit_contact.setText(self.contact)
        self.ui.lineEdit_corpation.setText(self.corporation)

        if self.date == "True":
            self.ui.checkBox_date.setChecked(True)
        else:
            self.ui.checkBox_date.setChecked(False)
        
        if self.tool_version == "True":
            self.ui.checkBox_version_fl.setChecked(True)
        else:
            self.ui.checkBox_version_fl.setChecked(False)