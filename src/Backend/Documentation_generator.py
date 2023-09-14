import json
from Backend.HDL import *
from fpdf import FPDF

class Documentation_generator():
    """
    This class generates a pdf with the description of the file
    """
    def __init__(self):
        self.read_config()
        self.pages = 0


    def read_config(self):
        """
        This method reads config file
        """
        try:
            file = open("./config/configuration.json", "r")
            self.data = json.load(file)
            self.source_code = self.data["Documentation_generator"][0]["source_code"]
            self.templates = self.data["Documentation_generator"][0]["templates"]
            self.current_template = self.data["Documentation_generator"][0]["current_template"]
        except:
            self.source_code = "True"
            self.current_template = "template_basic"
            self.templates = ["template_basic"]


    def generate(self, file_input, file_output):
        """
        This method calls the generate method and checks the options
        Input:
            - file_input: name of the file input
            - file_output: name of the file output
        """
        hdl = HDL(file_input)
        self.ports, self.generics, self.comments, _ = hdl.init()
        if self.source_code:
            self.file = open(file_input, "r")
            self.file = self.file.readlines()

        self.gen_pdf(file_output)
        
    
    def gen_pdf(self, file_output):
        """
        This method generates pdf
        Input:
            - file_output: this is the name of the pdf
        """
        self.pdf = FPDF()
        self.add_page()
        

        self.pdf_text(20, 35, file_output[:-4], size=30)
        base_x = 31
        base_y = 44
        
        base_y = self.pdf_generic(base_x, base_y)
        base_y = self.pdf_port(base_x, base_y)

        self.insert_code(base_y)

        self.pdf.output(file_output, 'F')


    def add_page(self):
        """
        This method adds a page with logo, lines and number
        """
        try:
            self.pdf.cell(0, 0, link=self.pdf.image('./img/logo/prueba.png', 190, 10, 7))
        except:
            pass
        self.pdf.add_page()
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.line(10, 20, 200, 20)
        self.pdf.line(10, 277, 200, 277)
        self.pages += 1
        self.pdf_text(190, 285, str(self.pages), size=13)
        self.pdf_text(20, 285, "Created by HDLHelper")


    def insert_code(self, y):
        """
        This method adds source code in pdf
        Input:
            - y: y position
        """
        if self.source_code == "True":
            self.pdf_text(11, y, "Source", underline=True, italic=True, color=(255,0,0), size=15)
            y=y+5
            self.insert_rect(20, y, 190, 273, fill=True, fill_color=(255, 215, 125))
            cont = 5
            cont_lines = 0
            lon_max = len(self.file)
            for line in self.file:
                cont_lines += 1
                line = line.replace("\t", "    ")
                self.pdf_text(25, y+cont, line, color=(0,0,255))
                cont += 5
                if y+cont > 270:
                    self.add_page()
                    if lon_max-cont_lines < 48:
                        self.insert_rect(20, 24, 190, 24+(lon_max-cont_lines)*5, fill=True, fill_color=(255, 215, 125))
                    else:
                        self.insert_rect(20, 24, 190, 273, fill=True, fill_color=(255, 215, 125))

                    y = 24
                    cont=5
            

    def insert_rect(self, x1, y1, x2, y2, color=(0,0,0), fill=False, fill_color=(0,0,0)):
        """
        This method inserts a retangle
        Input:
            - x1: first x position
            - y1: first y position
            - x2: second x position
            - y2: second y position
            - color: tuple with border color
            - fill: flag to fill rectangle
            - fill_color: tuple with the filled color
        """
        if x1 < x2:
            w = x2-x1
        else:
            w = x1-x2

        if y1 < y2:
            h = y2-y1
        else:
            h = y1-y2
        
        self.pdf.set_draw_color(color[0], color[1], color[2])
        self.pdf.rect(x1, y1, w, h)

        if fill:
            self.pdf.set_fill_color(fill_color[0], fill_color[1], fill_color[2])
            self.pdf.rect(x1, y1, w, h, 'F')

        

    def pdf_generic(self, base_x, base_y):
        """
        This method generates generics part
        Input:
            - base_x: x position
            - base_y: y position
        Output:
            - base_y: final y position
        """
        if self.generics:
            cont = 5
            self.pdf_text(11, base_y, "Generics", underline=True, italic=True, color=(255,0,0), size=15)
            for generic in self.generics:
                if type(generic[0]) is list:
                    for i in generic[0]:
                        cont += self.generic_desciption(base_x, base_y+cont, generic, i)
                else:
                    cont += self.generic_desciption(base_x, base_y+cont, generic)

            base_y= base_y+cont+5
        return base_y


    def pdf_port(self, base_x, base_y):
        """
        This method generates ports part
        Input:
            - base_x: x position
            - base_y: y position
        Output:
            - base_y: final y position
        """
        if self.ports:
            cont = 5
            self.pdf_text(11, base_y, "Ports", underline=True, italic=True, color=(255,0,0), size=15)
            for port in self.ports:
                if type(port[0]) is list:
                    for i in port[0]:
                        cont += self.port_desciption(base_x, base_y+cont, port, i)
                else:
                    cont += self.port_desciption(base_x, base_y+cont, port)
            base_y = base_y+cont+5
        return base_y


    def port_desciption(self, x, y, port, port_=""):
        """
        This method adds the description of the ports
        Input:
            - x: x position
            - y: y position
            - port: list with the port
            - port_: name of the port if it is individual
        Return:
            - cont: increment of lines after write one port
        """
        cont = 5
        if port_:
            self.pdf_text(x, y, '- '+port_)
        else:
            self.pdf_text(x, y, '- '+port[0])

        if port[1] == "in":
            type_ = "input"
        elif port[1] == "out":
            type_ = "output"
        elif port[1] == "inout":
            type_ = "input/output"
        text_type = " <type> " + type_ 
        self.pdf_text(x+40, y, text_type, color=(0,0,255))

        format_ = " <value> "
        if type(port[2]) is list:
            format_ += port[2][0]
            
            text_value = " <bits> " + port[2][1] + " " + port[2][2] + " " + port[2][3]
        else:
            format_ += port[2]
            text_value = ""
        
        value_text= format_ + " " + text_value
        self.pdf_text(x+75, y, value_text, color=(255,0,0))

        for com in self.comments:
            if com[1] == port[3]:
                self.pdf_text(x+40, y+5, ": " + com[0], color=(0, 111, 1))
                cont = 10
        
        return cont
        
    def generic_desciption(self, x, y, generic, generic_=""):
        """
        This method adds the description of the ports
        Input:
            - x: x position
            - y: y position
            - port: list with the port
            - port_: name of the port if it is individual
        Return:
            - cont: increment of lines after write one port
        """
        cont = 5
        if generic_:
            self.pdf_text(x, y, '- '+generic_)
        else:
            self.pdf_text(x, y, '- '+generic[0])

        text_type = " <type> " + generic[1] 
        self.pdf_text(x+40, y, text_type, color=(0,0,255))

        value_text = " <value> " + generic[2]

        self.pdf_text(x+75, y, value_text, color=(255,0,0))

        for com in self.comments:
            if com[1] == generic[3]:
                self.pdf_text(x+40, y+5, ": " + com[0], color=(0, 111, 1))
                cont = 10
        
        return cont


    def pdf_text(self, x, y, text, underline=False, bold=False, italic=False, color=(0,0,0), size=10):
        """
        This method writes text in the document
        Input:
            - x: integer of x position
            - y: integer of y position
            - text: string with text
            - underline: bool with the underline text option
            - color: tuple with color in RGB
            - size: size of the text
        """
        typ = ""
        if bold:
            typ += "B"
        if italic:
            typ += "I"
        if underline:
            typ += "U"
            
        self.pdf.set_font("Arial", typ, size=size)
        self.pdf.set_text_color(color[0], color[1], color[2])
        self.pdf.text(x, y, text)