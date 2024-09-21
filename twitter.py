import re

url = input("URL: ")

matches = re.search(r"(?:https?://)?|(?:www\.)?twitter\.com/(.+)$",url,re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1))