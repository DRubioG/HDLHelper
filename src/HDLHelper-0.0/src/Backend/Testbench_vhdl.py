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
        self.load_ports()
        self.exec()
    

    def load_config(self):
        file = open("./config/Testbench_generator_config.json", 'r')
        data = json.load(file)
        self.version = data["Testbench_generator"][0]["version"]
        self.tab_spaces = data["Testbench_generator"][0]["tab_spaces"]
        self.spaces = data["Testbench_generator"][0]["spaces"]
        self.ftext = data["Testbench_generator"][0]["ftext"]
        self.etext = data["Testbench_generator"][0]["etext"]
        self.uppercase_generics = data["Testbench_generator"][0]["uppercase_generics"]
        self.uppercase_ports = data["Testbench_generator"][0]["uppercase_ports"]

        
    def load_ports (self):
        self.hdl = HDL(self.file_input)
        self.ports, self.generics, self.comments = self.hdl.init()
        

    def exec(self):
        self.generate_file(self.file_output)
        output = self.write_libraries()
        output += self.write_component()
        self.close_file(output)


    def generate_file(self, output_file):
        self.file = open(output_file, 'w')


    def write_libraries(self):
        libraries = []
        for type in self.ports:
            if type == "unsigned":
                libraries.append("numeric_std")
        output = self.regen.libraries(self.file, libraries)
        return output
        

    def write_component(self):
        components = [self.ports, self.generics, self.comments]
        output = self.regen.component(self.file, components, self.name)
        return output
        
        
    def close_file(self, output):
        self.file.write(output)
        self.file.close()
   