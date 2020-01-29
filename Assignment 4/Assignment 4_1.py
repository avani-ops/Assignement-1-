# This program willtake dimension of room and display the area to determine the amount of floor covering required.



print("Please Enter Length of the room : ")
Length = float(input())
print("Please Enter Width of the room : ")
Width = float(input())
area = Length * Width
feet = area % 9
yard = (area -feet) / 9
yard_only = int(yard)
remain = yard - yard_only  
feet = feet +(remain*9)
print("Your Room area is "+str(yard_only) + " Sq. Yds. and "+str(feet) +" Sq. Ft.")