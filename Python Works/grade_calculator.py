# Grade calculator is a program that assigns a letter grade to a student based on the average of their scores.
# The program will ask the user for the number of tests and the scores for each test.
# The program will then calculate the average and assign a letter grade based on the following scale:

# 95-100 : A+
# 80-95 : A
# 70-80 : B
# 60-70 : C
# 50-60 : D
# 30-50 : E
# 20-30 : F
# 0-30 : F-

import time

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

time.sleep(0.5)

# Number of tests
try:
    number_of_tests = int(input("Enter the number of tests: "))
except ValueError:
    print("Please enter a valid number.")
    quit()

time.sleep(1)

# Test scores
test_scores = []
for i in range(number_of_tests):
    try:
        test_scores.append(int(input("Enter test score: ")))
    except ValueError:
        print("Please enter a valid number.")
        quit()

time.sleep(2)

# Average
average = sum(test_scores) / len(test_scores)
print("Average: ", average)

# Letter grade
if average > 95:
    print(f"Dear {first_name} {last_name}, you have received an A+!")
elif average > 80:
    print(f"Dear {first_name} {last_name}, you have received an A!")
elif average > 70:
    print(f"Dear {first_name} {last_name}, you have received a B!")
elif average > 60:
    print(f"Dear {first_name} {last_name}, you have received a C!")
elif average > 50:
    print(f"Dear {first_name} {last_name}, you have received a D!")
elif average > 30:
    print(f"Dear {first_name} {last_name}, you have received an E!")
elif average > 20:
    print(f"Dear {first_name} {last_name}, you have received an F!")
else:
    print(f"Dear {first_name} {last_name}, unfortunately you have failed. Your grade is an F-.")