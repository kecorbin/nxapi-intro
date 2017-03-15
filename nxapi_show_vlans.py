import requests
import json

# Change these parameters for your environment
url='http://192.168.51.128/ins'
switchuser='admin'
switchpassword='changeme'

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