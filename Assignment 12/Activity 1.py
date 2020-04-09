# This program takes grades from user store in dynamic array and
# dislay highest , lowest and average grade.


def get_average(marks):
    total = sum(marks)
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
        if score <= 0:
            break
        marks.append(score)
    return marks


def display_output(max, min, average):
    print("Maximum Grade : " + str(max))
    print("Minimum Grade : " + str(min))
    print("Average Grade : " + str(average))


def main():
    marks = get_marks()
    average = get_average(marks)
    display_output(max(marks), min(marks), average)


main()
