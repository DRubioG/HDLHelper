from PyQt5.QtWidgets import QWidget, QFileDialog

from UI.File_generator_UI import *

class File_generator_gui(QWidget):
    """
    This class creates a new file
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_File_generator_ui()
        self.ui.setupUi(self)
        self.connections()
        self.ports = []
        self.generics = []
        self.show()


    def connections(self):
        """
        This method connects gui with functions
        """
        self.ui.pushButton_add.clicked.connect(self.add_fn)
        self.ui.pushButton_cancel.clicked.connect(self.cancel_fn)
        self.ui.pushButton_create.clicked.connect(self.create_fn)
        self.ui.pushButton_config.clicked.connect(self.config_fn)
        self.ui.radioButton_sort.toggled.connect(self.sort_fn)
        self.ui.comboBox_port_generic.currentIndexChanged.connect(self.port_generic_fn)
        self.ui.lineEdit_entity.textChanged.connect(self.entity_text_fn)
        

    def port_generic_fn(self):
        """
        This method changes GUI when port or generic is chosen
        """
        if self.ui.comboBox_port_generic.currentText() == "generic":
            self.ui.comboBox_inout.hide()
            self.ui.comboBox_type.clear()
            self.ui.comboBox_type.addItem("integer")
            self.ui.comboBox_type.addItem("unsigned")
            self.ui.lineEdit_name.setGeometry(QtCore.QRect(110, 540, 170, 25))
            self.ui.label_inout.hide()
        elif self.ui.comboBox_port_generic.currentText() == "port":
            self.ui.comboBox_inout.show()
            self.ui.label_inout.show()
            self.ui.comboBox_type.clear()
            self.ui.comboBox_type.addItem("std_logic")
            self.ui.comboBox_type.addItem("unsigned")
            self.ui.comboBox_type.addItem("integer")
            self.ui.comboBox_type.addItem("std_ulogic")
            self.ui.lineEdit_name.setGeometry(QtCore.QRect(110, 540, 91, 25))


    def add_fn(self):
        """
        This method executes add button
        """
        port_generic = self.ui.comboBox_port_generic.currentText()
        name = self.ui.lineEdit_name.text()
        type = self.ui.comboBox_type.currentText()
        inout = self.ui.comboBox_inout.currentText()
        num_bits = self.ui.lineEdit_bits.text()
        if name:
            if port_generic == "port":
                if num_bits and num_bits!='1':
                    if type == "std_logic":
                        try:
                            num_bits = int(num_bits)
                            type_ = [str(num_bits-1), "std_logic_vector", "0"]
                        except:
                            type_ = [num_bits+"-1", "std_logic_vector", "0"]
                else:
                    if type == "std_logic":
                        type_ = type
                
                self.ports.append([name, inout, type_])
            elif port_generic == "generic":
                pass
        self.ui.lineEdit_name.clear()
        self.ui.lineEdit_bits.clear()


    def entity_text_fn(self):
        """
        This method updates architecture text
        """
        text = self.ui.lineEdit_entity.text()
        if text:
            text = "arch_" + text
        self.ui.lineEdit_architecture.setText(text)
        
    

    def sort_fn(self):
        """
        This method executes sort function
        """
        pass


    def create_fn(self):
        """
        Create method
        """
        pass


    def config_fn(self):
        """
        Config method
        """
        pass
        
    
    def cancel_fn(self):
        """
        Cancel method
        """
        self.close()