from importlib.metadata import entry_points
import os

class VHDL():
    def __init__(self, file_input):
        self.file_input = file_input
        self.ports = []
        self.generics = []
        self.comments = []

    def extract_file(self):
        file = open(self.file_input, 'r')
        text = file.readlines()
        return text

    def extract_entity(self):
        cont = 0
        entity = []
        entity_flag = 0
        line_counter = 0

        text = self.extract_file()
        # find the entity in the file
        for t in text:
            t = t.lower()
            t = t.replace("\n", "")
            t = t.replace(";", "")

            if t.find("entity")!= -1:
                entity_flag = 1
            
            if entity_flag == 1:
                cont += t.count("(")
                cont -= t.count(")")
                entity.append([t, line_counter])
            
            if t.find("end ") != -1:    # find the "end" of the entity
                if cont == 0:   # to avoid names with "end" characters in the name
                    entity_flag = 0
                    break   # finish the execution
            line_counter += 1
        # print(entity)
        return entity
        
    def vhdl_list(self):
        cont_generics = 0
        cont_ports = 0
        generic_flag = 0
        ports_flag = 0
        _generics = []
        _real_generic = []
        
        entity = self.extract_entity()

        # extract comments
        for comment in entity:
            if comment[0].find("--") != -1:
                com = comment[0].split("--")[1]
                line = comment[1]
                self.comments.append([com, line])
        
        # extract generics
        ## extract generic code from entity
        for generic in entity:
            if generic[0].find("generic") != -1:
                generic_flag = 1
            
            if generic_flag == 1:
                cont_generics += generic[0].count("(")
                cont_generics -= generic[0].count(")")
                _generics.append([generic[0], generic[1]])
                if cont_generics == 0:
                    break
        
        ## extract generics from generic structure
        for generic in _generics:
            generic[0] = generic[0].replace("\n", "")
            generic[0] = generic[0].replace("\t", "")
            generic[0] = generic[0].replace("(", "")
            generic[0] = generic[0].replace(")", "")
            generic[0] = generic[0].replace(" ", "")
            if generic[0] != "generic" and generic[0] != '':
                _real_generic.append(generic)

        ## extract all parts of generics and add to a generics list
        for generic in _real_generic:
            aux1 = generic[0].split(":=")
            aux2 = aux1[0].split(":")
            aux3 = aux2[0].split(",")

            if len(aux3)!= 1:
                name = aux3
            else:
                name = aux3[0]
            
            if len(aux1 ) == 1:
                value = ""
            else:
                value = aux1[1]

           
            type_ = aux2[1]
            line = generic[1]

            self.generics.append([name, type_, value, line])
            

        # extract ports
        print(self.generics)
            # print(rest)

       # print(_real_generic)




    # def extract_list(self):
    #     file = open(self.file_input, 'r')
    #     text = file.readlines()

    #     text = self.extract_comments(text)
    #     print(text)
    #     generic = self.extract_generics(text)

    # def extract_comments(self, text):
    #     line = 0
    #     for t in text:
            
    #         if t.find("--") != -1:
    #             end = t.find("\n")
    #             start = t.find("--")
    #             self.comments.append([start, end, t[start: end, line]])
    #             text[start:end]=""
            
    #         line += 1
    #     return text

if __name__=="__main__":
    vhdl = VHDL("Decoder.vhd")
    vhdl.vhdl_list()


