from HDL import *
from VHDL_regen import *


class Testbench_vhdl():
    def __init__(self, file_input, file_output):
        self.file_input = file_input
        self.name = self.file_input[:-4]
        self.file_output = file_output
        self.regen = VHDL_regen()
        self.init()
    
    def init(self):
        self.hdl = HDL(self.file_input)
        self.ports, self.generics, self.comments = self.hdl.init()

    def generate_file(self, output_file):
        self.file = open(output_file, 'w')

    def write_libraries(self):
        libraries = []
        for type in self.ports:
            if type == "unsigned":
                libraries.append("std_logic_unsigned")
        self.regen.libraries(self.file, libraries)
        
    def write_component(self):
        components = [self.ports, self.generics, self.comments]
        self.regen.component(self.file, components, self.name)
        

if __name__ == "__main__":
    testbench_vhdl = Testbench_vhdl("Decoder.vhd", "Decoder_tb")

