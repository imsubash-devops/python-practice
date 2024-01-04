import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

print(response)
print(type(response))
complete_detail = response.json()

for element in range (len(complete_detail)):
    print(complete_detail[element]["user"]["login"])