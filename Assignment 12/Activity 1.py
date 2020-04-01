# This program takes grades from user store in dynamic array and
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
    min = marks[0]
    for flag in range(0, subject, 1):
        if min > marks[flag]:
            min = marks[flag]
    return min


def get_outPut(max, min, average):
    print("Maximum Grade : " + str(max))
    print("Minimum Grade : " + str(min))
    print("Average Grade : " + str(average))


def add_marks(marks, score):
    marks.append(score)
    return marks


def main():
    marks = []
    flag = 0
    score = 1
    print("Please enter '0' or negative number to stop input grades")
    while True:
        score = get_marks()
        if score <= 0:
            break
        marks = add_marks(marks, score)
        flag = flag + 1

    max = get_max(marks, flag)
    min = get_min(marks, flag)
    average = get_average(marks, flag)
    get_outPut(max, min, average)


main()

