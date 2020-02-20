# This program will take yhe height an width of the room and
# count the area  of the room using function and display using the function


def get_length():
    print("Please enter the length of the room(in feets)")
    length = float(input())
    return length


def get_width():
    print("Please enter the Width of the room(in feets)")
    width = float(input())
    return width


def get_area(length, width):
    area = length * width
    return area


def display_area(area):
    print(f"The area of room is {area :.2f} square feets")


def get_yard(area):
    feet = area // 9
    yard = area - (feet * 9)
    display_yard(feet, yard)


def display_yard(feet, yard):
    print(f"The area of room is {feet: .0f} square feets and {yard: .2f} square yards")


def main():
    length = get_length()
    width = get_width()
    area = get_area(length, width)
    display_area(area)
    get_yard(area)

# main function body
main()
