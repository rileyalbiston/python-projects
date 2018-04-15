import PyPDF2
import re
import csv


content_list = []

# create universal lists for each column
date_list = []
tansactions_list = []
details_list = []

#
# append the content of each page in the pdf into a single list
#
def build_content(pdf_reader, number_of_pages, content_list):
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


#
# combine the three lists to create a csv file
#
def create_csv(date_list, tansactions_list, details_list):
#	print(date_list)
	combined = zip(date_list, tansactions_list, details_list)
	print(combined)
	with open('text.csv', 'w', newline='') as f:
	    writer = csv.writer(f)
	    writer.writerows(zip(date_list, tansactions_list, details_list))
#delimiter=','

#
# get the date column
#
def get_date(date_transaction_balance):
	for date in date_transaction_balance:
		date = re.findall("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]", date)
		date_list.append(date[0])

	return date_list

#
# get the transactions column
#
# this colum can contain unsigned numbers, representing money in and negative numbers, representing expenses
def get_transactions(date_transaction_balance):
	intermidate_tansactions_list = []

	for item in date_transaction_balance:
		item = re.split("[0-9][0-9]/[0-9][0-9]/2017", item)
		intermidate_tansactions_list.append(item[1])

	for item in intermidate_tansactions_list:
		item = re.search('[0-9-,]*[.][0-9][0-9]', item)
		tansactions_list.append(item.group(0))

	return tansactions_list


#
# get the details column
#
def get_details(body):
	details = re.split("[0-9][0-9]/[0-9][0-9]/2017[-0-9.,]*", body)
	del details[0]
	for item in details:
		details_list.append(item)

	return details_list


def main():

	pdf_file_obj = open("Orange Everyday 01-07-2017 to 30-09-2017.pdf", 'rb')
	pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

	number_of_pages = pdf_reader.numPages

	print("number of pages: ", number_of_pages)

	build_content(pdf_reader, number_of_pages, content_list)

	# convert the content_list into a string
	content_string = ''.join(content_list)
#	print(content_string)

	lower_content = content_string.lower()

	# split content into header and body sections
	split_content = lower_content.split("datedetailsmoney out $money in $balance $")


	header = split_content[0]
	body = split_content[1]


	body = re.sub('page \d{0,2} of \d{0,2}', '', body)
	body = re.sub(' [|] statement continued over', '', body)
	body = re.sub('e-\d{0,2}  s-\d{0,2}  i-\d{0,2}transactions [(]continued[)]datedetailsmoney out [$]money in [$]balance [$]', '', body)

	body = re.sub('total bonuses financial year to date: [$]0.00total bonuses for this statement: [$]\d{0,6}.\d{0,2}total rebates financial year to date: [$]\d{0,6}.\d{0,2}total rebates for this statement: [$]\d{0,6}.\d{0,2}total fees financial year to date: [$]\d{0,6}.\d{0,2}total fees for this statement: [$]\d{0,6}.\d{0,2} please check all transactions carefully. if you believe there is an error or unauthorised transaction, or if you haveany queries, please call us as soon as possible on 133 464.we recommend you retain a copy of your statement for taxation purposes and seek tax advice if required.e-\d{0,2}  s-\d{0,2}  i-\d{0,2}', '', body)

	#
	# start trying to build lists from the content
	#

	# get the section which include the strings of the date, transactions and balance
	# eg. 01/10/2017-63.863,294.86
	# eg. 01/10/2017-82.003,212.86
	# this sequence marks the start of each new transaction row in the pdf (split_sequence)
	date_transaction_balance = re.findall("[0-9][0-9]/[0-9][0-9]/2017[-0-9.,]*", body)

	get_date(date_transaction_balance)

	get_transactions(date_transaction_balance)

	get_details(body)

	create_csv(date_list, tansactions_list, details_list)

	
	for date in date_list:
		print(date)

	for transaction in tansactions_list:
		print(transaction)
	for detail in details_list:	 	
		print(detail)
	

	# a few sanity checks
	# make sure each list is the same length
	print()
	print("len date list: ", len(date_list))
	print("len trasnactions list: ", len(tansactions_list))
	print("len details list: ", len(details_list))
	print()

#	print(date_list)
#	print(tansactions_list)
#	print(details_list)

main()
