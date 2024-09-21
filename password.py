import re
password = input("what is your password? ")
matches = re.search(r"([A-Z]+)([a-z]+)([0-9]+)([\!\@\#\$\%\^\&\*\(\)]+)",password)
if matches.group(4):
    print("valid")
else:
    print("invalid")