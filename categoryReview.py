#!/usr/bin/python

import csv
import pandas
import numpy as np

with open('proxy.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['category'] == 'none':
			with open('event_cateogry_review.csv', 'a') as reviewProxy:
					reviewProxy.write(row['_time'] + '\t' + row['action'] + '\t' + row['bytes_in'] + '\t' + row['bytes_out'] + '\t' + row['c_ip'] + '\t' + row['category'] + '\t' + row['cs2'] + '\t' + row['cs_Referer'] + '\t' +	row['cs_User_Agent'] + '\t' + row['cs_bytes'] + '\t' + row['cs_categories'] + '\t' + row['cs_cookie'] + '\t' + row['cs_host'] + '\t' + row['cs_method'] + '\t' + row['cs_uri_path'] + '\t' + row['cs_uri_port'] + '\t' + row['cs_uri_query'] + '\t' + row['cs_uri_scheme'] + '\t' + row['cs_user'] + '\t' + row['cs_username'] + '\t' + row['date'] + '\t' + row['date_hour'] + '\t' + row['date_mday'] + '\t' + row['date_minute'] + '\t' + row['date_month'] + '\t' + row['date_second'] + '\t' + row['date_wday'] + '\t' + row['date_year'] + '\t' + row['date_zone'] + '\t' + row['dest_ip'] + '\t' + row['dest_port'] + '\t' + row['duration'] + '\t' + row['dvchost'] + '\t' + row['eventtype'] + '\t' + row['host'] + '\t' + row['http_content_type'] + '\t' + row['http_method'] + '\t' + row['http_referrer'] + '\t' + row['http_user_agent'] + '\t' + row['index'] + '\t' + row['linecount'] + '\t' + row['proxy_country'] + '\t' + row['proxy_dc'] + '\t' + row['proxy_ip_1'] + '\t' + row['proxy_ip_2'] + '\t' + row['proxy_region'] + '\t' + row['proxy_type'] + '\t' + row['punct'] + '\t' + row['rs_Content_Type'] + '\t' + row['s_action'] + '\t' + row['s_ip'] + '\t' + row['s_port'] + '\t' + row['s_sitename'] + '\t' + row['s_supplier_ip'] + '\t' + row['s_supplier_name'] + '\t' + row['sc_bytes'] + '\t' + row['sc_filter_result'] + '\t' + row['sc_status'] + '\t' + row['site'] + '\t' + row['source'] + '\t' + row['sourcetype'] + '\t' + row['splunk_server'] + '\t' + row['splunk_server_group'] + '\t' + row['src_ip'] + '\t' + row['status'] + '\t' + row['time'] + '\t' + row['time_taken'] + '\t' + row['timeendpos'] + '\t' + row['timestartpos'] + '\t' + row['uri_path'] + '\t' + row['uri_query'] + '\n')					


y = pandas.read_csv('proxy.csv')
table = pandas.pivot_table(y, index=['category'], values='_time', fill_value=0, margins=True, aggfunc=[np.count_nonzero])

table.to_csv('pt_output.csv', sep='\t')
