from Backend.HDL import *
from Backend.VHDL_regen import *
import json


class Testbench_vhdl():
    def __init__(self, file_input, file_output):
        self.file_input = file_input
        self.name = self.file_input[:-4]
        self.file_output = file_output
        self.regen = VHDL_regen()
        self.load_config()
        self.testbench()

    def load_config(self):
        try:
            file = open("./config/configuration.json", 'r')
            data = json.load(file)
            self.version = data["Testbench_generator"][0]["version"]
            self.tab_spaces = data["Testbench_generator"][0]["tab_spaces"]
            self.spaces = data["Testbench_generator"][0]["spaces"]
            self.ftext = data["Testbench_generator"][0]["ftext"]
            self.etext = data["Testbench_generator"][0]["etext"]
            self.uppercase_generics = data["Testbench_generator"][0]["uppercase_generics"]
            self.uppercase_ports = data["Testbench_generator"][0]["uppercase_ports"]
            self.comments_load = data["Testbench_generator"][0]["comments"]
        except:
            self.version = "87"
            self.tab_spaces = "tab"
            self.spaces = "4"
            self.ftext = ""
            self.etext = ""
            self.uppercase_generics = "True"
            self.uppercase_ports = "False"
            self.comments_load = "False"

    def testbench(self):
        self.hdl = HDL(self.file_input)
        self.ports, self.generics, self.comments, self.entity = self.hdl.init()

        self.open_file(self.file_output)
        name = self.file_output[:-4]
        output = self.write_libraries()
        output += self.write_entity(name)
        output += self.write_architecture(name, self.generics,
                                          self.ports, self.comments, self.entity, copy=True)
        self.close_file(output)

    def open_file(self, output_file):
        self.file = open(output_file, 'w')

    def write_libraries(self):
        libraries = []
        for type in self.ports:
            if type == "unsigned":
                libraries.append("numeric_std")
        output = self.regen.libraries(self.file, libraries)
        return output

    def write_entity(self, name):
        components = [self.ports, self.generics, self.comments]

        output = self.regen.entity(name)
        return output

    def write_architecture(self, name, generics, ports, comments, entity, copy):
        output = self.regen.architecture(name, generics=generics, ports=ports, comments=comments, entity=entity, component=True, copy=copy,
                                         uppercase_gen_cfg="True", uppercase_port_cfg=self.uppercase_ports, tab_space_cfg=self.tab_spaces, etext=self.etext, ftext=self.ftext)

        return output

    def close_file(self, output):
        self.file.write(output)
        self.file.close()
