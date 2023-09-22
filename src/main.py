from GUI.HDLHelper_gui import HDLHelper_gui
import sys
from PyQt5.QtWidgets import QApplication, QSplashScreen
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap

""" This code is the start point of the program

"""

app = QApplication(sys.argv)    # call Qt application class
app.setWindowIcon(QtGui.QIcon('icon.ico'))
hdlhelper_gui = HDLHelper_gui() # call HDLHelper application
hdlhelper_gui.show()            # show the interface
sys.exit(app.exec_())           # exit at the finish
