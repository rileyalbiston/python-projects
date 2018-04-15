import PyPDF2
import re


pdfFileObj = open('Orange Everyday 01-10-2017 to 31-12-2017.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


#print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)
content = pageObj.getContents()

print(type(content))

lower_content = content.lower()

print(lower_content)

#split_content = lower_content.split("datedetailsmoney out $money in $balance $")

#header = split_content[0]

#body = split_content[1]


'''
print(header)
print()
print(body)
'''
'''
transactions_list = body.split("card 7295")

first_transaction = transactions_list[0]

print(first_transaction)

date = re.findall('[0-9][0-9]/+[0-9][0-9]/+[0-9][0-9][0-9][0-9]', first_transaction)

trans = re.findall('[-][[0-9]*[.][0-9][0-9]', first_transaction)

balance = re.findall('[0-9][,][0-9]*[.][0-9][0-9]', first_transaction)

#find_details = re.findall('[.][0-9][0-9][a-z]', first_transaction)

#find_details = "".join(find_details)

#details = re.findall('[a-z ]*[-][a-z ]*[ ][0-9]*[a-z *]*', first_transaction)

details =first_transaction.split("purchase - receipt ")

print(date)

print(trans)

print(balance)

#print(find_details)

print(details[1])

'''
'''
# "datedetailsmoney out $money in $balance $"
transactions_list = body.split("card 7295")
for first_transaction in transactions_list: 

	date = re.findall('[0-9][0-9]/+[0-9][0-9]/+[0-9][0-9][0-9][0-9]', first_transaction)

	trans = re.findall('[-][0-9]*[.][0-9][0-9]', first_transaction)

#	balance = re.findall('[0-9][,][0-9]*[.][0-9][0-9]', first_transaction)

	#find_details = re.findall('[.][0-9][0-9][a-z]', first_transaction)

	#find_details = "".join(find_details)

	#details = re.findall('[a-z ]*[-][a-z ]*[ ][0-9]*[a-z *]*', first_transaction)

#	details = re.sub('\w+', first_transaction)
	details =first_transaction.split(" - receipt ")

	print(date)

	print(trans)

#	print(balance)

	#print(find_details)

	print(details[1])
	print()
	'''