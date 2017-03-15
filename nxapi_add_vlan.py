import requests
import json
import credentials

switch = credentials.switch
switchuser = credentials.user
switchpassword = credentials.password

url='http://{}/ins'.format(switch)

vlan = 346
myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "conf t",
      "version": 1
    },
    "id": 1
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "vlan {}".format(vlan),
      "version": 1
    },
    "id": 2
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "exit",
      "version": 1
    },
    "id": 3
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()