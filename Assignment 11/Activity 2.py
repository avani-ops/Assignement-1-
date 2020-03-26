# This program will take static array from user and
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
    x = 0
    while x < score - 1:
        y = x + 1
        while y < score:
            if(marks[x] > marks[y]):
                temp = marks[x]
                marks[x] = marks[y]
                marks[y] = temp
            y = y + 1
        x = x + 1
    return marks


def get_output(marks, subject):
    print("Grade in highest to minimum range")
    flag = subject - 1
    while flag >= 0:
        print(str(marks[flag]))
        flag = flag - 1


def main():
    subject = get_subject()
    flag = 0
    marks = [0] * (subject)
    while flag < subject:
        marks[flag] = get_marks()
        flag = flag + 1

    marks = get_sort(marks, subject)
    get_output(marks, subject)


main()
