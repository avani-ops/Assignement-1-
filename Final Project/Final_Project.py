## This program reads data from XML file from online and display in requested way,
## it also check data validation.
import urllib.request

def fetch_info():
    cd_catalog = "https://www.w3schools.com/xml/cd_catalog.xml"
    try:
        cd_data = urllib.request.urlopen(cd_catalog).read().decode()
        main_data = cd_data.split("<TITLE>")
    except Exception as exception:
        print("Try to connect internet or web page not available")
        exit(1)
    return main_data


def main():
    main_data = fetch_info()
    print(main_data)
    
    
    
main()


catalog_data = []
for line in cd_data.split("\n"):
    catalog_data.append(line)

title_data = []
artist_data= []
company_data = []
country_data = []
price_data = []
year_data = []

for i in range(0,len(catalog_data)-1,1):
    check = catalog_data[i].find("TITLE")
    if check >= 0:
        title_data.append(catalog_data[i])
        print(catalog_data[i])
        
for i in range(0,len(catalog_data)-1,1):
    check = catalog_data[i].find("ARTIST")
    if check >= 0:
        artist_data.append(catalog_data[i])
        print(catalog_data[i])

for i in range(0,len(catalog_data)-1,1):
    check = catalog_data[i].find("COMPANY")
    if check >= 0:
        company_data.append(catalog_data[i])
        print(catalog_data[i])


for i in range(0,len(catalog_data)-1,1):
    check = catalog_data[i].find("COUNTRY")
    if check >= 0:
        country_data.append(catalog_data[i])
        print(catalog_data[i])


for i in range(0,len(catalog_data)-1,1):
    check = catalog_data[i].find("PRICE")
    if check >= 0:
        price_data.append(catalog_data[i])
        print(catalog_data[i])

for i in range(0,len(catalog_data)-1,1):
    check = catalog_data[i].find("YEAR")
    if check >= 0:
        year_data.append(catalog_data[i])
        print(catalog_data[i])
        

