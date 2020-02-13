# This program will take yhe height an width of the room and
# count the area  of the room using function and display using the function


def getLength():
    print("Please enter the length of the room(in feets)")
    length = float(input())
    return length


def getWidth():
    print("Please enter the Width of the room(in feets)")
    width = float(input())
    return width


def getArea(length, width):
    area = length * width
    return area


def displayArea(area):
    print(f"The area of room is {area :.2f} square feets")


def getYard(area):
    feet = area // 9
    yard = area - (feet * 9)
    displayYard(feet, yard)


def displayYard(feet, yard):
    print(f"The area of room is {feet: .0f} square feets and {yard: .2f} square yards")


# main function body
Length = getLength()
Width = getWidth()

Area = getArea(Length, Width)

displayArea(Area)

getYard(Area)
