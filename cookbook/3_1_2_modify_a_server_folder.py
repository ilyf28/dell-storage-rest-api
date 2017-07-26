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





# capture all SC series arrays managed by this DSM instance
# declare and define the payload variable
payload = {}

# define the REST API call
REST = '/ApiConnection/ApiConnection/%s/StorageCenterList' % conn_instanceId

# build the complete REST API URL
completeURL = '%s%s' % (baseURL, REST if REST[0] != '/' else REST[1:])

# execute REST API call via the HTTP GET method
json_data = connection.get(completeURL, headers=header, verify=verify_cert)
stdout = json.loads(json_data.text)
scList = {}
print "Name\t\tSerial Number\t\tinstanceId\t\tIP"
for i in range(len(stdout)):
	print "%s\t\t%s\t\t\t%s\t\t%s" % (stdout[i]['name'], stdout[i]['scSerialNumber'], stdout[i]['instanceId'], stdout[i]['hostOrIpAddress'])
	scList[stdout[i]['name']] = {}
	scList[stdout[i]['name']]['instanceId'] = stdout[i]['instanceId']
	scList[stdout[i]['name']]['hostOrIP'] = stdout[i]['hostOrIpAddress']





# create Storage Center server folder object managed by DSM / SC 9
payload = {}
# user-defined string / folder name
payload['Name'] = 'RestTest'
payload['StorageCenter'] = scList['Storage Center 75618']['instanceId']
payload['Parent'] = scList['Storage Center 75618']['instanceId'] + ".0"
# user-defined string / notes
payload['Notes'] = 'Created via REST API'
REST = '/StorageCenter/ScServerFolder'
completeURL = '%s%s' % (baseURL, REST if REST[0] != '/' else REST[1:])
json_data = connection.post(completeURL, data=json.dumps(payload, ensure_ascii=False).encode('utf-8'), headers=header, verify=verify_cert)
stdout = json.loads(json_data.text)
print stdout

#srvFolderList = {} created earlier in Section 2.3.4 #2.3.5
srvFolderList = {}
srvFolderList[stdout['name']] = {}
srvFolderList[stdout['name']]['instanceId'] = stdout['instanceId']
srvFolderList[stdout['name']]['parent'] = 'Servers'






# rename server folder object
payload = {}
# user-defined string / new folder name
payload['Name'] = 'RestTest_001'
payload['Parent'] = scList['Storage Center 75618']['instanceId'] + ".0"
REST = '/StorageCenter/ScServerFolder/%s' % srvFolderList['RestTest']['instanceId']
completeURL = '%s%s' % (baseURL, REST if REST[0] != '/' else REST[1:])
json_data = connection.put(completeURL, data=json.dumps(payload, ensure_ascii=False).encode('utf-8'), headers=header, verify=verify_cert)
stdout = json.loads(json_data.text)
print stdout

srvFolderList[payload['Name']] = {}
# renamed folder retains the same instanceID value as the original folder
srvFolderList[payload['Name']]['instanceId'] = stdout['instanceId']
# remove duplicate list entry
del srvFolderList['RestTest']
