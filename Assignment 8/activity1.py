def displayExpression(value, expression, count):
    print(str(value) + " * " + str(expression) + " = " + str(count))

def getCount(value, expression):
    count = value * expression
    
    return count

def getExpression():
    print("Please Enter Expression for Multiplication")
    expression = int(input())
    
    return expression

def getValue():
    print("Please Enter the value :")
    value = int(input())
    
    return value

# Main
# This program takes value and expression from user and generates the multiplication expression for given input
expression = getExpression()
value = getValue()
flag = 1
while flag <= expression:
    count = getCount(value, flag)
    displayExpression(value, flag, count)
    flag = flag + 1
