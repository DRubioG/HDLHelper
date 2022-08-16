from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Testbench_generator(object):
    def setupUi(self, Testbench_generator):
        Testbench_generator.setObjectName("Testbench Generator")
        Testbench_generator.resize(523, 250)
         # ComboBox
        self.comboBox_input = QtWidgets.QComboBox(Testbench_generator)
        self.comboBox_input.setGeometry(QtCore.QRect(110, 80, 261, 21))
        self.comboBox_input.setObjectName("comboBox_input")
        self.comboBox_input.hide()


    # Label
        self.label_input = QtWidgets.QLabel(Testbench_generator)
        self.label_input.setText("Input File")
        self.label_input.setGeometry(QtCore.QRect(30, 80, 60, 17))

        self.label_output = QtWidgets.QLabel(Testbench_generator)
        self.label_output.setText("Output File")
        self.label_output.setGeometry(QtCore.QRect(30, 140, 70, 17))

    #QLineEdit
        self.lineEdit_input = QtWidgets.QLineEdit(Testbench_generator)
        self.lineEdit_input.setGeometry(QtCore.QRect(110, 80, 261, 21))

        self.lineEdit_output = QtWidgets.QLineEdit(Testbench_generator)
        self.lineEdit_output.setGeometry(QtCore.QRect(110, 140, 261, 21))

    # Buttons
        self.pushButton_input = QtWidgets.QPushButton("search", Testbench_generator)
        self.pushButton_input.setGeometry(QtCore.QRect(400, 70, 95, 36))
        self.pushButton_input.setObjectName("pushButton_input")
        self.pushButton_input.setToolTip('Input file')

        self.pushButton_output = QtWidgets.QPushButton("search", Testbench_generator)
        self.pushButton_output.setGeometry(QtCore.QRect(400, 130, 95, 36))
        self.pushButton_output.setObjectName("pushButton_output")
        self.pushButton_output.setToolTip('Output file')
    
        self.pushButton_create = QtWidgets.QPushButton("Create", Testbench_generator)
        self.pushButton_create.setGeometry(QtCore.QRect(300, 195, 95, 36))
        self.pushButton_create.setObjectName("pushButton_create")
        self.pushButton_create.setToolTip('Create')
        
        self.pushButton_cancel = QtWidgets.QPushButton("Cancel", Testbench_generator)
        self.pushButton_cancel.setGeometry(QtCore.QRect(409, 195, 95, 36))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_cancel.setToolTip('Cancel')

        self.pushButton_config = QtWidgets.QPushButton("Config", Testbench_generator)
        self.pushButton_config.setGeometry(QtCore.QRect(190, 195, 95, 36))
        self.pushButton_config.setObjectName("pushButton_config")
        self.pushButton_config.setToolTip('Configuration button')