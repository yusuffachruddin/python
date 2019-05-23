import re

def getEmail(text):
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
    return emails


text = "Please contact us at contact@tutorialspoint.com for further information. You can also give feedbacl at feedback@tp.com"

print(getEmail(text))
