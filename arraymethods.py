# Write a python program that do the following:

# - display the initial content of the array
# - display a menu of options
# - allow user to select item in the menu (check if valid)
# - perform the selected option (you may prompt additional info to user when need)
# - display the resulting values of the array

# Note: 
# - The program has an array variable containing 10 random numbers

list = [2, 4, 6, 10, 1, 3, 9, 7, 8, 5]

print("""
  Menu:
  1 -> Add an element
  2 -> Insert an element
  3 -> Modify an element
  4 -> Delete an element
  5 -> Arrange in ascending order
  6 -> Arrange in descending order
""")
print(f"Array: {list}")

# asking the user for preferred array method from the menu and validates if its from 1 to 6
while True:
    try:
        menuInput = int(input("What do you want to do? (1-6): "))
        if menuInput not in range(1, 7):
            print("Invalid! Please enter 1 to 6 only.")
    except ValueError:
        print("Invalid! Please enter a number only.")
    else:
        break

# adding an element
if menuInput == 1:
    numberAdd = int(input("Enter the number you want to add: "))
    list.append(numberAdd)
    print("The element has been added.")
    print(f"This is the new array. Array = {list}")

# inserting an element
elif menuInput == 2:
    numberInsert = int(input("Enter the number you want to insert: "))
    indexInsert = int(input(f"Enter the index you want to insert {numberInsert}: "))
    list.insert(indexInsert, numberInsert)
    print("The element has been inserted.")
    print(f"This is the new array. Array = {list}")

# modifying an element
elif menuInput == 3:
    indexModify = int(input("Enter the index you want to modify: "))
    numberModify = int(input(f"Enter the number you want to change in index {indexModify}: "))
    list[indexModify] = numberModify
    print("The element has been modified.")
    print(f"This is the new array. Array = {list}")

# deleting an element based on the user's inputted index
elif menuInput == 4:
    indexDelete = int(input("Enter the index you want to delete: "))
    list.pop(indexDelete)
    print("The element has been deleted.")
    print(f"This is the new array. Array = {list}")

# arranging elements in ascending order
elif menuInput == 5:
    list.sort()
    print("The list has been arranged in ascending order.")
    print(f"This is the new array. Array = {list}")

# arranging elements in descending order
elif menuInput == 6:
    list.sort(reverse=True)
    print("The list has been arranged in descending order.")
    print(f"This is the new array. Array = {list}")