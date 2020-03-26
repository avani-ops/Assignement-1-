# This program takes grades from user store in array and
# dislay highest , lowest and average grade.


def get_average(marks, subject):
    total = 0
    for flag in range(0, subject, 1):
        total = total + marks[flag]
    average = float(total) / subject
    return average


def get_marks():
    print("Please enter Grades :")
    marks = int(input())
    return marks


def get_max(marks, subject):
    max = 0
    for flag in range(0, subject, 1):
        if max < marks[flag]:
            max = marks[flag]
    return max


def get_min(marks, subject):
    min = marks[1]
    for flag in range(0, subject, 1):
        if min > marks[flag]:
            min = marks[flag]
    return min


def get_outPut(max, min, average):
    print("Maximum Grade : " + str(max))
    print("Minimum Grade : " + str(min))
    print("Average Grade : " + str(average))


def get_subject():
    print("Please Enter how many subjects you want to enter ?")
    subject = int(input())
    return subject


def main():
    subject = get_subject()
    marks = [0] * (subject)

    flag = 0
    while flag < subject:
        marks[flag] = get_marks()
        flag = flag + 1
    max = get_max(marks, subject)
    min = get_min(marks, subject)
    average = get_average(marks, subject)
    get_outPut(max, min, average)


main()
