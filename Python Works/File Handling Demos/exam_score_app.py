import time

# Background: The letter_grade() function is used in the calculate_scores() function.
def letter_grade(average):
    """
    90-100: AA / 4.00
    85-89: BA / 3.50
    80-84: BB / 3.00
    75-79: CB / 2.50
    70-74: CC / 2.00
    65-69: DC / 1.50
    60-64: DD / 1.00
    50-59: FD / 0.50
    0-49: FF / 0.00
    """

    if average >= 90:
        return "AA / 4.00"
    elif average >= 85:
        return "BA / 3.50"
    elif average >= 80:
        return "BB / 3.00"
    elif average >= 75:
        return "CB / 2.50"
    elif average >= 70:
        return "CC / 2.00"
    elif average >= 65:
        return "DC / 1.50"
    elif average >= 60:
        return "DD / 1.00"
    elif average >= 50:
        return "FD / 0.50"
    else:
        return "FF / 0.00"

# Background: The calculate_scores() function is used in the read_scores() function.
def calculate_scores(file):
    for line in file:
            names, scores = line.split(":")

            scores = scores.strip().strip("[]").split(", ") # This code line is very important. It strips the square brackets and splits the scores into a list.
            scores = [int(score) for score in scores]

            average = sum(scores) / len(scores)
            average = round(average, 2)

            time.sleep(0.25)

            print(names.ljust(20), str(scores).ljust(20), str(average).rjust(10), letter_grade(average).rjust(20))
            # ljust() and rjust() methods are used to align the text to the left and right respectively.
    

# Transaction 1: Read Scores
def read_scores():

    with open("exam_scores.txt", "r", encoding="utf-8") as file:
        print("Exam Scores".center(70, "="))
        print("Name".ljust(20), "Scores".ljust(20), "Average".rjust(10), "Grade".rjust(20))
        # At the top of the table, we have the titles of the columns.
        print("-"*70)
        calculate_scores(file)
        print("="*70)

# Transaction 2: Add Scores
def add_scores():

    time.sleep(1)

    name = input("Name: ")
    number_of_exams = int(input("Number of exams: "))
    scores = []

    for i in range(number_of_exams):
        score = int(input(f"Exam {i+1}: "))
        scores.append(score)    
    
    scores = str(scores).strip("[]")

    with open("exam_scores.txt", "a", encoding="utf-8") as file:
        file.write(f"{name}: {scores}\n")

# Transaction 3: Save Scores
def save_scores():
    # This function gives the averages, grades and names of the students in the exam_scores.txt file.
    
    time.sleep(1)

    with open("exam_scores.txt", "r", encoding="utf-8") as file:
        with open("results.txt", "w", encoding="utf-8") as file2:
            file2.write("Exam Scores".center(70, "="))
            file2.write("\n")
            file2.write("Name".ljust(20))
            file2.write("Scores".ljust(20))
            file2.write("Average".rjust(10))
            file2.write("Grade".rjust(20))
            file2.write("\n")
            file2.write("-"*70)
            file2.write("\n")
                
            for line in file:
                names, scores = line.split(":")

                scores = scores.strip().strip("[]").split(", ")
                scores = [int(score) for score in scores]

                average = sum(scores) / len(scores)
                average = round(average, 2)

                file2.write(names.ljust(20))
                file2.write(str(scores).ljust(20))
                file2.write(str(average).rjust(10))
                file2.write(letter_grade(average).rjust(20))
                file2.write("\n")
                
            file2.write("="*70)

while True:
    operation = input("1- Read Scores\n2- Add Scores\n3- Save Scores\n0- Exit\nSelect an operation: ")

    if operation == "1":
        read_scores()
    elif operation == "2":
        add_scores()
    elif operation == "3":
        save_scores()
    elif operation == "0":
        quit()