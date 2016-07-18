#!/usr/bin/python

import whois
import csv
import os
from datetime import datetime
from dateutil.parser import parse
import subprocess
import feedparser

'''
notes
if date matches a certain pattern { 14-nov-2000 }
format the date to the python format save that to a variable


format the time accessed date to the python format 

run the python date compare function 

then write an if statement...
	if the dates are within a 30 day range
	send the row to a csv 

'''

#try:
with open('testProxy2.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		#w = whois.whois(row['cs_host'])
		#y = w.creation_date
		w = (row['cs_host'])
		y = w.split('.')
		domain = y[-2]+'.'+y[-1]
		date = os.popen('whois -H' + ' ' + domain + ' | grep -i "Creation Date:" | sed "s/Creation Date://"').read()
		#print "made it 1"
		#date = subprocess.call("whois -H", domain, "|", "grep", "-i", "Creation Date:", "|", "sed", "s/Creation Date://")
		#date = subprocess.call(['whois', '-H', domain])
		#e = feedparser.parse(date)
		#f = feedparser.parse(date).feed.date
		print date
		#formattedDate = parse(date)
		#print formattedDate


#except:
	#print "error"
		#with open('whois-creation.txt') as whoIsCSV:
					#whoIsCSV.write(y + '\n')
		
