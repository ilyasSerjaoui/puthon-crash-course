import shodan
import time

SHODAN_API_KEY = "LGSZT7VDzl39EG0DlqET6xAwjY58pnyB"
api = shodan.Shodan(SHODAN_API_KEY)

words = open("bug-bounty-wordlist.txt", "r")
django_debug_list = open("django-debug-list.txt", "w")

for word in words.readlines():
    w = word.strip("\n").strip()
    if not w:
        continue

    # keep your original query format
    query = "html:'URLconf defined' ssl:" + w
    try:
        results = api.search(query)   # this may consume query credits / be limited on free plan
        print('Results found: {}'.format(results.get('total', 0)))

        for result in results.get('matches', []):
            print(word)
            print('IP: {}'.format(result.get('ip_str')))
            port = result.get('port')
            if port in [80, 443]:
               if port == 443:
                  ip = "https://" + result.get('ip_str')
               else:
                   ip = "http://" + result.get('ip_str')
            else:
                ip = "http://" + result.get('ip_str') + ":" + str(port)
            django_debug_list.write(ip + "\n")
            print('')

    except Exception as e:
        print(e)

    # Respect Shodan API rate limits (free/community accounts are rate-limited; 1 req/sec is typical)
    time.sleep(1)

# close files (minimal change)
words.close()
django_debug_list.close()
