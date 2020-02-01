def displayDays(days):
    print(" YOUR AGE IN DAYS : " + str(days) + " days")

def displayHours(hours):
    print(" YOUR AGE IN HOURS : " + str(hours) + " Hours")

def displayMonths(months):
    print(" YOUR AGE IN MONTHS : " + str(months) + " Months")

def displaySeconds(seconds):
    print(" YOUR AGE IN SECONDS : " + str(seconds) + " Secs")

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
age = getAge()
days = getDays(age)
months = getMonths(age)
hours = getHours(age)
seconds = getSeconds(age)
displayMonths(months)
displayDays(days)
displayHours(hours)
displaySeconds(seconds)
