import os
from PySide6.QtWidgets import QWidget, QFileDialog, QHeaderView, QComboBox
from PySide6 import QtWidgets, QtGui, QtCore
from UI.File_generator_UI import *

from Backend.VHDL_regen import *
from Backend.HDL import *

class File_generator_gui(QWidget):
    """
    This class creates a new file
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_File_generator_ui()
        self.ui.setupUi(self)
        self.connections()
        self.libraries = []
        self.ports = []
        self.generics = []
        self.currentrow = 0
        self.name_entity = ""
        self.file_regen = VHDL_regen()
        self.charge_table()
        self.show()


    def connections(self):
        """
        This method connects gui with functions
        """
        self.ui.pushButton_add.clicked.connect(self.add_fn)
        self.ui.pushButton_cancel.clicked.connect(self.cancel_fn)
        self.ui.pushButton_create.clicked.connect(self.create_fn)
        self.ui.pushButton_config.clicked.connect(self.config_fn)
        self.ui.pushButton_components.clicked.connect(self.add_component_fn)
        self.ui.checkBox_comments.toggled.connect(self.comments_fn)
        self.ui.comboBox_port_generic.currentIndexChanged.connect(self.port_generic_fn)
        self.ui.lineEdit_entity.textChanged.connect(self.entity_text_fn)

        font = self.ui.textEdit_text.font()
        fontMetrics = QtGui.QFontMetricsF(font)
        # spaceWidth = fontMetrics.width(' ')
        # self.ui.textEdit_text.setTabStopDistance(' ' * 4)
        self.ui.textEdit_text.setStyleSheet("""
                                            QTextEdit {
                                                font-family: "MS Shell Dlg 2"; 
                                                font-size: 8pt; 
                                                /*font-weight: 400; 
                                                font-style: normal;*/
                                            }""")
        

    def charge_table(self):
        """
        This method charges table config
        """
        self.ui.tableWidget_content.setColumnCount(6)
        self.ui.tableWidget_content.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget_content.setHorizontalHeaderLabels(["Name", 
                                                               "Inout", 
                                                               "Type", 
                                                               "Value", 
                                                               "Port/Gen", 
                                                               "Comment"])
        header = self.ui.tableWidget_content.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)


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
        # combo = QComboBox()
        # combo.addItems(["in", "out", "inout"])
        port_generic = self.ui.comboBox_port_generic.currentText()
        name = self.ui.lineEdit_name.text()
        type = self.ui.comboBox_type.currentText()
        inout = self.ui.comboBox_inout.currentText()
        num_bits = self.ui.lineEdit_bits.text()

        if name:
            if port_generic == "port":
                if num_bits and num_bits != '1':
                    if type == "std_logic":
                        try:
                            num_bits = int(num_bits)
                            type_ = ["std_logic_vector", str(num_bits-1), "downto", "0"]
                        except:
                            type_ = ["std_logic_vector", num_bits+"-1", "downto", "0"]
                else:
                    type_ = type
                
                self.ports.append([name, inout, type_])

            elif port_generic == "generic":
                self.generics.append([name, type, num_bits])

            # self.currentrow += 1
            self.regenerate_table()
            self.ui.lineEdit_name.clear()
            self.ui.lineEdit_bits.clear()

            output = self.file_regen.entity(self.name_entity, self.generics, self.ports)
            self.ui.textEdit_text.setText(output)


    def regenerate_table(self):
        """
        This method regenates the table
        """
        self.ui.tableWidget_content.insertRow(self.ui.tableWidget_content.rowCount())
        self.ui.tableWidget_content.clear()
        self.charge_table()
        cont = 0
        cont = self.insert_generics(cont)
        cont = self.insert_ports(cont)


    def insert_generics(self, cont):
        """
        This method insert generics in the table
        Input:
            - cont: counter of lines
        Return:
            - cont: counter of lines
        """
        if self.generics:
            for gen in self.generics:

                self.ui.tableWidget_content.setItem(cont, 0, QtWidgets.QTableWidgetItem(gen[0]))

                self.ui.tableWidget_content.setItem(cont, 2, QtWidgets.QTableWidgetItem(gen[1]))
                 
                if not gen[2]:
                    self.ui.tableWidget_content.setItem(cont, 3, QtWidgets.QTableWidgetItem("1"))
                else:
                    self.ui.tableWidget_content.setItem(cont, 3, QtWidgets.QTableWidgetItem(str(gen[2])))
                    
                self.ui.tableWidget_content.setItem(cont, 4, QtWidgets.QTableWidgetItem("generic"))
                cont += 1
        return cont


    def insert_ports(self, cont):
        """
        This method insert ports in the table
        Input:
            - cont: counter of lines
        Return:
            - cont: counter of lines
        """
        if self.ports:
            for port in self.ports:
                fv = ""
                num_bits = 0
                self.ui.tableWidget_content.setItem(cont, 0, QtWidgets.QTableWidgetItem(port[0]))
                
                self.ui.tableWidget_content.setItem(cont, 1, QtWidgets.QTableWidgetItem(port[1]))
                
                self.ui.tableWidget_content.setItem(cont, 4, QtWidgets.QTableWidgetItem("port"))
                
                if type(port[2]) is list:
                    self.ui.tableWidget_content.setItem(cont, 2, QtWidgets.QTableWidgetItem(port[2][0]))
                    try:
                        fv = int(port[2][1])
                        lv = int(port[2][3])
                        num_bits = max(fv, lv) - min(fv, lv) + 1
                    except:
                        if port[2][1][-2:] == "-1":
                            num_bits = port[2][1][:-2]
                        else:
                            num_bits = port[2][1]
                    self.ui.tableWidget_content.setItem(cont, 3, QtWidgets.QTableWidgetItem(str(num_bits)))
                    
                else:
                    self.ui.tableWidget_content.setItem(cont, 2, QtWidgets.QTableWidgetItem(port[2]))

                    self.ui.tableWidget_content.setItem(cont, 3, QtWidgets.QTableWidgetItem("1"))
                cont += 1
        return cont


    def entity_text_fn(self):
        """
        This method updates architecture text
        """
        self.name_entity = self.ui.lineEdit_entity.text().strip()
        if self.name_entity:
            text_arch = "arch_" + self.name_entity
        else:
            text_arch = ""
        self.ui.lineEdit_architecture.setText(text_arch)

        output = self.file_gen()
        self.ui.textEdit_text.setText(output)
        
    
    def file_gen(self):
        self.file_regen.libraries(self.libraries)
        output = self.file_regen.entity(self.name_entity, self.generics, self.ports)
        return output


    def comments_fn(self):
        """
        This method executes sort function
        """
        if self.ui.checkBox_comments.isChecked():
            self.comments = True
        else:
            self.comments = False
        


    def create_fn(self):
        """
        This method creates a file with the text in textedit
        """
        text = self.ui.textEdit_text.toPlainText()
        path = QFileDialog()
        path = path.getExistingDirectory(self)
        file = open(os.path.join(path, self.name_entity)+".vhd", "w")
        file.write(text)
        file.close()


    def add_component_fn(self):

        path = QFileDialog()
        file, _ = path.getOpenFileName(self, "Select file", QtCore.QDir.currentPath(
        ), "VHDL, verilog (*.vhd *.v) ;;VHDL (*.vhd);; Verilog (*.v);; Tesbenches (*_tb.vhd *_tb.v)")
        hdl = HDL(file)
        ports, generics, _, _ = hdl.init()
        regen = VHDL_regen()
        output = regen.component(ports, generics)





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
