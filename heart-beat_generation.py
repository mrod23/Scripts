#!/usr/bin/python

import pandas
import numpy as np
import csv


'''
	bring in proxy spreadsheet 
	convert all times to unix time 
	save as a new spreadsheet
	

'''

with open('testProxy.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['_time'] is not None:


'''
y = pandas.read_csv('testProxy8.csv')
table = pandas.pivot_table(y, index=['cs_host', 'c_ip'], values='_time', fill_value=0, margins=True, aggfunc=[np.count_nonzero, np.mean, np.var, np.std])



print table
'''