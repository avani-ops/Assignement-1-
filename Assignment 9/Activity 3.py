def displayDays(days):
    print(" Your age in days : " + str(days) + " days")

def displayHours(hours):
    print(" Your age in hours : " + str(hours) + " Hours")

def displayMonths(months):
    print(" Your age in months : " + str(months) + " Months")

def displaySeconds(seconds):
    print(" Your age in seconds : " + str(seconds) + " Secs")

def getAge():
    print("Please enter you age in years : ")
    age = float(input())
    
    return age

def getDays(age):
    days = age * 365
    
    return days

def getHours(age):
    hours = age * 8760
    
    return hours

def getMonths(age):
    months = age * 12
    
    return months

def getSeconds(age):
    seconds = age * 31556952
    
    return seconds

# Main
# This program takes age as input in years and display age i days , months , hours and seconds . Program will continue untill user negative or zero in age.
while True:    #This simulates a Do Loop
    age = getAge()
    if age > 0:
        days = getDays(age)
        months = getMonths(age)
        hours = getHours(age)
        seconds = getSeconds(age)
        displayMonths(months)
        displayDays(days)
        displayHours(hours)
        displaySeconds(seconds)
    else:
        print(" Wrong Input ...Please input correct age next time")
    if not(age > 0): break   #Exit loop
