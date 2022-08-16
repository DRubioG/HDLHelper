import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog
from PyQt5 import QtCore
from UI.HDLHelper_UI import *
from GUI.Testbench_generator_gui import *

class HDLHelper_gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HDLHelper()
        self.ui.setupUi(self)
        self.actions()
        self.show()
    
    def actions(self):
        self.ui.testbench_generator_button.clicked.connect(self.testbench_generator_fn)
        self.ui.calculator_button.clicked.connect(self.calculator_fn)
        self.ui.top_file_generator_button.clicked.connect(self.top_file_generator_fn)

    
    def testbench_generator_fn(self):
        print("pulsado")
        self.testbench_generator = Testbench_generator_gui()
        self.testbench_generator.show()
        
    def calculator_fn(self):
        self.coming_soon()

    def top_file_generator_fn(self):
        self.coming_soon()

    def coming_soon(self):
        self.w = QDialog()
        self.w.setWindowTitle("Coming soon ...")
        self.w.show()