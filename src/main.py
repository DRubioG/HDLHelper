from GUI.HDLHelper_gui import HDLHelper_gui
import sys
from PyQt5.QtWidgets import QApplication

""" This code is the start point of the program

"""

app = QApplication(sys.argv)    # call Qt application class
hdlhelper_gui = HDLHelper_gui() # call HDLHelper application
hdlhelper_gui.show()            # show the interface
sys.exit(app.exec_())           # exit at the finish
