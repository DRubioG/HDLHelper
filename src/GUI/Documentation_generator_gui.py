from PyQt5.QtWidgets import QWidget, QFileDialog

from UI.Documentation_generator_UI import *
from Backend.Documentation_generator import *

import os, json

class Documentation_generator_gui(QWidget):
    """
    This class connects GUI with operational methods
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_Documentation_generator()
        self.ui.setupUi(self)
        self.read_config()
        self.load_config()
        self.connections()
        self.show()
    

    def read_config(self):
        """
        This method reads configuration
        """
        try:
            file = open("./config/configuration.json", "r")
            self.data = json.load(file)
            self.source_code = self.data["Documentation_generator"][0]["source_code"]
            self.templates = self.data["Documentation_generator"][0]["templates"]
            self.current_template = self.data["Documentation_generator"][0]["current_template"]
        except:
            self.source_code = "True"
            self.current_template = "template_basic"
            self.templates = ["template_basic"]
            self.ui.checkBox.setEnabled(False)


    def load_config(self):
        """
        This method loads configuration in GUI
        """
        if self.source_code == "True":
            self.ui.checkBox.setChecked(True)
        
        self.ui.comboBox_templates.addItems(self.templates)
        cont = 0
        for template in self.templates:
            if template == self.current_template:
                index = cont
            cont += 1
        self.ui.comboBox_templates.setCurrentIndex(index)
        

    def connections(self):
        """
        This method connects events of the UI with operational methods
        """
        self.ui.pushButton_accept.clicked.connect(self.accept_fn)
        self.ui.pushButton_cancel.clicked.connect(self.cancel_fn)
        self.ui.pushButton_input.clicked.connect(self.search_input)
        self.ui.pushButton_output.clicked.connect(self.search_output)
        self.ui.checkBox_logo.toggled.connect(self.logo_fn)
        self.ui.lineEdit_output.setReadOnly(True)
        self.ui.lineEdit_file.setReadOnly(True)
        self.ui.pushButton_accept.setEnabled(False)
        self.ui.pushButton_output.setEnabled(False)
        self.ui.lineEdit_logo.setEnabled(False)
        self.ui.pushButton_logo.setEnabled(False)
        

    def logo_fn(self):
        if self.ui.checkBox_logo.isChecked():
            self.ui.lineEdit_logo.setEnabled(True)
            self.ui.pushButton_logo.setEnabled(True)
        else:
            self.ui.lineEdit_logo.setEnabled(False)
            self.ui.pushButton_logo.setEnabled(False)


    def cancel_fn(self):
        """
        This method exits window
        """
        self.close()
    
    def accept_fn(self):
        try:
            file = open("./config/configuration.json", 'w')

            if self.ui.checkBox.isChecked() == True:
                self.data["Documentation_generator"][0]["source_code"] = "True"
            else:
                self.data["Documentation_generator"][0]["source_code"] = "False"

            self.data["Documentation_generator"][0]["current_template"] = self.ui.comboBox_templates.currentText()

            json.dump(self.data, file, indent=4)
            file.close()
        except:
            pass
        documentation = Documentation_generator()
        documentation.generate(self.file_input, self.file_output)

        self.close()


    def search_input(self):
        """
        This method configures input
        """
        fileDialog = QFileDialog()
        files = fileDialog.getOpenFileName(self, "Select file", QtCore.QDir.currentPath(
        ), "VHDL, verilog (*.vhd *.v) ;;VHDL (*.vhd);; Verilog (*.v)")

        self.file_path = files[0]
        self.file_input = self.file_path
        self.file_name = os.path.splitext(os.path.basename(self.file_input))[0]
        self.file_output = self.file_name + ".pdf"

        self.ui.lineEdit_file.setText(self.file_name)
        self.ui.lineEdit_output.setText(self.file_output)
        self.ui.pushButton_output.setEnabled(True)
        self.ui.pushButton_accept.setEnabled(True)


    def search_output(self):
        """
        This method configures output
        """
        outputfileDialog = QFileDialog()
        self.file_path = outputfileDialog.getExistingDirectory(self)

        relative_path = os.path.relpath(self.file_output, self.file_path)
        self.ui.lineEdit_output.setText(relative_path[3:])
        
