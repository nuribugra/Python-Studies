def divide():
    print("*" * 20)

# 1- Create a function that prints the given word to the screen a specified number of times.

def prinTheWord(word, number):
    print(word * number)

prinTheWord("Selamlar\n", 5)

divide()
# 2- Create a function that converts an unlimited number of parameters sent to it into a list.

def createList(*params):
    new_list = []

    for i in params:
        new_list.append(i)
    
    return new_list

print(createList("selam", 34, True, "ankara"))

divide()
# 3- Find the all prime numbers between of two numbers sent.

def findPrimeNumbers(start, end):
    for number in range(start, (end + 1)):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    print(f"{number} is not a prime number.")
                    break
            else:
                print(f"{number} is a prime number.")

# start = int(input("Enter the start number:"))
# end = int(input("Enter the end number:"))

# findPrimeNumbers(start, end) 

# 4- Create a function that returns the divisors of a given number as a list.

def divisorList(number):
    list = []

    for i in range(1, (number + 1)):
        if (number % i) == 0:
            list.append(i)
    
    return list

print(divisorList(64))
