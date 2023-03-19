
class VHDL_regen():
   # def __init__(self):
    def libraries(self, file, libraries):
        output = "library IEEE;\nuse IEEE.std_logic_1164.all;\n"
        for lib in libraries:
            output = "use IEEE." + lib + ".all;\n"
        return output
        
    def architecture(self):
        pass
    def entity(self):
        pass
    def generics(self):
        pass
    def ports(self):
        pass
    def component(self, output, components, name):
        ports = components[0]
        generics = components[1]
        comments = components[2]
        name = name.split("/")[-1]
        output = "component " + name + " is\n"
        ## generics
        if generics is not None:
            output += "\tgeneric (\n"
            for generic in generics:
                if len(generic[0]) != 1:
                    cont = 0
                    for i in generic[0]:
                        output += "\t"
                        if cont == len(generic[0]):
                            output += i 
                        else:
                            output += i + ", "
                        cont += 1
                else:
                    output += "\t" + generic[0]
                output += " : " + generic[1] + " " + generic[2] + ";"
                for comment in comments:
                    if comment[1] == generic[3]:
                        output += "\t--" + comment[0]
                output += "\n"
            output += "\t)"


        ## ports
        if ports is not None:
            output += "\tport ("
            cont2 = 0
            for port in ports:
                if len(port[0]) != 1:
                    cont = 1
                    for j in port[0]:
                        output += "\t"
                        if cont == len(port[0]):
                            output += j
                        else:
                            output += j + ", "
                        cont += 1
                else:
                    output += "\t" + port[0][0]

                output += " : \t" + port[1] + " " 
                if len(port[2]) != 1:
                    output += port[2][0] + " (" + port[2][1] + " " + port[2][2] + " " + port[2][3] + ")"
                else:
                    output += port[2]
                
                if cont2 != len(ports):
                    output += ";"
                else:
                    output += ");"
                
                for comment in comments:
                    if comment[1] == port[3]:
                        output += "\t--" + comment[0]
                output += "\n"
            

        output += "end component;\n"
        return output


    def implementation(self):
        pass

