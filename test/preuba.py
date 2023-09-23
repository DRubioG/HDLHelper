import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
# from PyQt5 import 

def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QPushButton(w)
   b.setText("Show message!")

   b.move(50,50)
   b.clicked.connect(showdialog)
   w.setWindowTitle("PyQt Dialog demo")
   w.show()
   sys.exit(app.exec_())
	
def showdialog():
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Information)

   msg.setText("This is a message box")
   msg.setInformativeText("This is additional information")
   msg.setWindowTitle("MessageBox demo")
   # msg.setDetailedText("The details are as follows:")
   msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
   msg.buttonClicked.connect(msgbtn)
   dontShowCheckBox = QCheckBox("don't show this message again")
   dontShowCheckBox.setCheckable(True)
   msg.setCheckBox(dontShowCheckBox)

   retval = msg.exec_()

   if dontShowCheckBox.isChecked():
      print("Prueba")
   print("value of pressed message box button:", retval)
	
def msgbtn(i):
   print("Button pressed is:",i.text())
	
if __name__ == '__main__': 
   window()
