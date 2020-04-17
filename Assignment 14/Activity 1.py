# This program checks the file is available or not. After finiding the file
# program reads the data from file seperate the name and score and prints the
# maximum , minimum and average score


def check_file(filename):
    try:
        file = open(filename, "r")
        file.close()
        message = "Success"
    except:
        message = "Error"
    return message


def read_file(filename):
    file = open(filename, "r")
    file_data = []
    for line in file:
        line = line.replace("\n", "")
        file_data.append(line)
    file.close()
    return file_data


def get_score(file_data):
    score = []
    i = 1
    while i < len(file_data):
        score.append(int(file_data[i][file_data[i].find(",")+1: len(file_data[i])]))
        i = i + 1
    return score


def get_name(file_data):
    name = []
    i = 1
    while i < len(file_data):
        name.append(file_data[i][0:file_data[i].find(",")])
        i = i + 1
    return name


def get_average(score):
    total_score = 0
    for i in range(0, len(score)-1, 1):
        total_score = total_score + score[i]

    average = total_score / len(score)
    return average


def display_output(file_data):
    print("Content of File :")
    for i in range(0, len(file_data), 1):
        print(file_data[i])


def print_max(name, score, max_score):
    print("Maximum Score Result board")
    for i in range(0, len(score) - 1, 1):
        if(score[i] == max_score):
            print("Maximum Score is : " + str(max_score) + " , achieve by  " + name[i])


def print_min(name, score, min_score):
    print("Minimum Score Result board")
    for i in range(0, len(score) - 1, 1):
        if(score[i] == min_score):
            print("Manimum Score is : " + str(min_score) + " , achieve by  " + name[i])


def print_average(average):
    print(f"Average score  : {average:.2f}")


def main():
    filename = "scores.txt"
    file_status = check_file(filename)
    if file_status == "Success":
        file_data = read_file(filename)
        display_output(file_data)
        name = get_name(file_data)
        score = get_score(file_data)
        print_max(name, score, max(score))
        print_min(name, score, min(score))
        average = get_average(score)
        print_average(average)
    else:
        print("Mentioned file does not exist please create file first")


main()
