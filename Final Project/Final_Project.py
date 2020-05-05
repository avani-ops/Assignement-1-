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


def get_title_array(record):
    get_record = record.split("\n")
    data = ""
    for i in range(0,len(get_record),1):
        if(get_record[i].find("TITLE") > 0):
            end  = get_record[i].find("</TITLE>")
            data = get_record[i][:end]
    return data
        


def get_data_title(main_data):
    title_data = []
    for i in range(1,len(main_data),1):
        title_data.append(get_title_array(main_data[i]))
    
    return title_data

def get_artist_array(record):
    get_record = record.split("\n")
    data = ""
    for i in range(0,len(get_record),1):
        if(get_record[i].find("ARTIST") > 0):
            start = get_record[i].find(">") + 1
            end  = get_record[i].find("</ARTIST>")
            data = get_record[i][start:end]
    return data
        


def get_data_artist(main_data):
    artist_data = []
    for i in range(1,len(main_data),1):
        artist_data.append(get_artist_array(main_data[i]))
    print(artist_data)
    return artist_data


def get_country_array(record):
    get_record = record.split("\n")
    data = ""
    for i in range(0,len(get_record),1):
        if(get_record[i].find("COUNTRY") > 0):
            start = get_record[i].find(">") + 1
            end  = get_record[i].find("</COUNTRY>")
            data = get_record[i][start:end]
    return data


def get_data_country(main_data):
    country_data = []
    for i in range(1,len(main_data),1):
        country_data.append(get_country_array(main_data[i]))
    print(country_data)
    return country_data


def get_company_array(record):
    get_record = record.split("\n")
    data = ""
    for i in range(0,len(get_record),1):
        if(get_record[i].find("COMPANY") > 0):
            start = get_record[i].find(">") + 1
            end  = get_record[i].find("</COMPANY>")
            data = get_record[i][start:end]
    return data
        

def get_data_artist(main_data):
    company_data = []
    for i in range(1,len(main_data),1):
        company_data.append(get_artist_array(main_data[i]))
    print(artist_data)
    return artist_data


def main():
    main_data = fetch_info()
    title_data = get_data_title(main_data)
    artist_data = get_data_artist(main_data)


main()



'''catalog_data = []
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
        
#for j in range(0, len(title_data)-1 , 1):
    '''

