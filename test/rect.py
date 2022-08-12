import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtWidgets import QDialog, QWidget
from PyQt5.QtCore import Qt
from time import sleep
from estilo import style_sheet

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,200,600,400)
       # self.paint()
        self.show()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        # painter.setBrush(QBrush(Qt.green, Qt.DiagCrossPattern))
        painter.drawRect(100, 15, 300, 100)
        painter.eraseRect(self.rect())
      #  self.update()
        #sleep(3)
        painter.drawRect(100, 15, 100, 300)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())