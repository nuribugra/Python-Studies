list = ["1", "2", "5a", "10b", "abc", "10", "50"]

# Find the numerical values in the list

"""
for i in list:
    try:
        result = int(i)
        print(result)
    except ValueError:
        continue
"""

# Make sure that every input is a number unless the user enters the value 'q', otherwise print an error message.

"""
while True:
    number = input("Enter a number: ")
    if number == "q":
        break

    try:
        result = float(number)
        print("Number: ", result)
    except ValueError:
        print("You entered an invalid value. Please enter a number or 'q' to exit.")
"""
 
# Give a Turkish character error message password is entered. 

"""
password = input("Enter a password: ")

try:
    if password.isalpha(): # isalpha() metho checks whether the string consists of alphabetic characters only. 
        raise TypeError("You cannot use Turkish characters in your password.")
    else:
        print("Your password is: ", password)
except TypeError as error:
    print(error)
"""

password = input("Enter a password: ")

turkish_characters = "şçöğüıİ"

for i in turkish_characters:
    if i in password:
        raise TypeError("You cannot use Turkish characters in your password.")
    else:
        pass

print("Your password is: ", password)

# Create a factorial function and give an error message if the user enters a negative number.

"""
def calculate_factorial(x):
    
    result = 1

    if x > 0:
        for i in range(1, x + 1):
            result *= i

        print("Factorial of the given number is: ", result)
    elif x < 0:
        print("Negative numbers do not have a factorial value.")


calculate_factorial(6)
"""