# This program calculates the area of circle and rectangle and
# displays the output using class


class ShapeArea:
    height = 0
    width = 0
    radius = 0
    area = 0.00

    def __init__(self, h=0, w=0, r=0):
        try:
            self.height = float(h)
            self.width = float(w)
            self.radius = float(r)
        except:
            print("It looks like you have entered wrong dimension , system exit")
            exit()

    def calculate_area(self):
        if(self.height > 0):
            self.area = self.height * self.width
        if(self.radius > 0):
            self.area = (22/7) * (self.radius * self.radius)

    def calculate_area1(self):
        self.area = (22/7) * (self.radius * self.radius)

    def get_display(self):
        if(self.height > 0):
            print(f"Rectangle with height of {self.height} feet and width {self.width} feet has area {self.area :.2f} sq.feet")
        if(self.radius > 0):
            print(f" Circle with radius of {self.radius} feet has area of {self.area :.2f} sq.feet")


def get_choice():
    print("Press (A) to calculate rectangle area")
    print("Press (B) to calculate circle area")
    print("Enter your choice :")
    choice = input()
    return choice


def get_dimension():
    dimension = float(input())
    return dimension


def main():
    choice = get_choice()
    if(choice == 'A' or choice == 'a'):
        print("Enter Height(in feet)")
        height = get_dimension()
        print("Enter Width(in feet)")
        width = get_dimesion()
        rect = ShapeArea(h=height, w=width)
        rect.calculate_area()
        rect.get_display()
    elif(choice == 'B' or choice == 'b'):
        print("Enter radius of circle")
        radius = get_dimension()
        circle = ShapeArea(r=radius)
        circle.calculate_area()
        circle.get_display()
    else:
        print("You have enter wrong input, see you next time")
        exit(1)


main()
