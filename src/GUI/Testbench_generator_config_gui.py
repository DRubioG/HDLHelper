from PyQt5.QtWidgets import QDialog
from UI.Testbench_generator_config_UI import *
import json

class Testbench_generator_config_gui(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_testbench_generator_config()
        self.ui.setupUi(self)
        self.open_config()
        self.load_config()
        self.connections()
        self.show()


    def open_config(self):
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
            self.uppercase_generics = self.data["Testbench_generator"][0]["uppercase_generics"]
            self.uppercase_ports = self.data["Testbench_generator"][0]["uppercase_ports"]
            self.default_config = self.data["Testbench_generator"][0]["default_config"]
            self.comments = self.data["Testbench_generator"][0]["comments"]
        except:
            self.ui.pushButton_save.setEnabled(False)
            self.ui.label_config_file.setText("configuration.json doesn't exist")
            self.version = "87"
            self.tab_spaces = "tab"
            self.spaces = "4"
            self.ftext = ""
            self.etext = ""
            self.uppercase_generics = "True"
            self.uppercase_ports = "False"
            self.default_config = ""
            self.comments = "False"
            

    def load_config(self):
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

        self.ui.textEdit_default_config.setText(self.default_config)


    def tab_space(self):
        if self.ui.radioButton_spaces.isChecked():
            self.ui.lineEdit_number_spaces.setText(str(self.spaces))
            self.ui.lineEdit_number_spaces.setEnabled(True)
        else:
            self.ui.lineEdit_number_spaces.setEnabled(False)


    def connections(self):
        self.ui.pushButton_save.clicked.connect(self.save_file)
        self.ui.pushButton_cancel.clicked.connect(self.cancel)
        self.ui.radioButton_spaces.toggled.connect(self.tab_space)
    

    def cancel(self):
        self.close()
    

    def save_file(self):
        file = open("./config/configuration.json", 'r')

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

        self.data["Testbench_generator"][0]["default_config"] = self.ui.textEdit_default_config.toPlainText()

        json.dump(self.data, file, indent=4)
        file.close()
        self.close()
