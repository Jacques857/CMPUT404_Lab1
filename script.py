import requests
print(requests.__version__)
r = requests.get('http://www.google.com/')
print("Status: ", r.status_code, "\n", "Page contents:\n", r.text)
