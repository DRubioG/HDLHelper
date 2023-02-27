from Backend.VHDL import *#, Verilog

class HDL():
    def __init__(self, file_input):
        self.file_input = file_input 
        # self.init()
    
    def init(self):
        if self.file_input[-4:] == ".vhd":
            self.hdl = VHDL(self.file_input)
            ports, generics, comments = self.hdl.extract_list()
            return ports, generics, comments
       # elif self.file_input[-2:] == ".v":
           # self.hdl = Verilog(self.file_input)
