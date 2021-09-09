# Students_Information_Management_System

     Students_Information_Management




HYPOTHALAMUS
This is the main commanding part of the program. It consists of a loop which runs the program until the user successfully exits it.

1)	New Registrations
2)	Search
3)	Update
4)	Display
5)	Exit




HINDBRAIN
This is the part of the program which consists of the main functions (containing the other functions of the program ) of the program which is responsible for cleanliness and smooth functioning of the program.

1)	new_registration() : handles the entering of data by the user
2)	search() : searches and displays the data on the users command
3)	update() : modifies or deletes the data on the user command
4)	display() : displays the desired data on the user command
5)	exits() : takes the user out of the program and also takes feedback and ratings


MOTOR_CORTEX
This part of the program consists of the several functions which are responsible for the functioning of the program. It has all the basic functions which are the building blocks of the program.

1)	clean() : It cleans the terminal
2)	h_line() : it creates a line
3)	space_2() : creates a space of 2 lines
4)	space_3() : creates a space of 3 lines
5)	sub_details() : asks for the user to enter the basic data about the student 
6)	details() : takes the complete data of the student and stores in a file
7)	display_data() : it displays the required data according to the user
8)	modify() : it modifies the data according to the user
9)	feedback() : it takes feedback from the user and saves it
10)	ratings() : it takes ratings from the user and replies them according to their rating




HIPPOCAMPUS

This part of the program contains functions which are responsible for the interactions between the program and storage files.

1)	Storage(user) : it stores the data of the students in the file Data.txt
2)	Inlist(adm_no) : it checks if the admission no. entered by the user is present in the file Data.txt or not
3)	randf_storage(fb_data) : it stores the data of the feedback and ratings given by the user in the file Ratings_and_feedbacks.txt
4)	deletion_storage(d_data) : it stores the deleted details of the students in the file Deleted_files.txt
5)	delete(adm_no) : it deletes the details of the students according to the admission no. given by the user
