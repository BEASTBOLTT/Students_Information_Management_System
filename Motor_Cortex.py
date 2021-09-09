"""

This is the Motor Cortex Of the Program
It executes the functions of the program

"""


from Hippocampus import *


def clean():

    """

    cleans the terminal for a clear running of the program

    """

    print("\n" * 20)


def h_line():

    """

    It makes a line

    """

    print("-x-" * 15)


def space_2():

    """

    It gives a space of 2 lines

    """

    print("\n\n")


def space_3():

    """

    It gives a space of 3 lines

    """

    print("\n\n\n")


Fields = ["Addmision no.", "Name", "Phone no.", "Address", "Email id"]


def sub_details(adm_no):
    name = input("\nEnter the name of the student : ")
    phone_no = input("\nEnter the Phone no. : ")
    address = input("\nEnter the address : ")
    email_id = input("\nEnter the email Address : ")
    student_details = {
        "Addmision no.": adm_no,
        "Name": name,
        "Phone no.": phone_no,
        "Address": address,
        "Email id": email_id,
    }
    return student_details


def details():

    clean()

    h_line()

    space_3()

    """

    Entering the data of the students
    
    """

    adm_no = int(input("Enter the admission no. : "))
    try:
        uniqueness = inlist(adm_no)
    except FileNotFoundError:
        uniqueness = 0
    if uniqueness == 1:
        space_2
        print("This data is already present in the list !!!!")
        space_2
        print("Try again...")
        return
    else:
        name = input("\nEnter the name of the student : ")
        phone_no = input("\nEnter the Phone no. : ")
        address = input("\nEnter the address : ")
        email_id = input("\nEnter the email Address : ")

    """

    Storing the data of the students 

    """

    student_details = {
        "Addmision no.": adm_no,
        "Name": name,
        "Phone no.": phone_no,
        "Address": address,
        "Email id": email_id,
    }
    storage(student_details)


def display_data(adm_no):

    """


    This gives the data of user if present in database.

    :param int adm_no : Admission no of the student

    :return dict: dictionary containing the user data (if present)

    :return bool: 0: Not present
                  1: Present

    """

    if inlist(adm_no):
        with open("Data.txt", "r") as d:
            text = d.read()
            start_index = text.find("{'Addmision no.': " + str(adm_no))
            end_index = text.find("}", start_index)
            student = eval(text[start_index : end_index + 1])
            return student

    else:
        message = " The data you are asking for is not present...."
        return message


def modify(adm_no):
    new_data = sub_details(adm_no)

    with open("Data.txt", "r") as d:
        data = d.read()
        start_index = data.find("{'Addmision no.': " + str(adm_no))
        end_index = data.find("}", start_index)
        old_data = eval(data[start_index : end_index + 1])

    print("Old details : \n", old_data)
    print("\n Modified details : \n", new_data)

    with open("Data.txt", "r") as d:
        all_data = d.readlines()

    with open("Data.txt", "w") as d:
        for line in all_data:
            start_i = line.find(":") + 1
            end_i = line.find(",", start_i)
            if int(line[start_i:end_i]) == adm_no:
                d.write(str(new_data))
                continue
            else:
                d.write(line)


def feedback():

    """

    Takes feedback from user
    It saves the feedback in a new file

    """

    feed_back = input("Write your feed back here : ")

    print(
        "\n \n Thank you for your feedback.... \n We will surely work upon it ( If required ....). \n \n"
    )

    return feed_back


def ratings():
    space_2()
    while True:
        print("You can rate this program on the scale of 1 to 5")
        rate = int(input("Rate this program Here : "))
        space_2()
        if rate > 5:
            print(
                " We are very happy to see you this much Happy.... \nBut remember we should never forget our limits however happy we are  ;) ..... \n so please rate us from 1 to 5  :)"
            )
            continue
        elif rate == 5:
            print(
                " OMG this is great that you loved this program so much...... \n This makes the hardwork done by the programmer/coder successfull..... \n After seeing this rating the programmer/coder will cry out of happiness"
            )
            break
        elif rate == 4:
            print(
                " Thanks for your rating...... \n We know there might be some problem which is stopping you from giving full ratings...... \n The programmer/coder will surely try to solve the problem so that next time you dont have any excuse for not giving full ratings.... \n Do give your feedback when asked to do so.... "
            )
            break
        elif rate == 3:
            print(
                " Ohhhh!! There might be some serious issue which kept you 2 points away from full rating........ \n Please dont forget to mention that serious issue when the feedback is asked..... \n the programmer/coder of this program/code is very hard working and passionate and will surely try to solve the problem......"
            )
            break
        elif rate == 2:
            print(
                " We respect your thoughts about this program...... But dont you think its too less for this wonderfull program and the precious efforts and hard work put together to make this program..... \n this will surely hurt the programmer/coder :( ......"
            )
            break
        elif rate == 1:
            print(
                " Ohh God!!!!! ...... \n Now this is too much.... \n Haven't you seen the program before rating? ...... \n you surely dont have a taste for good things .... \n this is a wonderfull program..... \n The programmer get into a severe drepression state after seeing this :.(.. ..."
            )
            break
        else:
            print(
                " Was it a mistake or are you mad..... \n It is clearly mentioned that you have to rate from 1 to 5......"
            )
            continue

    print("\n")
    return rate
