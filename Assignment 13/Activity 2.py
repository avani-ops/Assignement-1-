# Program takes input from the user and reverse the string


def get_string():
    print("Enter String....lets print it reverse")
    name = str(input())
    name = name.strip()
    return name


def get_list(name):
    name_list = name.split()
    return name_list


def print_reverse(name):
    print(name[::-1])


def print_output(name_list):
    name_string = " ".join(name_list)
    print(" In reverse you string will look something like.....")
    print_reverse(name_string)


def main():
    name = get_string()
    name_list = get_list(name)
    print_output(name_list)


main()
