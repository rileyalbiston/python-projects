import PyPDF2
import re
import csv

content_list = []

pdf_file_obj = open('Orange Everyday 01-10-2017 to 31-12-2017.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

number_of_pages = pdf_reader.numPages



#print(lower_content)

# split content into header and body sections
#	split_content = lower_content.split("datedetailsmoney out $money in $balance $")

#	header = split_content[0]
#	body = split_content[1]

print("number of pages: ", number_of_pages)
#print(content)

def main(content_list):
	page_number = 0

	for page in range(number_of_pages - 1):
		page_obj = pdf_reader.getPage(page_number)
		content = page_obj.extractText()
		# turn all text into lowercase to make searching easier
		lower_content = content.lower()
		# append the content of each page to 
		content_list.append(lower_content)
		page_number += 1

	return content_list





main(content_list)

print(content_list)
