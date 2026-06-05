import requests

# print("Requests imported successfully!")

response = requests.get("https://wttr.in/Colombo?format=j1")

print(response.status_code)