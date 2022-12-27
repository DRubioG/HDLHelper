
class VHDL_regen():
   # def __init__(self):
    def libraries(self, output, libraries):
        output += "library IEEE;\n \
            use IEEE.std_logic_1164.all;\n"
        for lib in libraries:
            output = "use." + lib + ".all;\n"
            
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
        output += "component " + name + " is\n"
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
                    if comment[1] == generic[4]:
                        output += "\t--" + comment[0]
                output += "\n"


        ## ports
        if ports is not None:
            output += "\tport ("

        output += "end component;\n"
        return output


    def implementation(self):
        pass

