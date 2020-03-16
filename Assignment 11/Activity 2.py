# This program diaplays average marks


def get_marks():
    while True:
        print("Please enter your Marks")
        marks = int(input())
        return marks


def get_subject():
    while True:
        try:
            print("Please Enter how many subject's grade you want to enter:")
            subject = int(input())
            return subject
        except:
            print("Not an valid input!Please try again")


def get_all_marks(main_subject):
    all_marks = 0
    for i in range(0, main_subject):
        while True:
            try:
                main_marks = get_marks()
                break
            except:
                print("Not an valid grade!Please try again")

        all_marks = get_final_marks(all_marks, main_marks)
        i = i + 1
    return all_marks


def get_final_marks(all_marks, marks):
    total_marks = all_marks + marks
    return total_marks


def get_avg(all_marks, subject):
    avg = all_marks / subject
    return avg


def print_mark(all_marks):
    print("Total Marks input by user: " + str(all_marks))


def print_average(average):
    print(f"Average marks of all subject: {average:.2f}")


def main():
    main_subject = get_subject()
    all_marks = get_all_marks(main_subject)
    main_average = get_avg(all_marks, main_subject)
    print_mark(all_marks)
    print_average(main_average)


main()
