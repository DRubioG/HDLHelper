from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui
import pyperclip

from UI.Pulse_calculator_UI import *

class Pulse_calculator_gui(QWidget):
    """
    This class calculates pulses/frequency
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_Pulses_calculator()
        self.ui.setupUi(self)
        self.connections()
        self.show()


    def connections(self):
        """
        This class connects functional methods with UI
        """
        self.ui.pushButton_bin.clicked.connect(self.copy_bin_fn)
        self.ui.pushButton_hex.clicked.connect(self.copy_hex_fn)
        self.ui.pushButton_bin.setStyleSheet("QPushButton { text-align: left; }")
        self.ui.pushButton_hex.setStyleSheet("QPushButton { text-align: left; }")
        self.ui.pushButton_cancel.clicked.connect(self.cancel_fn)
        self.ui.pushButton_calculate.clicked.connect(self.calculate_fn)
        self.ui.pushButton_remove.clicked.connect(self.remove_data_fn)
        self.ui.comboBox_var1.currentIndexChanged.connect(self.clean1_fn)
        self.ui.comboBox_var2.currentIndexChanged.connect(self.clean2_fn)
        self.ui.comboBox_var3.currentIndexChanged.connect(self.clean3_fn)
        self.ui.comboBox_var4.currentIndexChanged.connect(self.clean4_fn)
        self.ui.radioButton_pulses.toggled.connect(self.pulses_fn)
        self.ui.pushButton_clean1.clicked.connect(self.clean1_fn)
        self.ui.pushButton_clean2.clicked.connect(self.clean2_fn)
        self.ui.pushButton_clean3.clicked.connect(self.clean3_fn)
        self.ui.pushButton_clean4.clicked.connect(self.clean4_fn)
        
        self.ui.pushButton_bin.hide()
        self.ui.pushButton_hex.hide()
        self.ui.label_binary_result.hide()
        self.ui.label_hexadecimal_result.hide()


    def cancel_fn(self):
        """
        This method closes the window
        """
        self.close()


    def calculate_fn(self):
        """
        This method calculates the desired value
        """
        unit1 = self.ui.comboBox_var1.currentText()
        unit2 = self.ui.comboBox_var2.currentText()
        unit3 = self.ui.comboBox_var3.currentText()
        unit4 = self.ui.comboBox_var4.currentText()

        unit_list = self.get_units([unit1, unit2, unit3, unit4])

        var1 = self.ui.lineEdit_var1.text().replace(" ", "")
        var2 = self.ui.lineEdit_var2.text().replace(" ", "")
        var3 = self.ui.lineEdit_var3.text().replace(" ", "")
        var4 = self.ui.lineEdit_var4.text().replace(" ", "")

        cont = 0
        calc = 0
        if not var1:
            cont += 1
            calc = "var1"
        if not var2:
            cont += 1
            calc = "var2"
        if not var3:
            cont += 1
            calc = "var3"
        if not var4:
            cont += 1
            calc = "var4"

        if cont == 1:
            self.ui.label_error.setText("")
            list_val, err = self.get_values(calc)
            if not err:
                result = self.calculate(list_val, unit_list, calc)
                self.write_result(calc, result)
        else:
            self.ui.label_error.setStyleSheet("""QLabel{color: red}""")
            self.ui.label_error.setText("Only one space must be empty")
            

    def write_result(self, calc, result): 
        """
        This method writes the result in the UI
        Input:
            - calc: name of the variable that wants calcute
            - result: value you want to write
        """
        self.ui.pushButton_bin.hide()
        self.ui.pushButton_hex.hide()
        self.ui.label_binary_result.hide()
        self.ui.label_hexadecimal_result.hide()
        if calc == "var1":
            self.ui.lineEdit_var1.setText(str(result).rstrip('0').rstrip('.'))
            self.ui.lineEdit_var1.setStyleSheet("""QLineEdit{border: 1px solid green}""")
        if calc == "var2":
            self.ui.lineEdit_var2.setText(str(result).rstrip('0').rstrip('.'))
            self.ui.lineEdit_var2.setStyleSheet("""QLineEdit{border: 1px solid green}""")
        if calc == "var3":
            self.ui.pushButton_bin.show()
            self.ui.pushButton_hex.show()
            self.ui.label_binary_result.show()
            self.ui.label_hexadecimal_result.show()

            self.ui.lineEdit_var3.setText(str(result).rstrip('0').rstrip('.'))
            self.ui.lineEdit_var3.setStyleSheet("""QLineEdit{border: 1px solid green}""")

            binary_text = str(bin(int(float(result))))
            tam = len(binary_text)-2
            self.binary = binary_text[2:]
            self.ui.pushButton_bin.setText("Bin("+str(tam)+"):")
            self.ui.label_binary_result.setText(binary_text)

            hex_text = str(hex(int(float(result))))
            tam = len(hex_text)-2
            self.hex = hex_text[2:]
            self.ui.label_hexadecimal_result.setText(hex_text)

        if calc == "var4":
            self.ui.lineEdit_var4.setText(str(result).rstrip('0').rstrip('.'))
            self.ui.lineEdit_var4.setStyleSheet("""QLineEdit{border: 1px solid green}""")


    def get_units(self, units):
        """
        This method exchanges string units for integer units
        Input:
            - units: list with the string names of the units
        Return:
            - list_output: list with the integer values
        """
        list_output = []
        conversion = {"MHz":1e6, "kHz":1e3, "Hz":1, "GHz":1e9, "sec":1, "msec":1e-3, "usec":1e-6, "nsec":1e-9, "Pul":1, "MPul":1e6, "kPul":1e3, "GPul":1e9}
        for unit in units:
            list_output.append(conversion.get(unit))
        return list_output


    def get_values(self, calc):
        """
        This method gets values from lineedits
        Input: 
            - calc: value you want to calculate
        Return:
            - <list>: list with the float values in the lineedit
            - err: boolean with the error information
        """
        err = False
        var1 = None
        var2 = None
        var3 = None
        var4 = None
        if calc != "var1":
            try:
                var1 = float(self.ui.lineEdit_var1.text().replace(",", "."))
                self.ui.lineEdit_var1.setStyleSheet("""QLineEdit{border: 1px solid black}""")
            except:
                self.ui.lineEdit_var1.setStyleSheet("""QLineEdit{border: 1px solid red}""")
                err = True
            
        if calc != "var2":
            try:
                var2 = float(self.ui.lineEdit_var2.text().replace(",", "."))
                self.ui.lineEdit_var2.setStyleSheet("""QLineEdit{border: 1px solid black}""")
            except:
                self.ui.lineEdit_var2.setStyleSheet("""QLineEdit{border: 1px solid red}""")
                err = True
           
        if calc != "var3":
            try:
                var3 = float(self.ui.lineEdit_var3.text().replace(",", "."))
                self.ui.lineEdit_var3.setStyleSheet("""QLineEdit{border: 1px solid black}""")
            except:
                self.ui.lineEdit_var3.setStyleSheet("""QLineEdit{border: 1px solid red}""")
                err = True
            
        if calc != "var4":
            try:
                var4 = float(self.ui.lineEdit_var4.text().replace(",", "."))
                self.ui.lineEdit_var4.setStyleSheet("""QLineEdit{border: 1px solid black}""")
            except:
                self.ui.lineEdit_var4.setStyleSheet("""QLineEdit{border: 1px solid red}""")
                err = True

        if err:
            self.ui.label_error.setStyleSheet("""QLabel{color: red}""")
            self.ui.label_error.setText("ERROR")
            
        return [var1, var2, var3, var4], err
    

    def calculate(self, list_var, units, calc):
        """
        This method calculates the result
        Input:
            - list_var: list with values in float format
            - units: list with units in float format
            - calc: value you want to calculate
        Return:
            - result: result of the calculate
        """
        result = 0
        if calc == "var1":
            result = list_var[1]*units[1]*list_var[2]*units[2] / (list_var[3]*units[3]*units[0])
        
        elif calc == "var2":
            result = list_var[0]*units[0]*list_var[3]*units[3] / (list_var[2]*units[2]*units[1])

        elif calc == "var3":
            result = list_var[0]*units[0]*list_var[3]*units[3] / (list_var[1]*units[1]*units[2])

        elif calc == "var4":
            result = list_var[1]*units[1]*list_var[2]*units[2] / (list_var[0]*units[0]*units[3])
        
        result = "{:.2f}".format(round(result, 2))
        return result


    def remove_data_fn(self):
        """
        This method removes all data from lineedits
        """
        self.ui.lineEdit_var1.clear()
        self.ui.lineEdit_var2.clear()
        self.ui.lineEdit_var3.clear()
        self.ui.lineEdit_var4.clear()


    def pulses_fn(self):
        """
        This method adds and removes data from combobox depeding of the option in radiobutton
        """
        list_puls = ["MPul", "Pul", "kPul", "GPul"]
        list_freq = ["Hz", "MHz", "kHz", "GHz"]
        if self.ui.radioButton_pulses.isChecked():
            self.ui.comboBox_var1.clear()
            self.ui.comboBox_var3.clear()
            for i in list_puls:
                self.ui.comboBox_var1.addItem(i)
                self.ui.comboBox_var3.addItem(i)
        elif self.ui.radioButton_frequency.isChecked():
            self.ui.comboBox_var1.clear()
            self.ui.comboBox_var3.clear()
            for i in list_freq:
                self.ui.comboBox_var1.addItem(i)
                self.ui.comboBox_var3.addItem(i)


    def clean1_fn(self):
        """
        This method removes var1 data from lineedit
        """
        self.ui.lineEdit_var1.clear()


    def clean2_fn(self):
        """
        This method removes var2 data from lineedit
        """
        self.ui.lineEdit_var2.clear()


    def clean3_fn(self):
        """
        This method removes var3 data from lineedit
        """
        self.ui.lineEdit_var3.clear()


    def clean4_fn(self):
        """
        This method removes var4 data from lineedit
        """
        self.ui.lineEdit_var4.clear()


    def copy_bin_fn(self):
        """
        This method copies binary value to clipboard
        """
        pyperclip.copy(self.binary)
    

    def copy_hex_fn(self):
        """
        This method copies hexadecimal value to clipboard
        """
        pyperclip.copy(self.hex)