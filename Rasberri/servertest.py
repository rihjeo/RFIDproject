import requests

if __name__ == "__main__":
    req = requests.get("http://192.168.0.14/check/123")
    print(req.text)
