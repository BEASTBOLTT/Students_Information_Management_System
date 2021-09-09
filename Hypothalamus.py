"""

This is the Hypothalamus of the program 
It Commands the program 
The Main Commanding Officer

"""


from Hindbrain import *
from Hippocampus import *
from Motor_Cortex import *


clean()
h_line()
space_2()


print(
    "Welcome to the student's information management portal  \nHow can I help you....."
)

space_2()


while True:

    h_line()

    print("\n\n1) New Registrations \n2) Search  \n3) Update  \n4) Display  \n5) Exit")

    option = int(input("Enter the option no. here : "))

    if option == 1:
        new_registration()

        space_2()
        response = input(
            "Press Enter to get back to the main menu and any other key to go to the Exit screen"
        )
        h_line()
        if response == "":
            continue

        else:
            result = exit()
            if result == 1:
                break
            else:
                continue

    elif option == 2:
        search()

        space_2()
        response = input(
            "Press Enter to get back to the main menu and any other key to go to the Exit screen"
        )
        h_line()
        if response == "":
            continue

        else:
            result = exit()
            if result == 1:
                break
            else:
                continue

    elif option == 3:
        update()

        space_2()
        response = input(
            "Press Enter to get back to the main menu and any other key to go to the Exit screen"
        )
        h_line()
        if response == "":
            continue

        else:
            result = exit()
            if result == 1:
                break
            else:
                continue

    elif option == 4:
        display()

        space_2()
        response = input(
            "Press Enter to get back to the main menu and any other key to go to the Exit screen"
        )
        h_line()
        if response == "":
            continue

        else:
            result = exit()
            if result == 1:
                break
            else:
                continue

    elif option == 5:
        result = exit()
        if result == 1:
            break
        else:
            continue

    else:
        space_2()
        print("Wrong option Selected...  \nPlease try again...\n")
        continue
