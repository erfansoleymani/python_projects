import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break

    url = address
    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print("Retrieved", len(data), "characters")
    print(data.decode())
    tree = ET.fromstring(data)

    count = 0
    results = tree.findall("comments")[0].findall("comment")
    for result in results:
        count += int(result.find("count").text)
    print(count)
