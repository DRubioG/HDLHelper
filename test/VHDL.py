import os

class VHDL:
    def __init__(self, document):
        self.document = document
        self.port_in = []
        self.port_out = []
        self.generics = []

    def analizar(self):
        if self.document.endswith(".vhd"):
            self.name = self.document[:-4]
        
        file = open(self.document, 'r')
        text = file.readlines()
        #text = self.minuscula(text)
        generics = self.ext_generics(text)
        ports = self.ext_ports(text)
        
    def ext_dat(self, text, loc="port("):
        plain_text = []
        cont = 0
        puertos = []
        port_flag = 0
        # localizar puertos
        for t in text:
            t = t.replace("\n", "")
            t = t.replace(";", "")
            t = t.replace(" ", "")
            plain_text.append(t)
            
            if t.find(loc) != -1:
                port_flag = 1

            if port_flag == 1:
                cont += t.count("(")
                cont -= t.count(")")
                puertos.append(t)
            
            if cont == 0:
                port_flag = 0 

        return puertos

    def minuscula(self, text):
        minus=[]
        for t in text:
            minus.append(t.lower())
        return minus

    def ext_generics(self, text):
        genericos = self.ext_dat(text, loc = "generic(")
        nombre = []
        tipo = []
        valor = []
        for gen in genericos[1:]:
            gen1 = gen.replace("(", "")
            gen1 = gen1.replace(")", "")
            if len(gen1) > 0:
                aux = gen1.split(":", 1)
                aux2 = aux[1].split(":=")
                nombre.append(aux[0])
                tipo.append(aux2[0])
                valor.append(aux2[1])
                self.generics.append([aux[0], aux2[0], aux2[1]])
        
        return self.generics


    def ext_ports(self, text):
        puertos = self.ext_dat(text)

        # distincion del tipo de puerto
        nombre = []
        tipo = []
        formato = []
        MSB = []
        LSB = []
        for pue in puertos[1:]:
            aux=pue.split(":", -1)
            nombre.append(aux[0])
            if aux[1][:2] == "in":
                tipo.append("in")
                aux3 = aux[1][2:]
            elif aux[1][:3] == "out":
                tipo.append("out")
                aux3 = aux[1][3:]
        # localizacion del tipo de dato
            aux3=aux3.replace("(", "")
            aux3=aux3.replace(")", "")
            if aux3.find("std_logic_vector") != -1:
                aux3=aux3[16:]
                if aux3.find("downto"):
                    aux4=aux3.split("downto", -1)
                    MSB.append(aux4[0])
                    LSB.append(aux4[1])
                else:
                    aux4=aux3.split("to", -1)
                    MSB.append(aux4[1])
                    LSB.append(aux4[0])
                formato.append("std_logic_vector")
            elif aux3=="std_logic":
                formato.append("std_logic")
                MSB.append(0)
                LSB.append(0)

        i = 0
        for j in tipo:
            if j=="in":
                self.port_in.append([nombre[i], formato[i], MSB[i], LSB[i]])
            elif j=="out":
                self.port_out.append([nombre[i], formato[i], MSB[i], LSB[i]])
            i += 1
        
        return self.port_in, self.port_out

if __name__=="__main__":
    vhdl = VHDL("PWM_generator.vhd")
    vhdl.analizar()