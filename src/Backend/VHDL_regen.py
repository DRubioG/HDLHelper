
class VHDL_regen():
   # def __init__(self):
    def libraries(self, output, libraries):
        output = "library IEEE;\n \
            use IEEE.std_logic_unsigned.all;\n"
        for lib in libraries:
            output = "use." + lib + ".all;n"
            
        return output
        
    def architecture(self):
        pass
    def entity(self):
        pass
    def generics(self):
        pass
    def ports(self):
        pass
    def component(self):
        pass
    def implementation(self):
        pass
