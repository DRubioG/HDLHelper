import VHDL, Verilog

class HDL():
    def __init__(self, file_input):
        self.file_input = file_input 
        self.init()
    
    def init(self):
        if self.file_input[:-4] == ".vhd":
            self.hdl = VHDL(self.file_input)
            self.hdl.extract_list()
        elif self.file_input[:-2] == ".v":
            self.hdl = Verilog(self.file_input)
