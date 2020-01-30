def displayAnnualy(annualy):
    print("Total Annualy Income : $ " + str(annualy))

def displayMonthly(monthly):
    print("Total Monthly Income : $ " + str(monthly))

def displayWeekly(weekly):
    print("Total Weekly Income : $ " + str(weekly))

def getAnnualy(weekly):
    annualy = weekly * 52
    
    return annualy

def getHour():
    print("Please Enter Working Hour of Week : ")
    hour = float(input())
    
    return hour

def getMonthly(annualy):
    monthly = annualy / 12
    
    return monthly

def getWage():
    print("Please Enter Your Wage per Hour : ")
    wage = float(input())
    
    return wage

def getWeekly(wage, hour):
    weekly = wage * hour
    
    return weekly

# Main
# This program will take wage and hour from user and count the weekly , monthly and annual income of the person
# Calling Function to take input from the user
wage = getWage()
hour = getHour()
weekly = getWeekly(wage, hour)
annualy = getAnnualy(weekly)
monthly = getMonthly(annualy)
displayWeekly(weekly)
displayMonthly(monthly)
displayAnnualy(annualy)
