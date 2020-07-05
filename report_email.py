#!/usr/bin/env python3
import os,datetime,reports,emails
import sys

def process_data():
	src = 'supplier-data/descriptions/'
	content = ''
	for i in os.listdir(src):
		with open(os.path.join(src,i),'r') as fptr:
			name = fptr.readline()
			weight = fptr.readline()
			str1 = "name:{}".format(name)+"<br/>"+"weight:{}".format(weight)+"<br/>"+"<br/>"
			content = content+str1
	return content
def generate_report():
	paragraph = process_data()
	dateobj = datetime.date.today()
	num_to_mth = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
	month = num_to_mth[dateobj.month]
	date = str(dateobj.day)
	year = str(dateobj.year)
	title = "Processed Update on {mth} {date},{year}".format(mth = month,date = date,year = year)
	reports.generate("/tmp/processed.pdf",title,paragraph)
if __name__ == "__main__":
	sender = "automation@example.com"
	receiver = "{}@example.com".format(os.environ.get("USER"))
	subject = "Upload Completed - Online Fruit Store"
	body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
	generate_report()
	message = emails.generate(sender,receiver,subject,body,"/tmp/processed.pdf")
	emails.send(message)
