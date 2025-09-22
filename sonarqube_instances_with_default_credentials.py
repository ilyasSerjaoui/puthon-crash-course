import shodan
SHODAN_API_KEY = "YOUR_SHODAN_API_KEY"
api = shodan.Shodan(SHODAN_API_KEY)
out_fiel = open("sonarqube-instances.txt","a")
query = "http.title:SonarQube"
try:
    results = api.search(query)
    print("Results found: {}".format(results["total"]))
    for result in results["matches"]:
        print("IP: {}".format(result["ip_str"]+":"+str(result["port"])))
        if result["port"] in [80,443]:
            if result["port"] == 80:
                scheme = "http://"
            else:
                scheme = "https://"
            out = scheme+result["ip_str"]
        else:
            out = "http://"+result["ip_str"]
        out_file.write(out+"\n")
except shodan.APIError as e:
    print("Error: {}".format(e))
