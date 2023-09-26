# Prime Numbers Demo

# Get a number from the user and check if it is prime or not (a number that is only divisible by itself and 1)

number = int(input("Enter a number: "))
IsPrime = True

if (number <= 1):
    IsPrime = False
elif (number == 2):
    IsPrime = True
else:
    for i in range(2, number):
        if (number % i == 0):
            IsPrime = False
            break

if IsPrime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")