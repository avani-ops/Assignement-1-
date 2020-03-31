# This program will take dynamic array from user and
# display in descending order


def get_marks():
    print("Please enter score:")
    marks = int(input())
    return marks


def get_subject():
    print("Please Enter how many score you want to enter ?")
    subject = int(input())
    return subject


def get_sort(marks, score):
    marks.sort()
    marks.reverse()
    return marks


def get_output(marks, subject):
    print("Grade in highest to minimum range")
    for i in range(0, subject, 1):
        print(marks[i])


def main():
    flag = 0
    marks = []
    while True:
        score = get_marks()
        if score <= 0:
            break
    marks.append(score)
    flag = flag + 1

    marks = get_sort(marks, flag)
    get_output(marks, flag)


main()
