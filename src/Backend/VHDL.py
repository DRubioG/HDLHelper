import os

class VHDL():
    """
    This class is used to convert VHDL code to a Python list
    """
    def __init__(self, file_input):
        self.file_input = file_input
        self.ports = []
        self.generics = []
        self.comments = []


    def read_file(self):
        """
        This method is used to read VHDL file
        Return:
            - text: a list with VHDL lines of the file
        """
        file = open(self.file_input, 'r')
        self.text = file.readlines()


    def get_entity(self):
        """
        This method split the entity part of the VHDL code
        Return:
            - entity: a list with the lines of the entity
        """
        cont = 0
        entity = []
        entity_flag = 0
        line_counter = 0

        self.read_file()
        # find the entity in the file
        for t in self.text:
            t = t.replace("\n", "")
            t = t.replace(";", "")

            if t.find("entity") != -1:
                entity_flag = 1

            if entity_flag == 1:
                cont += t.count("(")
                cont -= t.count(")")
                entity.append([t, line_counter])

            if cont == 0:
                if entity_flag == 1:
                    if t[:3] == "end":
                        break

            line_counter += 1

        return entity


    def get_comments(self, code):
        """
        This method gets VHDL comments of the input list
        Comment list follows this scheme: [<comment>, <number of the line>]
        Input:
            - code: a list with VHDL line with comments
        Return:
            - entity: a list of comments and the number of the line too
        """
        entity = []

        for comment_line in code:
            if comment_line[0].find("--") != -1:
                text, comment = comment_line[0].split("--")
                self.comments.append([comment.strip(), comment_line[1]])
                entity.append([text, comment_line[1]])
            else:
                entity.append(comment_line)

        return entity


    def get_generics(self, entity):
        """
        This method gets the generics of the list of lines of VHDL code
        List follows this scheme: [<name>, <type>, <value>, <number of the line>]
        Input:
            - entity: a list with the list of VHDL lines
        """
        cont_generics = 0
        generic_flag = 0
        _generics = []
        _real_generic = []

        # get generic code from entity
        for generic in entity:
            if generic[0].lower().find("generic") != -1:
                generic_flag = 1

            if generic_flag == 1:
                cont_generics += generic[0].count("(")
                cont_generics -= generic[0].count(")")
                _generics.append([generic[0], generic[1]])
                if cont_generics == 0:
                    break

        # extract generics from generic structure
        for generic in _generics:
            generic[0] = generic[0].replace("\n", "")
            generic[0] = generic[0].replace("\t", "")
            generic[0] = generic[0].replace("(", "")
            generic[0] = generic[0].replace(")", "")
            generic[0] = generic[0].replace(" ", "")
            if generic[0] != "generic" and generic[0] != '':
                _real_generic.append(generic)

        # extract all parts of generics and add to a generics list
        for generic in _real_generic:
            aux1 = generic[0].split(":=")
            aux2 = aux1[0].split(":")
            aux3 = aux2[0].split(",")

            if len(aux3) != 1:
                name = aux3
            else:
                name = aux3[0]

            if len(aux1) == 1:
                value = ""
            else:
                value = aux1[1]

            type_ = aux2[1]
            line = generic[1]

            self.generics.append([name, type_, value, line])


    def get_ports(self, entity):
        """
        This method gets the port lines of the VHDL code
        Ports list follows this scheme:
        Only one bit:   [<name>, <in/out/inout>, <type>, <number of line>]
        Multiple bits:  [<name>, <in/out/inout>, [<type>, <first value>, <downto/to>, <last value>], <number of line>]
        Input:
            - entity: a list of the entity lines of VHDL code
        """
        cont_ports = 0
        ports_flag = 0
        _ports = []
        _real_ports = []

        # extract ports code from entity
        for ports in entity:
            if ports[0].lower().find("port") != -1:
                ports_flag = 1

            if ports_flag == 1:
                cont_ports += ports[0].count("(")
                cont_ports -= ports[0].count(")")
                _ports.append([ports[0], ports[1]])
               # print(ports)
                if cont_ports == 0:
                    break

        # extract generics from generic structure
        for ports in _ports:
            ports[0] = ports[0].replace("\n", "")
            ports[0] = ports[0].replace("\t", "")
            ports[0] = ports[0].replace(" ", "")

            if ports[0].lower() != "port(" and ports[0].lower() != '' and ports[0] != ")":
                _real_ports.append(ports)

       # print(_real_ports)

        # extract all parts of the ports and add to the port list
        cont = 1
        for ports in _real_ports:

            aux2 = ports[0].split(":")
            if aux2[0].find(",") != -1:
                name = aux2[0].split(",")
            else:
                name = aux2[0]

            type_aux = aux2[1]
            if type_aux[:2].lower() == "in":
                inout = "in"
                aux3 = type_aux[2:]
            elif type_aux[:3].lower() == "out":
                inout = "out"
                aux3 = type_aux[3:]
            elif type_aux[:5].lower() == "inout":
                inout = "inout"
                aux3 = type_aux[5:]

            if aux3.find("(") != -1:
                if aux3.lower().find("downto") != -1:
                    div = aux3.split("downto")
                    mv = "downto"
                elif aux3.lower().find("to"):
                    div = aux3.split("to")
                    mv = "to"

                div[0] = div[0].split("(", 1)

                type = div[0][0].lower()
                fv = div[0][1]

                if cont != len(_real_ports):
                    lv = div[1][:-1]
                else:
                    lv = div[1][:-2]

                self.ports.append([name, inout, [type, fv, mv, lv], ports[1]])
            else:
                type = aux3.lower()
                self.ports.append([name, inout, type, ports[1]])

            cont += 1


    def vhdl_list(self):
        """
        This method executes the necesary methods to get the differents part of an VHDL file
        """

        # get entity
        entity_comments = self.get_entity()

        self.entity = entity_comments[1:-1]

        # get comments
        entity = self.get_comments(entity_comments)

        # get generics
        self.get_generics(entity)

        # extract ports
        self.get_ports(entity)


    def get_list(self):
        """
        This method is called to get the parts of an VHDL file
        Return:
            - self.port: global list of ports in VHDL
            - self.generics: global list of generics in VHDL 
            - self.comments: global list of comments about VHDL file
            - self.entity: global list of the literal entity
        """
        self.vhdl_list()
        return self.ports, self.generics, self.comments, self.entity


    def get_signals(self):
        """
        This method returns the signals in the following scheme of list:
        Non declared:   [<name>, <type>]
        Declared:       [<name>, <type>, [<MSB>, <downto/to>, <LSB>]]
        Return:
            - signal_list: a list with the signals
        """
        self.read_file()
        signal_raw = []
        signal_list = []
        # find signal in the file
        for t in self.text:
            t = t.replace("\n", "")

            if t.find("signal") != -1:
                t1 = t.replace("signal ", "")
                t1 = t1.split(":")
                t1[0] = t1[0].replace(" ", "")
                t1[1] = t1[1].split("(")
                if len(t1[1]) != 1:
                    t1[1][1] = t1[1][1][:t1[1][1].find(";")-1]
                    t1[1][1] = t1[1][1].split(" ")
                else:
                    t1[1][0] = t1[1][0].replace(";", "")
                t1[1][0] = t1[1][0].replace(" ", "")
                signal_raw.append(t1)

        for signal in signal_raw:
            signal_aux = []
            if len(signal[1]) != 1:
                signal_aux.append(signal[0])
                signal_aux.append(signal[1][0])
                signal_aux.append(signal[1][1])
                signal_list.append(signal_aux)
            else:
                signal_aux.append(signal[0])
                signal_aux.append(signal[1][0])
                signal_list.append(signal_aux)

        return signal_list
            

    def get_constants(self):
        """
        This method returns the signals in the following scheme of list:
        Non declared:   [<name>, <type>, <value>]
        Declared:       [<name>, <type>, [<MSB>, <downto/to>, <LSB>], <value>]
        Return:
            - constant_list: a list with the constants
        """
        for t in self.text:
            t = t.replace("\n", "")




if __name__ == "__main__":
    vhdl = VHDL("Decoder.vhd")
    print(vhdl.get_signals())
