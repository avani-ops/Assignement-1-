# This program accepts age from user and convert age into
# months,days,hours and seconds and print the out according to
# user choice


def display_days(days):
    print(" Your age in days : " + str(days) + " days")


def display_hours(hours):
    print(" Your age in hours : " + str(hours) + " Hours")


def display_months(months):
    print(" Your age in months : " + str(months) + " Months")


def display_seconds(seconds):
    print(" Your age in seconds : " + str(seconds) + " Secs")


def get_age():
    print("Please enter you age in years : ")
    age = float(input())
    return age


def get_choice():
    print("Please Choose One from below")
    print("1 . Enter 'M' to see your age in months")
    print("2 . Enter 'D' to see your age in days")
    print("3 . Enter 'H' to see your age in hours")
    print("4 . Enter 'S' to see your age in seconds")
    choice = str(input())
    return choice


def get_days(age):
    days = age * 365
    return days


def get_hours(age):
    hours = age * 8760
    return hours


def get_months(age):
    months = age * 12
    return months


def get_seconds(age):
    seconds = age * 31556952
    return seconds


def main():
    age = get_age()
    choice = get_choice()
    if choice == "D" or choice == "d":
        days = get_days(age)
        display_days(days)
    elif choice == "M" or choice == "m":
        months = get_months(age)
        display_months(months)
    elif choice == "H" or choice == "h":
        hours = get_hours(age)
        display_hours(hours)
    elif choice == "S" or choice == "s":
        seconds = get_seconds(age)
        display_seconds(seconds)
    else:
        print("Please select option from given choices")


main()
