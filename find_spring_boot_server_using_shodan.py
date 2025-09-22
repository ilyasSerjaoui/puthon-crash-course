import shodan
SHODAN_API_KEY = "LGSZT7VDzl39EG0DlqET6xAwjY58pnyB"
api = shodan.Shodan(SHODAN_API_KEY)
out_file = open("sping-boot-server.txt", "a")
query = "http.favicon.hash:116323821"
try:
    result = api.search(query)
    print('Results found: {}'.format(results["total"]))
    for result in results["matches"]:
        print("IP: {}".format(resut["ip_str"]+":"+str(result["port"])))
        if result["port"] in [80,443]:
            if result["port"]==80:
                scheme = "http://"
            else:
                scheme = "https://"
            out = scheme+result["ip_str"]
        else:
            out = "http://"+result["ip_str"]+":"+str(result["port"])
        out_file.write(out+"\n")
        print('')
except shodan.APIError as e:
    print("Error: {}".format(e))
