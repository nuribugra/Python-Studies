def add_item():
    shopping_list = []

    while True:
        item = input("Please, enter the item: \n(Press 0 to finish.)\n")

        if item == "0":
            break
        else:
            shopping_list.append(item)

    with open("shopping_list.txt", "a", encoding="utf-8") as file:
        counter = 0
        for i in shopping_list:
            counter = counter + 1
            file.write(f"{counter}-{i}\n")


def show_list():
    with open("shopping_list.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip("\n")
            print(line)

    quit()


while True:
    operation = int(input("1-Add Item\n2-Show List\n0-Exit\n"))

    if operation == 1:
        add_item()
    elif operation == 2:
        show_list()
    elif operation == 0:
        quit()
