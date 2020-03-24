def getAverage(marks, subject):
    total = 0
    for flag in range(0, subject - 1 + 1, 1):
        total = total + marks[flag]
    average = float(total) / subject
    
    return average

def getMarks():
    print("Please enter Grades :")
    marks = int(input())
    
    return marks

def getMax(marks, subject):
    max = 0
    for flag in range(0, subject - 1 + 1, 1):
        if max < marks[flag]:
            max = marks[flag]
    
    return max

def getMin(marks, subject):
    min = marks[1]
    for flag in range(0, subject - 1 + 1, 1):
        if min > marks[flag]:
            min = marks[flag]
    
    return min

def getOutPut(max, min, average):
    print("Maximum Grade : " + str(max))
    print("Minimum Grade : " + str(min))
    print("Average Grade : " + str(average))

def getSubject():
    print("Please Enter how many subjects you want to enter ?")
    subject = int(input())
    
    return subject

# Main
# This program takes grades from user store in array and islay highest , lowest and average grade.
subject = getSubject()
marks = [0] * (subject)

flag = 0
while flag < subject:
    marks[flag] = getMarks()
    print(marks[flag])
    flag = flag + 1
max = getMax(marks, subject)
min = getMin(marks, subject)
average = getAverage(marks, subject)
getOutPut(max, min, average)
