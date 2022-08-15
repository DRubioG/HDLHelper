import HDL, VHDL_regen

class Testbench_vhdl():
    def __init__(self, file_input, file_output):
        self.file_input = file_input
        self.file_output = file_output
        self.init()
    
    def init(self):
        self.hdl = HDL(self.file_input)
        self.vhdl_regen = VHDL_regen()
        

