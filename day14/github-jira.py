import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request

load_dotenv()
app = Flask(__name__)

@app.route("/createJIRA", methods=["POST"])
def createJIRA():
    # Jira API endpoint
    url = "https://subbaneupane43.atlassian.net//rest/api/3/issue"
    
    # Fetch Jira API token from environment variables
    API_TOKEN = os.environ.get('JIRA_API_TOKEN')

    # Set up basic authentication
    auth = HTTPBasicAuth("subbaneupane43@gmail.com", API_TOKEN)
    
    # Set headers for the API request
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    payload = json.dumps(
        {
            "fields": {
                "description": {
                    "content": [
                        {
                            "content": [{"text": "My First Jira Ticket", "type": "text"}],
                            "type": "paragraph",
                        }
                    ],
                    "type": "doc",
                    "version": 1,
                },
                "issuetype": {"id": "10007"},
                "project": {"key": "SUB"},
                "summary": "First Jira Ticket",
            },
            "update": {},
        }
    )

    # Check if the condition is true before making the API request
    if "/jira" in request.json["issue"]["body"]:
        # Perform the API request only if the condition is true
        response = requests.post(url, data=payload, headers=headers, auth=auth)

        # Check the status code of the API response
        if "/jira" in response.text and response.status_code == 201:  # Assuming 201 is the success status code
            print("API creation successful!")
        else:
            print(f"API creation failed with status code: {response.status_code}")
    else:
        print("Comment should be /jira only")
        return json.dumps({"message": "Comment should be /jira only"})

    # Return the API response in JSON format
    return json.dumps(
        json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")
    )

if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000)
