from bs4 import BeautifulSoup as sp
import requests
import tldextract

url = "https://github.com"
webpage = requests.get(url=url)
soup = sp(webpage.content, 'html.parser')

tables = soup.find_all('table')


if len(tables) > 4:
    a_tags = tables[4].find_all('a')
else:
    a_tags = soup.find_all('a')  # fallback to all <a> tags

# write sites
with open("bug-bounty-sites.txt", "w") as sites_list:
    for a in a_tags:
        href = a.get('href')
        if href:
            sites_list.write(href + '\n')


'''
Domain List
'''

# read sites back
with open("bug-bounty-sites.txt", "r") as site_list:
    sites = site_list.readlines()

# write domains
with open("bug-bounty-domain.txt", "w") as domain_list:
    for site in sites:
        site = site.strip()
        if not site or 'mailto' in site:
            continue
        split_site = site.split('/')
        if len(split_site) > 2:  # make sure index 2 exists
            domain_list.write(split_site[2] + '\n')

'''
KeyWord List
'''


domain_list = open("bug-bounty-domains.txt", "r")
with open("bug-bounty-wordlist.txt","w") as word_list:
    for domain in domain_list.readlines():
        split_domain = domain.split(".")
        if len(split_domain)>1:
            if len(split_domain[-2])>2:
                word_list.write(split_domain[-2]+"\n")




domain_list = open("bug-bounty-domains.txt","r")
with open("bug-bounty-wordlist.txt","w") as word_list:
    for domain in domain_list.readlines():
        tld = tldextract.extract(domain)
        word_list.write(tld.domain+"\n")















