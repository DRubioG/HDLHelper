import sys, json
from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog, QMenu, QLabel, QAction
from PyQt5 import QtCore
from PyQt5.QtCore import QUrl

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
        self.connections()
        self.show()
    
    def addMenuBar(self):

        menuBar = self.menuBar()

        # File
        fileMenu = menuBar.addMenu("File")

        exitAction = QAction('Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.cancelOperation)
        fileMenu.addAction(exitAction)

        # Edit
        editMenu = menuBar.addMenu("Edit")
        preferences = QAction('Preferences...', self)
        preferences.triggered.connect(self.preferences_fn)
        editMenu.addAction(preferences)


        # Execute
        executeMenu = menuBar.addMenu("Execute")

        testbench_generator = QAction("Testbench Generator", self)
        calculator = QAction("Calculator", self)
        top_file_generator = QAction("Top file generator", self)
        ticks_calculator = QAction("Ticks calculator", self)
        translator = QAction("v <-> vhd", self)
        hdl_generator = QAction("HDL generator", self)
        editor = QAction("Editor", self)
        documentation_generator = QAction("Documentation generator", self)
        analize_dependencies = QAction("Analize dependencies", self)
        gen_state_machine = QAction("Gen. State Machine", self)
        ascii_conversor = QAction("Ascii Conversor", self)
        auto_improve = QAction("Auto-improve", self)

        testbench_generator.setShortcut('Ctrl+T')
        calculator.setShortcut('Ctrl+C')
        editor.setShortcut('Ctrl+E')
        ascii_conversor.setShortcut('Ctrl+A')

        testbench_generator.triggered.connect(self.testbench_generator_fn)
        calculator.triggered.connect(self.calculator_fn)
        top_file_generator.triggered.connect(self.top_file_generator_fn)
        ticks_calculator.triggered.connect(self.ticks_calculator_fn)
        translator.triggered.connect(self.hdl_translator_fn)
        hdl_generator.triggered.connect(self.hdl_generator_fn)
        editor.triggered.connect(self.editor_fn)
        documentation_generator.triggered.connect(self.documentation_generator_fn)
        analize_dependencies.triggered.connect(self.analize_dependencies_fn)
        gen_state_machine.triggered.connect(self.generate_state_machine_fn)
        ascii_conversor.triggered.connect(self.ascii_conversor_fn)
        auto_improve.triggered.connect(self.auto_improve_fn)

        executeMenu.addAction(testbench_generator)
        executeMenu.addAction(calculator)
        executeMenu.addAction(top_file_generator)
        executeMenu.addAction(ticks_calculator)
        executeMenu.addAction(translator)
        executeMenu.addAction(hdl_generator)
        executeMenu.addAction(editor)
        executeMenu.addAction(documentation_generator)
        executeMenu.addAction(analize_dependencies)
        executeMenu.addAction(gen_state_machine)
        executeMenu.addAction(ascii_conversor)
        executeMenu.addAction(auto_improve)

        # Help
        helpMenu = menuBar.addMenu("Help")

        about = QAction("About ...", self)
        version = QAction("Version", self)
        about.triggered.connect(self.about_fn)
        version.triggered.connect(self.version_fn)
        helpMenu.addAction(about)
        helpMenu.addAction(version)


    def addStatusBar(self):
        statusbar = self.statusBar()
        try:
            import requests
            reponse = requests.get("https://api.github.com/repos/DRubioG/HDLHelper/releases/latest")
            new_version = reponse.json()["name"][1:]
        except:
            new_version = None
        file = open("./config/configuration.json", "r")
        version_act = json.load(file)["version"]
        if  new_version == None:
            version_tag = "Version {}".format(version_act)
        elif version_act == new_version:
            version_tag = "Version {}".format(version_act)
        else:
            version_tag = "<a href ='https://github.com/DRubioG/HDLHelper'>New version available(" + version_act + " -> "+ new_version + ")[copy link]</a>"
        statusbar.addPermanentWidget(QLabel(version_tag))
    
    def connections(self):
        # first row
        self.ui.testbench_generator_button.clicked.connect(self.testbench_generator_fn)
        self.ui.calculator_button.clicked.connect(self.calculator_fn);                              self.ui.calculator_button.hide()
        self.ui.top_file_generator_button.clicked.connect(self.top_file_generator_fn);              self.ui.top_file_generator_button.hide()
        # second row
        self.ui.ticks_calculator_button.clicked.connect(self.ticks_calculator_fn);                  self.ui.ticks_calculator_button.hide()
        self.ui.hdl_translator_button.clicked.connect(self.hdl_translator_fn);                      self.ui.hdl_translator_button.hide()
        self.ui.hdl_generator_button.clicked.connect(self.hdl_generator_fn);                        self.ui.hdl_generator_button.hide()
        # third row
        self.ui.editor_button.clicked.connect(self.editor_fn);                                      self.ui.editor_button.hide()
        self.ui.documentation_generator_button.clicked.connect(self.documentation_generator_fn);    self.ui.documentation_generator_button.hide()
        self.ui.analize_dependencies_button.clicked.connect(self.analize_dependencies_fn);          self.ui.analize_dependencies_button.hide()
        #fourth row
        self.ui.generate_state_machine_button.clicked.connect(self.generate_state_machine_fn);      self.ui.generate_state_machine_button.hide()
        self.ui.ascii_conversor_button.clicked.connect(self.ascii_conversor_fn);             self.ui.ascii_conversor_button.hide()
        self.ui.auto_improve_button.clicked.connect(self.auto_improve_fn);                self.ui.auto_improve_button.hide()

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
    def editor_fn(self):
        self.coming_soon()

    def documentation_generator_fn(self):
        self.coming_soon()

    def analize_dependencies_fn(self):
        self.coming_soon()

    #fourth row
    def generate_state_machine_fn(self):
        self.coming_soon()

    def ascii_conversor_fn(self):
        self.coming_soon()

    def auto_improve_fn(self):
        self.coming_soon()

    # MenuBar options
    def about_fn(self):
        self.coming_soon()

    def version_fn(self):
        self.coming_soon()
    
    def preferences_fn(self):
        self.coming_soon()

    # Coming soon
    def coming_soon(self):
        self.w = QDialog()
        self.w.setWindowTitle("Coming soon ...")
        self.w.show()
    
    def cancelOperation(self):
        quit()