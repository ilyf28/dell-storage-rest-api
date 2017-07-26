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





# declare and define the payload variable
payload = {}

# define the REST API call
REST = '/StorageCenter/StorageCenter/%s/VolumeFolderList' % (scList['Storage Center 75618']['instanceId'])

# build the complete REST API URL
completeURL = '%s%s' % (baseURL, REST if REST[0] != '/' else REST[1:])

# execute REST API call via the HTTP GET method
json_data = connection.get(completeURL, headers=header, verify=verify_cert)
stdout = json.loads(json_data.text)
volFolderList = {}
print "Name\t\t\t\t\tinstanceId\t\tParent"
for i in range(len(stdout)):
	if stdout[i]['name'] == "Volumes":
		continue
	print "%s\t\t\t\t%s\t\t%s" % (stdout[i]['name'], stdout[i]['instanceId'], stdout[i]['parent']['instanceName'])
	volFolderList[stdout[i]['name']] = {}
	volFolderList[stdout[i]['name']]['instanceId'] = stdout[i]['instanceId']
	volFolderList[stdout[i]['name']]['parent'] = stdout[i]['parent']['instanceName']





# declare and define the payload variable
payload = {}

# define the REST API call
REST = '/StorageCenter/StorageCenter/%s/VolumeList' % (scList['Storage Center 75618']['instanceId'])

# build the complete REST API URL
completeURL = '%s%s' % (baseURL, REST if REST[0] != '/' else REST[1:])

# execute REST API call via the HTTP GET method
json_data = connection.get(completeURL, headers=header, verify=verify_cert)
stdout = json.loads(json_data.text)
volList = {}
print "Name\t\t\t\t\tinstanceId\t\tPath"
for i in range(len(stdout)):
	print "%s\t\t%s\t\t%s" % (stdout[i]['name'], stdout[i]['instanceId'], stdout[i]['volumeFolderPath'])
	volList[stdout[i]['name']] = {}
	volList[stdout[i]['name']]['instanceId'] = stdout[i]['instanceId']
	volList[stdout[i]['name']]['path'] = stdout[i]['volumeFolderPath']





# declare and define the payload variable
payload = {}

# define the REST API call
REST = '/StorageCenter/StorageCenter/%s/ServerFolderList' % (scList['Storage Center 75618']['instanceId'])

# build the complete REST API URL
completeURL = '%s%s' % (baseURL, REST if REST[0] != '/' else REST[1:])

# execute REST API call via the HTTP GET method
json_data = connection.get(completeURL, headers=header, verify=verify_cert)
stdout = json.loads(json_data.text)
srvFolderList = {}
print "Name\t\t\t\t\tinstanceId\t\tParent"
for i in range(len(stdout)):
	if stdout[i]['name'] == "Servers":
		continue
	print "%s\t\t\t\t%s\t\t%s" % (stdout[i]['name'], stdout[i]['instanceId'], stdout[i]['parent']['instanceName'])
	srvFolderList[stdout[i]['name']] = {}
	srvFolderList[stdout[i]['name']]['instanceId'] = stdout[i]['instanceId']
	srvFolderList[stdout[i]['name']]['parent'] = stdout[i]['parent']['instanceName']





# declare and define the payload variable
payload = {}

# define the REST API call
REST = '/StorageCenter/StorageCenter/%s/ServerList' % (scList['Storage Center 75618']['instanceId'])

# build the complete REST API URL
completeURL = '%s%s' % (baseURL, REST if REST[0] != '/' else REST[1:])

# execute REST API call via the HTTP GET method
json_data = connection.get(completeURL, headers=header, verify=verify_cert)
stdout = json.loads(json_data.text)
srvList = {}
print "Name\t\t\t\t\tinstanceId\t\tPath"
for i in range(len(stdout)):
	print "%s\t\t\t\t%s\t\t%s" % (stdout[i]['name'], stdout[i]['instanceId'], stdout[i]['serverFolderPath'])
	srvList[stdout[i]['instanceName']] = {}
	srvList[stdout[i]['instanceName']]['instanceId'] = stdout[i]['instanceId']
	srvList[stdout[i]['instanceName']]['path'] = stdout[i]['serverFolderPath']
