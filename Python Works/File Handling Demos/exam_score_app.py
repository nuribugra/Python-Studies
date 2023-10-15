def read_scores():
    pass

def enter_score():
    student_name = input("Enter student name: ")
    number_of_exams = int(input("Enter number of exams: "))
    scores= []
    for i in range(number_of_exams):
        exam_score = int(input("Enter exam score: "))
        scores.append(exam_score)


    with open("exam_notes.txt", "a", encoding="utf-8") as file:
        file.write(f"{student_name}: {scores[0]}, {scores[1]}, {scores[2]}\n")


def save_scores():
    pass

def delete_score():
    pass

while True:
    selection = input("1- Read Scores\n2- Add Score\n3- Save Scores\n4- Delete Score\n0- Exit\nSelect an operation: ")

    if selection == "1":
        read_scores()
    elif selection == "2":
        enter_score()
    elif selection == "3":
        save_scores()
    elif selection == "4":
        delete_score()
    elif selection == "0":
        quit()
