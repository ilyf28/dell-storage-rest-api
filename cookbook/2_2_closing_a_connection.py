#!/usr/bin/python

from main import *

# login to DSM instance
# declare and define the payload variable
payload = {}

# define the REST API call
REST = '/ApiConnection/Login'

# build the complete REST API URL
completeURL = '%s%s' % (baseURL, REST if REST[0] != '/' else REST[1:])

# execute REST API call via the HTTP POST method
print connection.post(completeURL, data=json.dumps(payload, ensure_ascii=False).encode('utf-8'), headers=header, verify=verify_cert)

# logout from DSM instance
# declare and define the payload variable
payload = {}

# define the REST API call
REST = '/ApiConnection/Logout'

# build the complete REST API URL
completeURL = '%s%s' % (baseURL, REST if REST[0] != '/' else REST[1:])

# execute REST API call via the HTTP POST method
print connection.post(completeURL, data=json.dumps(payload, ensure_ascii=False).encode('utf-8'), headers=header, verify=verify_cert)
