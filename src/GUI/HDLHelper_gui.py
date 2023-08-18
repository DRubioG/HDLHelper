import sys
import json
from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog, QMenu, QLabel, QAction
from PyQt5 import QtCore
from PyQt5.QtCore import QUrl

from UI.HDLHelper_UI import *
from GUI.Testbench_generator_gui import *

from UI.StyleSheet.StyleSheet_testbench_generator import testbench_generator_gui


class HDLHelper_gui(QMainWindow):
    """
    This is the GUI controller class of the HDLHelper
    """

    def __init__(self):
        """
        This is the constructor, it has the aim to load the stylesheet, the user interface,
        to setup the user interface, to write the name in the window, to load the menu bar,
        to load the status bar, the connections of the buttons with the tools and show the 
        window.
        """
        super().__init__()      # start the main window
        self.setStyleSheet(testbench_generator_gui)     #load the stylesheet of the window
        self.ui = Ui_HDLHelper()    # create an object with the user interface
        self.ui.setupUi(self)   # to setup the UI
        self.setWindowTitle("HDLHelper")    #gives the name of the window
        self.addMenuBar()       # to load the menu bar
        self.addStatusBar()     # to load the status bar
        self.connections()      # to connect the UI with the operational classes
        self.show()             # to show the window


    def addMenuBar(self):
        """
        This method adds the status bar to the window of HDLHelper.
        This status bar has add the differents options, like Preferences or
        direct access to the tools of HDLHelper. Also, this status bar connects
        the events of keywords with different options.
        """

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
        # calculator = QAction("Calculator", self)
        # top_file_generator = QAction("Top file generator", self)
        # ticks_calculator = QAction("Ticks calculator", self)
        # translator = QAction("v <-> vhd", self)
        # hdl_generator = QAction("HDL generator", self)
        # editor = QAction("Editor", self)
        # documentation_generator = QAction("Documentation generator", self)
        # analize_dependencies = QAction("Analize dependencies", self)
        # gen_state_machine = QAction("Gen. State Machine", self)
        # ascii_conversor = QAction("Ascii Conversor", self)
        # auto_improve = QAction("Auto-improve", self)

        testbench_generator.setShortcut('Ctrl+T')
        # calculator.setShortcut('Ctrl+C')
        # editor.setShortcut('Ctrl+E')
        # ascii_conversor.setShortcut('Ctrl+A')

        testbench_generator.triggered.connect(self.testbench_generator_fn)
        # calculator.triggered.connect(self.calculator_fn)
        # top_file_generator.triggered.connect(self.top_file_generator_fn)
        # ticks_calculator.triggered.connect(self.ticks_calculator_fn)
        # translator.triggered.connect(self.hdl_translator_fn)
        # hdl_generator.triggered.connect(self.hdl_generator_fn)
        # editor.triggered.connect(self.editor_fn)
        # documentation_generator.triggered.connect(self.documentation_generator_fn)
        # analize_dependencies.triggered.connect(self.analize_dependencies_fn)
        # gen_state_machine.triggered.connect(self.generate_state_machine_fn)
        # ascii_conversor.triggered.connect(self.ascii_conversor_fn)
        # auto_improve.triggered.connect(self.auto_improve_fn)

        executeMenu.addAction(testbench_generator)
        # executeMenu.addAction(calculator)
        # executeMenu.addAction(top_file_generator)
        # executeMenu.addAction(ticks_calculator)
        # executeMenu.addAction(translator)
        # executeMenu.addAction(hdl_generator)
        # executeMenu.addAction(editor)
        # executeMenu.addAction(documentation_generator)
        # executeMenu.addAction(analize_dependencies)
        # executeMenu.addAction(gen_state_machine)
        # executeMenu.addAction(ascii_conversor)
        # executeMenu.addAction(auto_improve)

        # Help
        helpMenu = menuBar.addMenu("Help")

        about = QAction("About ...", self)
        version = QAction("Version", self)
        about.triggered.connect(self.about_fn)
        version.triggered.connect(self.version_fn)
        helpMenu.addAction(about)
        helpMenu.addAction(version)     


    def addStatusBar(self):
        """
        This method adds the status bar to the HDLHelper UI.
        The method first check, if there are internet connection, what version 
        of HDLHelper is on GitHub and compares with the installed version, write in
        config.json file, if the version doesn't match, it means that there are a new 
        version on GitHub and writes in HDLHelper a message telling that there are a new 
        version and gives the links for download.
        """
        statusbar = self.statusBar()        # create an object for the status bar

        # this part checks if there are a new version of HDLHelper on GitHub
        try:
            import requests
            reponse = requests.get(
                "https://api.github.com/repos/DRubioG/HDLHelper/releases/latest")
            new_version = reponse.json()["name"][1:]
        except:
            new_version = None
        try:
            file = open("./config/configuration.json", "r")
            version_act = json.load(file)["version"]
        except:
            version_act = "Unknown"

        # This part compare the version number, and gives the actual version or a message for
        # download the last version
        if new_version == None or version_act == "Unknown":
            version_tag = "Version {}".format(version_act)
        elif version_act == new_version:
            version_tag = "Version {}".format(version_act)
        else:
            version_tag = "<a href ='https://github.com/DRubioG/HDLHelper'>New version available(" + \
                version_act + " -> " + new_version + ")[copy link]</a>"
        # add a version or a message
        statusbar.addPermanentWidget(QLabel(version_tag))


    def connections(self):
        """
        This method connects the UI with the functinonal methods.
        """
        # first row
        self.ui.testbench_generator_button.clicked.connect(
            self.testbench_generator_fn)
        self.ui.calculator_button.clicked.connect(self.calculator_fn)
        self.ui.calculator_button.hide()
        self.ui.top_file_generator_button.clicked.connect(
            self.top_file_generator_fn)
        self.ui.top_file_generator_button.hide()
        # second row
        self.ui.ticks_calculator_button.clicked.connect(
            self.ticks_calculator_fn)
        self.ui.ticks_calculator_button.hide()
        self.ui.hdl_translator_button.clicked.connect(self.hdl_translator_fn)
        self.ui.hdl_translator_button.hide()
        self.ui.hdl_generator_button.clicked.connect(self.hdl_generator_fn)
        self.ui.hdl_generator_button.hide()
        # third row
        self.ui.editor_button.clicked.connect(self.editor_fn)
        self.ui.editor_button.hide()
        self.ui.documentation_generator_button.clicked.connect(
            self.documentation_generator_fn)
        self.ui.documentation_generator_button.hide()
        self.ui.analize_dependencies_button.clicked.connect(
            self.analize_dependencies_fn)
        self.ui.analize_dependencies_button.hide()
        # fourth row
        self.ui.generate_state_machine_button.clicked.connect(
            self.generate_state_machine_fn)
        self.ui.generate_state_machine_button.hide()
        self.ui.ascii_conversor_button.clicked.connect(self.ascii_conversor_fn)
        self.ui.ascii_conversor_button.hide()
        self.ui.auto_improve_button.clicked.connect(self.auto_improve_fn)
        self.ui.auto_improve_button.hide()

    # first row
    def testbench_generator_fn(self):
        """
        This method opens the GUI of Testbench generator
        """
        self.testbench_generator = Testbench_generator_gui()
        self.testbench_generator.show()

    def calculator_fn(self):
        self.coming_soon()

    def top_file_generator_fn(self):
        self.coming_soon()

    # second row
    def ticks_calculator_fn(self):
        self.coming_soon()

    def hdl_translator_fn(self):
        self.coming_soon()

    def hdl_generator_fn(self):
        self.coming_soon()

    # third row
    def editor_fn(self):
        self.coming_soon()

    def documentation_generator_fn(self):
        self.coming_soon()

    def analize_dependencies_fn(self):
        self.coming_soon()

    # fourth row
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
        """
        This method closes the HDLHelper GUI.
        """
        quit()
