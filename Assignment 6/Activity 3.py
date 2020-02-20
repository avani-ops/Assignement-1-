# This program convert mile into yards , feet , inch , kilometer ,
# meter , centimeter using function and display the output using function


def get_mile():
    print("Please Enter Distance in Miles ")
    mile = float(input())
    return mile


def get_yard(mile):
    yard = mile * 1760
    return yard


def get_feet(mile):
    feet = mile * 5280
    return feet


def get_inch(mile):
    inch = mile * 63360
    return inch


def get_centimeter(mile):
    centimeter = mile * 160934
    return centimeter


def get_meter(centimeter):
    meter = centimeter / 100
    return meter


def get_kilometer(meter):
    kilometer = meter / 1000
    return kilometer


def display_yard(yard):
    print("Your distance in yards : " + str(yard) + " Yds")


def display_feet(feet):
    print("Your distance in feets : " + str(feet) + " Fts")


def display_inch(inch):
    print("Your distance in inches : " + str(inch) + " Inches")


def display_centimeter(centimeter):
    print("Your distance in centimeters : " + str(centimeter) + " Cms")


def display_meter(meter):
    print("Your distance in meters : " + str(meter) + " Meters")


def display_kilometer(kilometer):
    print("Your distance in Kilometers : " + str(kilometer) + " Kms")


#  main function code starts from here
def main():
    mile = get_mile()

    yard = get_yard(mile)
    feet = get_feet(mile)
    inch = get_inch(mile)
    centimeter = get_centimeter(mile)
    meter = get_meter(centimeter)
    kilometer = get_kilometer(meter)

    display_yard(yard)
    display_feet(feet)
    display_inch(inch)
    display_centimeter(centimeter)
    display_meter(meter)
    display_kilometer(kilometer)

main()
