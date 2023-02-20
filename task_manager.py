# Software Engineer: RIAAN VAN DEVENTER (SN: RV22110005417)
# This was programmed for the Software Engineering BOOTCAMP
# Adjusted on 18 December 2022 from project task_manager_L1T19

# ************** L1T24 - TASK1 ASSIGNMENT **************   
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
#   ■ Either a ‘Yes’ or ‘No’ value that specifies if the task has been completed yet.
# 
# <user.txt> stores the username and password for each user that has permission to use the program (task_manager.py). 
# This text file already contains one default user that has the username, ‘admin’ and the password, ‘adm1n’. 
# The username and password for each user must be written to this file in the following format:
#   ■ The username followed by a comma, a space and then the password.
#   ■ One username and corresponding password per line.
# The program should allow your users to do the following:
#   ○ Login. 
#           The user should be prompted to enter a username and password. 
#           Valid usernames and passwords are stored in a text file called user.txt. 
#           Display an appropriate error message if the user enters a username that is not listed in user.txt 
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
#   ○ If the user admin chooses ‘r’ to register a user, the user should be prompted for the new username and password. 
#           The user should also be asked to confirm the password. 
#           If the value entered to confirm the password matches the value of the password, the username
#           and password should be written to user.txt in the appropriate format.
#           No other users are aloud to register users.
#   ○ If the user chooses ‘a’ to add a task, the user should be prompted to enter the username of the person 
#           the task is assigned to, the title of the task, a description of the task and the due date of the 
#           task. The data about the new task should be written to tasks.txt. The date on which the task is 
#           assigned should be the current date. Also assume that whenever you add a new task, the value that 
#           indicates whether the task has been completed or not is ‘No’.
#   ○ If the user chooses ‘va’ to view all tasks, display the information for each task on the screen in 
#           the format below.
#
#           Task:               Assign initial tasks
#           Assigned to:        admin
#           Date assigned:      10 Oct 2019
#           Due date:           25 Oct 2019
#           Task completed:     No
#           Task dscription:    Use task_manager.py to assign each team member with appropriate tasks
#             
#   ○ If the user chooses ‘vm’ to view the tasks that are assigned to them, only display all the tasks that have 
#           been assigned to the user, that is currently logged-in, on the screen in the format above.
#           Make sure that each task is displayed with a corresponding number which can be used to identify the task.
#           -   Allow the user to select either a specific task (by entering a number) or 
#               input ‘-1’ to return to the main menu.
#           -   If the user selects a specific task, they should be able to choose to either :
#                   * mark the task as complete or 
#                   * edit the task. 
#           -   If the user chooses to mark a task as complete, the ‘Yes’/’No’ value that
#               describes whether the task has been completed or not should be changed to ‘Yes’. 
#           -   If the user chooses to edit a task, the username of the person to whom the task 
#               is assigned or the due date of the task can be edited. 
#           -   The task can only be edited if it has not yet been completed.
#
# *****************************************************

#=========== Importing Libraries ===========
from datetime import datetime
import os.path

    # =================  Declare Functions  =====================

# ------------------> Function to validate and login the user.
def login_usr_fnc () :

    # Open file with users details.
    f_users = open ("./user.txt", "r")

    # String variable to compensate for possible bug. Reading next line (\n) into data.
    # The \n is invisible in the output file, at the same time the last password in the file, 
    # can change to password\n. The \n will be visible in a list and you can see it in a 
    # string only if you print the string content like this >content<, the < character 
    # will appear on the next line. 
    # I chose to deal with this by replacing any possible "\n" with "". 
    # If the code or file does not have this problem, then no harm done with the replace strategy.
    file_contents_str = ""

    # Declare variables to separate the username and password into 2 lists.
    file_contents_lst = []
    user_lst = []
    pw_lst = []

    # Read through the file and store data in lists.
    for line in f_users :
        # Compensate for empty lines.
        if line.strip () :
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
            if lst_idx_int == len (user_lst) - 1 :      # Remember len of list = n and end of indexes is (n - 1), so index = n will be out of range.
                break
            else :
                # Go to next username in list.
                lst_idx_int += 1

        if user_lst [lst_idx_int].lower () == login_usr_name.lower () :
            # The moment the below if statement is valid, the inner and outer while loop will exit. 
            if pw_lst [lst_idx_int] == login_usr_pw :      # Password in pw_lst is at the same index as relevant user in user_lst
                login_verified_bln = True                  # If user and password correspons to input, login is verified.
                print ("--> Welcome! You are now logged into the system.")
            # The moment the below else statement is valid, only the inner while loop will exit. 
            else : 
                print (f"--> Password for user {login_usr_name} is incorrect. Try again!\n")
        else :
            print ("--> Username not found. Try again!\n")
 
    return (login_usr_name, user_lst)

# ------------------> Function to show menu options and return option entered.
def menu_disp_fnc (login_usr_name) :
    print ()
    # Below if is to display menu for user admin with extra menu option.
    if login_usr_name == "admin" :
        print ("=========== TASK MANAGER MENU ===========\n")
        menu_opt_str = input('''Select one of the following options:\n
r \t- \tRegistering a user
a \t- \tAdding a task
va \t- \tView all tasks
vm \t- \tView my tasks
gr \t- \tGenerate Reports
dr \t- \tDisplay Reports
ds \t- \tDisplay Statistics
e \t- \tExit \n
=========================================\n
> ''').lower()
    else :
        print ("=========== TASK MANAGER MENU ===========\n")
        menu_opt_str = input('''Select one of the following options:\n
r \t- \tRegistering a user
a \t- \tAdding a task
va \t- \tView all tasks
vm \t- \tView my tasks
e \t- \tExit \n
=========================================\n
> ''').lower()
    
    # Above we formatted the menu input to lowercase to eliminate testing of multiple variances
    # Below we remove space inputs.
    menu_opt_str = menu_opt_str.replace (" ","")

    return (menu_opt_str)

# ------------------> Function to register a new user and add details to user.txt file.
def reg_user_fnc (user_lst) :
    usr_avail_bln = False

    # Keep requesting new username until the username is available.
    while usr_avail_bln == False :
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
            print ()
            print (f"--> Username {new_usr_name} is not available. Try again!")
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
            # If they are the same, add them to the user.txt file, else present a relevant message.
            if new_usr_pw == cnfrm_pw_str :
                # Open the file users.txt for append mode else we will loose our user details.
                f_users = open ("./user.txt", "a")
                f_users.write ("\n")
                f_users.write (new_usr_name + ", " + new_usr_pw)
                f_users.close ()

                # Also remember to add the details to our user list in case another user is registered.
                user_lst.append (new_usr_name)
                # We do not need to remember the password, since we wrote it in the user.txt file and 
                # and a new login will again read in the detail from the user.txt file.
            
                print ()
                print (f"--> User {new_usr_name} has been added successfully!")
            else :
                print ()
                print ("--> Passwords do not match!")

# ------------------> Function to allow a user to add a new task to task.txt file
def add_task_fnc (user_lst) :
    # Request input of the username of the person whom the task is assigned to.
    print ()
    task_usr_name = input ("Enter username of person to assign this task to : ")
    task_usr_name = task_usr_name.strip ()

    # Read through the user details to search for the username.
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
        task_contents_str = task_usr_name + ", " + task_title_str + ", " + task_desc_str  + ", " + task_assign_date + ", " + task_due_date + ", " + task_complt_str + "\n"

        # Open the file tasks.txt for append mode else we will loose our tasks details.
        f_tasks = open ("./tasks.txt", "a")
        f_tasks.write (task_contents_str)
        f_tasks.close ()

        print ()
        print (f"--> The task for user {task_usr_name} has been added successfully!")

# ------------------> Function to view tasks. If input is blank, display all tasks else 
# ------------------> for username input display user tasks only.
def view_tasks_fnc (login_usr_name = "") :
    # Open the file tasks.txt for read mode.
    f_tasks = open ("./tasks.txt", "r")
    
    # Declare a list to split file line items.
    task_contents_list = []
    # Set a boolean variable to False to test if there are any tasks for the logged in user.
    tasks_assigned_bln = False
    # Set int counter for user task displays.
    view_usr_int = 0
    # Set into counter for all task displays.
    view_all_int = 0 

    for line in f_tasks :
        # Compensate for blank lines.
        if line.strip () :
            # Making provision for possible next line read errors.
            task_contents_str = line.replace ("\n","")

            # Split data parts separated with ", "
            task_contents_list = task_contents_str.split (", ")
        
            # Keep track of number of task displays.
            if task_contents_list [0].lower () == login_usr_name.lower () :
                view_usr_int += 1
                task_num_cnt = view_usr_int
            elif login_usr_name == "" :
                view_all_int += 1
                task_num_cnt = view_usr_int

            # Note to reviewer: Tested below print and not getting any index error on my side, 
            #                   at the same time I compensated for possible empty lines 
            #                   by reading only "if line.strip () :" (line does not consist of only spaces)
            # Print the data in a user-friendly manner.
            if task_contents_list [0].lower () == login_usr_name.lower () or login_usr_name == "" :
                print ("-----------------------------------------------------------------------------")
                print (f"Task Number :\t\t {task_num_cnt}")
                print (f"Task:\t\t\t {task_contents_list [1]}")
                print (f"Assigned to:\t\t {task_contents_list [0]}")
                print (f"Date assigned:\t\t {task_contents_list [3]}")
                print (f"Due date:\t\t {task_contents_list [4]}")
                print (f"Task completed:\t\t {task_contents_list [5]}")
                print (f"Task description:\t {task_contents_list [2]}")

                # Set a boolean to indicate that at least 1 task was printed.
                tasks_assigned_bln = True

    f_tasks.close ()

    if tasks_assigned_bln == True :
        print ("-----------------------------------------------------------------------------")
    elif login_usr_name == "" :
        print (f"--> There are no tasks assigned.")
    else :
        print (f"--> There are no tasks assigned to user {login_usr_name}.")

    # Return the number of tasks displayed.
    return (task_num_cnt)

# ------------------> Function to edit tasks. Input is login_usr_name & number of tasks displayed.
def edit_tasks_fnc (login_usr_name, view_usr_int, user_lst) :

    # ---------------  Read the tasks from file tasks.txt -------------------------------
    
    # Open the file tasks.txt for read mode.
    f_tasks = open ("./tasks.txt", "r")
    
    # Declare a list to split file line items.
    task_contents_list = []
    usr_tasks_lst = []
    all_tasks_lst = []
    read_cnt_int = 0

    for line in f_tasks :
        # Only read lines with data; no empty lines.
        if line.strip () :
            # Store all task lines in list
            all_tasks_lst.append (line)

            # Split data parts separated with ", " to identify user.
            task_contents_list = line.split (", ")
            # We must remember to add \n again before we write tje usr_tasks back to the file. 
            task_contents_list [-1] = task_contents_list [-1].replace ("\n", "")

            # Store user tasks and keep track of index in all_tasks_lst.
            if task_contents_list [0].lower () == login_usr_name.lower () :
                # Store the user task line in list usr_tasks_lst after we added the index of all_task_lst
                task_contents_list.append (read_cnt_int)
                usr_tasks_lst.append (task_contents_list)

            # Prepare counter for next read.
            read_cnt_int += 1

    f_tasks.close ()

    # ---------------  End of reading file tasks.txt -------------------------------

    edit_opt_int = 0
    
    # Loop while until user choose to see main menu.
    # We will make all the updates in usr_tasks_lst until user choose to exit updates.

    # We must keep track if any updates has been done as to not update the tasks.txt file without reason.
    task_updated_bln = False

    while edit_opt_int != -1 :
        print ()
        edit_opt_int = int (input ("--> Enter a task number to edit task OR enter -1 to return to menu! > "))
        chg_opt_str = ""

        # Edit for valid task number.
        if edit_opt_int > 0 and edit_opt_int <= view_usr_int :
            print ()
            chg_opt_str = input('''Select one of the following options:\n
c \t- \tMark task as (c)omplete
u \t- \tChange task assigned to (u)sername
d \t- \tChange task (d)ue date
t \t- \tChoose a different (t)ask number\n
=========================================\n
> ''').lower()
        
        # Do to Mark task as (c)omplete
        if chg_opt_str == "c" :
            # The index for the chosen task will be [task number - 1]. The task completion status is at index 5 in layout.
            usr_tasks_lst [edit_opt_int - 1] [5] = "Yes"
            task_updated_bln = True
            print ()
            print (f"--> Task number {edit_opt_int} has been marked as complete.")

        # Do to Change task assigned to (u)sername
        if chg_opt_str == "u" :
            if usr_tasks_lst [edit_opt_int - 1] [5] != "Yes" :
                # Request input of the username of the person whom the task is assigned to.
                print ()
                task_usr_name = input ("Enter username of person to assign this task to : ")
                task_usr_name = task_usr_name.strip ()

                # Read through the user details to search for the username.
                lst_idx_int = 0
                while user_lst [lst_idx_int].lower () != task_usr_name.lower () :
                    # Below if statement is to prevent an index out of range error for the while condition.
                    if lst_idx_int == len (user_lst) - 1 :      # Remember len of list = n and end of index is (n - 1), so index = n will be out of range.
                        break
                    else :
                        # Go to next username in list.
                        lst_idx_int += 1

                # Set boolean if the username exists or not.
                if user_lst [lst_idx_int].lower () == task_usr_name.lower () :
                    usr_tasks_lst [edit_opt_int - 1] [0] = task_usr_name
                    print ()
                    print (f"--> Task number {edit_opt_int} is now assigned to {task_usr_name}.")
                    task_updated_bln = True    
                else :
                    print ()
                    print (f"--> Username {task_usr_name} does not exist. Try again!\n")
            else :
                print ()
                print ("--> The task is marked as complete and cannot be changed.")

        # Do to Change task (d)ue date
        if chg_opt_str == "d" :
            if usr_tasks_lst [edit_opt_int - 1] [5] != "Yes" :
                # Request the due date for the task.
                print ()
                usr_tasks_lst [edit_opt_int - 1] [4] = input ("Enter the due date for the task (e.g. 10 Oct 2022): ")
                # We can add testing for a valid date here if required.
                print ()
                print (f"--> Task number {edit_opt_int} due data was changed to {usr_tasks_lst [edit_opt_int - 1] [4]}.")
                task_updated_bln = True
            else:
                print ()
                print ("--> The task is marked as complete and cannot be changed.")

        # Code will repeat while (asking for task number) until -1 is entered, so t will also ask for different task.                
        if chg_opt_str == "t" :
            pass 

    # When we come out of the while, write changes to file tasks.txt if there were any changes.
    if task_updated_bln == True :

        # Update the all_tasks_lst with changes made to usr_tasks_lst
        # We know that the value input to this function named view_usr_int tells us how many tasks there are for this user.
        for i in range (0, (view_usr_int)) :

            # The instance [i] in usr_tasks_lst [last value in list] is the index in all_tasks_lst that we stored.
            all_tasks_idx = usr_tasks_lst [i][-1]

            # Since we added the index value to the usr_tasks_lst, we now want to exclude it to get the original string.
            del usr_tasks_lst [i][-1]

            # Also remember to add the next line character that we removed previously.
            all_tasks_lst [all_tasks_idx] = ", ".join (usr_tasks_lst [i]) + "\n"        
        
        # Now that our all_tasks_lst is update, we can write all the lines to our tasks.txt file.

    # ---------------  Write the tasks to file tasks.txt -------------------------------

        # Open the file tasks.txt for writing mode. This will overwrite the previous  data.
        f_tasks = open ("./tasks.txt", "w")

        for i in range (0, len (all_tasks_lst)) :
            # Write the all_tasks_lst items to the file.
                f_tasks.write (all_tasks_lst [i])

        f_tasks.close ()
 
    # Nothing to return.
    return ()

# ------------------> Function to Generate Reports
def gen_reports_fnc () :
    # ---> Retrieve and store all the data needed.
    # Data needed from tasks.txt is:
    ''' -   total_tasks + per user
        -   total_complete + per user
        -   total_incomplete + per user
        -   total_late_tasks + per user - due date < today
    '''
    # To simplify our logic, we will just deal with the total over all users, as if the total is just another user.
    # So total over all users is a user named total.

    # Open the file tasks.txt for read mode.
    f_tasks = open ("./tasks.txt", "r")
    
    # Declare a nested dictionary to store user stats.
    # Just for fun, since we can use double or single quotes for strings, where possible 
    # I will use double quotes for outer keys and single quotes for inner keys just for easier readability.
    # Referenced https://stackoverflow.com/questions/16333296/how-do-you-create-nested-dict-in-python
    usr_stats_ndict = {}

    # Store today's date to use for past due date tasks. Only date portion of datetime stored.
    date_now_date = datetime.now().date()
 
    for line in f_tasks :
        # Only process lines with data.
        if line.strip() :
            # Create or update sub dictionary to keep track of task totals for all users.
            if 'total' in usr_stats_ndict.keys () : 
                usr_stats_ndict ["total"]['tasks'] += 1
            else :
                usr_stats_ndict ["total"] = {'tasks': 1, 'compl': 0, 'incompl': 0, 'late': 0}

            # Split data parts separated with ", " to identify user.
            task_contents_list = line.split (", ")
            # task_contents_list [-1] stores the last value in the line and the value should end with \n.
            task_contents_list [-1] = task_contents_list [-1].replace ("\n", "")

            # Create or update sub dictionary to keep track of task totals for current user.
            # task_contents_list [0] stores the username.
            if task_contents_list [0] in usr_stats_ndict.keys () : 
                usr_stats_ndict [task_contents_list [0]]['tasks'] += 1
            else :
                usr_stats_ndict [task_contents_list [0]] = {'tasks': 1, 'compl': 0, 'incompl': 0, 'late': 0}

            # If the task is completed, add 1 to compl stats.
            if task_contents_list [-1] == "Yes" :
                usr_stats_ndict ["total"]['compl'] += 1
                usr_stats_ndict [task_contents_list [0]]['compl'] += 1
            # If the task is not completed, add 1 to incompl stats.
            else :
                usr_stats_ndict ["total"]['incompl'] += 1
                usr_stats_ndict [task_contents_list [0]]['incompl'] += 1          

                # If the task is not completed and overdue, add 1 to late stats.

                # ---------------------- Prepare Due Date ----------------------------
                # Get due date 
                date_tst_lst = task_contents_list [4].split ()
                # For date example 10 Oct 2019, date_tst_lst [1] will be the month portion after the split ().
                # Referenced https://stackoverflow.com/questions/3418050/how-to-map-month-name-to-month-number-and-vice-versa
                
                # Replace mmm with month number integer in date_tst_lst
                date_tst_lst [1] = datetime.strptime(date_tst_lst [1], '%b').month
                
                # Build date string
                due_date_str = (str (date_tst_lst [0]) + "-" + str (date_tst_lst [1]) + "-" + str (date_tst_lst [2]))
                
                # Cast to datetime type to only store the date.
                date_due_date = (datetime.strptime(due_date_str, '%d-%m-%Y')).date()
                # ---------------------- Due Date Format Ready -------------------------

                if date_due_date < date_now_date :
                    usr_stats_ndict ["total"]['late'] += 1
                    usr_stats_ndict [task_contents_list [0]]['late'] += 1   

    f_tasks.close ()

    # Data needed from user.txt is:
    ''' -   total_usr_int       '''

    # Open the file user.txt for read mode.
    f_user = open ("./user.txt", "r")
    
    total_usr_int = 0

    for line in f_user :
        if line.strip():
            total_usr_int += 1
   
    f_user.close ()

    # ---> All needed data now retrieved and stored. 

    # ---> Now we will write the task_overview report. 
    '''
    o task_overview.txt should contain:

    ▪ The total number of tasks. - Count reads from tasks.txt
    ▪ The total number of completed tasks. - Count Yes
    ▪ The total number of incompleted tasks. - Count No
            ▪ The total number of tasks that haven't been completed and that are overdue.
                    - Make date readable and count date < than today
    ▪ The percentage of tasks that are incomplete. - (Count No / Count reads) * 100
    ▪ The percentage of tasks that are overdue. - (overdue / count No) * 100
    '''

    # Open the file task_overview.txt for writing mode. This will overwrite any previous report.
    f_task_reprt = open ("./task_overview.txt", "w")

    f_task_reprt.write (f"================ TASK OVERVIEW - PREPARED DATE : {date_now_date} ================\n")
    f_task_reprt.write ("\n")

    f_task_reprt.write (f"The total number of tasks :\t\t\t {usr_stats_ndict ['total']['tasks']}\n")
        
    f_task_reprt.write (f"The total number of completed tasks :\t\t {usr_stats_ndict ['total']['compl']}\n")
    
    f_task_reprt.write (f"The total number of incompleted tasks :\t\t {usr_stats_ndict ['total']['incompl']}\n")
    
    f_task_reprt.write (f"The total number of overdue tasks :\t\t {usr_stats_ndict ['total']['late']}\n")
    
    f_task_reprt.write (f"The percentage of tasks that are incomplete :\t {((usr_stats_ndict ['total']['incompl'] / usr_stats_ndict ['total']['tasks']) * 100):.2f} %\n")
    
    f_task_reprt.write (f"The percentage of incomplete tasks overdue :\t {((usr_stats_ndict ['total']['late'] / usr_stats_ndict ['total']['incompl']) * 100):.2f} %\n")
    f_task_reprt.write ("\n")

    f_task_reprt.write (f"============================================================================")

    f_task_reprt.close ()
 
    # ---> Now we will write the user_overview report. 
    '''
    o user_overview.txt should contain:
    
    ▪ The total number of users. - Count reads from user.txt
    ▪ The total number of tasks. - Count reads from tasks.txt
    ▪ For each user also describe:
        ▪ The total number of tasks assigned to that user. Count specific user tasks.
        ▪ The percentage of the total number of tasks that have been assigned to that user. (tasks for user / total tasks) * 100
        ▪ The percentage of the tasks assigned to that user that have been completed (user completed / tasks for user) * 100
        ▪ The percentage of the tasks assigned to that user that must still be completed (user incomplete / tasks for user) * 100
        ▪ The percentage of the tasks assigned to that user that have not yet been completed and are overdue (user overdue / tasks for user) * 100
    '''
    
    # Open the file task_overview.txt for writing mode. This will overwrite any previous report.
    f_user_reprt = open ("./user_overview.txt", "w")

    f_user_reprt.write (f"=============== USER OVERVIEW - PREPARED DATE : {date_now_date} ==============\n")
    f_user_reprt.write ("\n")
    
    f_user_reprt.write (f"The total number of users :\t\t\t {total_usr_int}\n")
    f_user_reprt.write (f"The total number of tasks :\t\t\t {usr_stats_ndict ['total']['tasks']}\n")
    f_user_reprt.write ("\n")

    # Use a for loop to print the stats for each user.
    for user_key in usr_stats_ndict :

        # We already printed the total stats in the task_overview report. Here we will only print the user individual stats.
        if user_key != "total" :

            f_user_reprt.write (f"----------------------- OVERVIEW for user {user_key} -------------------------\n")
            f_user_reprt.write ("\n")
            
            f_user_reprt.write (f"The assigned number of tasks :\t\t\t {usr_stats_ndict [user_key]['tasks']}\n")
            
            f_user_reprt.write (f"The percentage of total number of tasks :\t {((usr_stats_ndict [user_key]['tasks'] / usr_stats_ndict ['total']['tasks']) * 100):.2f} %\n")
            
            f_user_reprt.write (f"The percentage of tasks that are completed :\t {((usr_stats_ndict [user_key]['compl'] / usr_stats_ndict [user_key]['tasks']) * 100):.2f} %\n")
            
            f_user_reprt.write (f"The percentage of tasks that are incomplete :\t {((usr_stats_ndict [user_key]['incompl'] / usr_stats_ndict [user_key]['tasks']) * 100):.2f} %\n")
            
            f_user_reprt.write (f"The percentage of incomplete tasks overdue :\t {((usr_stats_ndict [user_key]['late'] / usr_stats_ndict [user_key]['incompl']) * 100):.2f} %\n")
            f_user_reprt.write ("\n")

    f_user_reprt.write (f"=========================================================================")        
    f_user_reprt.close ()
 
    print ()
    print ("--> Reports have been generated successfully!")

    # Nothing to return.
    return ()

# ------------------> Function to Display Reports
def disp_reports_fnc () :

    # If files exist, continue else generate reports.
    # Referenced https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
    if os.path.exists ("./task_overview.txt") and os.path.exists ("./user_overview.txt"):
        pass
    else :
        # To call a function from a function, the function you call must be above the function you are calling from.
        gen_reports_fnc ()

    # Open the file task_overview.txt for read mode.
    f_task_reprt = open ("./task_overview.txt", "r")

    print ()
    for line in f_task_reprt :
        if line.strip () :
            print (line)

    f_task_reprt.close ()
                
    # Open the file user_overview.txt for read mode.
    f_user_reprt = open ("./user_overview.txt", "r")

    print ()
    for line in f_user_reprt :
        if line.strip () :
            print (line)

    f_user_reprt.close ()

    # Nothing to return.
    return ()    

# ------------------> Function to Display Statistics
def disp_stats_fnc () :
    # Open the file tasks.txt for read mode and count the lines.
    task_cnt_int = 0
    f_tasks = open ("./tasks.txt", "r")

    for line in f_tasks :
        if line.strip () :
            task_cnt_int += 1

    f_tasks.close ()
                
    # Open the file user.txt for read mode and count the lines.
    user_cnt_int = 0
    f_user = open ("./user.txt", "r")

    for line in f_user :
        if line.strip () :
            user_cnt_int += 1

    f_user.close ()
        
    # Print the data in user-friendly manner
    print ()
    print ("------------------------- STATISTICS FOR TASK MANAGER -----------------------\n")
    print (f"Total Tasks:\t\t {task_cnt_int}\n")
    print (f"Total Users:\t\t {user_cnt_int}\n")
    print ("-----------------------------------------------------------------------------")

# =================  End of Function Declarations  =====================

# =================  START PROGRAM LOGIC HERE  ====================

# Call the function login_usr_fnc and return validated logged in user and the 
# user list to use for menu option -r-.
login_return_lst = login_usr_fnc ()

# Bring returned values internal for easy referencing.
login_usr_name = login_return_lst [0]
user_lst = login_return_lst [1]

# Now that the login is validated, we can present the user with a menu.
# We will display the menu until a valid option is presented.
while True :
    # Display relevant menu and return option.
    menu_opt_str = menu_disp_fnc (login_usr_name)

    # Only admin to register new users.
    if menu_opt_str == 'r' and login_usr_name == "admin" :
        print ()
        print ("You chose option -r-")

        # Call the function to register the new user
        reg_user_fnc (user_lst)

    # Display message to unauthorized users not being able to register new users. 
    elif menu_opt_str == 'r' : 
        print ()
        print ("You are not authorized to register new users!")

    # Deal with menu option -a-
    elif menu_opt_str == 'a':
        print ()
        print ("You chose option -a-")
        
        # Call the function to add a task to assigned user.
        add_task_fnc (user_lst)

    # Deal with menu option -va-
    elif menu_opt_str == 'va':
        print ()
        print ("You chose option -va-")

        # Call the function to view tasks and leave input blank to show all tasks.
        view_tasks_fnc ()

    # Deal with menu option -vm-
    elif menu_opt_str == 'vm':
        print ()
        print ("You chose option -vm-")

        # Call the function to view tasks and input login user name to show only user tasks. 
        # Return number of tasks displayed in integer value.
        view_usr_int = view_tasks_fnc (login_usr_name)

        # if any tasks were displayed, give the option to edit the tasks.
        if view_usr_int != 0 :
            edit_tasks_fnc (login_usr_name, view_usr_int, user_lst)

    # Additional menu option -gr- for admin user.
    elif menu_opt_str == 'gr' and login_usr_name == "admin" :
        print ()
        print ("You chose option -gr-")

        # Call the function to generate reports.
        gen_reports_fnc ()

# Additional menu option -dr- for admin user.
    elif menu_opt_str == 'dr' and login_usr_name == "admin" :
        print ()
        print ("You chose option -dr-")

        # Call the function to display reports.
        disp_reports_fnc ()

    # Additional menu option -ds- for admin user.
    elif menu_opt_str == 'ds' and login_usr_name == "admin" :
        print ()
        print ("You chose option -ds-")

        # Call the function to display statistics.
        disp_stats_fnc ()

    # Greet and exit program for menu option -e-
    elif menu_opt_str == 'e':
        print ()
        print ('--> Goodbye!!!\n')
        exit ()

    # Handle invalid menu options.
    else:
        print ()
        print ("You did not choose a valid option. Please try again!\n")

# End While loop - Will only exit menu if option -e- is chosen from menu.

# =================  END PROGRAM LOGIC HERE  ====================