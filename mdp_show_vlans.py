import requests
import json
import credentials

switch = credentials.switch
username = credentials.user
password = credentials.password

def get_token(switch, user, password):
    """
    Generate webtoken for authenticated REST requests
    :param switch: str ip address of switch
    :param user: str username to authenticate
    :param password: str password
    :return: str webtoken
    """

    payload = {"aaaUser": {"attributes": {"name": username,
                                          "pwd": password
                                          }
                           }
               }
    login_url = "http://{}/api/aaaLogin.json".format(switch)
    headers = {'Content-Type': "application/json"}
    response = requests.post(login_url, data=json.dumps(payload), headers=headers)
    print(response.text)
    token = response.json()['imdata'][0]['aaaLogin']['attributes']['token']
    return token

token = get_token(switch, username, password)
headers = {
    'Content-Type': "application/json",
    'Cookie': "APIC-Cookie={}".format(token)
    }

vlans = requests.get('http://{}/api/class/l2BD.json'.format(switch), headers=headers).json()
for bd in vlans['imdata']:
    print(bd['l2BD']['attributes'])