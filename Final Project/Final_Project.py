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
    data = "Not Available"
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
    data = "Not Available"
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
    return artist_data


def get_country_array(record):
    get_record = record.split("\n")
    data = "Not Available"
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
    return country_data


def get_company_array(record):
    get_record = record.split("\n")
    data = "Not Available"
    for i in range(0,len(get_record),1):
        if(get_record[i].find("COMPANY") > 0):
            start = get_record[i].find(">") + 1
            end  = get_record[i].find("</COMPANY>")
            data = get_record[i][start:end]
    return data
        

def get_data_company(main_data):
    company_data = []
    for i in range(1,len(main_data),1):
        company_data.append(get_company_array(main_data[i]))
    return company_data



def get_price_array(record):
    get_record = record.split("\n")
    data = 0.00
    for i in range(0,len(get_record),1):
        if(get_record[i].find("PRICE") > 0):
            start = get_record[i].find(">") + 1
            end  = get_record[i].find("</PRICE>")
            data = get_record[i][start:end]
            try:
                data =  float(data)
            except :
                data = 0.00
    return data
        


def get_data_price(main_data):
    price_data = []
    for i in range(1,len(main_data),1):
        price_data.append(get_price_array(main_data[i]))
    return price_data


def get_year_array(record):
    get_record = record.split("\n")
    data = "Not Available"
    for i in range(0,len(get_record),1):
        if(get_record[i].find("YEAR") > 0):
            start = get_record[i].find(">") + 1
            end  = get_record[i].find("</YEAR>")
            data = get_record[i][start:end]
    return data
        


def get_data_year(main_data):
    year_data = []
    for i in range(1,len(main_data),1):
        year_data.append(get_year_array(main_data[i]))
    return year_data


def print_output(title_data,artist_data,country_data,company_data,price_data,year_data):
    for i in range (0, len(title_data),1):
        print(f"{title_data[i]} - {artist_data[i]} - {country_data[i]} - {company_data[i]} - $ {price_data[i]} - {year_data[i]}")


def get_data_average(price):
    total = 0
    for i in range(0,len(price),1):
        total = total + price[i]
    
    average = total / len(price)
    return average

def print_output_average(record,average):
    print(f" Total Records Available in Catalog : {record}")
    print(f" Average price of items in Catalog  : {average :.2f}")

def main():
    main_data = fetch_info()
    title_data = get_data_title(main_data)
    artist_data = get_data_artist(main_data)
    country_data = get_data_country(main_data)
    company_data = get_data_company(main_data)
    price_data = get_data_price(main_data)
    year_data = get_data_year(main_data)
    print_output(title_data,artist_data,country_data,company_data,price_data,year_data)
    average_data = get_data_average(price_data)
    print_output_average(len(title_data),average_data)

main()

