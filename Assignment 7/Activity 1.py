def displayGrossPay(pay):
    print("Total Weekly Gross Payment : $ " + str(pay))

def getGrossPay(hour, wage):
    grosspay = hour * wage
    
    return grosspay

def getHour():
    print("Please Enter your Weekly working Hours :")
    hour = float(input())
    
    return hour

def getOvertime(hour, wage):
    overtime = hour * (wage * 1.5)
    
    return overtime

def getOvertimeHour(hour, wage):
    overtimehour = wage * 40 + (hour - 40) * (wage * 1.5)
    
    return overtimehour

def getRate():
    print("Please Enter Wages/per hour ")
    rate = float(input())
    
    return rate

# Main
hour = getHour()
wage = getRate()
if hour < 40:
    grossPay = getGrossPay(hour, wage)
else:
    grossPay = getOvertimeHour(hour, wage)
displayGrossPay(grossPay)
