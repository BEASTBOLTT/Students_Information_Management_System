"""


It is the Hippocampus of the program
It stores and manages the storage system of the program


"""


def storage(user):

    """
    This stores the user's data in database

    :param dict user: dictionary containing user data
    """

    with open("Data.txt", "a") as d:
        d.write(str(user) + "\n")


def inlist(adm_no):

    """


    This checks the presence of user data in database.

    :param int adm_no. : admission no. of the student

    :return bool: 0: Not present
                  1: Present


    """

    with open("Data.txt", "r") as d:
        detail = d.read()
        start_index = detail.find("{'Addmision no.': " + str(adm_no))

        if start_index == -1:
            return 0

        else:
            return 1


def randf_storage(fb_data):

    """


    It stores and manages the feedback data
    :param dict fb_data : dictionary containing feedback and ratings

    """

    with open("Ratings_and_feedback.txt", "a") as fd:
        fd.write(str(fb_data) + "\n")


def deletion_storage(d_data):

    """


    It stores and manages the deleted data
    :param dict d_data : dictionary containing deleted data

    """

    with open("Deleted_files.txt", "a") as df:
        df.write(str(d_data) + "\n")


def delete(adm_no):

    """

    This deletes the student's data from database.

    :param int adm_no: admission no. of student

    """

    with open("Data.txt", "r") as d:
        data = d.read()
        start_index = data.find("{'Addmision no.': " + str(adm_no))
        end_index = data.find("}", start_index)
        delete_data = eval(data[start_index : end_index + 1])
        deletion_storage(delete_data)

    with open("Data.txt", "r") as d:
        all_data = d.readlines()

    with open("Data.txt", "w") as d:
        for line in all_data:
            start_i = line.find(":") + 1
            end_i = line.find(",", start_i)
            if int(line[start_i:end_i]) == adm_no:
                continue
            else:
                d.write(line)
