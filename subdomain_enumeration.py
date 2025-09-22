import sublist3r
domains = open("bug-bounty-domains-2.txt")
for domain in domains.readlines():
    domain = domain.rstrip("\n")
    subdomains = sublist3r.main(domain, 40, domain+"_subdomains.txt",silent=True,engines=None, enable_bruteforce=False,verbose=False,ports=None)
    for sub in subdomains:
        print(sub)
