import shodan
SHODAN_API_KEY = "LGSZT7VDzl39EG0DlqET6xAwjY58pnyB"
api = shodan.Shodan(SHODAN_API_KEY)
words = open("bug-bounty-wordlist.txt", "r")
django_debug_list = open("django-debug-list.txt","w")
for word in words.readlines():
    query = "html:'URLconf defined' ssl:"+word.strip("\n")
    try:
        results = api.search(query)
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
            print(word)
            print('IP: {}'.format(result['ip_str']))
            port = result['port']
            if port in [80,443]:
               if port == 443:
                  ip = "https://"+result['ip_str']
               else:
                   ip = "http://"+result['ip_str']
            else:
                ip = "http://"+result['ip_str']+":"+str(port)
            django_debug_list.write(ip+"\n")
            print('')
    except Exception as e:
        print(e)
