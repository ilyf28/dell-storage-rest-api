#!/usr/bin/python

# import modules into Python script
import requests, json, http, httplib2, urllib, urllib2
import os, sys, subprocess, math
import math, time
import logging
from simplejson import scanner

# setup logging to scapi.log
logging.basicConfig(level=logging.DEBUG, filename='scapi.log', format='[%(asctime)s] %(levelname)s %(message)s')

# define env incl. DSM IP addr, port & login credentials
DSM_ip = '192.168.0.1' # IP address of DSM instance
DSM_port = '3033' # Default port of DSM instance
DSM_id = 'ID' # Login credentials for DSM
DSM_pass = 'PASSWORD' # Password
verify_cert = False # Default = False
apiversion = '2.0' # Default = 2.0

# define base URL for DSM REST API interface
baseURL = 'https://%s:%s/api/rest/' % (DSM_ip, DSM_port)

# define HTTP content headers
header = {}
header['Content-Type'] = 'application/json; charset=utf-8'
header['Accept'] = 'application/json'
header['x-dell-api-version'] = apiversion

# define the connection session
connection = requests.Session()
connection.auth = (DSM_id, DSM_pass)
