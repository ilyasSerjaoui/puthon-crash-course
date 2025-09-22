import requests as rt
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urls = open("sonarqube-instance.txt","r")
data = {"login":"admin","password":"admin"}
endpoint = "/api/authentication/login"
for url in urls.readlines():
    print("Testing - "+url)
    try:
        req = rt.post(url=url.rstrip("\n")+endpoint, data=data,verify=False)
        if req.status_code == 200:
            print("Login success")
    except:
        pass
