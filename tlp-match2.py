#!/usr/bin/python

import string
from tld import get_tld


tlp = open('/home/mr43559/Documents/CSFC/Scripts/tlp/sample_domain.txt')

splitTLP = tlp.read().split()

whiteList = ['com', 'gov', 'edu', 'net', 'org']

startLine = 2
urlLineTotal = len(splitTLP)

while startLine < urlLineTotal:
	reviewURL = []
	
	y = splitTLP[startLine].rsplit('.', 1)[1]	
	
	z = splitTLP[startLine]
	#print z
	#print y
	for x in range(len(whiteList)):
		if y == whiteList[x]:
			value = 1
			break
		else: 
			value = 0

	if value == 0:
		reviewURL = 'URLs to be reviewed: '
		with open('output.txt', 'a') as reviewURL:
			reviewURL.write(z + '\n')

	startLine = startLine + 1
