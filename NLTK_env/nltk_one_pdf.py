#This is just to open one pdf for NLTK reader

import nltk
import PyPDF2

mypdf = open("/home/scott/projects/RedTideResearch/dataHarvests/COHH-impleplan_31823.pdf", mode="rb")

pdf_document = PyPDF2.PdfFileReader(mypdf)

first_page = pdf_document.getPage(3)

print(first_page.extractText())