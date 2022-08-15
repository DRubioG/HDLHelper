import sys
from GUI.Testbench_gui import Testbench_gui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5 import QtCore
#from StyleSheet import style_sheet

class HDLHelper_gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.show()

    def initializeUI(self):
        self.setFixedSize(523,250)
        self.setWindowTitle('HDLHelper')

        self.pushButton_input = QPushButton("testbench generator", self)
        self.pushButton_input.setGeometry(QtCore.QRect(10, 70, 200, 36))
        self.pushButton_input.setObjectName("testbench_generator")
        self.pushButton_input.setToolTip('Testbench Generator')
        self.pushButton_input.clicked.connect(self.testbench_generator)
    
    def testbench_generator(self):
        w=Testbench_gui()
       # w.setStyleSheet(style_sheet)
        w.exec()
        print("botono")

if __name__=="__main__":
    app = QApplication(sys.argv)
    hdlhelper_gui = HDLHelper_gui()
    hdlhelper_gui.show()
    sys.exit(app.exec_())