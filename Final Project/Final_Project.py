# This program reads data from XML file from online and display in
# requested way, it also check data validation.

import urllib.request


def fetch_info():
    cd_catalog = "https://www.w3schools.com/xml/cd_catalog.xml"
    try:
        cd_data = urllib.request.urlopen(cd_catalog).read().decode()
        main_data = cd_data.split("</CD>")
    except Exception as exception:
        print("Try to connect internet or web page not available")
        exit(1)
    return main_data


def get_array(record, tag):
    get_record = record.split("\n")
    data = "None"
    try:
        for i in range(0, len(get_record), 1):
            if(get_record[i].find(tag) > 0):
                start = get_record[i].find(">") + 1
                end = get_record[i].find(tag)
                data = get_record[i][start:end]
    except:
        data = "None"
    return data


def get_data(main_data, tag):
    year_data = []
    for i in range(0, len(main_data)-1, 1):
        year_data.append(get_array(main_data[i], tag))
    return year_data


def check_price(price):
    for i in range(0, len(price), 1):
        try:
            price[i] = float(price[i])
        except:
            print(f"Invalid price data: price[{i}] = {price[i]}")
            price[i] = 0.00
    return price


def print_output(title_data, artist_data, country_data, company_data, price_data, year_data):
    length = max(
            len(title_data), 
            len(artist_data), 
            len(country_data), 
            len(company_data),
            len(price_data), 
            len(year_data))

    if len(title_data) < length:
        print("Invalid data: missing titles")
        return

    if len(artist_data) < length:
        print("Invalid data: missing artists")
        return

    if len(country_data) < length:
        print("Invalid data: missing countries")
        return

    if len(company_data) < length:
        print("Invalid data: missing companies")
        return

    if len(price_data) < length:
        print("Invalid data: missing prices")
        return

    if len(year_data) < length:
        print("Invalid data: missing years")
        return

    for i in range(len(title_data)):
        print(f"{title_data[i]} - {artist_data[i]} - {country_data[i]} - {company_data[i]} - $ {price_data[i]} - {year_data[i]}")


def get_data_average(price):
    total = 0
    for i in range(0, len(price), 1):
        total = total + price[i]
    average = total / len(price)
    return average


def print_output_average(record, average):
    print(f" Total Records Available in Catalog : {record}")
    print(f" Average price of items in Catalog  : {average :.2f}")


def main():
    main_data = fetch_info()
    title_data = get_data(main_data, "</TITLE>")
    artist_data = get_data(main_data, "</ARTIST>")
    country_data = get_data(main_data, "</COUNTRY>")
    company_data = get_data(main_data, "</COMPANY>")
    price_data = get_data(main_data, "</PRICE>")
    price_data = check_price(price_data)
    year_data = get_data(main_data, "</YEAR>")
    print_output(title_data, artist_data, country_data, company_data, price_data, year_data)
    average_data = get_data_average(price_data)
    print_output_average(len(title_data), average_data)

main()

