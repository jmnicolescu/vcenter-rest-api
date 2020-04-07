# juliusn - Tue Apr  7 11:35:08 BST 2020
# 

import requests
import os

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def authvc(api_url,user,password):
    r = requests.post(f'{api_url}/rest/com/vmware/cis/session',auth=(user,password),verify=False)
    if r.status_code == 200:
        print ("Authentication Success")
        return r.json()['value']
    else:
        return print("Fail with Status Code "+r.status_code)
		
def getapidata(path):
    get_url = os.environ['api_url']
    get_user = os.environ['api_user']
    get_passwd = os.environ['api_passwd']
	
    sid = authvc(get_url,get_user,get_passwd)
    r = requests.get(f'{get_url}/rest{path}',headers={'vmware-api-session-id':sid},verify=False)
    if r.status_code == 200:
        return r.json()
    else:
        return print("Fail with Status Code "+r.status_code)