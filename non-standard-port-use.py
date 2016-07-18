
#!/usr/bin/python

import csv

standardSSHPorts = ['22']
standardHTTPPorts = ['80', '443']
standardFTPPorts = ['20', '21'] 

with open('testProxy.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['cs_uri_scheme'] == 'ssh':
			for x in range(len(standardSSHPorts)):
				if row['cs_uri_port'] == standardSSHPorts[x]:
					value = 1
					break
				else:
					value = 0
			if value ==0:
				with open('proxyNonStandardReview.csv', 'a') as reviewProxy:
					reviewProxy.write(row['_time'] + ' ' + row['action'] + ' ' + row['bytes_in'] + ' ' + row['bytes_out'] + ' ' + row['c_ip'] + ' ' + row['category'] + ' ' + row['cs2'] + ' ' + row['cs_Referer'] + ' ' +	row['cs_User_Agent'] + ' ' + row['cs_bytes'] + ' ' + row['cs_categories'] + ' ' + row['cs_cookie'] + ' ' + row['cs_host'] + ' ' + row['cs_method'] + ' ' + row['cs_uri_path'] + ' ' + row['cs_uri_port'] + ' ' + row['cs_uri_query'] + ' ' + row['cs_uri_scheme'] + ' ' + row['cs_user'] + ' ' + row['cs_username'] + ' ' + row['date'] + ' ' + row['date_hour'] + ' ' + row['date_mday'] + ' ' + row['date_minute'] + ' ' + row['date_month'] + ' ' + row['date_second'] + ' ' + row['date_wday'] + ' ' + row['date_year'] + ' ' + row['date_zone'] + ' ' + row['dest_ip'] + ' ' + row['dest_port'] + ' ' + row['duration'] + ' ' + row['dvchost'] + ' ' + row['eventtype'] + ' ' + row['host'] + ' ' + row['http_content_type'] + ' ' + row['http_method'] + ' ' + row['http_referrer'] + ' ' + row['http_user_agent'] + ' ' + row['index'] + ' ' + row['linecount'] + ' ' + row['proxy_country'] + ' ' + row['proxy_dc'] + ' ' + row['proxy_ip_1'] + ' ' + row['proxy_ip_2'] + ' ' + row['proxy_region'] + ' ' + row['proxy_type'] + ' ' + row['punct'] + ' ' + row['rs_Content_Type'] + ' ' + row['s_action'] + ' ' + row['s_ip'] + ' ' + row['s_port'] + ' ' + row['s_sitename'] + ' ' + row['s_supplier_ip'] + ' ' + row['s_supplier_name'] + ' ' + row['sc_bytes'] + ' ' + row['sc_filter_result'] + ' ' + row['sc_status'] + ' ' + row['site'] + ' ' + row['source'] + ' ' + row['sourcetype'] + ' ' + row['splunk_server'] + ' ' + row['splunk_server_group'] + ' ' + row['src_ip'] + ' ' + row['status'] + ' ' + row['time'] + ' ' + row['time_taken'] + ' ' + row['timeendpos'] + ' ' + row['timestartpos'] + ' ' + row['uri_path'] + ' ' + row['uri_query'] + '\n')					
		if row['cs_uri_scheme'] == 'http':
			for x in range(len(standardSSHPorts)):
				if row['cs_uri_port'] == standardHTTPPorts[x]:
					value = 1
					break
				else:
					value = 0
			if value ==0:
				with open('proxyNonStandardReview.csv', 'a') as reviewProxy:
					reviewProxy.write(row['_time'] + ' ' + row['action'] + ' ' + row['bytes_in'] + ' ' + row['bytes_out'] + ' ' + row['c_ip'] + ' ' + row['category'] + ' ' + row['cs2'] + ' ' + row['cs_Referer'] + ' ' +	row['cs_User_Agent'] + ' ' + row['cs_bytes'] + ' ' + row['cs_categories'] + ' ' + row['cs_cookie'] + ' ' + row['cs_host'] + ' ' + row['cs_method'] + ' ' + row['cs_uri_path'] + ' ' + row['cs_uri_port'] + ' ' + row['cs_uri_query'] + ' ' + row['cs_uri_scheme'] + ' ' + row['cs_user'] + ' ' + row['cs_username'] + ' ' + row['date'] + ' ' + row['date_hour'] + ' ' + row['date_mday'] + ' ' + row['date_minute'] + ' ' + row['date_month'] + ' ' + row['date_second'] + ' ' + row['date_wday'] + ' ' + row['date_year'] + ' ' + row['date_zone'] + ' ' + row['dest_ip'] + ' ' + row['dest_port'] + ' ' + row['duration'] + ' ' + row['dvchost'] + ' ' + row['eventtype'] + ' ' + row['host'] + ' ' + row['http_content_type'] + ' ' + row['http_method'] + ' ' + row['http_referrer'] + ' ' + row['http_user_agent'] + ' ' + row['index'] + ' ' + row['linecount'] + ' ' + row['proxy_country'] + ' ' + row['proxy_dc'] + ' ' + row['proxy_ip_1'] + ' ' + row['proxy_ip_2'] + ' ' + row['proxy_region'] + ' ' + row['proxy_type'] + ' ' + row['punct'] + ' ' + row['rs_Content_Type'] + ' ' + row['s_action'] + ' ' + row['s_ip'] + ' ' + row['s_port'] + ' ' + row['s_sitename'] + ' ' + row['s_supplier_ip'] + ' ' + row['s_supplier_name'] + ' ' + row['sc_bytes'] + ' ' + row['sc_filter_result'] + ' ' + row['sc_status'] + ' ' + row['site'] + ' ' + row['source'] + ' ' + row['sourcetype'] + ' ' + row['splunk_server'] + ' ' + row['splunk_server_group'] + ' ' + row['src_ip'] + ' ' + row['status'] + ' ' + row['time'] + ' ' + row['time_taken'] + ' ' + row['timeendpos'] + ' ' + row['timestartpos'] + ' ' + row['uri_path'] + ' ' + row['uri_query'] + '\n')					
		if row['cs_uri_scheme'] == 'ftp':
			for x in range(len(standardFTPPorts)):
				if row['cs_uri_port'] == standardFTPPorts[x]:
					value = 1
					break
				else:
					value = 0
			if value ==0:
				with open('proxyNonStandardReview.csv', 'a') as reviewProxy:
					#reviewProxy.write(row['_raw'] + ' ' + row['_time'] + '\n')
					reviewProxy.write(row['_time'] + ' ' + row['action'] + ' ' + row['bytes_in'] + ' ' + row['bytes_out'] + ' ' + row['c_ip'] + ' ' + row['category'] + ' ' + row['cs2'] + ' ' + row['cs_Referer'] + ' ' +	row['cs_User_Agent'] + ' ' + row['cs_bytes'] + ' ' + row['cs_categories'] + ' ' + row['cs_cookie'] + ' ' + row['cs_host'] + ' ' + row['cs_method'] + ' ' + row['cs_uri_path'] + ' ' + row['cs_uri_port'] + ' ' + row['cs_uri_query'] + ' ' + row['cs_uri_scheme'] + ' ' + row['cs_user'] + ' ' + row['cs_username'] + ' ' + row['date'] + ' ' + row['date_hour'] + ' ' + row['date_mday'] + ' ' + row['date_minute'] + ' ' + row['date_month'] + ' ' + row['date_second'] + ' ' + row['date_wday'] + ' ' + row['date_year'] + ' ' + row['date_zone'] + ' ' + row['dest_ip'] + ' ' + row['dest_port'] + ' ' + row['duration'] + ' ' + row['dvchost'] + ' ' + row['eventtype'] + ' ' + row['host'] + ' ' + row['http_content_type'] + ' ' + row['http_method'] + ' ' + row['http_referrer'] + ' ' + row['http_user_agent'] + ' ' + row['index'] + ' ' + row['linecount'] + ' ' + row['proxy_country'] + ' ' + row['proxy_dc'] + ' ' + row['proxy_ip_1'] + ' ' + row['proxy_ip_2'] + ' ' + row['proxy_region'] + ' ' + row['proxy_type'] + ' ' + row['punct'] + ' ' + row['rs_Content_Type'] + ' ' + row['s_action'] + ' ' + row['s_ip'] + ' ' + row['s_port'] + ' ' + row['s_sitename'] + ' ' + row['s_supplier_ip'] + ' ' + row['s_supplier_name'] + ' ' + row['sc_bytes'] + ' ' + row['sc_filter_result'] + ' ' + row['sc_status'] + ' ' + row['site'] + ' ' + row['source'] + ' ' + row['sourcetype'] + ' ' + row['splunk_server'] + ' ' + row['splunk_server_group'] + ' ' + row['src_ip'] + ' ' + row['status'] + ' ' + row['time'] + ' ' + row['time_taken'] + ' ' + row['timeendpos'] + ' ' + row['timestartpos'] + ' ' + row['uri_path'] + ' ' + row['uri_query'] + '\n')					