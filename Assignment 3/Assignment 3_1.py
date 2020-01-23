# This program will count the  Weekly , Monthly and Yearly(Gross Income) according to user input wage and hours
print("Please Enter Hourly Rate : ")
wage = float(input())
print("Please Enter Hours Work : ")
hour = float(input())
weekly = wage * hour
annualy = wage * hour * 52
monthly = annualy / 12
print("Your Weekly Income is : $" + str(weekly))
print("Your Monthly Income is : $" + str(monthly))
print("Your Annual Income is : $" + str(annualy))
