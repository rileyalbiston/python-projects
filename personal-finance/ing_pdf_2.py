import PyPDF2
import re


pdf_file_obj = open('Orange Everyday 01-10-2017 to 31-12-2017.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

#print(pdfReader.numPages)

# chose which page to parse and extract the content
page_obj = pdf_reader.getPage(0)
content = page_obj.extractText()

#print(content)

# turn all text into lowercase to make searching easier
lower_content = content.lower()

#print(lower_content)

# split content into header and body sections
split_content = lower_content.split("datedetailsmoney out $money in $balance $")

header = split_content[0]
body = split_content[1]

#print(body)
print()


#
# start trying to build lists from the content
#

# get the section which include the strings of the data, transactions and balance
# eg. 01/10/2017-63.863,294.86
# eg. 01/10/2017-82.003,212.86
# this sequence marks the start of each new transaction row in the pdf
date_transaction_balance = re.findall("[0-9][0-9]/[0-9][0-9]/2017[-0-9.,]*", body)

#
# get the details column
#
sp_body = re.split("[0-9][0-9]/[0-9][0-9]/2017[-0-9.,]*", body)
del sp_body[0]


for i in sp_body:
 	print(i)
#print(sp_body)

#
# get the date column
#
def get_date():
	date_list = []

	for date in date_transaction_balance:
		date = re.findall("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]", date)
	#	print(date)
		date_list.append(date[0])
		return date_list

#	for d in date_list:
#		print(d)

	

get_date()

#for item in test:
#	print(item)
#print(test)

print()

#
# get the transactions column
#
# this colum can contain unsigned numbers, representing money in and negative numbers, representing expenses
i_list = []

for i in date_transaction_balance:
	i = re.split("[0-9][0-9]/[0-9][0-9]/2017", i)
#	i = re.findall("[0-9]*.[0-9][0-9]", str(i)
#	del i[0]
	i_list.append(i[1])


#print(i_list)

j_list = []

for j in i_list:
	j = re.search("[0-9-]*.[0-9][0-9]", j)
	#print(j.group(0))
	j_list.append(j.group(0))

print()
#print(j_list)
for b in j_list:
	print(b)


# a few sanity checks
# make sure each list is the same length
print()
print("len date list: ", len(date_list))
print("len details list: ", len(sp_body))
print("len sp_body j_list: ", len(j_list))