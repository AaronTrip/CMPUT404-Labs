import requests




print("requests version is " + requests.__version__)

print()
print()


google = requests.get("https://www.google.com")
#print(google.text)


url = "https://raw.githubusercontent.com/AaronTrip/CMPUT404-Labs/main/Lab1.py"

urlfile = requests.get(url, allow_redirects=True)


print()
print("Here is the files source code")
print()


print(urlfile.content)
