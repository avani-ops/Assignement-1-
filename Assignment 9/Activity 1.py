# This program takes input for grade and score from user
# and depend on that input it will calculate Average of those grades
# This pogram uses do..while loop to execute this


def get_grade():
    print("Enter your grade :")
    grade = float(input())
    return grade


def display_score(total_grades, average):
    print("Sum of all grades enter by you :" + str(total_grades))
    print(f"Average of all your grades :{average:.2f}")


def get_average(total_grades, score):
    average = total_grades / score
    return average


def get_total_grades(total_grades, grade):
    sum_grade = total_grades + grade
    return sum_grade


def main():
    total_grades = 0
    flag = 0
    while True:
        grade = get_grade()
        if(grade<0):
            break
        total_grades = get_total_grades(total_grades, grade)
        flag = flag + 1
   
 
    average = get_average(total_grades, flag)
    display_score(total_grades, average)


main()
