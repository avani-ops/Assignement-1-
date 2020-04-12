# Program takes first name and last name from user
# it handles all input validation and print Lastname, F.


def get_name():
    print("Enter Your Name in one line text in (FirstName LastName) format")
    while True:
        name = str(input())
        name = name.strip()
        name_list = name.split()
        error = check_name(name_list, name)
        if error == "success":
            break

        print("Wrong input please try again")

    return name_list


def check_name(name_list, name):
    if name.isalpha() == "False":
        error = "fail"
    elif len(name_list) == 2:
        error = "success"
    else:
        error = "fail"
    return error


def get_firstname(name_list):
    firstname = name_list[0].capitalize()
    return firstname


def get_lastname(name_list):
    lastname = name_list[1].capitalize()
    return lastname


def get_output(firstname, lastname):
    print(lastname + ", " + firstname[0] + ". ")


def main():
    name_list = get_name()
    firstname = get_firstname(name_list)
    lastname = get_lastname(name_list)
    get_output(firstname, lastname)

main()
