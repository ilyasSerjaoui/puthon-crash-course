import shodan
SHODAN_API_KEY = "Your Shodan API"
api = shodan.Shodan(SHODAN_API_KEY)
out_file = open("grafana-instances.txt","a")
query = '"http.title:"Grafana'
try:
    results = api.search(query)
    print("Results found: {}".format(results["total"]))
    for result in results["matches"]:
        print("IP: {}".format(result["ip_str"]+":"+str(result["port"])))
        if result["port"] in [80,443]:
            if result["port"]==80:
                scheme = "http://"
            else:
                scheme = "http://"
            out = scheme+result["ip_str"]
        else:
            out = "http://"+result["ip_str"]+":"+str(result["port"])
        out_file.write(out+"\n")
        print('')
except shodan.APIError as e:
    print("Error: {}".format(e))
