import os

class VHDL():
    def __init__(self, file_input):
        self.file_input = file_input
        self.input_ports = []
        self.output_ports = []
        self.generics = []
        self.comments = []

    def extract_list(self):
        file = open(self.file_input, 'r')
        text = file.readlines()

        text = self.extract_comments(text)
        print(text)
        generic = self.extract_generics(text)

    def extract_comments(self, text):
        line = 0
        for t in text:
            
            if t.find("--") != -1:
                end = t.find("\n")
                start = t.find("--")
                self.comments.append([start, end, t[start: end, line]])
                text[start:end]=""
            
            line += 1
        return text

if __name__=="__main__":
    vhdl = VHDL("../../../Decoder.vhd")
    vhdl.extract_list()


