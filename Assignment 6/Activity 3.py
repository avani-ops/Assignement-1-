# This program convert mile into yards , feet , inch , kilometer ,
# meter , centimeter using function and display the output using function


def getMile():
    print("Please Enter Distance in Miles ")
    mile = float(input())
    return mile


def getYard(mile):
    yard = mile * 1760
    return yard


def getFeet(mile):
    feet = mile * 5280
    return feet


def getInch(mile):
    inch = mile * 63360
    return inch


def getCentimeter(mile):
    centimeter = mile * 160934
    return centimeter


def getMeter(centimeter):
    meter = centimeter / 100
    return meter


def getKilometer(meter):
    kilometer = meter / 1000
    return kilometer


def displayYard(yard):
    print("Your distance in yards : " + str(yard) + " Yds")


def displayFeet(feet):
    print("Your distance in feets : " + str(feet) + " Fts")


def displayInch(inch):
    print("Your distance in inches : " + str(inch) + " Inches")


def displayCentimeter(centimeter):
    print("Your distance in centimeters : " + str(centimeter) + " Cms")


def displayMeter(meter):
    print("Your distance in meters : " + str(meter) + " Meters")


def displayKilometer(kilometer):
    print("Your distance in Kilometers : " + str(kilometer) + " Kms")


#  main function code starts from here
def main():
    Mile = getMile()

    Yard = getYard(Mile)
    Feet = getFeet(Mile)
    Inch = getInch(Mile)
    Centimeter = getCentimeter(Mile)
    Meter = getMeter(Centimeter)
    Kilometer = getKilometer(Meter)

    displayYard(Yard)
    displayFeet(Feet)
    displayInch(Inch)
    displayCentimeter(Centimeter)
    displayMeter(Meter)
    displayKilometer(Kilometer)

main()
