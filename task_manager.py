'''
-------------------------------------   Change Log  ---------------------------------------------
| Version   | Date          | Change
-------------------------------------------------------------------------------------------------
| 1.0       | 15/12/2022    | Original Version
| 1.1       | 14/02/2023    | user.txt was changed to app-users.txt and logic adjusted to use

-------------------------------------------------------------------------------------------------
'''
# Software Engineer: RIAAN VAN DEVENTER (SN: RV22110005417)
# This was programmed for the Software Engineering BOOTCAMP
# Written on 15 December 2022

# ************** L1T19 - TASK - PART1 & PART2 ASSIGNMENT **************   
# Create a program for a small business that can help it to manage tasks assigned to each member of the team. 
# This program will work with two text files, user.txt and tasks.txt. 
#
# <tasks.txt> stores a list of all the tasks that the team is working on.
# This text file already contains data about two tasks. 
# The data for each task is stored on a separate line in the text file. 
# Each line includes the following data (separated by a comma and space) about a task in this order:
#   ■ The username of the person to whom the task is assigned.
#   ■ The title of the task.
#   ■ A description of the task.
#   ■ The date that the task was assigned to the user.
#   ■ The due date for the task.
#   ■ Either a 'Yes' or 'No' value that specifies if the task has been completed yet.
# 
# <app-users.txt> stores the username and password for each user that has permission to use the program (task_manager.py). 
# This text file already contains one default user that has the username, 'admin' and the password, 'adm1n'. 
# The username and password for each user must be written to this file in the following format:
#   ■ The username followed by a comma, a space and then the password.
#   ■ One username and corresponding password per line.
# The program should allow your users to do the following:
#   ○ Login. 
#           The user should be prompted to enter a username and password. 
#           Valid usernames and passwords are stored in a text file called app-users.txt. 
#           Display an appropriate error message if the user enters a username that is not listed in app-users.txt 
#           or enters a valid username but not a valid password. 
#           The user should repeatedly be asked to enter a valid username and password until they provide
#           appropriate credentials.
#           The following menu should be displayed once the user has successfully logged in:
#           -   Please select one of the following options :
#           -   r - register User
#           -   a - add task
#           -   va - view all tasks
#           -   vm - view my tasks
#           -   e - exit
#   ○ If the user chooses 'r' to register a user, the user should be prompted for the new username and password. 
#           The user should also be asked to confirm the password. 
#           If the value entered to confirm the password matches the value of the password, the username
#           and password should be written to app-users.txt in the appropriate format.
#   ○ If the user chooses 'a' to add a task, the user should be prompted to enter the username of the person 
#           the task is assigned to, the title of the task, a description of the task and the due date of the 
#           task. The data about the new task should be written to tasks.txt. The date on which the task is 
#           assigned should be the current date. Also assume that whenever you add a new task, the value that 
#           indicates whether the task has been completed or not is 'No'.
#   ○ If the user chooses 'va' to view all tasks, display the information for each task on the screen in 
#           the format below.
#
#           Task:               Assign initial tasks
#           Assigned to:        admin
#           Date assigned:      10 Oct 2019
#           Due date:           25 Oct 2019
#           Task completed:     No
#           Task dscription:    Use task_manager.py to assign each team member with appropriate tasks
#             
#   ○ If the user chooses 'vm' to view the tasks that are assigned to them, only display all the tasks that have 
#           been assigned to the user, that is currently logged-in, on the screen in the format above.
# *****************************************************

#=========== Importing Libraries ===========
'''This is the section where you will import libraries'''
from datetime import datetime

#=========== Login Section ===========
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the app-users.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

# Open file with users details.
f_users = open ("./app-users.txt", "r")

# String variable to compensate for possible bug. Reading next line (\n) into data.
# If you add new user to file with funtion according to instruction, 
# e.g.  f_users.write ("\n")
#       f_users.write (new_usr_name + ", " + new_usr_pw)
# The \n is invisible in the output file, at the same time the last password in the file, 
# before the above write, actually changes to password\n. The \n will be visible in a list and you can
# see it in a string only if you print the string content like this >content<, the < character 
# will appear on the next line. Any explanation will be welcome. 
# I chose to deal with this by replacing any possible "\n" with "". If the code or file does not have this
# problem, then no harm done with the replace strategy.
file_contents_str = ""

# Declare variables to separate the username and password into 2 lists.
file_contents_lst = []
user_lst = []
pw_lst = []

# Read through the file and store data in lists.
for line in f_users :
    file_contents_str = line.replace ("\n", "")
    file_contents_lst = file_contents_str.split (", ")

    user_lst.append (file_contents_lst [0])
    pw_lst.append (file_contents_lst [1])

# Since we now have the data we need stored in lists, we can close the file.
f_users.close ()

# Define a boolean to monitor if the user details have been verified or not.
login_verified_bln = False

# Run a while loop until login verification is True.
while login_verified_bln == False :

    # Request username and password from user.
    print ()
    print ("=========== TASK MANAGER LOGIN ===========\n")

    login_usr_name = input ("Username : ") 
    print ()
    login_usr_pw = input ("Password : ")
    print ()
    print ("==========================================\n")
    # Declare and set variable to read through the lists. 
    lst_idx_int = 0

    # Read through the user details until you find a match or break at the end of the list.
    while user_lst [lst_idx_int].lower () != login_usr_name.lower () :
        # Below if statement is to prevent an index out of range error for the while condition.
        if lst_idx_int == len (user_lst) - 1 :      # Remember len of list = n and end of index is (n - 1), so index = n will be out of range.
            break
        else :
            # Go to next username in list.
            lst_idx_int += 1

    if user_lst [lst_idx_int].lower () == login_usr_name.lower () :
            # The moment the below if statement is valid, the inner and outer while loop will exit. 
            if pw_lst [lst_idx_int] == login_usr_pw :           # Password in pw_lst is at the same index as relevant user in user_lst
                login_verified_bln = True                       # If user and password correspons to input, login is verified.
                print ("--> Welcome! You are now logged into the system.")
            # The moment the below else statement is valid, only the inner while loop will exit. 
            else : 
                print (f"--> Password for user {login_usr_name} is incorrect. Try again!\n")
    else :
        print ("--> Username not found. Try again!\n")

# Now that the login is validate, we can present the user with a menu.
# We will repeat the display of the menu until a valid option is presented.
while True :
    print ()
    # Part 2: Below if is to display menu for user admin with extra menu option.
    if login_usr_name == "admin" :
        print ("=========== TASK MANAGER MENU ===========\n")
        menu = input('''Select one of the following options:\n
r \t- \tRegistering a user
a \t- \tAdding a task
va \t- \tView all tasks
vm \t- \tView my tasks
s \t- \tDisplay Statistics
e \t- \tExit \n
=========================================\n
> ''').lower()
    else :
        print ("=========== TASK MANAGER MENU ===========\n")
        menu = input('''Select one of the following options:\n
r \t- \tRegistering a user
a \t- \tAdding a task
va \t- \tView all tasks
vm \t- \tView my tasks
e \t- \tExit \n
=========================================\n
> ''').lower()
    

    # Above we formatted the menu input to lowercase to eliminate testing of multiple variances
    # Below we remove space inputs.
    menu = menu.replace (" ","")

    # Part 2: The -and- portion of this if was an adjustment made for only admin to register new users.
    if menu == 'r' and login_usr_name == "admin" :
        print ()
        print ("You chose option -r-")

        # Write code to add a new user to the app-users.txt file
        
        # Request input of a new username.
        print ()
        new_usr_name = input ("New username : ")

        # Read through the user details to see if the username is available.
        lst_idx_int = 0
        while user_lst [lst_idx_int].lower () != new_usr_name.lower () :
            # Below if statement is to prevent an index out of range error for the while condition.
            if lst_idx_int == len (user_lst) - 1 :      # Remember len of list = n and end of index is (n - 1), so index = n will be out of range.
                break
            else :
                # Go to next username in list.
                lst_idx_int += 1

        # Test if the new username already exit or not.
        if user_lst [lst_idx_int].lower () == new_usr_name.lower () :
            usr_avail_bln = False
            print ()
            print (f"--> Username {new_usr_name} is not available. Try again!\n")
        else :
            usr_avail_bln = True

        # If the username is available, let user choose a password.
        if usr_avail_bln == True :
            # Request input of a password for new user.
            print ()
            new_usr_pw = input ("Password : ")

            # Request input of password confirmation.
            cnfrm_pw_str = input ("Confirm password : ")

            # Check if the new and confirmed passwords are the same.
            # If they are the same, add them to the app-users.txt file, else present a relevant message.
            if new_usr_pw == cnfrm_pw_str :
                # Open the file users.txt for append mode else we will loose our user details.
                f_users = open ("./app-users.txt", "a+")
                f_users.write ("\n")
                f_users.write (new_usr_name + ", " + new_usr_pw)
                f_users.close ()

                # Also remember to add the details to our user & password list in case another user is registered.
                user_lst.append (new_usr_name)
                pw_lst.append (new_usr_pw)

                print ()
                print (f"--> User {new_usr_name} has been added successfully!")
            else :
                print ()
                print ("--> Passwords do not match!")
    # Part 2: elif statement displays message to unauthorized users to not register new users. 
    elif menu == 'r' : 
        print ()
        print ("You are not authorized to register new users!")

    elif menu == 'a':
        print ()
        print ("You chose option -a-")

        # Write code that will allow a user to add a new task to task.txt file
        
        # Request input of the username of the person whom the task is assigned to.
        print ()
        task_usr_name = input ("Enter username of person to assign this task to : ")
        task_usr_name = task_usr_name.strip ()

        # Read through the user details to see if the username exists.
        lst_idx_int = 0
        while user_lst [lst_idx_int].lower () != task_usr_name.lower () :
            # Below if statement is to prevent an index out of range error for the while condition.
            if lst_idx_int == len (user_lst) - 1 :      # Remember len of list = n and end of index is (n - 1), so index = n will be out of range.
                break
            else :
                # Go to next username in list.
                lst_idx_int += 1

        # Test if the username exists or not.
        if user_lst [lst_idx_int].lower () == task_usr_name.lower () :
            usr_exist_bln = True        
        else :
            usr_exist_bln = False
            print ()
            print (f"--> Username {task_usr_name} does not exist. Try again!\n")

        # If the username exists, request further details.
        if usr_exist_bln == True :
            # Request a title for the task.
            print ()
            task_title_str = input ("Enter the title of the task : ")

            # Request a description for the task.
            print ()
            task_desc_str = input ("Enter a description for the task : ")

            # Get the current date and store it as the date the task was assigned.
            # See Import section for <from datetime import datetime>
            # Referenced https://stackoverflow.com/questions/61699115/b-vs-b-in-datetime-module-python-3 for the month format.
            
            task_assign_date = str (datetime.now().day) + " " + datetime.now().strftime("%b") + " " + str (datetime.now().year)

            # Request the due date for the task.
            print ()
            task_due_date = input ("Enter the due date for the task (e.g. 10 Oct 2022): ")
            # We can add testing for a valid date here if required.

            # Store 'No' as the task completion status.
            task_complt_str = "No"

            # Prepare the data format for file writing.
            task_contents_str = task_usr_name + ", " + task_title_str + ", " + task_desc_str  + ", " + task_assign_date + ", " + task_due_date + ", " + task_complt_str

            # Open the file tasks.txt for append mode else we will loose our tasks details.
            f_tasks = open ("./tasks.txt", "a+")
            f_tasks.write ("\n")
            f_tasks.write (task_contents_str)
            f_tasks.close ()

            print ()
            print (f"--> The task for user {task_usr_name} has been added successfully!")

    elif menu == 'va':
        print ()
        print ("You chose option -va-")
        print ()

        # Open the file tasks.txt for read mode.
        f_tasks = open ("./tasks.txt", "r")
    
        # Declare a list to split file line items.
        task_contents_list = []

        for line in f_tasks :
            # Making provision for possible next line read errors.
            task_contents_str = line.replace ("\n","")

            # Split data parts separated with ", "
            task_contents_list = task_contents_str.split (", ")
            
            # Print the data in user-friendly manner
            print ("-----------------------------------------------------------------------------")
            print (f"Task:\t\t\t {task_contents_list [1]}")
            print (f"Assigned to:\t\t {task_contents_list [0]}")
            print (f"Date assigned:\t\t {task_contents_list [3]}")
            print (f"Due date:\t\t {task_contents_list [4]}")
            print (f"Task completed:\t\t {task_contents_list [5]}")
            print (f"Task description:\t {task_contents_list [2]}")

        print ("-----------------------------------------------------------------------------")
        f_tasks.close ()

    elif menu == 'vm':
        print ()
        print ("You chose option -vm-")
        print ()

        # Open the file tasks.txt for read mode.
        f_tasks = open ("./tasks.txt", "r")
    
        # Declare a list to split file line items.
        task_contents_list = []
        # Set a boolean variable to False to test if there are any tasks for the logged in user.
        tasks_assigned_bln = False

        for line in f_tasks :
            # Making provision for possible next line read errors.
            task_contents_str = line.replace ("\n","")

            # Split data parts separated with ", "
            task_contents_list = task_contents_str.split (", ")
            
            # Print the data in user-friendly manner if the task is assigned to the logged in user.
            if task_contents_list [0].lower () == login_usr_name.lower () :
                tasks_assigned_bln = True
                print ("-----------------------------------------------------------------------------")
                print (f"Task:\t\t\t {task_contents_list [1]}")
                print (f"Assigned to:\t\t {task_contents_list [0]}")
                print (f"Date assigned:\t\t {task_contents_list [3]}")
                print (f"Due date:\t\t {task_contents_list [4]}")
                print (f"Task completed:\t\t {task_contents_list [5]}")
                print (f"Task description:\t {task_contents_list [2]}")

        f_tasks.close ()

        if tasks_assigned_bln == True :
            print ("-----------------------------------------------------------------------------")
        else :
            print (f"--> There are no tasks assigned to user {login_usr_name}.")
    
    # Part 2: Additional menu option for admin user.
    elif menu == 's' and login_usr_name == "admin" :
        print ()
        print ("You chose option -s-")
        print ()

        # Open the file tasks.txt for read mode and count the lines.
        task_cnt_int = 0
        f_tasks = open ("./tasks.txt", "r")

        for line in f_tasks :
            if line.strip () :
                task_cnt_int += 1

        f_tasks.close ()
                
        # Open the file app-users.txt for read mode and count the lines.
        user_cnt_int = 0
        f_user = open ("./app-users.txt", "r")

        for line in f_user :
            if line.strip () :
                user_cnt_int += 1

        f_user.close ()
        
        # Print the data in user-friendly manner
        print ("------------------------- STATISTICS FOR TASK MANAGER -----------------------\n")
        print (f"Total Tasks:\t\t {task_cnt_int}\n")
        print (f"Total Users:\t\t {user_cnt_int}\n")
        print ("-----------------------------------------------------------------------------")

    elif menu == 'e':
        print ()
        print ('--> Goodbye!!!\n')
        exit ()

    else:
        print ()
        print ("You did not choose a valid option. Please try again!\n")