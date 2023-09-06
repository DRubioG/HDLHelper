
class VHDL_regen():
    """
    This class has the purpose to regenerate VHDL files using the list of the components of the class HDL.
    """
    def libraries(self, file, libraries):
        """
        This method is used to regenerate the libraries of VHDL. Library std_logic_1164 is included by default.
        Input:
            - libraries: a list of libraries used in VHDL
        Return:
            - one string with libraries generated
        """
        output = "library IEEE;\nuse IEEE.std_logic_1164.all;\n"
        for lib in libraries:
            output = "use IEEE." + lib + ".all;\n"
        return output

    def architecture(self, name_ent, generics=[], ports=[], comments=[], entity=[], vhdl_version="Mixed", component=False, copy=False, uppercase_gen_cfg="False", uppercase_port_cfg="False", tab_space_cfg="", ftext="", etext="", default_config=""):
        output = "architecture arch_" + name_ent + " of " + name_ent + " is\n\n"

        if component is True and vhdl_version == "Mixed":
            output += self.arch_Mixed(name_ent, generics, ports, comments, entity, vhdl_version, copy, uppercase_gen_cfg, uppercase_port_cfg, tab_space_cfg, ftext, etext, default_config)
        elif component is True and vhdl_version == "87":
            output += self.arch_87(name_ent, generics, ports, comments, entity, vhdl_version, copy, uppercase_gen_cfg, uppercase_port_cfg, tab_space_cfg, ftext, etext, default_config)
        elif component is True and vhdl_version == "93":
            output += self.arch_93(name_ent, generics, ports, comments, entity, vhdl_version, copy, uppercase_gen_cfg, uppercase_port_cfg, tab_space_cfg, ftext, etext, default_config)

        output += "\n" + default_config + "\n\n"
        output += "end architecture arch_" + name_ent + ";"
        return output
    
    def arch_Mixed(self, name_ent, generics=[], ports=[], comments=[], entity=[], vhdl_version="Mixed", copy=False, uppercase_gen_cfg="False", uppercase_port_cfg="False", tab_space_cfg="", ftext="", etext="", default_config=""):
        output = self.component(ports, generics, comments, name_ent, copy,
                                    entity, uppercase_port_cfg, uppercase_gen_cfg, tab_space_cfg, comments)
        output += self.constants(generics,
                                    tab_space_cfg, uppercase_gen_cfg)
        output += self.signals(ports, uppercase_port_cfg,
                                uppercase_gen_cfg, tab_space_cfg, ftext, etext)
        output += "\nbegin\n"
        output += self.implementation(name_ent, generics, ports, ftext,
                                        etext, tab_space_cfg, uppercase_port_cfg, uppercase_gen_cfg, vhdl_version)
        return output
    
    def arch_87(self, name_ent, generics=[], ports=[], comments=[], entity=[], vhdl_version="87", copy=False, uppercase_gen_cfg="False", uppercase_port_cfg="False", tab_space_cfg="", ftext="", etext="", default_config=""):
        output = self.component(ports, generics, comments, name_ent, copy,
                                    entity, uppercase_port_cfg, uppercase_gen_cfg, tab_space_cfg, comments)
        output += self.constants(generics,
                                    tab_space_cfg, uppercase_gen_cfg)
        output += self.signals(ports, uppercase_port_cfg,
                                uppercase_gen_cfg, tab_space_cfg, ftext, etext)
        output += "\nbegin\n"
        output += self.implementation(name_ent, generics, ports, ftext,
                                        etext, tab_space_cfg, uppercase_port_cfg, uppercase_gen_cfg, vhdl_version)
        return output
    
    def arch_93(self, name_ent, generics=[], ports=[], comments=[], entity=[], vhdl_version="93", copy=False, uppercase_gen_cfg="False", uppercase_port_cfg="False", tab_space_cfg="", ftext="", etext="", default_config=""):
        output = self.constants(generics,
                                    tab_space_cfg, uppercase_gen_cfg)
        output += self.signals(ports, uppercase_port_cfg,
                                uppercase_gen_cfg, tab_space_cfg, ftext, etext)
        output += "\nbegin\n"
        output += self.implementation(name_ent, generics, ports, ftext,
                                        etext, tab_space_cfg, uppercase_port_cfg, uppercase_gen_cfg, vhdl_version)
        return output

    def entity(self, name, generics=[], ports=[], comments=[], uppercase_gen_cfg="", uppercase_port_cfg="", tab_spaces_cfg="", comments_cfg=""):
        output = "\nentity " + name + " is\n"
        output += self.generics(generics, comments,
                                uppercase_gen_cfg, tab_spaces_cfg, comments_cfg)
        output += self.ports(ports, comments, uppercase_port_cfg,
                             uppercase_gen_cfg, tab_spaces_cfg, comments)
        output += "end entity " + name + ";\n\n"
        return output

    def tab_spaces(self, type,  num):
        output = ""
        if type == "tab":
            type = "\t"
        for i in range(num):
            output += type
        return output

    def uppercase(self, uppercase_conf, variable):
        if uppercase_conf == "True":
            return variable.upper()
        return variable

    def generics(self, generics, comments, uppercase_cfg, tab_spaces_cfg, comment_cfg, N=1):
        output = ""
        if generics != []:

            lon_max = 0
            lon_max_type = 0
            lon_max_val = 0
            existence_equal = 0
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

                if lon_max_val <= len(generic_len[2]):
                    lon_max_val = len(generic_len[2])

                if generic_len[2] != '':
                    existence_equal = 1

            output += self.tab_spaces(tab_spaces_cfg, N) + "generic (\n"

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
                    output += self.tab_spaces(tab_spaces_cfg, N+1) + \
                        self.uppercase(uppercase_cfg, generic[0])

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

                output += self.tab_spaces(tab_spaces_cfg,
                                          1) + " : " + generic[1]

                if generic[2] != '':
                    for j in range(lon_max_type - len(generic[1])):
                        output += " "
                    output += " := " + \
                        self.tab_spaces(tab_spaces_cfg, N) + \
                        self.uppercase(uppercase_cfg, generic[2])

                if cont_gen != len(generics):
                    output += ";"

                l1 = 1
                if comment_cfg == "True":
                    if existence_equal == 1 and generic[2] == '':

                        if cont_gen == len(generics):
                            l1 = 0
                        for i in range(lon_max_type - len(generic[1]) - l1):
                            output += " "
                        output += " "*4 + self.tab_spaces(tab_spaces_cfg, N)
                        for i in range(lon_max_val):
                            output += " "

                    for comment in comments:
                        if comment[1] == generic[3]:
                            output += self.tab_spaces(tab_spaces_cfg,
                                                      N+1) + "-- " + comment[0]
                            break
                cont_gen += 1
                output += "\n"
            output += self.tab_spaces(tab_spaces_cfg, N) + ");" + "\n"
        return output

    def ports(self, ports, comments, uppercase_port_cfg, uppercase_gen_cfg, tab_spaces_cfg, comment_cfg, N=1):
        output = ""
        if ports != []:

            lon_val = 0
            lon_max = 0
            lon_max_inout = 0
            lon_max_val = 0
            existence_equal = 0
            for port_len in ports:
                lon = 0
                if type(port_len[0]) is list:
                    cont = 0
                    for generic in port_len[0]:
                        cont += 1
                        lon += len(generic)
                        if cont != len(port_len[0]):
                            lon += 2
                else:
                    lon = len(port_len[0])
                if lon >= lon_max:
                    lon_max = lon

                if lon_max_inout <= len(port_len[1])+1:
                    lon_max_inout = len(port_len[1])+1

                if type(port_len[2]) is list:
                    lon_val = 5
                    for values in port_len[2]:
                        lon_val += len(values)
                else:
                    lon_val += len(port_len[2])
                if lon_max_val <= lon_val:
                    lon_max_val = lon_val

            output = self.tab_spaces(tab_spaces_cfg, N) + "port (\n"

            cont_ports = 1
            for port in ports:
                if type(port[0]) is list:
                    output += self.tab_spaces(tab_spaces_cfg, N+1)
                    cont = 1
                    for i in port[0]:
                        output += self.uppercase(uppercase_port_cfg, i)
                        if cont != len(port[0]):
                            output += ", "
                        cont += 1
                else:
                    output += self.tab_spaces(tab_spaces_cfg, N+1) + \
                        self.uppercase(uppercase_port_cfg, port[0])

                if type(port[0]) is list:
                    lon_aux = 0
                    cont = 0
                    for j in port[0]:
                        cont += 1
                        lon_aux += len(j)
                        if cont != len(port[0]):
                            lon_aux += 2
                    dif = lon_max - lon_aux
                else:
                    dif = lon_max - len(port[0])

                for j in range(dif):
                    output += " "

                output += self.tab_spaces(tab_spaces_cfg, 1) + " : " + port[1]

                for i in range(lon_max_inout - len(port[1])):
                    output += " "

                if type(port[2]) != list:
                    output += self.tab_spaces(tab_spaces_cfg, N) + port[2]
                else:
                    output += self.tab_spaces(tab_spaces_cfg, N) + port[2][0] + "(" + self.uppercase(uppercase_gen_cfg, port[2][1]) + \
                        " " + port[2][2] + " " + \
                        self.uppercase(uppercase_gen_cfg, port[2][3]) + ")"

                if cont_ports != len(ports):
                    output += ";"
                else:
                    output += ");"

                l1 = 1
                if comment_cfg == "True":
                    if cont_ports == len(ports):
                        l1 = 2

                    lonc = 0
                    if type(port[2]) is list:
                        lonc = 4
                        for values in port[2]:
                            lonc += len(values)
                    else:
                        lonc = len(port[2])

                    for i in range(lon_max_val - lonc - l1):
                        output += " "

                    for comment in comments:
                        if comment[1] == port[3]:
                            output += self.tab_spaces(tab_spaces_cfg,
                                                      N+1) + "-- " + comment[0]
                            break

                cont_ports += 1
                output += "\n"

        return output

    def component(self, ports, generics, comments, name, copy, entity, uppercase_port_cfg, uppercase_gen_cfg, tab_spaces_cfg, comment_cfg):
        name = name.split("/")[-1]
        output = "component " + name + " is\n"

        if copy == "True":
            output += self.paste_component(entity)
        else:
            # generics
            output += self.generics(generics, comments,
                                    uppercase_gen_cfg, tab_spaces_cfg, comment_cfg)

            # ports
            output += self.ports(ports, comments, uppercase_port_cfg,
                                 uppercase_gen_cfg, tab_spaces_cfg, comment_cfg)

        output += "end component;\n\n"
        return output

    def implementation(self, name,  generics, ports, ftext, etext, tab_spaces_cfg, uppercase_port_cfg, uppercase_gen_cfg, vhdl_version, N=0):
        """
        This method defines the implementation of the code in the testbench

        """

        output = "\n" + name[:-3] + "_inst : " + name + "\n"

        # This part defines the implementation of the generics
        if generics != []:      # analize if there are generics

            # Calculates the number of characters of the more longer name in generics
            lon_max = 0
            for generic_len in generics:
                if type(generic_len[0]) is list:    # this part is refered to the option of the nested generics in the list
                    for i in generic_len[0]:        # in the implementation is not contemplate the nested generics
                        lon = len(i)
                        if lon_max <= lon:
                            lon_max = lon
                else:               # if there are not nested generic names, the length is direct
                    lon = len(generic_len[0])
                if lon_max <= lon:
                    lon_max = lon

            # Ahead is the implementation of the generic map
            cont_gen = 1
            output += self.tab_spaces(tab_spaces_cfg, N+1) + "generic map (\n"
            for generic in generics:
                if type(generic[0]) is list:
                    for i in generic[0]:        # this part individualize the nested generics
                        output += self.tab_spaces(tab_spaces_cfg, N+2) + \
                            self.uppercase(uppercase_gen_cfg, i)
                        if vhdl_version != "87":
                            for j in range(lon_max - len(i)):       # this part add spaces to align the generic map
                                output += " "
                            output += self.tab_spaces(tab_spaces_cfg, N+1) + " => " + self.tab_spaces(
                                tab_spaces_cfg, N+1) + self.uppercase(uppercase_gen_cfg, i)
                        if cont_gen != len(generics):
                            output += ",\n"
                    # if cont_gen != len(generics): # this part add at the end ',' if it's not the final generic
                    #     output += ","
                    # cont_gen += 1
                else:       # this part regenerate non-nested generics
                    output += self.tab_spaces(tab_spaces_cfg, N+2) + \
                        self.uppercase(uppercase_gen_cfg, generic[0])
                    if vhdl_version != "87":
                        for j in range(lon_max - len(generic[0])):
                            output += " "
                        output += self.tab_spaces(tab_spaces_cfg, N+1) + " => " + self.tab_spaces(
                            tab_spaces_cfg, N+1) + self.uppercase(uppercase_gen_cfg, generic[0])

                    if cont_gen != len(generics): # this part add at the end ',' if it's not the final generic
                        output += ","

                    output += "\n"  # This line add a line jumping at the end of the line
                cont_gen += 1
            output += self.tab_spaces(tab_spaces_cfg, N+1) + ")\n"

        if ports != []:
            lon_max = 0
            for port_len in ports:
                if type(port_len[0]) is list:
                    for i in port_len[0]:
                        lon = len(i)+1
                        if lon_max <= lon:
                            lon_max = lon
                else:
                    lon = len(port_len[0])+1
                if lon_max <= lon:
                    lon_max = lon

            cont_port = 0
            output += self.tab_spaces(tab_spaces_cfg, N+1) + "port map (\n"
            for port in ports:
                if type(port[0]) is list:
                    cont = 1
                    for i in port[0]:
                        output += self.tab_spaces(tab_spaces_cfg, N+2) + \
                            self.uppercase(uppercase_port_cfg, i)
                        if vhdl_version != "87":
                            for j in range(lon_max - len(i)):
                                output += " "
                            output += " => " + self.tab_spaces(tab_spaces_cfg, N+1) + ftext + self.uppercase(
                                uppercase_port_cfg, i) + etext
                        if cont != len(port[0]):
                            output += ",\n"
                        cont += 1
                    if cont_port != len(ports):
                        output += ","
                    cont_port += 1
                else:
                    output += self.tab_spaces(tab_spaces_cfg, N+2) + \
                        self.uppercase(uppercase_port_cfg, port[0])
                    if vhdl_version != "87":
                        for j in range(lon_max - len(port[0])):
                            output += " "
                        output += " => " + self.tab_spaces(tab_spaces_cfg, N+1) + ftext + self.uppercase(
                            uppercase_port_cfg, port[0][0]) + etext

                    if cont_port != len(ports):
                        output += ","

                output += "\n"
                cont_port += 1
            output += self.tab_spaces(tab_spaces_cfg, N+1) + ")"

        output += ";\n"

        return output

    def signals(self, ports, uppercase_port_cfg, uppercase_gen_cfg, tab_space_cfg, ftext, etext, N=0):

        if ports != []:
            lon_max = 0     # check the maximum number of characters in the longer port
            for port_len in ports:
                lon = 0
                if type(port_len[0]) is list:
                    cont_port = 1
                    for i in port_len[0]:
                        lon += len(ftext) + len(i) + len(etext)
                        if cont_port != len(port_len[0]):
                            lon += 2        # add the space and coma to the next port
                        cont_port += 1
                else:
                    lon += len(ftext) + len(port_len[0]) + len(etext)

                if lon_max <= lon:
                    lon_max = lon

            output = ""     # define the writtable variable
            for port in ports:      
                output += self.tab_spaces(tab_space_cfg, N) + "signal "
                if type(port[0]) is list:       # check if the port is nested
                    cont = 1
                    for i in port[0]:
                        output += ftext + \
                            self.uppercase(uppercase_port_cfg, i) + etext
                        if cont != len(port[0]):
                            output += ", "
                        cont += 1
                else:
                    output += ftext + \
                        self.uppercase(uppercase_port_cfg, port[0]) + etext

                if type(port[0]) is list:       # this part adds spaces 
                    lon_port = 0
                    cont_aux = 1
                    for i in port[0]:
                        lon_port += len(i) + len(ftext) + len(etext)
                        if cont_aux != len(port[0]):
                            lon_port += 2
                            cont_aux += 1
                    for j in range(lon_max-lon_port):
                        output += " "
                else:
                    for j in range(lon_max - len(port[0]) -len(etext) - len(ftext)):
                        output += " "

                output += " : "
                if type(port[2]) == list:
                    output += port[2][0] + "(" + self.uppercase(uppercase_gen_cfg, port[2][1]) + \
                        " " + \
                        port[2][2] + " " + \
                        self.uppercase(uppercase_gen_cfg, port[2][3]) + ");\n"
                else:
                    output += port[2] + ";\n"

            return output

    def constants(self,
                  generics, tab_config, upper_generics, N=1):

        if generics != []:
            output = ""
            lon_max = 0
            for generic_len in generics:
                if type(generic_len[0]) is list:
                    cont = 1
                    for i in generic_len[0]:
                        lon = len(i)
                        if cont != len(generic_len[0]):
                            lon += 2
                        cont += 1
                        if lon_max <= lon:
                            lon_max = lon

                else:
                    lon = len(generic_len[0])
                if lon_max <= lon:
                    lon_max = lon

            for constant in generics:
                output += "constant "
                if type(constant[0]) is list:
                    cont = 1
                    for j in constant[0]:
                        output += self.uppercase(upper_generics, j)
                        if cont != len(constant[0]):
                            output += ", "
                        cont += 1
                else:
                    output += self.uppercase(upper_generics, constant[0])
                for j in range(lon_max - len(constant[0])):
                    output += " "
                output += self.tab_spaces(tab_config, N) + " : " + constant[1]
                if constant[2] != '':
                    output += " := " + \
                        self.tab_spaces(tab_config, N) + constant[2]
                output += ";\n"
            output += "\n"

            return output

    def paste_component(self, entity):
        output = "\n"
        for i in entity:
            output += i + "\n"
