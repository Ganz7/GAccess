#Author : Ganz7
#This script retreives the number of mails and their size from your mail box.

import  poplib
from sys import argv
from email import parser

script, gmailUname, gmailPswd = argv

popSession = poplib.POP3_SSL('pop.gmail.com')
popSession.user(gmailUname)
popSession.pass_(gmailPswd)

(numMsgs, totalSize) = popSession.stat()

print "No of messages :", numMsgs, "\nSize : ", totalSize