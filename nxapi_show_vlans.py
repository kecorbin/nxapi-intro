import requests
import json
import credentials

switch = credentials.switch
switchuser = credentials.user
switchpassword = credentials.password

url = "http://{}/ins".format(switch)

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show vlan",
      "version": 1
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

vlans = response['result']['body']['TABLE_vlanbrief']['ROW_vlanbrief']

for v in vlans:
    vlan = v['vlanshowbr-vlanid']
    print("VLAN {} is configured".format(vlan))