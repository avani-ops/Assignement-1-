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
    file = open(filename, "r")
    file_data = ""
    data = []
    for line in file:
        file_data = file_data + line
    file.close()
    return file_data


def print_data(file_data):
    address = file_data.split("\n\n")
    for i in range(0, len(address), 1):
        address_comma = get_address(address[i])
        print(address_comma)


def get_address(address):
    sep_add = address.split("\n")
    address_comma = ""
    for i in range(0, len(sep_add) - 1, 1):
        address_comma = address_comma + sep_add[i] + ","

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
