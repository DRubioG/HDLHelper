from PyQt5.QtWidgets import QDialog
from UI.Testbench_overwrite_UI import *
import json

class Testbench_overwrite_gui(QDialog):
    """
    This method shows a window when overwrite an existing testbench
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_Testbench_overwrite()
        self.ui.setupUi(self)
        self.open_config()
        self.connections()
        if self.overwrite_message == "True":
            self.show()

    def open_config(self):
        """
        This method reads the parameter about overwriting in config json
        """
        try:
            file = open("./config/configuration.json", "r")
            self.data = json.load(file)
            self.overwrite_message = self.data["configuration"][0]["overwrite_window"]
        except:
            self.overwrite_message = "True"
        
        
    def connections(self):
        """
        This method connects UI with the operational methods
        """
        self.ui.pushButton_accept.clicked.connect(self.accept_fn)
        

    def accept_fn(self):
        """
        This method configures the clicked of accept button. It also
        read 'doesn't show again' checkbox
        """
        file = open("./config/configuration.json", "w")
        if self.ui.checkBox.isChecked() == True:
            self.data["configuration"][0]["overwrite_window"] = "False"
        else:
            self.data["configuration"][0]["overwrite_window"] = "True"

        json.dump(self.data, file, indent=4)
        file.close()
        self.close()
