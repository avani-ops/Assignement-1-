
import urllib.request
cd_catalog = "https://www.w3schools.com/xml/cd_catalog.xml"
try:
    cd_data = urllib.request.urlopen(cd_catalog).read().decode()
except Exception as exception:
    print("Try to connect internet or web page not available")
    exit(1)


catalog_data = []
for line in cd_data.split("\n"):
    catalog_data.append(line)

print(catalog_data)

for i in range(0,len(catalog_data)-1,1):
    check = catalog_data[i].find("TITLE")
    if check >= 0:
        print(catalog_data[i])
