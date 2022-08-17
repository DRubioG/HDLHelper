import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog, QMenu, QLabel
from PyQt5 import QtCore
from UI.HDLHelper_UI import *
from GUI.Testbench_generator_gui import *

class HDLHelper_gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HDLHelper()
        self.ui.setupUi(self)
        self.setWindowTitle("HDLHelper")
        self.addMenuBar()
        self.addStatusBar()
        self.actions()
        self.show()
    
    def addMenuBar(self):
        menuBar = self.menuBar()
        menuBar.addMenu("File")
        menuBar.addMenu("Edit")
        menuBar.addMenu("Options")

    def addStatusBar(self):
        statusbar = self.statusBar()
        statusbar.addPermanentWidget(QLabel("Version 0.0"))
    
    def actions(self):
        # first row
        self.ui.testbench_generator_button.clicked.connect(self.testbench_generator_fn)
        self.ui.calculator_button.clicked.connect(self.calculator_fn)
        self.ui.top_file_generator_button.clicked.connect(self.top_file_generator_fn)
        # second row
        self.ui.ticks_calculator_button.clicked.connect(self.ticks_calculator_fn); self.ui.ticks_calculator_button.hide()
        self.ui.hdl_translator_button.clicked.connect(self.hdl_translator_fn); self.ui.hdl_translator_button.hide()
        self.ui.hdl_generator_button.clicked.connect(self.hdl_generator_fn); self.ui.hdl_generator_button.hide()
        # third row
        self.ui.visualizer.clicked.connect(self.visualizer_fn); self.ui.visualizer.hide()
        self.ui.documentation_generator_button.clicked.connect(self.documentation_generator_fn); self.ui.documentation_generator_button.hide()
        self.ui.analize_dependencies_button.clicked.connect(self.analize_dependencies_fn); self.ui.analize_dependencies_button.hide()
        #fourth row
        self.ui.generate_state_machine_button.clicked.connect(self.generate_state_machine_fn); self.ui.generate_state_machine_button.hide()
        self.ui.empty.hide()
        self.ui.empty_2.hide()

    #first row
    def testbench_generator_fn(self):
        print("pulsado")
        self.testbench_generator = Testbench_generator_gui()
        self.testbench_generator.show()
        
    def calculator_fn(self):
        self.coming_soon()

    def top_file_generator_fn(self):
        self.coming_soon()

    #second row
    def ticks_calculator_fn(self):
        self.coming_soon()

    def hdl_translator_fn(self):
        self.coming_soon()

    def hdl_generator_fn(self):
        self.coming_soon()
    
    #third row
    def visualizer_fn(self):
        self.coming_soon()

    def documentation_generator_fn(self):
        self.coming_soon()

    def analize_dependencies_fn(self):
        self.coming_soon()

    #fourth row
    def generate_state_machine_fn(self):
        self.coming_soon()


    # Coming soon
    def coming_soon(self):
        self.w = QDialog()
        self.w.setWindowTitle("Coming soon ...")
        self.w.show()
    
