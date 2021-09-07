import requests




print("requests version is " + requests.__version__)

print()
print()


google = requests.get("https://www.google.com")
print(google.text)


