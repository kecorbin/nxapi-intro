import sys
import json
import requests

my_headers = {'content-type': 'application/json-rpc'}

# Change these parameters for your environment
url = "http://192.168.51.128/ins"
username = "admin"
password = "changeme"

payload = [{'jsonrpc': '2.0', 'method': 'cli', 'params': ['show version',1], 'id': '1'}]
my_data = json.dumps(payload)
response = requests.post(url, data=my_data, headers=my_headers, auth=(username, password)).json()

result = response['result']
kick_start_image = response['result']['body']['kickstart_ver_str']
host_name = response['result']['body']['host_name']

print("")
print("===============================")
print('host name:'+ host_name)
print("Image version:" + kick_start_image)
print("===============================")
