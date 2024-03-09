from GUI.HDLHelper_gui import HDLHelper_gui
import sys
from PySide6.QtWidgets import QApplication
from PySide6 import QtGui

""" This code is the start point of the program

"""

app = QApplication(sys.argv)    # call Qt application class
app.setWindowIcon(QtGui.QIcon('icon.ico'))
hdlhelper_gui = HDLHelper_gui() # call HDLHelper application
hdlhelper_gui.show()            # show the interface
sys.exit(app.exec())           # exit at the finish
