import requests

req = requests.get("http://192.168.0.6:8000/check/"+"111")
print(req.text)