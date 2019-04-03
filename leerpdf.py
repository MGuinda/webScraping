import PyPDF2
import bormeparser
from lxml import html
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import PyPDF2
from urllib.request import urlretrieve


date = (2015, 6, 2)
xml_url = bormeparser.get_url_xml(date)
pdf_url = bormeparser.get_url_pdf(date, bormeparser.SECCION.A, bormeparser.PROVINCIA.MADRID)

print("URL")
print(xml_url)

print("PDF")
print(pdf_url)

#DESCARGAR EL BORME PDF

path = 'C:/Users/Marta/Documents/TFG/Web Scraping/pdf1.pdf'
pdf1 = bormeparser.download_pdf(date, path, bormeparser.SECCION.A, bormeparser.PROVINCIA.MALAGA)

#Extraer texto 

pdf_file = open('pdf1.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()  
page = read_pdf.getPage(0)
page_content = page.extractText()
print (page_content)
print("Número de páginas: " )
print(number_of_pages)

