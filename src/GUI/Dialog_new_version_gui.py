from PySide6.QtWidgets import QDialog
from UI.New_version_advise_UI import *
from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
import json


class Dialog_new_version_gui(QDialog):
    """
    This is the GUI controller of the new version of HDLHelper
    """
    def __init__(self, version_act, new_version):
        super().__init__()
        self.ui = Ui_Dialog_new_version()
        self.ui.setupUi(self)
        self.version_act = version_act
        self.new_version = new_version
        self.update_dialog()
        self.open_config()
        self.connections()
        # if the checkbox is marked with doesn't show
        if self.new_version_message == "True":
            self.show()
        
    def open_config(self):
        """
        This method reads in the config file if it has to show new version window
        """
        try:
            file = open("./config/configuration.json", "r")
            self.data = json.load(file)
            self.new_version_message = self.data["configuration"][0]["new_version_message"]
        except:
            self.new_version_message = "True"
      
    def connections(self):
        """
        This method connects user interface with the working methods
        """
        self.ui.pushButton_ok.clicked.connect(self.accept_fn)
        self.ui.pushButton_web.clicked.connect(self.web)
    
    def accept_fn(self):
        """
        This method configures the accept button. It also reads the checkbox of
        'doesn't show again' and change the value of the json file
        """
        file = open("./config/configuration.json", "w")
        if self.ui.checkBox_show_again.isChecked() == True:
            self.data["configuration"][0]["new_version_message"] = "False"
        else:
            self.data["configuration"][0]["new_version_message"] = "True"

        json.dump(self.data, file, indent=4)
        file.close()
        self.close()

    def update_dialog(self):
        """
        This method updates labels of the interface to show the versions of updates
        """
        self.ui.label_previous_version.setText(self.version_act)
        self.ui.label_new_version.setText(self.new_version)

    def web(self):
        """
        This method redirects to the browser to see the new version of HDLHelper
        """
        url = QUrl("https://github.com/DRubioG/HDLHelper")
        QDesktopServices.openUrl(url)
        