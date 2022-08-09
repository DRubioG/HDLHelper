from VHDL import VHDL

class top:
    def __init__(self, top_name, *bottom_files):
        self.document = self.name(top_name)
        self.bottom_files = bottom_files
        self.num_files = len(bottom_files)
        self.port_in = []
        self.port_out = []
        self.generics = []
        self.component = []
        self.implement = []
    
    def name(self, document):
        if document[4:] == ".vhd":
            nomb = document[:4]
        return nomb

    def generate(self):
        for i in range(self.num_files):
            self.vhdl = VHDL(self.bottom_files[i])
            self.vhdl.analizar()
            self.port_in = self.vhdl.port_in
            self.port_out = self.vhdl.port_out
            self.generics = self.vhdl.generics
            self.name = self.vhdl.name
            self.component.append(self.generate_component())
            self.implement.append(self.generate_impl())
        text = self.generate_top()
        file = open(self.document + ".vhd", 'w')
        file.write(text)
        file.close()

    def generate_impl(self):
        wr = "\n" + self.name + "_impl : entity work." + self.name
        if self.generics is not None:
            wr += "\n\tgeneric map("
            cont = 0
            for gen in self.generics:
                wr += "\n\t\t" + gen[0] + " => " + gen[0] + "_top"
                if cont != len(self.generics)-1:
                    wr += ","
            wr += "\n\t)"

        num_port = len(self.port_in) + len(self.port_out)
        wr += "\n\tport map("
        cont = 0
        for port in self.port_in:
            wr += "\n\t\t" + port[0] + " => " + port[0] + "_top"
            if cont != num_port-1:
                wr += ","
                cont += 1
        for port in self.port_out:
            wr += "\n\t\t" + port[0] + " => " + port[0] + "_top"
            if cont != num_port-1:
                wr += ","
                cont += 1
        wr += "\n\t);"

        return wr

        
    
    def generate_component(self):
        wr = "\ncomponent " + self.name + " "
        if self.generics is not None:
            wr += "\ngeneric("
            cont = 0
            for gen in self.generics:
                wr += "\n\t" + gen[0] + " : " + gen[1] + " := " + gen[2]
                if cont != len(self.generics)-1:
                    wr +=";"
                    cont += 1
                else: 
                    wr += "\n\t);"
        
        wr += "\nport ("
        num_port = len(self.port_in) + len(self.port_out)
        cont=0
        for port in self.port_in:
            wr += "\n\t" + port[0] + " : in " + str(port[1])
            if port[1] == "std_logic_vector":
                wr += "("
                if port[3] == "0":
                    wr += port[2] + " downto 0)"
                elif port[2].isnumeric() and port[3].isnumeric():
                    if int(port[2]) > int(port[3]):
                        wr += port[2] + " downto " + port[3]
                    else:
                        wr += port[2] + " to " + port[3]
            if cont != num_port-1:
                cont += 1
                wr += ";"

        for port in self.port_out:
            wr += "\n\t" + port[0] + " : out " + str(port[1])
            if port[1] == "std_logic_vector":
                wr += "("
                if port[3] == "0":
                    wr += port[2] + " downto 0)"
                elif port[2].isnumeric() and port[3].isnumeric():
                    if int(port[2]) > int(port[3]):
                        wr += port[2] + " downto " + port[3]
                    else:
                        wr += port[2] + " to " + port[3]
            if cont != num_port-1:
                cont += 1
                wr += ";" 
                    
        wr += "\n\t);\nend component;"

        return wr
        
        
    def generate_top(self):
        wr = "library ieee;\nuse ieee.std_logic_1164.all;\nuse ieee.numeric_std.all;\n\n"
        wr += "entity " + self.document + " is\n\n\nentity " + self.document +";\n"
        wr += "\narchitecture arch_" + self.document + " of " + self.document + " is\n"
        for comp in self.component:
            wr += comp + "\n"
        wr += "\n\nbegin"
        for imp in self.implement:
            wr += imp + "\n"
        
        wr += "\nend arch_" + self.document

        return wr

if __name__=="__main__":
    top = top("hola.vhd", "PWM_generator.vhd")

    top.generate()