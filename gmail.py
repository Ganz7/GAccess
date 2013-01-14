#Author:Ganz7
#This script sends a mail using your gmail account.

import smtplib
import os
import sys

os.system('clear')
print "Logging you in...\n"

script, gmailUname, gmailPswd = sys.argv

session = smtplib.SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()
try:
	session.login(gmailUname,gmailPswd)
except:
	print "Error: Please check your username and password.\n"
	sys.exit(1)

recipient = raw_input(">> To: ")
mail_subject = raw_input(">> Subject: ")
mail_body = raw_input(">> Message: ")

headers = "\r\n".join(["from: " + gmailUname,
			"subject : " + mail_subject,
			"to : " + recipient,
			"mime-version : 1.0",
			"content-type: text/html"])

content = headers + "\r\n\r\n" + mail_body

print "Sending mail...\n"
try:
	session.sendmail(gmailUname, recipient.split(','), content)
except:
	print "Error! Unable to send mail"
print "Sent!"
session.close()