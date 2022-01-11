import requests
print(requests.__version__, "\n\n")

r = requests.get('http://www.google.com/')
print("Status: ", r.status_code, "\n", "Page contents:\n", r.text, "\n\n")

r = requests.get('https://raw.githubusercontent.com/Jacques857/CMPUT404_Lab1/main/script.py')

open('downloadedScript.py', 'wb').write(r.content)

print("Source code:\n" + r.text)
