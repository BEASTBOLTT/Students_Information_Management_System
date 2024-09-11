"""

This is the Hindbrain of the program
It tells the system how to execute the functions

"""

from Motor_Cortex import *
from Hippocampus import *


def new_registration():

    clean()

    h_line()

    space_3()

    """
    
     To check for the no.of entries to be made

     """

    loop = int(input("How many entries are to be made : "))

    x = 1

    while x < loop or x == loop:
        details()

        if x == 1:
            space_3()
            print(" One entry successfully made !!!!!")

        elif x == 0:
            space_3()
            print("\n \n \n One more entry successfully made !!!!!")

        x = x + 1


def search():

    clean()

    h_line()

    space_3()

    """
    
    This function is used to search for a required data asked by the user
    
    """

    adm_no = int(
        input("Enter the admission no. of the student whose info is to be searched : ")
    )
    if inlist(adm_no):
        space_3()
        print("The required data is present.\n Do you want to display it ?")
        space_2()
        display_confirmation = int(input("Press 1 for yes and 0 for no : "))
        if display_confirmation == 1:
            result = display_data(adm_no)
            space_2()
            print("The search result : \n", result)
        elif display_confirmation == 0:
            space_2()
            print("Ok")
            return
        else:
            space_2()
            print("Invalid Input !!!")

    else:
        space_3()
        print("The required detail is not present.")


def update():

    """

    This function is used the update the database
    It can delete the data from the database
    it can modify the existing details of the students

    """

    adm_no = int(
        input(
            "Enter the admission number of the student whose data is to be modified : "
        )
    )

    if inlist(adm_no):
        print(
            "1) Delete the existing data from the database \n2) Modify the existing data of the student "
        )
        answer = int(input("Enter your option number here : "))

        if answer == 1:
            delete(adm_no)
            print("\nSUCCESS ...... \nThe data is deleted from the database")
        elif answer == 2:
            modify(adm_no)
            print("\nSUCCESS ....... \nThe details are modified ")
        else:
            print("Invalid Input!!!")
    else:
        print("The admission no. does not exists in the database\nPlease try again")


def display():

    clean()

    h_line()

    space_3()

    """
    
    This function is used to display data 
    
    """

    print(
        "Do you want to display the whole database or the data of some specific student ?"
    )
    space_2()
    answer = int(input("Press 1 for whole database and 0 for specific student : "))

    if answer == 1:
        space_2()
        print("The database: \n")
        with open("Data.txt", "r") as d:
            print(d.read())

    elif answer == 0:
        space_3()
        adm_no = int(input("Enter the admission no. to display data : "))
        result = display_data(adm_no)
        space_2()
        print(result)
        space_3()

    else:
        space_3()
        print("Invalid Input !!!")


def exit():

    clean()

    h_line()

    space_3()

    """

    It controls the exit part of the program
    It also manages the feedback function presentation
    
    """

    while True:
        print(" Are you sure you want to exit ?")

        space_2()
        exit_confirmation = int(input("Press 1 for yes and 0 for no : "))

        if exit_confirmation == 1:

            space_2
            randf_name = input("Enter your name : ")

            while True:
                space_3()
                print("Would you like to mention some feedback ? ")

                space_2()
                feedback_confirmation = int(input("Press 1 for yes and 0 for no : "))

                if feedback_confirmation == 1:
                    f_d = feedback()

                    while True:
                        print("would you like to give ratings ?")
                        ratings_confirmation = int(
                            input("Press 1 for yes and 0 for no : ")
                        )
                        if ratings_confirmation == 1:
                            r_d = ratings()
                            randf_data = {
                                "Name": randf_name,
                                "Ratings": r_d,
                                "Feedback": f_d,
                            }
                            randf_storage(randf_data)
                            break
                        elif ratings_confirmation == 0:
                            space_2()
                            print("Ok no problem...")
                            randf_data = {
                                "Name": randf_name,
                                "Ratings": "Not given",
                                "Feedback": f_d,
                            }
                            randf_storage(randf_data)
                            break
                        else:
                            space_2()
                            print("Invalid Input!!")
                            continue

                    break

                elif feedback_confirmation == 0:

                    while True:
                        print("would you like to give ratings ?")
                        print("would you like to give ratings ?")
                        ratings_confirmation = int(
                            input("Press 1 for yes and 0 for no : ")
                        )
                        if ratings_confirmation == 1:
                            r_d = ratings()
                            randf_data = {
                                "Name": randf_name,
                                "Ratings": r_d,
                                "Feedback": "No feedback given",
                            }
                            randf_storage(randf_data)
                            break
                        elif ratings_confirmation == 0:
                            space_2()
                            print("Ok no problem...")
                            break
                        else:
                            space_2()
                            print("Invalid Input!!")
                            continue

                    break

                else:
                    space_3()
                    print("\n  Invalid Input !!!")
                    space_2()
                    print("\n  Try Again....")
                    continue

            return 1

        elif exit_confirmation == 0:
            space_3()
            print("\n \n Let's get back to the program then...")
            return 0

        else:
            space_3()
            print("\n \n Invalid Input !!!")
            space_2()
            print("\n \n Please try Again.....")
            continue
