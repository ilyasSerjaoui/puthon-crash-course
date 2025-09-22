import re

url="http://google.com"
port=8080
version=5.5
vulnerable=True
domains=['uber.com','yahoo.com','envoy.com']
ip=("255.255.255.255","255.255.255.255")
sever={"uber":"nginx","zomato":"envoy"}
vulnerable_version={4.4,4.5,4.6,4.7}

'''
String Content
'''

print(url[7])

print(len(url))

'''
Example Of String Function
'''

print(url.split('/')[2]) # Split

bugType="cross-site scripting"
print(bugType.strip("c")) # strip

bugType="cross origin reference share"
print(bugType.rstrip("c")) # rstrip

bugType="sql injection"
print(bugType.lstrip("s")) # lstrip

bugType="server side requerst forgery"
print(bugType.replace("s","X")) # replace

bugType="Api Testing"
print(bugType.count("i")) # count

'''
Startswith And Endswith
'''

bugType="cross-site request forgery"
print(bugType.startswith("c"))
print(bugType.endswith("y"))

'''
String Formatting
'''
app="wordpress"
version=4.8
print("%s version %s is vunlerable" % (app,version))
# %s is for String
# %d is for Integers
# %f is for Floating point number
# %x is for hex representation

'''
PYTHON COLLECTION
'''
# LIST
# Tuples
# Set
# Dictionary

'''
List
'''

print("domain: "+domains[0])
print("domain: "+domains[-2])
print(len(domains))

# List Function

#domains.remove("uber.com")
#domains.append("uber.com")
#domains.insert(0,"uber.com")
#domains.pop()
#domains.clear()

'''
Tuple
'''

tup=("amazon.com",443,5.5)

'''
Set
'''

numbers={1,2,3,4,5,6}
numbers_2={4,5,6,7,8,9}
print(numbers.union(numbers_2))
print(numbers.intersection(numbers_2))

'''
Dictionary
'''

phone={"redmi":1000,"nokia":1500,"oppo":2000}
print(phone["redmi"])
print(phone["nokia"])

print(phone.keys())
print(phone.values())

phone.update({"oneplue":2000})
print(phone)
del phone["oppo"]
print(phone)

print(phone.get("redmi"))

'''
Basic Operators
'''

a=5
b=2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)

string_1="Bug "
string_2="Bounty "
string_3="Automation "
print(string_1+string_2+string_3)

hello="hello"
print(hello*5)

list_1=[1,2,3,4,5]
list_2=[6,7,8,9,0]
print(list_1+list_2)
print(list_1*3)

'''
Conditions And Loops
'''

'''
If Conditions
'''

fixed_version=8.4
version=8.3
if version < fixed_version:
    print("version {} is vulnerable".format(version))
else:
    print("Not Vulnerable")

'''
Else If
'''

app="wordpress"
if app=="drupal":
    wordlist="drupal.txt"
elif app == "wordpress":
    wordlist="wordpress.txt"


'''
While Loop
'''

i=1
while i<=5:
    print(i)
    i+=1

'''
For Loop
'''

for i in range(1,6):
    print(i)

for domain in domains:
    print(domain)

for p in phone:
    print(phone[p])

for u in url:
    print(u)

'''
Functions
'''

def hello():
    print("Hello world")
hello()

def add(a,b):
    return a+b
print(add(5,4))

def isdomainlive(domain):
    return True

if isdomainlive("subdomain.example.com"):
    print("domain is live")

'''
Arbitrary Arguments
'''

def printdomain(*domains):
    for domain in domains:
        print(domain)
printdomain('uber.com','yahoo.com','envoy.com')

'''
Arbitrary Keyword Arguments
'''
def domaininfo(**domain):
    for key in domain:
        print(domain[key])
domaininfo(host="google.com", port=443)

'''
Default Parameter Value
'''

def vulnerable(yes=True):
    if yes:
        print("vulnerable")
    else:
        print("not vulnerable")
vulnerable(yes=False)
vulnerable()

def printobject(data):
    if isinstance(data,dict):
        for key in data:
            print(data[key])
    else:
        for value in data:
            print(value)
printobject([1,2,3,4,5])
printobject(("A","B","C","D"))
printobject({1.1,2.2,3.3,4.4})
printobject({"redmi":5000,"oppo":10000})

'''
File Operations
'''

dom_file=open("domains_list.txt","w")
for domain in domains:
    dom_file.write(domain+"\n")
dom_file.close()

dom_file=open("domains_list.txt","r")
print(dom_file.read())
for dom in dom_file.readlines():
    print(dom)
dom_file.close()

dom_2=["facebook.com", "pinterest.com", "amazon.com"]
dom_file=open("domains_list.txt","a")
for domain in dom_2:
    dom_file.write(domain+"\n")
dom_file.close()

'''
Exception Handling
'''

try:
    testfile=open("filenamr.txt","r")
except:
    print("File not found")

'''
Regular Expression
'''


webpage_content='''Django error occurred something...
            URLconf defined
'''
if re.search(r'URLconf\sdefined',webpage_content):
    print("Django Debug mode enabled")