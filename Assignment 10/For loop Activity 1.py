def getAnswer(value, expression):
    answer = value * expression
    
    return answer

def getExpression():
    print("Enter how many expression you want to print")
    expression = int(input())
    
    return expression

def getOutput(value, expression, answer):
    print(str(value) + " * " + str(expression) + " = " + str(answer))

def getValue():
    print("Enter Value to be printed")
    value = int(input())
    
    return value

# Main
# This program accepts value and expression from user and using for loop it prints the multiplication table for value till expression
value = getValue()
expression = getExpression()
for flag in range(1, expression + 1, 1):
    answer = getAnswer(value, flag)
    getOutput(value, flag, answer)
