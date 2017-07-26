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





# capture API connection instanceId
# declare and define the payload variable
payload = {}

# define the REST API call
REST = '/ApiConnection/ApiConnection'

# build the complete REST API URL
completeURL = '%s%s' % (baseURL, REST if REST[0] != '/' else REST[1:])

# execute REST API call via the HTTP GET method
json_data = connection.get(completeURL, headers=header, verify=verify_cert)
stdout = json.loads(json_data.text)
conn_instanceId = stdout['instanceId']
print conn_instanceId
