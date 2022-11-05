# Write a python program that do the following:
# - display the initial content of the array
# - display a menu of options
# - allow user to select item in the menu (check if valid)
# - perform the selected option (you may prompt additional info to user when need)
# - display the resulting values of the array

# Note: 
# - The program has an array variable containing 10 random numbers

list = [2, 4, 6, 10, 1, 3, 9, 7, 8, 5]
print(f"Array: {list}")
print("""
  Menu:
  1 -> Add an element
  2 -> Insert an element
  3 -> Modify an element
  4 -> Delete an element
  5 -> Arrange in ascending order
  6 -> Arrange in descending order
""")

# asking the user for preferred array method from the menu and validates if its from 1 to 6
def askMenuInput():
    while True:
        try:
            menuInput = int(input("What do you want to do? (1-6): "))
            if menuInput not in range(1, 7):
                print("Invalid! Please enter 1 to 6 only.")
        except ValueError:
            print("Invalid! Please enter a number only.")
        else:
            break
    return menuInput

# adding an element
def addNumber():
    numberAdd = int(input("Enter the number you want to add: "))
    list.append(numberAdd)
    print("The element has been added.")
    print(f"This is the new array. Array = {list}")

# inserting an element
def insertNumber():
    numberInsert = int(input("Enter the number you want to insert: "))
    indexInsert = int(input(f"Enter the index you want to insert {numberInsert}: "))
    list.insert(indexInsert, numberInsert)
    print("The element has been inserted.")
    print(f"This is the new array. Array = {list}")

def modifyElement():
    indexModify = int(input("Enter the index you want to modify: "))
    numberModify = int(input(f"Enter the number you want to change in index {indexModify}: "))
    list[indexModify] = numberModify
    print("The element has been modified.")
    print(f"This is the new array. Array = {list}")

# deleting an element based on the user's inputted index
def deleteElement():
    indexDelete = int(input("Enter the index you want to delete: "))
    list.pop(indexDelete)
    print("The element has been deleted.")
    print(f"This is the new array. Array = {list}")

# arranging elements in ascending order
def ascendingOrderElements():
    list.sort()
    print("The list has been arranged in ascending order.")
    print(f"This is the new array. Array = {list}")

def descendingOrderElements():
    list.sort(reverse=True)
    print("The list has been arranged in descending order.")
    print(f"This is the new array. Array = {list}")

# main program
def startProgram ():
    menu = askMenuInput()
    if menu == 1:
        addNumber()
    elif menu == 2:
        insertNumber()
    elif menu == 3:
        modifyElement()
    elif menu == 4:
        deleteElement()
    elif menu == 5:
        ascendingOrderElements()
    elif menu == 6:
        descendingOrderElements()
def startAgain():
    while True:
        tryAgainInput = input("Do you want to try again? Y/N: ")
        tryAgain = tryAgainInput.upper()
        if tryAgain == "Y":
            print("\n")
            startProgram()
        elif tryAgain == "N":
            print("-----------------------------")
            print("Goodbye! Hope you enjoy learning array methods!")
            break
        else:
            print("\nEnter Y if you want to start again, or N to exit the program.")

print("Welcome to the program of Array Methods")
print("----------------------------------------")
startProgram()
startAgain()