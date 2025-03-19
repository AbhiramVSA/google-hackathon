import requests

# ✅ API Endpoint
url = "http://127.0.0.1:8000/upload-csv/"

# ✅ CSV File
files = {'file': open("data.csv", "rb")}

# ✅ Send the POST request
response = requests.post(url, files=files)

# ✅ Print the response
print(response.status_code)
print(response.json())
