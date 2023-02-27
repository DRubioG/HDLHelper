from PyQt5.QtWidgets import QDialog
from UI.Testbench_generator_config_UI import *

class Testbench_generator_config_gui(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_testbench_generator_config()
        self.ui.setupUi(self)
        # self.setFixedSize(-1,-1)
        self.show()