from PyQt5.QtWidgets import QDialog
from UI.New_version_advise_UI import *
from PyQt5.Qt import QDesktopServices, QUrl
import json


class Dialog_new_version_gui(QDialog):
    def __init__(self, version_act, new_version):
        super().__init__()
        self.ui = Ui_Dialog_new_version()
        self.ui.setupUi(self)
        self.version_act = version_act
        self.new_version = new_version
        self.update_dialog()
        self.open_config()
        self.connections()
        if self.new_version_message == "True":
            self.show()
        
    def open_config(self):
        try:
            file = open("./config/configuration.json", "r")
            self.data = json.load(file)
            self.new_version_message = self.data["configuration"][0]["new_version_message"]
        except:
            self.new_version_message = "True"
      
    def connections(self):
        self.ui.pushButton_ok.clicked.connect(self.accept_fn)
        self.ui.pushButton_web.clicked.connect(self.web)
    
    def accept_fn(self):
        file = open("./config/configuration.json", "w")
        if self.ui.checkBox_show_again.isChecked() == True:
            self.data["configuration"][0]["new_version_message"] = "False"
        else:
            self.data["configuration"][0]["new_version_message"] = "True"

        json.dump(self.data, file, indent=4)
        file.close()
        self.close()

    def update_dialog(self):
        self.ui.label_previous_version.setText(self.version_act)
        self.ui.label_new_version.setText(self.new_version)

    def web(self):
        url = QUrl("https://github.com/DRubioG/HDLHelper")
        QDesktopServices.openUrl(url)
        