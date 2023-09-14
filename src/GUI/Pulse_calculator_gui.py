from PyQt5.QtWidgets import QWidget

from UI.Pulse_calculator_UI import *

class Pulse_calculator_gui(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Pulses_calculator()
        self.ui.setupUi(self)
        self.connections()
        self.show()

    def connections(self):
        self.ui.pushButton_cancel.clicked.connect(self.cancel_fn)
        self.ui.pushButton_calculate.clicked.connect(self.calculate_fn)

    def cancel_fn(self):
        self.close()

    def calculate_fn(self):
        
        self.comboBox_f_p_general = self.ui.comboBox_f_p_general.currentText()
        self.comboBox_f_p_local = self.ui.comboBox_f_p_local.currentText()
        self.comboBox_seconds_general = self.ui.comboBox_seconds_general.currentText()
        self.comboBox_seconds_local = self.ui.comboBox_seconds_local.currentText()

        try:
            self.lineEdit_f_p_global = self.ui.lineEdit_f_p_global.text()
            self.lineEdit_f_p_local = self.ui.lineEdit_f_p_local.text()
            self.lineEdit_seconds_general = self.ui.lineEdit_seconds_general.text()
            self.lineEdit_seconds_local = self.ui.lineEdit_seconds_local.text()
        except:
            pass

        self.ui.lineEdit_f_p_global.clear()
        self.ui.lineEdit_f_p_local.clear()
        self.ui.lineEdit_seconds_general.clear()
        self.ui.lineEdit_seconds_local.clear()
        pass