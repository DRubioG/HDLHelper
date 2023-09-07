import sys
import os
from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5 import QtCore

from UI.Testbench_generator_UI import *
from UI.StyleSheet.StyleSheet_testbench_generator import testbench_generator_gui

from GUI.Testbench_generator_config_gui import *
from GUI.Testbench_overwrite_gui import *

from Backend.HDLHelper import *


class Testbench_generator_gui(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(testbench_generator_gui)
        self.ui = Ui_Testbench_generator()
        self.ui.setupUi(self)
        self.connections()
        self.show()

    def connections(self):
        self.ui.pushButton_input.clicked.connect(self.searchInputFile)
        self.ui.pushButton_output.clicked.connect(self.seachOutputFile)
        self.ui.pushButton_config.clicked.connect(self.configFile)
        self.ui.pushButton_create.clicked.connect(self.createFile)
        self.ui.pushButton_cancel.clicked.connect(self.cancelOperation)
        self.ui.pushButton_output.setEnabled(False)
        self.ui.pushButton_create.setEnabled(False)
        self.ui.lineEdit_output.setReadOnly(True)
        self.ui.lineEdit_input.setReadOnly(True)

    def searchInputFile(self):
        fileDialog = QFileDialog()
        files = fileDialog.getOpenFileName(self, "Select file", QtCore.QDir.currentPath(
        ), "VHDL, verilog (*.vhd *.v) ;;VHDL (*.vhd);; Verilog (*.v);; Tesbenches (*_tb.vhd *_tb.v)")

        self.file_path = files[0]
        self.file_input = self.file_path
        self.file_output = self.file_path.replace(".", "_tb.")

        if self.file_input.find("\\") != -1:
            self.file_input = self.file_input.split("\\")[-1]
            self.file_output = self.file_output.split("\\")[-1]
        else:
            self.file_input = self.file_input.split("/")[-1]
            self.file_output = self.file_output.split("/")[-1]

        self.ui.lineEdit_input.setText(self.file_input)
        self.ui.lineEdit_output.setText(self.file_output)

        self.overwriteButton()  # check if the file exists in the folder

        self.ui.pushButton_output.setEnabled(True)
        self.ui.pushButton_create.setEnabled(True)

    def overwriteButton(self):
        if os.path.exists(self.file_output) == True:
            self.overwrite = 1
            self.ui.pushButton_create.setText("Overwrite")
            self.ui.pushButton_create.setStyleSheet("QPushButton#pushButton_create:hover{background-color: #f1a629}")
        else:
            self.overwrite = 0
            self.ui.pushButton_create.setText("Create")
            self.ui.pushButton_create.setStyleSheet("QPushButton#pushButton_create:hover{background-color: #5ce75f}")

    def seachOutputFile(self):
        outputfileDialog = QFileDialog()
        self.file_output = outputfileDialog.getExistingDirectory(self)
        if self.file_input.find("\\") != -1:
            output = "\\"
        else:
            output = "/"
        self.file_output += output + self.file_input.replace(".", "_tb.")
        
        self.overwriteButton()      # check if the file exists in the folder
        
        relative_path = os.path.relpath(self.file_output, self.file_path)
        self.ui.lineEdit_output.setText(relative_path[3:])

    def configFile(self):
        self.testbench_generator_config = Testbench_generator_config_gui()

    def createFile(self):
        if self.overwrite == 1:
            self.overwrite_config = Testbench_overwrite_gui()
            self.hdlhelper = HDLHelper(
                self.file_path, self.file_output, "testbench")
            self.close()
        else:
            self.hdlhelper = HDLHelper(
                    self.file_path, self.file_output, "testbench")
            self.close()

    def cancelOperation(self):
        self.close()
