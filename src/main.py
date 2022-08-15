from GUI.HDLHelper_gui import HDLHelper_gui
import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
hdlhelper_gui = HDLHelper_gui()
hdlhelper_gui.show()
sys.exit(app.exec_())