import os

class VHDL():
    def __init__(self, file_input, copy):
        self.file_input = file_input
        self.ports = []
        self.generics = []
        self.comments = []
        self.copy = copy

    def read_file(self):
        file = open(self.file_input, 'r')
        text = file.readlines()
        return text

    def get_entity(self):
        cont = 0
        entity = []
        entity_flag = 0
        line_counter = 0

        text = self.read_file()
        # find the entity in the file
        for t in text:
            t = t.replace("\n", "")
            t = t.replace(";", "")

            if t.find("entity")!= -1:
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
        cont_generics = 0
        generic_flag = 0
        _generics = []
        _real_generic = []

        ## get generic code from entity
        for generic in entity:
            if generic[0].lower().find("generic") != -1:
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

        #print(_real_generic)
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

        
    def get_ports(self, entity):
        cont_ports = 0
        ports_flag = 0
        _ports = []
        _real_ports = []

        ## extract ports code from entity
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
           

        ## extract generics from generic structure
        for ports in _ports:
            ports[0] = ports[0].replace("\n", "")
            ports[0] = ports[0].replace("\t", "")
            ports[0] = ports[0].replace(" ", "")
            
            if ports[0].lower() != "port(" and ports[0].lower() != '' and ports[0] != ")":
                _real_ports.append(ports)
        
       # print(_real_ports)



        ## extract all parts of the ports and add to the port list
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
        
        # get entity
        entity_comments = self.get_entity()
        if self.copy == 1:
            self.entity = entity_comments[1:-1]
            
        else:
            # get comments
            entity = self.get_comments(entity_comments)
            
            # get generics
            self.get_generics(entity)
                
                

            # extract ports
            self.get_ports(entity)
        

            

    def get_list(self):
        self.vhdl_list()
        if self.copy == 1:
            return self.entity, None, None
        else:
            return self.ports, self.generics, self.comments

if __name__=="__main__":
    vhdl = VHDL("Decoder.vhd", copy=0)
    print(vhdl.get_list())
    # print(vhdl.comments)
    # print(vhdl.ports)
    # print(vhdl.generics)



