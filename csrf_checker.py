import request

 datarul = "https://toyota.com/vulnerable-endpoint"
Data = {
   "username":"XXXXXX"
   "password": "XXXXXxx"
}

response = requests.post(url,data=data)

if "Success" in response response.text:
    print("CSRF vulnerability found!")
else:
      print("CSF protection is in place.")
