import sys, os
from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5 import QtCore

from UI.Testbench_generator_UI import *
from UI.StyleSheet.StyleSheet_testbench_generator import testbench_generator_gui

from GUI.Testbench_generator_config_gui import *

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

    def searchInputFile(self):
        fileDialog = QFileDialog()
        files = fileDialog.getOpenFileNames(self, "Select file", QtCore.QDir.currentPath(), "VHDL, verilog (*.vhd *.v) ;;VHDL (*.vhd);; Verilog (*.v);; Tesbenches (*_tb.vhd *_tb.v)")
        test_bench = []
        self.file = []

        for file in files[0]:
            test_bench = file.replace(".", "_tb.")

        self.file_input = files[0][0]
        self.file_output = test_bench
        self.ui.lineEdit_output.setText(self.file_output)
        self.ui.lineEdit_input.setText(self.file_input)
        
        

    def seachOutputFile(self):
        outputfileDialog = QFileDialog()
        outputfile = outputfileDialog.getExistingDirectory(self)
        self.ui.lineEdit_output.setText(outputfile+self.file_output)
        
    def configFile(self):
        self.testbench_generator_config = Testbench_generator_config_gui()


    def createFile(self):
        self.hdlhelper = HDLHelper(self.file_input, self.file_output, "testbench")
        self.close()
        
    def cancelOperation(self):
        self.close()
