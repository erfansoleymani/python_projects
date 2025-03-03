# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = int(input("Enter count: ")) + 1
position = int(input("Enter position: ")) - 1

for cnt in range(count):
    print("Retrieving: ", url)
    # Retrieve all of the anchor tags
    internal_counter = 0
    tags = soup("a")
    for tag in tags:
        if internal_counter == position:
            url = tag.get("href", None)
            break
        else:
            internal_counter += 1

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
