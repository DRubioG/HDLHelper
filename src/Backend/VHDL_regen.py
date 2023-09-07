
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

    def architecture(self, name_ent, generics=[], ports=[], comments=[], entity=[], vhdl_version="Mixed", component=False, copy=False, uppercase_gen_cfg="False", uppercase_port_cfg="False", tab_space_cfg="", ftext="", etext="", default_config="", split_signal_constant="True"):
        """
        This method creates an VHDL architecture
        Input:
            - name_ent: string with the name of the architecture
            - generics: list with generics
            - ports: list with ports
            - comments: list with comments
            - entity: list with the entity
            - vhdl_version: string with VHDL version
            - component: flag that marks if there are a compenent in architecture
            - copy: flag about if the entity is a copy
            - uppercase_gen_cfg: flag about if generics has to be in uppers
            - uppercase_port_cfg: flag about if ports has to be in uppers
            - tab_space_cfg: flag about the type separation in code
            - ftext: string with the previous part of the signals
            - etext: string with the forward part of the signals
            - default_config: <unkown>
        Return:
            - output: string with the architecture created
        """
        output = "architecture arch_" + name_ent + " of " + name_ent + " is\n\n"

        # different options of architecture type
        if component is True and vhdl_version == "Mixed":
            output += self.arch_Mixed(name_ent, generics, ports, comments, entity, vhdl_version, copy, uppercase_gen_cfg, uppercase_port_cfg, tab_space_cfg, ftext, etext, default_config, split_signal_constant)
        elif component is True and vhdl_version == "87":
            output += self.arch_87(name_ent, generics, ports, comments, entity, vhdl_version, copy, uppercase_gen_cfg, uppercase_port_cfg, tab_space_cfg, ftext, etext, default_config, split_signal_constant)
        elif component is True and vhdl_version == "93":
            output += self.arch_93(name_ent, generics, ports, comments, entity, vhdl_version, copy, uppercase_gen_cfg, uppercase_port_cfg, tab_space_cfg, ftext, etext, default_config, split_signal_constant)

        output += "\n" + default_config + "\n\n"
        output += "end architecture arch_" + name_ent + ";"
        
        return output
    
    def arch_Mixed(self, name_ent, generics=[], ports=[], comments=[], entity=[], vhdl_version="Mixed", copy=False, uppercase_gen_cfg="False", uppercase_port_cfg="False", tab_space_cfg="", ftext="", etext="", default_config="", split_signal_constant="True"):
        """
        This method creates a mixed option VHDL architecture
        Input:
            - name_ent: string with the name of the architecture
            - generics: list with generics
            - ports: list with ports
            - comments: list with comments
            - entity: list with the entity
            - vhdl_version: string with VHDL version
            - copy: flag about if the entity is a copy
            - uppercase_gen_cfg: flag about if generics has to be in uppers
            - uppercase_port_cfg: flag about if ports has to be in uppers
            - tab_space_cfg: flag about the type separation in code
            - ftext: string with the previous part of the signals
            - etext: string with the forward part of the signals
            - default_config: <unkown>
        Return:
            - output: string with the architecture created
        """
        output = self.component(ports, generics, comments, name_ent, copy,
                                    entity, uppercase_port_cfg, uppercase_gen_cfg, tab_space_cfg, comments)
        output += self.constants(generics,
                                    tab_space_cfg, uppercase_gen_cfg, tab_space_cfg, split_signal_constant)
        output += self.signals(ports, uppercase_port_cfg,
                                uppercase_gen_cfg, tab_space_cfg, ftext, etext, split_signal_constant)
        output += "\nbegin\n"
        output += self.implementation(name_ent, generics, ports, ftext,
                                        etext, tab_space_cfg, uppercase_port_cfg, uppercase_gen_cfg, vhdl_version)
        
        return output
    
    def arch_87(self, name_ent, generics=[], ports=[], comments=[], entity=[], vhdl_version="87", copy=False, uppercase_gen_cfg="False", uppercase_port_cfg="False", tab_space_cfg="", ftext="", etext="", default_config="", split_signal_constant="True"):
        """
        This method creates a '87 option VHDL architecture
        Input:
            - name_ent: string with the name of the architecture
            - generics: list with generics
            - ports: list with ports
            - comments: list with comments
            - entity: list with the entity
            - vhdl_version: string with VHDL version
            - copy: flag about if the entity is a copy
            - uppercase_gen_cfg: flag about if generics has to be in uppers
            - uppercase_port_cfg: flag about if ports has to be in uppers
            - tab_space_cfg: flag about the type separation in code
            - ftext: string with the previous part of the signals
            - etext: string with the forward part of the signals
            - default_config: <unkown>
        Return:
            - output: string with the architecture created
        """
        output = self.component(ports, generics, comments, name_ent, copy,
                                    entity, uppercase_port_cfg, uppercase_gen_cfg, tab_space_cfg, comments)
        output += self.constants(generics,
                                    tab_space_cfg, uppercase_gen_cfg, split_signal_constant)
        output += self.signals(ports, uppercase_port_cfg,
                                uppercase_gen_cfg, tab_space_cfg, ftext, etext, split_signal_constant)
        output += "\nbegin\n"
        output += self.implementation(name_ent, generics, ports, ftext,
                                        etext, tab_space_cfg, uppercase_port_cfg, uppercase_gen_cfg, vhdl_version)
        
        return output
    
    def arch_93(self, name_ent, generics=[], ports=[], comments=[], entity=[], vhdl_version="93", 
                copy=False, uppercase_gen_cfg="False", uppercase_port_cfg="False", tab_space_cfg="", 
                ftext="", etext="", default_config="", split_signal_constant="True"):
        """
        This method creates a '93 option VHDL architecture
        Input:
            - name_ent: string with the name of the architecture
            - generics: list with generics
            - ports: list with ports
            - comments: list with comments
            - entity: list with the entity
            - vhdl_version: string with VHDL version
            - copy: flag about if the entity is a copy
            - uppercase_gen_cfg: flag about if generics has to be in uppers
            - uppercase_port_cfg: flag about if ports has to be in uppers
            - tab_space_cfg: flag about the type separation in code
            - ftext: string with the previous part of the signals
            - etext: string with the forward part of the signals
            - default_config: <unkown>
        Return:
            - output: string with the architecture created
        """
        output = self.constants(generics, tab_space_cfg, uppercase_gen_cfg, split_signal_constant)
        output += self.signals(ports, uppercase_port_cfg, uppercase_gen_cfg, tab_space_cfg, ftext, etext, split_signal_constant)
        output += "\nbegin\n"
        output += self.implementation(name_ent, generics, ports, ftext, 
                                      etext, tab_space_cfg, uppercase_port_cfg, uppercase_gen_cfg, vhdl_version)
        
        return output


    def entity(self, name_ent, generics=[], ports=[], comments=[], uppercase_gen_cfg="", uppercase_port_cfg="", tab_spaces_cfg="", comments_cfg=""):
        """
        This method creates an VHDL entity
        Input:
            - name_ent: string with the name of the architecture
            - generics: list with generics
            - ports: list with ports
            - comments: list with comments
            - uppercase_gen_cfg: flag about if generics has to be in uppers
            - uppercase_port_cfg: flag about if ports has to be in uppers
        Return:
            - output: string with the architecture created
        """
        output = "architecture arch_" + name_ent + " of " + name_ent + " is\n\n"
        output = "\nentity " + name_ent + " is\n"
        output += self.generics(generics, comments,
                                uppercase_gen_cfg, tab_spaces_cfg, comments_cfg)
        output += self.ports(ports, comments, uppercase_port_cfg,
                             uppercase_gen_cfg, tab_spaces_cfg, comments)
        output += "end entity " + name_ent + ";\n\n"
        
        return output


    def tab_spaces(self, type,  num):
        """
        This method separates code using spaces or tabulations
        Input:
            - type: flag with the separation option
            - num: number of spaces needs
        Return:
            - output: string with the separation elected
        """
        output = ""
        if type == "tab":
            type = "\t"
        for i in range(num):
            output += type

        return output


    def uppercase(self, uppercase_conf, variable):
        """
        This method change to uppers if the option is elected
        Input:
            - uppercase_conf: flag with the option elected
            - variable: string that could be changed
        Return:
            - variable: string with the option elected
        """
        if uppercase_conf == "True":
            return variable.upper()
        
        return variable


    def generics(self, generics, comments, uppercase_cfg, tab_spaces_cfg, comment_cfg, N=1):
        """
        This method creates a generic part of an VHDL file
        Input:
            - generics: list with generics
            - comments: list with comments
            - uppercase_cfg: flag about use upperscase in generics
            - tab_spaces: flag about use tabs or spaces
            - comments_cfg: flag about create generics with comments
            - N: integer with number of tabs/spaces
        Return:
            - output: string with generics created
        """

        output = ""
        if generics:

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
        """
        This method creates a ports part of an VHDL file
        Input:
            - ports: list with ports
            - comments: list with comments
            - uppercase_port_cfg: flag about use upperscase in ports
            - uppercase_gen_cfg: flag about use upperscase in generics
            - tab_spaces_cfg: flag about use tabs or spaces
            - comments_cfg: flag about create generics with comments
            - N: integer with number of tabs/spaces
        Return:
            - output: string with ports created
        """

        output = ""
        if ports:

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
        """
        This method creates a component in VHDL
        Input:
            - ports: list with ports
            - generics: list with generics
            - name: name of the component
            - copy: flag of direct copy
            - entity: list with the entity to paste in file, only if copy flag is "True"
            - uppercase_port_cfg: flag about using uppercase in ports
            - uppercase_gen_cfg: flag about using uppercase in generics
            - tab_spaces_cfg: flag about using tab or spaces
            - comment_cfg: flag about using comments in component
        Return:
            - output: string with component generated inside
        """
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

        return output + "end component;\n\n"


    def implementation(self, name,  generics, ports, ftext, etext, tab_spaces_cfg, uppercase_port_cfg, uppercase_gen_cfg, vhdl_version, N=0):
        """
        This method defines the implementation of the code in the testbench
        Input:
            - name: name of the instance
            - generics: list with generics
            - ports: list with ports
            - ftext: string previous to ports
            - etext: string forward to ports
            - tab_spaces_cfg: flag about using tabs or spaces
            - uppercase_port_cfg: flag about using uppercase in ports
            - uppercase_gen_cfg: flag about using uppercase in generics
            - vhdl_version: flag about version of vhdl elected
            - N: number of tab/spaces
        Return:
            - output: string with the implementation inside
        """

        output = "\n" + name[:-3] + "_inst : " + name + "\n"

        # This part defines the implementation of the generics
        if generics:      # analize if there are generics

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

        if ports:
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

        
        return output + ";\n"


    def max_length(self, input, split="True", ftext="", etext=""):
        """
        This method calculates the length of a list
        Input:
            - input: list of list values
            - split: flag with split option
            - ftext: previous string
            - etext: forward string
        Return:
            - lon_max: integer with the maximum length
        """
        lon_max = 0
        for var in input:
            lon = 0
            if type(var[0]) is list:   # if list is nested
                cont = 1
                for nested in var[0]:
                    if split == "True":
                        lon = len(nested) + len(ftext) + len(etext)
                        lon_max = max(lon, lon_max)
                    else:
                        lon += len(nested) + len(ftext) + len(etext)
                        if cont != len(var[0]):
                            lon += 2
                        cont += 1
            else:
                lon = len(var[0]) + len(ftext) + len(etext)
            
            lon_max = max(lon, lon_max)

        return lon_max


    def space_alignment(self, value, lon_max, ftext="", etext=""):
        """
        This method adds spaces to align the text
        Input:
            - value: string/list of input
            - lon_max: integer with the maximum variable
            - ftext: previous string
            - etext: forward string
        Return:
            - spaces: string of align spaces
        """
        spaces = ""
        
        if type(value) is list:
            lon = 0
            cont = 1
            for i in value:
                lon += len(i) + len(ftext) + len(etext)
                if cont != len(value):
                    lon += 2
                cont += 1
            dif = lon_max - lon
        else:
            dif = lon_max - len(value) - len(ftext)- len(etext)
        
        for sp in range(dif):
            spaces += " "

        return spaces


    def end_signal(self, port, uppercase_gen_cfg):
        """
        This method adds the end part of the signals
        Input:
            - port: string/list of inputs
            - uppercase_gen_cfg: flag for capital letters
        Return:
            - output: string with the end part of the signal
        """
        output = ""
        if type(port[2]) == list:
            output += port[2][0] + "(" + self.uppercase(uppercase_gen_cfg, port[2][1]) + " " + \
                port[2][2] + " " + self.uppercase(uppercase_gen_cfg, port[2][3]) + ")"
        else:
            output += port[2] 

        return output + ";\n"


    def signals(self, ports, uppercase_port_cfg, uppercase_gen_cfg, tab_space_cfg, ftext, etext, split_signal_constant, N=0):
        """
        This method creates a signal from a port list
        Input:
            - ports: list with ports
            - uppercase_port_cfg: flag about using uppercase in signals
            - uppercase_gen_cfg: flag about using uppercase in the generics of the composed ports
            - tab_space_cfg: flag about using tabs or spaces
            - ftext: string previous a signal name
            - etext: string forward a signal name
            - N: number of tabs/spaces used
        Return:
            - output: string with signals inside
        """

        if ports:
            lon_max = self.max_length(ports, split_signal_constant, ftext, etext)

            output = ""     # define the writtable variable
            signal_pre = self.tab_spaces(tab_space_cfg, N) + "signal "

            for port in ports:      
                if type(port[0]) is list:       # check if the port is nested
                    cont = 1
                    if split_signal_constant != "True":
                        output += signal_pre

                    for i in port[0]:
                        if split_signal_constant == "True":
                            output += signal_pre + ftext + self.uppercase(uppercase_port_cfg, i) + etext
                            output += self.space_alignment(i, lon_max, ftext, etext) + " : "
                            output += self.end_signal(port, uppercase_gen_cfg)

                        else:
                            output += ftext + self.uppercase(uppercase_port_cfg, i) + etext
                            if cont != len(port[0]):
                                output += ", "
                            cont += 1

                    if split_signal_constant != "True":
                        output += self.space_alignment(port[0], lon_max, ftext, etext) + " : "
                        output += self.end_signal(port, uppercase_gen_cfg)

                else:
                    output += signal_pre + ftext + self.uppercase(uppercase_port_cfg, port[0]) + etext
                    output += self.space_alignment(port[0], lon_max, ftext, etext) + " : "
                    output += self.end_signal(port, uppercase_gen_cfg)

            return output +"\n"


    def end_constant(self, constant):
        """
        This method adds the end part of the constants
        Input:
            - constant: list of constants
        Return:
            - output: string with the end part of constants
        """
        output = constant[1]
        if constant[2]:
            output += "\t := " + constant[2]
        output += ";\n"

        return output


    def constants(self, generics, tab_config, upper_generics, tab_space_cfg, split_signal_constant, N=0):
        """
        This method generates constant using a list of generics
        Input:
            - generics: list of generics
            - tab_config: flag about using tabs or spaces
            - upper_generics: flag of using uppercase in generics
            - N: number of tabs/spaces used
        Return:
            - output: string with constants inside
        """
        if generics:
            output = ""
                
            lon_max = self.max_length(generics, split_signal_constant)
            constant_pre = self.tab_spaces(tab_space_cfg, N) + "constant "

            for constant in generics:

                if type(constant[0]) is list:
                    cont = 1
                    if split_signal_constant != "True":
                        output += constant_pre

                    for j in constant[0]:
                        if split_signal_constant == "True":
                            output += constant_pre + self.uppercase(upper_generics, j)
                            output += self.space_alignment(j, lon_max) + " : "
                            output += self.end_constant(constant)
                        
                        else:
                            output += j
                            if cont != len(constant[0]):
                                output += ", "
                            cont += 1
                    
                    if split_signal_constant != "True":
                        output += self.space_alignment(constant[0], lon_max) + " : "
                        output += self.end_constant(constant)

                else:
                    output += constant_pre + self.uppercase(upper_generics, constant[0])
                    output += self.space_alignment(constant[0], lon_max) + " : "
                    output += self.end_constant(constant)

            return output + "\n"


    def paste_component(self, entity):
        """
        This method returns a component with a direct copy of an entity
        Input:
            - entity: list with the entity
        Return:
            - output: string with entity inside
        """
        output = "\n"
        for i in entity:
            output += i + "\n"
        
        return output
