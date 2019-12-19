# Merge PDFs using PyPDF2

import PyPDF2
import glob
from natsort import natsorted

pdfs = glob.glob("/home/scott/projects/RedTideResearch/dataHarvests/*.pdf")
new_merged_pdf = "/home/scott/projects/RedTideResearch/dataHarvests/new_merged_pdf.pdf"

merge_pdfs = PyPDF2.PdfFileMerger()

for pdf in natsorted(pdfs):
    merge_pdfs.append(open(pdf, 'rb'))

merge_pdfs.write(open(new_merged_pdf, 'wb'))


read_pdf = PyPDF2.PdfFileReader(open("/home/scott/projects/RedTideResearch/dataHarvests/new_merged_pdf", 'rb'))
pdf_get_page = read_pdf.getPage(0)
pdf_get_page.extractText()