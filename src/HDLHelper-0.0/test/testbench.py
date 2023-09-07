from VHDL import VHDL

class testbench:
    def __init__(self, document, testbench_name=None):
        self.document = document
        self.testbench_name = testbench_name
        self.vhdl = VHDL(document)
        self.port_in = []
        self.port_out = []
        self.generics = []
        self.name = ""

    def generate(self):
        self.vhdl.analizar()
        self.port_in = self.vhdl.port_in
        self.port_out = self.vhdl.port_out
        self.generics = self.vhdl.generics
        self.name = self.vhdl.name
        if self.testbench_name == None:
            self.testbench_name = self.name + "_tb"

        testbench = self.generar_testbench()
        file = open(self.testbench_name+".vhd", "w")
        file.write(testbench)
        file.close()

    def generar_testbench(self):
        num_port = len(self.port_in) + len(self.port_out)
        wr="library IEEE; \nuse IEEE.STD_LOGIC_1164.ALL;\nuse ieee.numeric_std.all;\n\nentity " + self.name + "_tb is\nend " + self.name + "_tb;\n\narchitecture arch_" + self.name + "_tb of " + self.name + "_tb is\n"
        cont=0
        cont_g = 0
        wr += "component "+ self.name + " is\n"
        if self.generics != None:
            num_gen = len(self.generics)
            print(num_gen)
            wr += "\tgeneric (\n"
            for g in self.generics:
                wr += "\t\t" + g[0] + " : " + g[1] + " := " + g[2] 
                if cont_g != num_gen-1:
                    wr += ";\n"
                    cont_g += 1
                else:
                    wr += "\n\t);\n"

        wr +="\tport ( \n\t\t"
        for h in self.port_in:
            if h[1] == "std_logic":
                wr += h[0] + " : in " + h[1] 
            elif h[1]== "std_logic_vector":
                wr += h[0] + " : in " + h[1] +"("+ str(h[2]) + " downto " + str(h[3]) + ")"
            if cont != num_port-1:
                wr += ";\n\t\t"
                cont+=1
            else:
                wr += "\n\t\t"
        for r in self.port_out:
            if r[1] == "std_logic":
                wr +=   r[0] + " : out " + r[1]
            elif r[1]== "std_logic_vector":
                wr +=   r[0] + " : out " + str(r[1]) +"("+ str(r[2]) + " downto " +r[3] + ")"
            if cont != num_port-1:
                wr += ";\n\t\t"
                cont+=1
            else:
                wr += "\n\t"
        wr +=");"
        wr += "\nend component;\n"
        wr += self.generador_senales("")
        wr += "\nbegin"
        wr += self.component()

        file_config = open("testbench.config", 'r')
        text = file_config.readlines()
        wr += '\n\n'
        for t in text:
            wr += t 
        wr +="\n\nend architecture;"

        return wr
    
    def generador_senales(self, fin=""):
        sn ="\n"
        for h in self.port_in:
            if h[1] == "std_logic":
                sn += "signal " + h[0] + fin + " : " + h[1] + ";\n"
            else:
                sn += "signal " + h[0] + fin + " : " + h[1] + "(" + str(h[2]) + " downto "+ str(h[3]) + ");\n"
        for r in self.port_out:
            if r[1] == "std_logic":
                sn += "signal " + r[0] + fin + " : " + r[1] + ";\n"
            else:
                sn += "signal " + r[0] + fin + " : " + r[1] + "(" + str(r[2]) + " downto "+ str(r[3]) + ");\n"
        
        return sn

    def component(self):
        num_port = len(self.port_in) + len(self.port_out)
        cont=0
        cmp="\nDUT : entity work." + self.name
        cmp+="\n\tport map("
        for h in self.port_in:
            cmp+="\n\t\t"+ h[0] + " => " + h[0] 
            if cont != num_port-1:
                cmp += ","
                cont+=1
        for h in self.port_out:
            cmp+="\n\t\t"+ h[0] + " => " + h[0] 
            if cont != num_port-1:
                cmp += ","
                cont+=1
        cmp+="\n\t);"
        return cmp


if __name__=="__main__":
    test= testbench("PWM_generator.vhd")
    test.generate()