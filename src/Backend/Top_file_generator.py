import os, json

from Backend.HDL import *
from Backend.VHDL_regen import *

class Top_file_generator():
    def __init__(self, name_p, files):
        self.name = name_p
        self.files = files
        self.vhdl_regen = VHDL_regen()
        self.read_config()
        self.create_file()

    def read_config(self):

        try:
            file = open("./config/configuration.json", 'r')
            data = json.load(file)      # get the configuration parameters
            self.version = data["version"]

            self.tool_comments = data["preferences"][0]["tool_comments"]
            self.user = data["preferences"][0]["user"]
            self.corporation = data["preferences"][0]["corporation"]
            self.contact = data["preferences"][0]["contact"]
            self.user_version = data["preferences"][0]["user_version"]
            self.tool_version_fl = data["preferences"][0]["tool_version"]
            self.date_fl = data["preferences"][0]["date"]

            self.vhdl_version = data["Top_file_generator"][0]["version"]
            self.tab_spaces = data["Top_file_generator"][0]["tab_spaces"]
            self.spaces = data["Top_file_generator"][0]["spaces"]
            self.uppercase_generics = data["Top_file_generator"][0]["uppercase_generics"]
            self.uppercase_ports = data["Top_file_generator"][0]["uppercase_ports"]
            self.comments_load = data["Top_file_generator"][0]["comments"]
        except:
            self.version = "unkown"

            self.tool_comments = "True"
            self.user = ""
            self.corporation = ""
            self.contact = ""
            self.user_version = ""
            self.tool_version_fl = "False"
            self.date_fl = "False"

            self.vhdl_version = "87"
            self.tab_spaces = "tab"
            self.spaces = "4"
            self.uppercase_generics = "True"
            self.uppercase_ports = "False"
            self.comments_load = "False"


    def create_file(self):
        ports = []
        generics = []
        comments = []
        full_entity = []
        output = ""
        for file in self.files:
            hdl = HDL(file)
            list_out = hdl.init()
            ports.append(list_out[0])
            generics.append(list_out[1])
            comments.append(list_out[2])
            full_entity.append(list_out[3])
        

        name, _ = os.path.splitext(self.name)
        _, name = os.path.split(name)

        output += self.vhdl_regen.entity(name)

        output += self.vhdl_regen.architecture(name, generics=generics, 
                                             ports=ports, 
                                             comments=comments, 
                                             component=True)

        file = open(self.name, "w")
        file.write(output)
        file.close()
        pass

        
