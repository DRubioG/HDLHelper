import os

from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6 import QtCore

from UI.Top_file_generator_UI import *
from Backend.Top_file_generator import *

class Top_file_generator_gui(QWidget):
    """
    This class generates a top file with the bottom files
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_Top_file_generator()
        self.ui.setupUi(self)
        self.connections()
        self.show()


    def connections(self):
        """
        This method connects GUI with methods
        """
        self.ui.pushButton_cancel.clicked.connect(self.cancel_fn)
        self.ui.pushButton_create.clicked.connect(self.create_fn)
        self.ui.pushButton_config.clicked.connect(self.config_fn)
        self.ui.pushButton_search.clicked.connect(self.search_fn)
        self.ui.lineEdit_name_file.textChanged.connect(self.file_fn)
        self.ui.pushButton_create.setEnabled(False)
        self.ui.lineEdit_name_file.setEnabled(False)
    

    def config_fn(self):
        """
        This method opens the config GUI
        """
        pass
    

    def search_fn(self):
        """
        This method searchs bottom files
        """
        path = QFileDialog()
        self.files, _ = path.getOpenFileNames(self, "Select file", QtCore.QDir.currentPath(
        ), "VHDL, verilog (*.vhd *.v) ;;VHDL (*.vhd);; Verilog (*.v);; Tesbenches (*_tb.vhd *_tb.v)")
        if self.files:
            self.ui.comboBox_files.clear()
            self.ui.comboBox_files.addItems(self.files)
            self.ui.lineEdit_name_file.setEnabled(True)
            self.ui.label_type.setText(".vhd")


    def create_fn(self):
        """
        This method creates top file
        """
        if len(self.files) != 1:
            path, _ = os.path.split(self.files[0])
        else:
            path, _ = os.path.split(self.files)
        file_name = self.ui.lineEdit_name_file.text().strip() + ".vhd"
        file_path = os.path.join(path, file_name)
        Top_file_generator(file_path, self.files)

        self.close()
        

    def file_fn(self):
        """
        This method enables create button
        """
        if self.ui.lineEdit_name_file.text().strip():
            self.ui.pushButton_create.setEnabled(True)
        else:
            self.ui.pushButton_create.setEnabled(False)


    def cancel_fn(self):
        """
        This method cancels window
        """
        self.close()