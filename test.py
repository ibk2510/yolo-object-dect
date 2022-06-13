import requests

url = 'http://127.0.0.1:8000/upload' ## change this to your server's url`
myfiles = {'file': open('fd.jpg' ,'rb')}
payload = requests.post(url, files = myfiles)
print(payload.text)



