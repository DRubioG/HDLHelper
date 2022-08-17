import sys
from UI.Testbench_generator_UI import *
from UI.StyleSheet import testbench_generator_gui
from PyQt5.QtWidgets import QDialog, QMainWindow, QFileDialog, QWidget
from PyQt5 import QtCore

class Testbench_generator_gui(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(testbench_generator_gui)
        self.ui = Ui_Testbench_generator()
        self.ui.setupUi(self)
        self.actions()
        self.show()

    def actions(self):
        self.ui.pushButton_input.clicked.connect(self.searchInputFile)
        self.ui.pushButton_create.clicked.connect(self.createFile)
        self.ui.pushButton_cancel.clicked.connect(self.cancelOperation)

    def searchInputFile(self):
        fileDialog = QFileDialog()
        files = fileDialog.getOpenFileNames(self, "Select file", QtCore.QDir.homePath(), "VHDL, verilog (*.vhd *.v) ;;VHDL (*.vhd);; Verilog (*.v);; Tesbenches (*_tb.vhd *_tb.v)")
        test_bench = []
        self.file = []
        self.ui.lineEdit_input.hide()
        self.ui.comboBox_input.addItems(files[0])
        self.ui.comboBox_input.show()

        for file in files[0]:
            test_bench.append(file.replace(".", "_tb."))

        #test_bench = files[0][0].replace(".", "_tb.")
        self.ui.lineEdit_input.setText(files[0][0])
        self.ui.lineEdit_output.setText(test_bench[0])
        
        print(self.file)
    
    def createFile(self):
        #self.file.write("hole")
            #self.file.append(open(test_bench[-1], 'w'))
        self.close()
        
    def cancelOperation(self):
        quit()