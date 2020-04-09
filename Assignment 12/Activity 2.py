# This program will ask user to guess one number
# between 1 - 100 and using guuessing mid point
# find the correct number and display the number
# of guesses


def get_answer(max_no, min_no):
    guess = []
    mid_no = get_midno(min_no, max_no)
    while True:
        choice = get_choice(mid_no)
        if choice == 1:
            guess = get_guess(guess, mid_no)
            min_no = mid_no
            mid_no = get_midno(min_no, max_no)
        elif choice == 2:
            guess = get_guess(guess, mid_no)
            max_no = mid_no
            mid_no = get_midno(min_no, max_no)
        elif choice == 3:
            guess = get_guess(guess, mid_no)
            break
    return guess


def get_midno(min_no, max_no):
    mid_no = int((min_no + max_no)/2)
    return mid_no


def get_guess(guess, new_guess):
    guess.append(new_guess)
    return guess


def get_choice(mid_no):
    print(" Enter '1' if your number is less than: " + str(mid_no))
    print(" Enter '2' if your number is greater than :" + str(mid_no))
    print(" Enter '3' if you number is equal to: " + str(mid_no))
    choice = int(input())
    return choice


def get_display(guess):
    print("Total Guess made : " + str(len(guess)))
    print("Total guesses are mentioned below ")
    print(guess)


def main():
    print("Please select one number between 1 - 100")
    guess = get_answer(0, 100)
    get_display(guess)


main()
