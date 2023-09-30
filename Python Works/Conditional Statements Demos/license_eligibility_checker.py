# Min age is 18 and min highschool diploma is required for license eligibility.

from datetime import datetime
import time

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

try:
    birth_year = int(input("Enter your birth year: "))
except ValueError:
    print("Please enter a valid birth year.")
    quit()

try:
    education = int(input("What is your level of education(1-High School, 2-Undergraduate+): "))
except ValueError:
    print("Please enter a valid education level.")
    quit()

education_name = ""

if education == 1:
    education_name = "High School"
elif education == 2:
    education_name = "Undergraduate+"

date = datetime.now()
current_year = date.year
age = current_year - birth_year

print("Calculating your eligibility...")

time.sleep(2) # 2 seconds delay

print(f"Your age is {age}.")
print(f"Your education level is {education_name}.")

time.sleep(1)

if (age < 0):
    if ((education < 1) or (education > 2)):
        print("Please enter a valid birth year and education level.")
    else:
        print("Please enter a valid birth year.")
elif ((education < 1) or (education > 2)):
    if (age < 0):
        print("Please enter a valid birth year and education level.")
    else:
        print("Please enter a valid education level.")
else:
    if (age >= 18) and (education >= 1):
        print(f"Congratulations {first_name} {last_name}! You are eligible for a driver's license.")
    elif (age < 18) and (education >= 1):
        print(f"Sorry {first_name} {last_name}, your age is not eligible for a driver's license.")
    elif (age >= 18) and (education < 1):
        print(f"Sorry {first_name} {last_name}, your education level is not eligible for a driver's license.")
    else:
        print(f"Sorry {first_name} {last_name}, your age and education level are not eligible for a driver's license.")
