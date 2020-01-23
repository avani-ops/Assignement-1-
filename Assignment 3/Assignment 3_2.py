# This program will convert the Age into Months , Days , Hours, and Seconds
print("Please Enter Your Age : ")
age = int(input())
months = age * 12
days = age * 365
hours = age * 8760
seconds = age * 31556952
print("Your Age in Months : " + str(months) + " months")
print("Your Age in Days : " + str(days) + " days")
print("Your Age in Hours : " + str(hours) + " hours")
print("Your Age in Months : " + str(seconds) + " seconds")
