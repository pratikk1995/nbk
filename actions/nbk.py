import sys
import json
import requests
from st2common.runners.base_action import Action
class Myclass:
    def run(self,id,title,timeout):
      try:
            x = {"ID": id, "TITLE": title}
            x1= json.dumps(x)
            url='https://fakerestapi.azurewebsites.net/api/Books'
            headers='Content-Type: application/json'
            r = requests.post(url, headers= headers, data = x1,timeout=6.0)
            y= r.json()
            print(r)
            print(y)
      except requests.exceptions.Timeout:
             print("timeout")
             sys.exit(0)
    
