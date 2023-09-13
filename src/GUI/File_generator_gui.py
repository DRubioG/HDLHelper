from PyQt5.QtWidgets import QWidget, QFileDialog

from UI.File_generator_UI import *

class File_generator_gui(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_File_generator_ui()
        self.ui.setupUi(self)
        self.connections()

    def connections(self):
        self.ui.pushButton_add.clicked.connect(self.add_fn)
        
    def add_fn(self):
        port_generic = self.ui.comboBox_port_generic.currentText()
        name = self.ui.lineEdit_name.text()
        
    
