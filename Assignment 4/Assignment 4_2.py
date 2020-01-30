# This program converts miles into yards , feet
# , inch , kilometer , meter, centimere

print("Please Enter Distance in Miles : ")
mile = float(input())
yards = mile * 1760
feet = mile * 5280
inch = mile * 63360
centimeter = mile * 160934
meter = centimeter / 100
kilometer = meter / 1000

print("Your distance in yards:" + str(yards) + " Yds")

print("Your distance in feets:" + str(feet) + " Fts")

print("Your distance in inches:" + str(inch) + " Inches")

print("Your distance in Kilometer:" + str(kilometer) + " Kms")

print("Your distance in meter:" + str(meter) + " Meters")

print("Your distance in centimeter:" + str(centimeter) + " Cms")
