from Backend.VHDL import *#, Verilog

class HDL():
    """ This class takes the generics, ports, comments and entity and
        returns to the 

        Attributes:
        -   file_input : file where it will search the main parts

        Method:
        -   init(): this method analises the attribute and return the main parts
    """

    def __init__(self, file_input):
        self.file_input = file_input 
        self.init()
    
    def init(self):
        """
        This method checks type of the file and applies specific configuration
        """
        if self.file_input[-4:] == ".vhd":
            self.hdl = VHDL(self.file_input)
            ports, generics, comments, entity = self.hdl.get_list()
            return ports, generics, comments, entity
       # elif self.file_input[-2:] == ".v":
           # self.hdl = Verilog(self.file_input)
