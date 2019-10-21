import requests

parameter = {"_url": "906747215@qq.com"}
response = requests.post("http://47.94.134.159:8080/validateEmailAddress", json=parameter)
print(response.text)
