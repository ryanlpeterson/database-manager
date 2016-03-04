#no lengths or amounts completed greater than 999

#don't ask for save if previously saved and no new changes

import sys

from Table import Table
from Record import Record

table = Table("The Fox's Collection")

table.add_item(Record("Saga", 30, 30))
table.add_item(Record("The Walking Dead", 36, 144))
table.add_item(Record("Parks and Recreation", 7, 7))
table.add_item(Record("30 Rock", 4, 7))

command = input("What would you like to do? (add, delete, write, open, exit): ")
while True:

    if command == "add":
        name = input("Name: ")
        amount_completed = int(input("Amount Completed: "))
        length = int(input("Length: "))
        table.add_item(Record(name, amount_completed, length))
    elif command == "delete":
        name = input("Name: ")
        table.delete_item(name)
    elif command == "write":
        file_name = input("File name (example.txt): ")
        table.write_to_file(file_name)
    elif command == "open":
        while True:
            save = input("Would you like to save changes? (y/n): ")
            if save == "y":
                file_name = input("File name (example.txt): ")
                table.write_to_file(file_name)
                break
            elif save == "n":
                break
            else:
                print("Sorry I don't understand.")

        file_name = input("File name (example.txt): ")
        table = Table.open_file(file_name) #for some reason combining
    elif command == "exit":
        while True:
            save = input("Would you like to save changes? (y/n): ")
            if save == "y":
                file_name = input("File name (example.txt): ")
                table.write_to_file(file_name)
                break
            elif save == "n":
                break
            else:
                print("Sorry I don't understand.")
        break
    else:
        print("Sorry I don't understand.")

    command = input("What would you like to do? (add, delete, write, open , exit): ")

print("\nSee you later!")
