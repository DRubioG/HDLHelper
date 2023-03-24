
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

    def tab_spaces(self, type,  num):
        output = ""
        for i in range(num):
            output += type
        return output
    
    def uppercase(self, uppercase_conf, variable):
        if uppercase_conf == "True":
            return variable.upper()
        return variable

    def generics(self, generics, comments, uppercase_cfg, tab_spaces_cfg, comment_cfg):
        N = 1
        if generics is not None:

            lon_max = 0
            lon_max_type = 0
            for generic_len in generics:
                lon = 0
                if type(generic_len[0]) is list:
                    cont = 0
                    for generic in generic_len[0]:
                        cont += 1
                        lon += len(generic)
                        if cont != len(generic_len[0]):
                            lon += 2
                else:
                    lon = len(generic_len[0])
                if lon >= lon_max:
                    lon_max = lon

                if lon_max_type <= len(generic_len[1]):
                    lon_max_type = len(generic_len[1])
                

            output = self.tab_spaces(tab_spaces_cfg, N) + "generic (\n"

            cont_gen = 1
            for generic in generics:
                if type(generic[0]) is list:
                    output += self.tab_spaces(tab_spaces_cfg, N+1)
                    cont = 1
                    for i in generic[0]:
                        output += self.uppercase(uppercase_cfg, i)
                        if cont != len(generic[0]):
                            output += ", "
                        cont += 1
                else:
                    output += self.tab_spaces(tab_spaces_cfg, N+1) + self.uppercase(uppercase_cfg, generic[0])
                
                if type(generic[0]) is list:
                    lon_aux = 0
                    cont = 0
                    for j in generic[0]:
                        cont += 1
                        lon_aux += len(j)
                        if cont != len(generic[0]):
                            lon_aux += 2
                    dif = lon_max - lon_aux
                else:
                    dif = lon_max - len(generic[0])

                for j in range(dif):
                    output += " "

                output += self.tab_spaces(tab_spaces_cfg, 1) + " : " + generic[1]
                
                if generic[2] != '':
                    for j in range(lon_max_type - len(generic[1])):
                        output += " "
                    output += " := " + self.tab_spaces(tab_spaces_cfg, N) + self.uppercase(uppercase_cfg, generic[2])
                    
                if cont_gen != len(generics):
                    output += ";"
                cont_gen += 1

                if comment_cfg == "True":
                    for comment in comments:
                        if comment[1] == generic[3]:
                            output += self.tab_spaces(tab_spaces_cfg, N+1) + "-- " + comment[0]
                            break
                output += "\n"
            output += self.tab_spaces(tab_spaces_cfg, N) + ")" + "\n"
        return output
    

    def ports(self):
        pass

    
    def component(self, output, components, name):
        ports = components[0]
        generics = components[1]
        comments = components[2]
        name = name.split("/")[-1]
        output = "component " + name + " is\n"

        ## generics
        tab_spaces_cfg = "\t"
        uppercase_gen_cfg = "True"
        comment_cfg = "True"
        
        output += self.generics(generics, comments, uppercase_gen_cfg, tab_spaces_cfg, comment_cfg)
        


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
                        output += "--" + comment[0]
                output += "\n"
            

        output += "end component;\n"
        return output


    def implementation(self):
        pass

