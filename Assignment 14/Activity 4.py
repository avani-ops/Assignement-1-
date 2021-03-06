# This program will read the address file and print each address
# in comma separated text


def check_file(filename):
    try:
        file = open(filename, "r")
        file.close()
        message = "Success"
    except:
        message = "Error"
    return message


def read_file(filename):
    with open(filename, "r") as file:
        file_data = file.read()
    # Using with, it is not necessary to close the file.
    # file.close()
    return file_data


def print_data(file_data):
    address = file_data.split("\n\n")
    for i in range(0, len(address), 1):
        address_comma = get_address(address[i])
        print(address_comma)


def get_name(name):
    name_list = name.split(" ")
    name = name_list[1] + "," + name_list[0]
    return name


def get_address(address):
    sep_add = address.split("\n")
    address_comma = get_name(sep_add[0]) + ","
    address_comma = address_comma + sep_add[1] + ","
    state_split = sep_add[len(sep_add) - 1].split(",")
    address_comma = address_comma + state_split[0] + ","
    state_split[1] = state_split[1].strip()
    state_split = state_split[1].split()
    address_comma = address_comma + state_split[0] + "," + state_split[1]
    return address_comma


def main():
    filename = "address.txt"
    file_status = check_file(filename)
    if file_status == "Success":
        file_data = read_file(filename)
        print_data(file_data)
    else:
        print("File does not exist , please create file first")


main()
