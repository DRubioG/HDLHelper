from Backend.VHDL import *#, Verilog

class HDL():
    def __init__(self, file_input, copy):
        self.file_input = file_input 
        self.copy = copy
        self.init()
    
    def init(self):
        if self.file_input[-4:] == ".vhd":
            self.hdl = VHDL(self.file_input, self.copy)
            ports, generics, comments = self.hdl.get_list()
            return ports, generics, comments
       # elif self.file_input[-2:] == ".v":
           # self.hdl = Verilog(self.file_input)
