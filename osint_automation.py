import requests, re

# FIX 1: open file in read mode, not write
django_debug_list = open("django-debug-list.txt", "r")

regex = r"(?:mongodb|redis):\/\/"

for ip in django_debug_list.readlines():
    try:
        response = requests.post(url=ip.rstrip("\n") + "/admin", data={}, verify=False)

        # FIX 2: response.content is bytes → use response.text (string)
        if re.search(regex, response.text):
            print("Mongodb/Redis URI Found")

    except Exception as e:
        print(e)

# FIX 3: close file after use
django_debug_list.close()
