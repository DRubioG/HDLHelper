import os
from PyQt5.QtWidgets import QWidget, QFileDialog, QHeaderView, QComboBox
from UI.File_generator_UI import *

from Backend.VHDL_regen import *

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
        self.ui.checkBox_comments.toggled.connect(self.comments_fn)
        self.ui.comboBox_port_generic.currentIndexChanged.connect(self.port_generic_fn)
        self.ui.lineEdit_entity.textChanged.connect(self.entity_text_fn)

        font = self.ui.textEdit_text.font()
        fontMetrics = QtGui.QFontMetricsF(font)
        spaceWidth = fontMetrics.width(' ')
        self.ui.textEdit_text.setTabStopDistance(spaceWidth * 4)
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
            self.ui.tableWidget_content.insertRow(self.ui.tableWidget_content.rowCount())
            self.ui.tableWidget_content.setItem(self.currentrow, 0, QtWidgets.QTableWidgetItem(name))
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
                self.ui.tableWidget_content.setItem(self.currentrow, 1,
                                                     QtWidgets.QTableWidgetItem(inout))
                self.ui.tableWidget_content.setItem(self.currentrow, 2,
                                                     QtWidgets.QTableWidgetItem(type))
                if not num_bits:
                    self.ui.tableWidget_content.setItem(self.currentrow, 3,
                                                         QtWidgets.QTableWidgetItem("1"))
                else:
                    self.ui.tableWidget_content.setItem(self.currentrow, 3,
                                                         QtWidgets.QTableWidgetItem(str(num_bits)))
                self.ui.tableWidget_content.setItem(self.currentrow, 4,
                                                     QtWidgets.QTableWidgetItem("port"))

            elif port_generic == "generic":
                self.ui.tableWidget_content.setItem(self.currentrow, 2,
                                                     QtWidgets.QTableWidgetItem(type))
                if not num_bits:
                    self.ui.tableWidget_content.setItem(self.currentrow, 3,
                                                         QtWidgets.QTableWidgetItem("1"))
                else:
                    self.ui.tableWidget_content.setItem(self.currentrow, 3,
                                                         QtWidgets.QTableWidgetItem(str(num_bits)))
                self.ui.tableWidget_content.setItem(self.currentrow, 4,
                                                     QtWidgets.QTableWidgetItem("generic"))
                self.generics.append([name, type, num_bits])

            self.currentrow += 1

            self.ui.lineEdit_name.clear()
            self.ui.lineEdit_bits.clear()

            output = self.file_regen.entity(self.name_entity, self.generics, self.ports)
            self.ui.textEdit_text.setText(output)



    def entity_text_fn(self):
        """
        This method updates architecture text
        """
        self.name_entity = self.ui.lineEdit_entity.text()
        if self.name_entity:
            text_arch = "arch_" + self.name_entity
        else:
            text_arch = ""
        self.ui.lineEdit_architecture.setText(text_arch)

        output = self.file_regen.entity(self.name_entity, self.generics, self.ports)
        self.ui.textEdit_text.setText(output)
        
    

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
        Create method
        """
        text = self.ui.textEdit_text.toPlainText()
        path = QFileDialog()
        path = path.getExistingDirectory(self)
        file = open(os.path.join(path, self.name_entity)+".vhd", "w")
        file.write(text)
        file.close()


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
