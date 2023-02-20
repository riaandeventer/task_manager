# Managing Worker Tasks

This program is for a small business that can help it to manage tasks assigned to each member of the team. 
This program will work with two text files, user.txt for access management and tasks.txt to keep track of the tasks.

## Description

<tasks.txt> stores a list of all the tasks that the team is working on. This text file already contains data about two tasks. 
The data for each task is stored on a separate line in the text file. 

Each line includes the following data (separated by a comma and space) about a task in this order:
* The username of the person to whom the task is assigned.
* The title of the task.
* A description of the task.
* The date that the task was assigned to the user.
* The due date for the task.
* Either a ‘Yes’ or ‘No’ value that specifies if the task has been completed yet.

<user.txt> stores the username and password for each user that has permission to use the program (task_manager.py). 
This text file already contains one default user that has the username, ‘admin’ and the password, ‘adm1n’. 

The username and password for each user must be written to this file in the following format:
* The username followed by a comma, a space and then the password.
* One username and corresponding password per line.

The program allows users to do the following:

* Login. 

The user is prompted to enter a username and password. Valid usernames and passwords are stored in text file user.txt. 
An appropriate error message is displayed if the user enters a username that is not listed in user.txt or enters a valid username but not a valid password. 
The user is repeatedly asked to enter a valid username and password until they provide appropriate credentials.

![Main Menu](/images/login.jpg)

A menu is displayed once the user has successfully logged in.

## Table of Content
1. Installation
2. Executing Program
3. Authors

### Dependencies

* This program uses the tabulate function.

### Installation

### 1.  Implementing the program in a virtual environment.

##### 1.1   Dependencies

The virtual environment requires the installation of python & tabulate.

##### 1.2   Copying Files

Go to the directory or folder where you want to install the project and enter the following command in the command line:
```
>git clone https://github.com/riaandeventer/task_manager
```
If you are asked for a login then it should be because you might have made a typing error with the link.

##### 1.3   Run Program

If your files copied successfully, there should be a folder task_manager when you (for windows) enter the >dir command.
Go to this directory with below command.
```
>cd task_manager
```
Now we can run the program with below command:
```
>python task_manager.py
```
### Executing Program

* Run the program
* You will see the menu.

![Main Menu](/images/menu.jpg)

* Menu Option r: Register a user, the user is prompted for the new username and password. The user is asked to confirm the password.   
      If the value entered to confirm the password matches the value of the password, the username and password is written to user.txt 
      in the appropriate format. No other users are aloud to register users.
      
* Menu Option a: Add a task, the user is prompted to enter the username of the person the task is assigned to, 
    the title of the task, a description of the task and the due date of the task. The data about the new task is written to tasks.txt. 
    The date on which the task is assigned is the current date. Whenever you add a new task, the value that indicates whether 
    the task has been completed or not is ‘No’.
    
* Menu Option va: View all tasks, display the information for each task on the screen in the format below.

    Task:               Assign initial tasks
    Assigned to:        admin
    Date assigned:      10 Oct 2019
    Due date:           25 Oct 2019
    Task completed:     No
    Task dscription:    Use task_manager.py to assign each team member with appropriate tasks
    
* Menu Option vm: View the tasks that are assigned to them, only display all the tasks that have been assigned to the user, 
    that is currently logged-in, on the screen in the format above.
    Each task is displayed with a corresponding number which can be used to identify the task.
    -   The user can select either a specific task (by entering a number) or input ‘-1’ to return to the main menu.
    -   If the user selects a specific task, they can choose to either mark the task as complete or edit the task. 
    -   If the user chooses to mark a task as complete, the ‘Yes’/’No’ value that
        describes whether the task has been completed or not should be changed to ‘Yes’. 
    -   If the user chooses to edit a task, the username of the person to whom the task is assigned or the due date of the task can be edited. 
    -   The task can only be edited if it has not yet been completed.
    
* Menu Option gr: This is an option for __admin__ only. This option generates a task overview and writes it to file ![task_overview.txt](/task_overview.txt) and
      it also generates a total and per user overview of their task completion and writes it to file ![user_overview.txt](/user_overview.txt).
      
* Menu Option dr: This is an option for __admin__ only. This option displays the reports generated with Option gr.

* Menu Option ds: This is an option for __admin__ only. This option displays the total tasks and total users.

* Menu Option e: Search for books with below menu.

## Authors

Riaan Deventer  - [LinkedIn: @riaandeventer](https://www.linkedin.com/in/riaandeventer/)
