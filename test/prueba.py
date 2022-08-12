import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QFileSystemModel, QVBoxLayout, QLineEdit, QHBoxLayout, QPlainTextEdit, QTextEdit
from PyQt5.QtCore import QModelIndex, QDir
from PyQt5.QtGui import QColor, QFont, QFontDatabase
from stylesheet import style_sheet
import re

class FileSystemView(QWidget):
    def __init__(self, dir_path):
        super().__init__()
        self.dir_path = dir_path

        #TITULO Y DIMENSIONES DE LA VENTANA.
        self.setWindowTitle('File System Viewer')
        self.setGeometry(300, 300, 800, 300)

        #DEFINIR DIRECTORIO.
        self.model = QFileSystemModel()
        self.model.setRootPath(dir_path)
        

        #GENERAR VISTA DE ARCHIVOS Y CARPETAS.
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(dirPath))
        self.tree.setColumnWidth(200,250)
        self.tree.setAlternatingRowColors(True)
        self.r = QModelIndex()
        self.tree.clicked.connect(self.on_treeView_clicked)

        self.line = QTextEdit()
        self.line.setReadOnly(True)


        #MOSTRAR VENTANA CON LAS VISTA.
        layout = QHBoxLayout()
        layout.addWidget(self.tree)
        layout.addWidget(self.line)


        self.setLayout(layout)

    def on_treeView_clicked(self):
        redColor = QColor(255, 0, 0)
        blackColor = QColor(0, 0, 0)

   #     self.line.setTextColor(redColor)

    ##    redText = "I want this text red"
    #    self.line.write(redText)


      #  self.line.setTextColor(blackColor)

     #   blackText = "And this text black"
    #    self.line.append(blackText)

        s=self.tree.selectedIndexes()
        #print(self.model)
       # try:
        fileName= self.model.filePath(s[0])
        #text_edit=QTextEdit()
        text=open(fileName).read()
        #print(text)
        #text=text.replace("\n", "&#10;&#13;")
        #textprv= "<span style=\" font-size:8pt; font-weight:600; color:blue; white-space:pre-line;\" >"
        #textprv+=text
        #textprv+="</span>"
          #  print(fileName)
           # if fileName[-3:] == "vhd":
         #       word="entity"
         #       t = text.find(word)
          #      textColor=text[t:t+len(word)]
          #      print(textColor)
                #print(text[t:t+len(word)])
               # print(textColor)
         #       textColor.setTextColor(QColor(0,255,0))
         #       textColor.write(word)
          #      text.replace(word, textColor)
                
         #       self.line.setPlainText(text)
                #print(t)
         #   else:
          #      print("No entro")
                #print(fileName[-3:])
       # print()
        entity_loc = text.find("entity")
       # p=[]
        db = QFontDatabase()
        self.line.clear()
        font = db.font("Roboto", "Medium Italic", 7)
        self.line.setFont(font)
        if entity_loc != -1:
           # print("dentro")
           # p.append(text[:entity_loc])
           # p.setTextColor(QColor(0, 0, 255))
           # p.append(text[entity_loc:entity_loc+len("entity")])
           # p.setTextColor(QColor(0, 0, 0))
           # p.append(text[entity_loc+len("entity"):])
           # self.line.append(p)
            n=5
            text = text.replace("\t", " "*n)
            self.line.append(text[:entity_loc])

            self.line.setTextColor(QColor(0,0,255))
            self.line.setFontWeight(QFont.Bold)
            #self.line.append("<span style=\" font-size:8pt; font-weight:600; color:#ff0000; \">")
            self.line.insertPlainText(text[entity_loc:entity_loc+len("entity ")])

            # self.line.append("</span>")
            self.line.setTextColor(QColor(0, 0, 0))
            self.line.setFontWeight(QFont.Normal)
            #self.line.setFont(font)
            #self.line.setFont(self.font)
            self.line.insertPlainText(text[entity_loc+len("entity "):])

            
            # print(self.line)
            # self.line.setTe
            #self.line.setTextColor('#FFFFFF') 
                        
            #print(self.model.filePath(s[0]))
    #    except:
     #       None
        #for i in text:
         #   print(text)
     #   coment = [i for i in len(text) text.find("--")
        #if coment != -1:
        end_line = [_.start() for _ in re.finditer("\n", text)] 
        start_comment = [_.start() for _ in re.finditer("--", text)] 
        print(end_line)
        print(start_comment)
        cadena=[]
        for i in start_comment:
            for j in end_line:
                if j > i:
                    cadena.append((i, j))
                   
                    break

        print(cadena)
        """for i in str(start_comment[0]):
            for j in end_line:
                if j>i:
                  #  print(i)
                  #  print(j)
                    break
        """    

    


if __name__ == '__main__':
    app = QApplication(sys.argv)

    #DIRECTORIO BASE.
    dirPath = os.getcwd()
   # app.setStyleSheet("""
    #QTreeView{
     #   alternate-background-color: rgb(255, 255, 0);
      #  color: rgb(0, 0, 0);
 #   }
  #  QTreeView::item:selected{
   #     background-color: red;
    #    color:blue
#    }
 #   QTreeView::branch:adjoins-item{
  #      image: url(icon.png);
   # }
#""")
    demo = FileSystemView(dirPath)
    demo.show()
    sys.exit(app.exec_())