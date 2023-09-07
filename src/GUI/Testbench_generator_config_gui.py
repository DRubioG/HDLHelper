from PyQt5.QtWidgets import QDialog
from UI.Testbench_generator_config_UI import *
from UI.StyleSheet.StyleSheet_testbench_generator_config import testbench_generator_config_gui

import json

class Testbench_generator_config_gui(QDialog):
    """
    This class executes the config interface
    """
    def __init__(self):
        super().__init__()
        self.setStyleSheet(testbench_generator_config_gui)
        self.ui = Ui_testbench_generator_config()
        self.ui.setupUi(self)
        self.open_config()
        self.load_config()
        self.connections()
        self.show()


    def open_config(self):
        """
        This method opens the config file
        """
        try:
            file = open("./config/configuration.json", "r")
            self.data = json.load(file)
            self.ui.pushButton_save.setEnabled(True)
            self.ui.label_config_file.setText("")
            self.version = self.data["Testbench_generator"][0]["version"]
            self.tab_spaces = self.data["Testbench_generator"][0]["tab_spaces"]
            self.spaces = self.data["Testbench_generator"][0]["spaces"]
            self.ftext = self.data["Testbench_generator"][0]["ftext"]
            self.etext = self.data["Testbench_generator"][0]["etext"]
            self.copy = self.data["Testbench_generator"][0]["copy"]
            self.uppercase_generics = self.data["Testbench_generator"][0]["uppercase_generics"]
            self.uppercase_ports = self.data["Testbench_generator"][0]["uppercase_ports"]
            self.default_config = self.data["Testbench_generator"][0]["default_config"]
            self.comments = self.data["Testbench_generator"][0]["comments"]
            self.tool_comments = self.data["Testbench_generator"][0]["tool_comments"]
            self.split_signal_constant = self.data["Testbench_generator"][0]["split_signal_constant"]
        except:
            self.ui.comboBox_language.setEnabled(False)
            self.ui.pushButton_save.setEnabled(False)
            self.ui.groupBox_tab_space.setEnabled(False)
            self.ui.groupBox_version.setEnabled(False)
            self.ui.groupBox_3.setEnabled(False)
            self.ui.checkBox_comments.setEnabled(False)
            self.ui.checkBox_uppercase_generics.setEnabled(False)
            self.ui.checkBox_uppercase_ports.setEnabled(False)
            self.ui.textEdit_default_config.setEnabled(False)
            self.ui.checkBox_tool_coments.setEnabled(False)
            self.ui.label_config_file.setText("configuration.json doesn't exist")
            self.ui.groupBox.setEnabled(False)
            self.ui.checkBox_signal_constant.setEnabled(False)
            self.version = "87"
            self.tab_spaces = "tab"
            self.spaces = "4"
            self.ftext = ""
            self.etext = ""
            self.copy = "False"
            self.uppercase_generics = "True"
            self.uppercase_ports = "False"
            self.default_config = ""
            self.comments = "False"
            self.tool_comments = "True"
            self.split_signal_constant = "True"
            

    def load_config(self):
        """
        This method changes the user interface with the configuration 
        """
        self.ui.radioButton_08.setCheckable(False)
        if self.version == "87":
            self.ui.radioButton_87.setChecked(True)
        elif self.version == "93":
            self.ui.radioButton_93.setChecked(True)
        elif self.version == "08":
            self.ui.radioButton_08.setChecked(True)
        else:
            self.ui.radioButton_mixed.setChecked(True)
        
        if self.tab_spaces == "tab":
            self.ui.radioButton_tab.setChecked(True)
            self.ui.lineEdit_number_spaces.setEnabled(False)
        else:
            self.ui.radioButton_spaces.setChecked(True)
            self.ui.lineEdit_number_spaces.setText(str(self.spaces))
            self.ui.lineEdit_number_spaces.setEnabled(True)
        
        self.ui.lineEdit_begin.setText(self.ftext)
        self.ui.lineEdit_end.setText(self.etext)

        if self.copy == "True":
            self.ui.radioButton_copy.setChecked(True)
            self.ui.radioButton_regenerate.setChecked(False)
            self.ui.checkBox_comments.setEnabled(False)
            self.ui.checkBox_uppercase_generics.setEnabled(False)
            self.ui.checkBox_uppercase_ports.setEnabled(False)
        else:
            self.ui.radioButton_copy.setChecked(False)
            self.ui.radioButton_regenerate.setChecked(True)
            self.ui.checkBox_comments.setEnabled(True)
            self.ui.checkBox_uppercase_generics.setEnabled(True)
            self.ui.checkBox_uppercase_ports.setEnabled(True)

        if self.split_signal_constant == "True":
            self.ui.checkBox_signal_constant.setChecked(True)
        else:
            self.ui.checkBox_signal_constant.setChecked(False)

        if self.uppercase_generics == "True":
            self.ui.checkBox_uppercase_generics.setChecked(True)
        else:
            self.ui.checkBox_uppercase_generics.setChecked(False)

        if self.uppercase_ports == "True":
            self.ui.checkBox_uppercase_ports.setChecked(True)
        else:
            self.ui.checkBox_uppercase_ports.setChecked(False)    

        if self.comments == "True":
            self.ui.checkBox_comments.setChecked(True)
        else:
            self.ui.checkBox_comments.setChecked(False) 

        if self.tool_comments == "True":
            self.ui.checkBox_tool_coments.setChecked(True)
        else:
            self.ui.checkBox_tool_coments.setChecked(False)
        self.ui.textEdit_default_config.setText(self.default_config)


    def tab_space(self):
        """
        This method changes tab option
        """
        if self.ui.radioButton_spaces.isChecked():
            self.ui.lineEdit_number_spaces.setText(str(self.spaces))
            self.ui.lineEdit_number_spaces.setEnabled(True)
        else:
            self.ui.lineEdit_number_spaces.setEnabled(False)


    def copy_option(self):
        """
        This method configures the copy options
        """
        if self.ui.radioButton_copy.isChecked():
            self.ui.checkBox_comments.setEnabled(False)
            self.ui.checkBox_uppercase_generics.setEnabled(False)
            self.ui.checkBox_uppercase_ports.setEnabled(False)
        else:
            self.ui.checkBox_comments.setEnabled(True)
            self.ui.checkBox_uppercase_generics.setEnabled(True)
            self.ui.checkBox_uppercase_ports.setEnabled(True)


    def connections(self):
        """
        This method configurates buttons and radius options
        """
        self.ui.pushButton_save.clicked.connect(self.save_file)
        self.ui.pushButton_cancel.clicked.connect(self.cancel)
        self.ui.radioButton_spaces.toggled.connect(self.tab_space)
        self.ui.radioButton_copy.toggled.connect(self.copy_option)
    

    def cancel(self):
        """
        This method configures cancel option
        """
        self.close()
    

    def save_file(self):
        """
        This method configures save option
        """
        file = open("./config/configuration.json", 'w')

        if self.ui.radioButton_87.isChecked():
            self.data["Testbench_generator"][0]["version"] = "87"
        elif self.ui.radioButton_93.isChecked():
            self.data["Testbench_generator"][0]["version"] = "93"
        elif self.ui.radioButton_08.isChecked():
            self.data["Testbench_generator"][0]["version"] = "08"
        else:
            self.data["Testbench_generator"][0]["version"] = "Mixed"

        if self.ui.radioButton_tab.isChecked():
            self.data["Testbench_generator"][0]["tab_spaces"] = "tab"
        else: 
            self.data["Testbench_generator"][0]["tab_spaces"] = "spaces"
            self.data["Testbench_generator"][0]["spaces"] = self.ui.lineEdit_number_spaces.text()

        self.data["Testbench_generator"][0]["ftext"] = self.ui.lineEdit_begin.text()
        self.data["Testbench_generator"][0]["etext"] = self.ui.lineEdit_end.text()

        if self.ui.checkBox_signal_constant.isChecked() == True:
            self.data["Testbench_generator"][0]["split_signal_constant"] = "True"
        else:
            self.data["Testbench_generator"][0]["split_signal_constant"] = "False"

        if self.ui.checkBox_uppercase_generics.isChecked() == True:
            self.data["Testbench_generator"][0]["uppercase_generics"] = "True"
        else:
            self.data["Testbench_generator"][0]["uppercase_generics"] = "False"

        if self.ui.checkBox_uppercase_ports.isChecked() == True:
            self.data["Testbench_generator"][0]["uppercase_ports"] = "True"
        else:
            self.data["Testbench_generator"][0]["uppercase_ports"] = "False"

        if self.ui.checkBox_comments.isChecked() == True:
            self.data["Testbench_generator"][0]["comments"] = "True"
        else:
            self.data["Testbench_generator"][0]["comments"] = "False"

        if self.ui.checkBox_tool_coments.isChecked() == True:
            self.data["Testbench_generator"][0]["tool_comments"] = "True"
        else:
            self.data["Testbench_generator"][0]["tool_comments"] = "False"


        self.data["Testbench_generator"][0]["default_config"] = self.ui.textEdit_default_config.toPlainText()

        json.dump(self.data, file, indent=4)
        file.close()
        self.close()
