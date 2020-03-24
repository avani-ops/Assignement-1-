# This program will take static array from user and
# display in descending order


def getMarks():
    print("Please enter score:")
    marks = int(input())
    return marks


def getSubject():
    print("Please Enter how many score you want to enter ?")
    subject = int(input())
    return subject


def getSort(Marks, score):
    x = 1
    while x < score:
        y = x + 1
        while y <= score:
            if(Marks[x] > Marks[y]):
                temp = Marks[x]
                Marks[x] = Marks[y]
                Marks[y] = temp
            y = y + 1
        x = x + 1
    return Marks


def getOutPut(marks, subject):
    print("Grade in highest to minimum range")
    flag = subject
    while flag >= 1:
        print(str(marks[flag]))
        flag = flag - 1


def main():
    subject = getSubject()
    flag = 0
    marks = [subject]
    sortMarks = [subject]
    while flag < subject:
        value = getMarks()
        marks.append(value)
        flag = flag + 1

    sortMarks = getSort(marks, subject)
    getOutPut(sortMarks, subject)


main()
