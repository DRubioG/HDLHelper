import Testbench_vhdl, Testbench_verilog

class HDLHelper():
    def __init__(self, file_input, file_output, operation="testbench"):
        self.file_input = file_input
        self.file_output = file_output
        self.operation = operation
        self.init()
    
    def init(self):
        if self.operation == "testbench":
            if self.file_output[:-4] == ".vhd":
                Testbench_vhdl(self.file_input, self.file_output)
            elif self.file_output[:-2]==".v":
                Testbench_verilog(self.file_input, self.file_output)
            else:
                print("Error, file not recognized")