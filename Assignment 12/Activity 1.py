# This program takes grades from user store in dynamic array and
# dislay highest , lowest and average grade.


def get_average(marks):
    total = 0
    for flag in range(len(marks)):
        total = total + marks[flag]
    average = float(total) / len(marks)
    return average


def get_score():
    print("Please enter Grades :")
    marks = float(input())
    return marks


def get_marks():
    marks = []
    print("Please enter '0' or negative number to stop input grades")
    while True:
        score = get_score()
        if score < 0:
            break
        marks.append(score)
    return marks


def get_max(marks):
    max = 0
    for flag in range(len(marks)):
        if max < marks[flag]:
            max = marks[flag]
    return max


def get_min(marks):
    min = marks[0]
    for flag in range(1, len(marks)):
        if min > marks[flag]:
            min = marks[flag]
    return min


def display_output(max, min, average):
    print("Maximum Grade : " + str(max))
    print("Minimum Grade : " + str(min))
    print("Average Grade : " + str(average))


def main():
    marks = get_marks()
    max = get_max(marks)
    min = get_min(marks)
    average = get_average(marks)
    display_output(max, min, average)


main()
