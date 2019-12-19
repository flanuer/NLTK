# -*- coding: utf-8 -*-


import PyPDF2

pdffileobj=open("/home/scott/projects/RedTideResearch/dataHarvests/Blasco-1977-Limnology_and_Oceanography.pdf", 'rb')
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
x=pdfreader.numPages
pageobj=pdfreader.getPage(3)
text=pageobj.extractText()

file1=open("/home/scott/projects/RedTideResearch/dataHarvests/1.txt", "a")
file1.writelines(text)
file1.close()