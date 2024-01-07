# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import os
import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv

url = "https://subbaneupane43.atlassian.net//rest/api/3/project"

API_TOKEN = os.environ.get('JIRA_API_TOKEN')

auth = HTTPBasicAuth("subbaneupane43@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

##to print the specific project details
#output = json.loads(response.text)
#example 
#name = output [0]["name"]
#print(name)