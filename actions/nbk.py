import sys
import requests
from st2common.runners.base_action import Action

  class Myclass:
    def run(self, id, title)
          try:
            x = { "id": "id","title": "title"}
            x1=json.dumps(x)
            r = requests.get('https://api.github.com/events')
    
