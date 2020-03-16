def getvalue(value1, value2):
    for value in range(1, value2 + 1, 1):
        times = value1 * value
        print(str(value1) + " * " + str(value) + " = " + str(times))

def getValue1():
    print("Please enter a value")
    value1 = int(input())
    
    return value1

def getValue2():
    print("please enter anothe value")
    value2 = int(input())
    
    return value2

# Main
value1 = getValue1()
value2 = getValue2()
getvalue(value1, value2)
