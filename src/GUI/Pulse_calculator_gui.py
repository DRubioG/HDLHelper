from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui

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
        self.ui.pushButton_remove.clicked.connect(self.remove_data_fn)

    def cancel_fn(self):
        self.close()

    def calculate_fn(self):
        
        self.comboBox_f_p_general = self.ui.comboBox_f_p_general.currentText()
        self.comboBox_f_p_local = self.ui.comboBox_f_p_local.currentText()
        self.comboBox_seconds_general = self.ui.comboBox_seconds_general.currentText()
        self.comboBox_seconds_local = self.ui.comboBox_seconds_local.currentText()
        
        try:
            self.lineEdit_f_p_global = float(self.ui.lineEdit_f_p_global.text().replace(",", "."))
            self.ui.lineEdit_f_p_global.setStyleSheet("""QLineEdit{border: 1px solid black}""")
        except:
            self.ui.lineEdit_f_p_global.setStyleSheet("""QLineEdit{border: 1px solid red}""")
            self.ui.label_error.setText("ERROR")
            

        try:
            self.lineEdit_f_p_local = float(self.ui.lineEdit_f_p_local.text().replace(",", "."))
            self.ui.lineEdit_f_p_local.setStyleSheet("""QLineEdit{border: 1px solid black}""")
        except:
            self.ui.lineEdit_f_p_local.setStyleSheet("""QLineEdit{border: 1px solid red}""")
           

        try:
            self.lineEdit_seconds_general = float(self.ui.lineEdit_seconds_general.text().replace(",", "."))
            self.ui.lineEdit_seconds_general.setStyleSheet("""QLineEdit{border: 1px solid black}""")
        except:
            self.ui.lineEdit_seconds_general.setStyleSheet("""QLineEdit{border: 1px solid red}""")
            

        try:
            self.lineEdit_seconds_local = float(self.ui.lineEdit_seconds_local.text().replace(",", "."))
            self.ui.lineEdit_seconds_local.setStyleSheet("""QLineEdit{border: 1px solid black}""")
        except:
            self.ui.lineEdit_seconds_local.setStyleSheet("""QLineEdit{border: 1px solid red}""")
            

        pass

    def remove_data_fn(self):
        self.ui.lineEdit_f_p_global.clear()
        self.ui.lineEdit_f_p_local.clear()
        self.ui.lineEdit_seconds_general.clear()
        self.ui.lineEdit_seconds_local.clear()
