# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# PYChang,11.16.2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection
strTask = ""  # Task entered
strPriority = ""  # Priority for the task
strDelete = ""  # Task to be deleted


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("/Users/pchang/Documents/_PythonClass/Assignment05/ToDoList.txt", 'r')
for row in objFile:
    strData = row.split(",")
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        print("Here are the current data in the ToDo list: \n")
        for row in lstTable:
            print(row["Task"] + "," + "[" + row["Priority"] + "]")
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strTask = str(input("What is the task?: ")).strip()
        strPriority = str(input("What is the priority?: ")).strip()
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        strDelete = str(input("What task do you want to delete?: "))
        for row in lstTable:
            if row["Task"] == strDelete:
                lstTable.remove(row)
                print("Task Removed")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        print("Would you like to save your data?" )
        strSaveFile = str(input("Enter 'Y' OR 'N': "))
        if strSaveFile.lower() == 'y':
            objFile = open("ToDoList.txt", "w")
            for row in lstTable:
                objFile.write(row["Task"] + "," + row["Priority"] + "\n")
            objFile.close()
            print("Data Saved to File")
        elif strSaveFile.lower() == 'n':
            print("Data Not Saved")
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        break  # and Exit the program

