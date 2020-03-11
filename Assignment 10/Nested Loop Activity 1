# This program will user nested for loop to generate mulitplication
# table


def get_start():
    print("Please enter start number")
    start = int(input())
    return start


def get_end():
    print("Please enter end number")
    end = int(input())
    return end


def get_output(start, end):
    print_x = start
    print("", end='\t')
    for print_x in range(start, end + 1):
        print(str(print_x), end='\t')


def get_series(start, end):
    print_x = start
    for print_x in range(start, end + 1):
        print("", end='\n')
        print(str(print_x), end='\t')
        print_y = start
        for print_y in range(start, end + 1):
            print(str(print_x * print_y), end='\t')


def main():
    start = get_start()
    end = get_end()
    get_output(start, end)
    get_series(start, end)


main()
