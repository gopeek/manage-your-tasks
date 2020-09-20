#import date time to get current date
from datetime import date, datetime
now = datetime.now() #assign datetime.now() to variable now
import sys #to allow the system to exit
import os #to be used to delete the user_overview file before writing to it

today = date.today() #assign today function to variable today this will be used to get the current date later on

"""
FUNCTIONS: BEGIN
"""
#function to get the username to use in reg_user function in order to validate
def get_user():#this is a function called get_user which will get the users from user.txt
      create_user_list = [] #create a list to store only the user names
      with open('user.txt','r') as my_file: #open the file user.txt as my_file
            for line in my_file: #for every line in my File
                  #e.g. admin, adm1n
                  split_username_and_password = line.strip().split(', ') #split the username and password seperatley 
                  create_user_list.append(split_username_and_password[0]) #append to the create_user_list only the usernames i.e. split_username_and_password[0]
      return create_user_list #return the create_user_list ['admin','gopeek'] etc.

#function for registering a user
def reg_user():
      user_list = get_user() #get the users from the textfile by calling get_user() and store it in user_list
      #Password_check is just a variable can can be changed to anything you wish
      password_check = False # we will need to loop for registration until the password matches
      username_check = False # we will need to loop through users.txt to check if the user exits when the user enters their username
      #register user
      while (username_check == False): #while the boolean is false this is done to keep asking for the username if the username already exists in the user_list
            enter_username = input("Enter a username ") #ask for the user name
            if enter_username in user_list:
                  print("username already exists")
                  username_check = False
            else:
                  username_check = True

      while (password_check == False):
            enter_password = input("Enter a password " ) #ask for a password
            enter_confirm_password = input("Re-enter a password ") #confirmation password
            if (username == "admin"): #only admins can update the user
                  if ((enter_password == enter_confirm_password)): #if the passwords match
                        user_file_append = open('user.txt','a+') #open the file users
                        print("user registered")
                        user_file_append.write(f"\n{enter_username}, {enter_password}") #write the username and password to the file
                        user_file_append.close() #close the file
                        password_check = True #set the password check to true
                        print_menu(username)
                  elif (enter_password != enter_confirm_password):#if passwords do not match
                        print("Passwords do not match")
                        password_check = False #password check is false so ask the user again for a username and password
            elif (username != "admin"): #if the user is not an admin user
                  print("You are not the admin only admins can register a user")
                  print_menu(username)
            #print(enter_username)
            #print(enter_password)

#function for adding a task
def add_task():
      task_user = input("Username of the person task is assigned to ")
      task_title = input("Enter the task title ")
      task_description = input("Enter a description of the task ")
      task_current_date = today.strftime("%d %b %Y") #create the date e.g. 10 Oct 2020
      task_due_date = input("Enter the task Due Date ")
      task_completion = "No"
      task_file = open("tasks.txt","a+") #append to the tasks.txt
      #write to the file
      task_file.write(f"\n{task_user}, {task_title}, {task_description}, {task_current_date}, {task_due_date}, {task_completion}")
      #close the file
      task_file.close()
      print_menu(username)
#function for viewing all tasks
def view_all():
      task_file = open("tasks.txt","r+") # open the file
      for line in task_file:# assign each value to a variable
            task_user, task_title, task_description, task_current_date, task_due_date, task_completion = line.split(", ")
            #display all tasks
            print(f"""
            User : {task_user}
            Title : {task_title}
            Task Description : {task_description}
            Task Current Date : {task_current_date}
            Task Due Date : {task_due_date}
            Task Completed : {task_completion}
            """)
      task_file.close()
      print_menu(username)

#function for printing the menu
def print_menu(username):
      if (username == "admin"): #if the user is an admin menu option will be below
            choice = input("""
            Please select one of the follwing options:
            r - register user
            a - add task
            va - view all tasks
            vm - view my tasks
            vs - view stats
            gr - generate reports
            ds - display statistics
            e - exit
            """)
      elif (username != "admin"): #if the user is not an admin print the menu option below
            choice = input("""
            Please select one of the follwing options:
            r - register user
            a - add task
            va - view all tasks
            vm - view my tasks
            e - exit
            """)

            #it is important then to set the password check to false
      if choice == "r": #choice = register
            reg_user() #call function reg_user
      elif choice == "a": #choice = add task
            add_task() #call function add_task
      elif choice == "va":#choice = view all tasks
            view_all() #call function view_all
      elif choice == "vm": #choice = view my tasks
            view_mine(username) #call function view_mine to view my task
      elif choice == "vs":#viewing the stats this menu option only available for the admin
            view_stats()#call funtion to view the stats
      elif choice == "gr":#if choice gr generate report
            generate_report() #call function generate report
      elif choice == "ds": #if choice is ds display stats
            display_stats() #display stats from generate report
      elif choice == "e":#exit the program
            sys.exit(0)
#function to generate_report
def generate_report():
      """
      task overview report :BEGIN
      """

      task_overdue_counter = 0 #task overdue counter
      task_completed_counter = 0 #task completed
      task_uncompleted_counter = 0 #task not completed
      count_task_overdue_by_date_and_status_no = 0
      with open('tasks.txt', 'r+') as f: #open the tasks file as f
            task_list = f.readlines() #read the lines from the file
      for row in task_list: #for every row in task_list
                  #assign each row to it's relevant variable
            task_user,task_title,task_description,task_current_date,task_due_date,task_completion = row.strip().split(", ")
            datetime_object = datetime.strptime(task_due_date,'%d %b %Y') #turn the task_due date into a dateime variable
            dt_string = now.strftime("%d %b %Y") #get to todays date as string object
            datetime_today = datetime.strptime(dt_string ,"%d %b %Y") #convert that string object of dt_string into a datetime variable
            if (datetime_object < datetime_today): #if the task_due_date is than todays date
                  task_overdue_counter += 1 #increment the counter for task_overdue
            if (task_completion == "No"):#if the task is not completed
                  task_uncompleted_counter += 1 #increment the task not  complete
            if (task_completion == "Yes"): #if the task is completed
                  task_completed_counter += 1 #increment the task completed counter
            if (datetime_object < datetime_today and task_completion == "No"):
                  count_task_overdue_by_date_and_status_no += 1

      #total tasks
      total_tasks = task_uncompleted_counter + task_completed_counter
      total_tasks_to_file = 'Total tasks: {}'.format(total_tasks)
      #task overdue by date
      task_overdue_by_date = 'Tasks overdue by date: {}'.format(task_overdue_counter)
      #task_not_completed_status_no
      task_not_completed_status_no = 'task uncompleted i.e. status No: {}'.format(task_uncompleted_counter)
      #task_not_completed_status_yes
      task_not_completed_status_yes= 'task completed i.e. status Yes: {}'.format(task_completed_counter)
      #task_overdue_by_date_and_status_no
      task_overdue_by_date_and_status_no = 'task overdue by date and status No: {}'.format(count_task_overdue_by_date_and_status_no)
      total_tasks = task_uncompleted_counter + task_completed_counter
      #percentage uncompleted
      percentage_uncompleted = (float(task_uncompleted_counter)/float(total_tasks))*100
      #percentage of tasks uncompleted by status No
      percentage_uncompleted_tasks_by_status_no = 'Percentage of tasks uncompleted by status No: {:.2f}%'.format(percentage_uncompleted)
      # percentage_tasks_overdue_by_date_calculation
      percentage_tasks_overdue_by_date_calculation = (float(task_overdue_counter) / float(total_tasks))*100
      #percentage tasks overdue by date
      percentage_tasks_overdue_by_date = 'Percentage of tasks uncompleted by due date: {:.2f}%'.format(percentage_tasks_overdue_by_date_calculation)

      task_overview = open("task_overview_for_display_stats.txt","w",encoding='utf-8') #write to the tasks.txt
      #write to the file
      task_overview.write(f"{total_tasks_to_file}, {task_overdue_by_date}, {task_not_completed_status_no}, {task_not_completed_status_yes}, {task_overdue_by_date_and_status_no}, {percentage_uncompleted_tasks_by_status_no}, {percentage_tasks_overdue_by_date}")
      #close the file
      task_overview.close()

      task_overview_report = open("task_overview.txt","w",encoding='utf-8')
      task_overview_report.write(f"{total_tasks_to_file}\n {task_overdue_by_date}\n {task_not_completed_status_no}\n {task_not_completed_status_yes}\n {task_overdue_by_date_and_status_no}\n {percentage_uncompleted_tasks_by_status_no}\n {percentage_tasks_overdue_by_date}")
      task_overview.close()


      """
      task overview report :END
      """


      """
      user overview report :BEGIN
      """
      
      with open("user.txt",'r+') as f: # read the file as f and split the file by ", " and read eachline
            user_list = [i.strip().split(", ") for i in f.readlines()] # read the file as f and split the file by ", " and read eachline

      with open('tasks.txt', 'r') as f: #open the tasks file as f
            task_list = f.readlines() #read the lines from the file
      #delete the user_overview.txt file if file doesn't exist
      if(os.path.isfile('user_overview_for_stats_display.txt')):
            os.remove('user_overview_for_stats_display.txt')
      if(os.path.isfile('user_overview.txt')):
            os.remove('user_overview.txt')
      for x in range(0,len(user_list)):#we are looking for every user in the user text file
            count_tasks = 0 #count for the number of tasks
            count_task_completion_no = 0 #count for task completion no
            count_task_completion_yes = 0 #count for task completeion yes
            count_task_pass_due_date_and_completion_no = 0#count for task completeion no and pass due date
            for row in task_list:#for every in the task file
                  #create a variable for each column
                  task_user,task_title,task_description,task_current_date,task_due_date,task_completion = row.strip().split(", ")
                  ##turn the task_due date into a dateime variable
                  datetime_object = datetime.strptime(task_due_date,'%d %b %Y')
                  #get to todays date as string object
                  dt_string = now.strftime("%d %b %Y")
                  #convert that string object of dt_string into a datetime variable
                  datetime_today = datetime.strptime(dt_string ,"%d %b %Y")
                  #if the task_user from task file is = the name from the user file
                  #this will check for each user in the user file as we are passing x from the range
                  if (task_user == user_list[x][0]):
                        #count the number of tasks
                        count_tasks += 1
                        if (task_completion == "No"): #if the task_completion is no
                              #count task completion no increments by 1
                              count_task_completion_no += 1
                        elif (task_completion == "Yes"): #if the task_completion is yes
                              #count task completion no increments by 1
                              count_task_completion_yes += 1
                              #if the task_due_date is less than todays date and task completion is No
                              #we run this as a seperate if because task_completion = No will will remove users from the test
                        if (datetime_object < datetime_today and task_completion == "No"):
                              #count task completion no increments
                              count_task_pass_due_date_and_completion_no += 1

            #print('{}, {}, {}, {}, {}, {}'.format(user_list[x][0],len(task_list),count_tasks, count_task_completion_no,count_task_completion_yes,count_task_pass_due_date_and_completion_no))
            #open the file for user task overview
            user_task_overview = open("user_overview_for_stats_display.txt","a+",encoding='utf-8') #append to the tasks.txt
            #write to the file
            user_task_overview.write(f"{user_list[x][0]}, {len(task_list)}, {count_tasks}, {count_task_completion_no}, {count_task_completion_yes}, {count_task_pass_due_date_and_completion_no}\n")
            #close the file
            user_task_overview.close()
            #percentage of total number of task have been assigned to that user 
            #the format part does all the calculations
            """
            e.g. user = admin 
            total task of user = 3
            percentage of total task have been assigned to that user 
            float(count_tasks) = 3
            float(user_overview[1]) = 12
            answer = 3/12 * 100 
            THE IF PART OF THE FORMAT CHECK IF WE DIVIDING BY IF WE DIVIDING BY 0 then the code will default the answer to 0
            """
            #user overview report
            percentage_overall_task = float(count_tasks)/float(len(task_list)) * 100 if float(len(task_list)) !=0 else 0
            percentage_overall_task = '{:.2f}%'.format(percentage_overall_task)
            percentage_task_completed_not_completed = float(count_task_completion_no)/float(count_tasks)*100 if float(count_tasks) !=0 else 0
            percentage_task_completed_not_completed = '{:.2f}%'.format(percentage_task_completed_not_completed)
            percentage_task_completed_completed = float(count_task_completion_yes)/float(count_tasks)*100 if float(count_tasks) !=0 else 0
            percentage_task_completed_completed = '{:.2f}%'.format(percentage_task_completed_completed)
            percentage_count_task_pass_due_date_and_completion_no = float(count_task_pass_due_date_and_completion_no)/float(count_tasks)*100 if float(count_tasks) !=0 else 0
            percentage_count_task_pass_due_date_and_completion_no = '{:.2f}%'.format(percentage_count_task_pass_due_date_and_completion_no)
            # if(os.path.isfile('user_overview.txt')):
            #     os.remove('user_overview.txt')
            user_task_overview_report = open("user_overview.txt","a+",encoding='utf-8') #append to the tasks.txt
            #write to the file
            user_task_overview_report.write(f"""
            Username {user_list[x][0]}
            Total Tasks {len(task_list)}
            Amount of tasks assigned to user {count_tasks}
            What percentage of the total number of tasks have been assigned to that user? {percentage_overall_task}
            What percentage of the tasks assigned to that user must still be completed? {percentage_task_completed_not_completed}
            What percentage of the tasks assigned to that user have been completed? {percentage_task_completed_completed},
            What percentage of the tasks assigned to that user have not yet been completed and are overdue? {percentage_count_task_pass_due_date_and_completion_no}\n""")
            #close the file
            user_task_overview_report.close()
      """
      user overview report :END
      """

#function to display_stats
def display_stats():
      """
      task overview report :BEGIN
      """
      check_file_exists = False #boolean to check if file exists
      while (check_file_exists == False): #while the boolean is false
            #check if file exists if it doesn't for both file run generate report
            if ((os.path.exists('user_overview_for_stats_display.txt') is False) or (os.path.exists('task_overview_for_display_stats.txt') is False)):
                  generate_report() #run generate report
                  check_file_exists = True #set while loop to true once generate_report completed and carry on with the rest of the tasks

            task_overview_file = open("task_overview_for_display_stats.txt","r+") # open the file
            for line in task_overview_file:# assign each value to a variable
                  task_overview = line.split(", ") #split the file by the ,
                  print("\t\tSUMMARY OF ALL TASKS") #print a heading
                  for task in range(0,len(task_overview)): #for each task in the range of 0 up to the length of task overview
                        print(task_overview[task]) #print the results

            """
            task overview report :BEGIN
            """
            print('\n')
            """
            user overview report :BEGIN
            """
            user_overview_file = open("user_overview_for_stats_display.txt","r+") # open the file
            for line in user_overview_file:# assign each value to a variable
                  user_overview = line.split(", ") #split the file by the ,
                  print('User name:\t\t\t\t\t\t\t\t\t\t\t {}'.format(user_overview[0])) #print the user name
                  print('Number of tasks assigned to user:\t\t\t\t\t\t\t\t {}'.format(user_overview[2])) #total number of tasks assigned to the user
                  #percentage of total number of task have been assigned to that user 
                  #the format part does all the calculations
                  """
                  e.g. user = admin 
                  total task of user = 3
                  percentage of total task have been assigned to that user 
                  float(user_overview[2]) = 3
                  float(user_overview[1]) = 12
                  answer = 3/12 * 100 
                  THE IF PART OF THE FORMAT CHECK IF WE DIVIDING BY IF WE DIVIDING BY 0 then the code will default the answer to 0
                  """
                  print('What percentage of the total number of tasks have been assigned to that user?:\t\t\t {:.2f}%'.format((float(user_overview[2])/float(user_overview[1])*100 if float(user_overview[1]) != 0 else 0 )))
                  print('What percentage of the tasks assigned to that user have been completed?:\t\t\t {:.2f}%'.format((float(user_overview[4])/float(user_overview[2])*100 if float(user_overview[2]) != 0 else 0 )))
                  print('What percentage of the tasks assigned to that user must still be completed?:\t\t\t {:.2f}%'.format((float(user_overview[3])/float(user_overview[2])*100 if float(user_overview[2]) != 0 else 0 )))
                  print('What percentage of the tasks assigned to that user have not yet been completed and are overdue?: {:.2f}%'.format((float(user_overview[5])/float(user_overview[2])*100 if float(user_overview[2]) != 0 else 0 )))
                  print('\n')
            """
            user overview report :END
            """
            user_overview_file.close()
            print_menu(username)



#function for view my tasks
def view_mine(username):
      task_number_list = 0 #create a task number starting from 0
      with open('tasks.txt', 'r') as f: #open the tasks file as f
            task_list = f.readlines() #read the lines from the file
      for row in task_list: #for every row in task_list
            #assign each row to it's relevant variable
            task_user,task_title,task_description,task_current_date,task_due_date,task_completion = row.strip().split(", ")
            #task number list increments by 1
            task_number_list += 1
            if (username == task_user): #if the username is for the particular user
                  #print the tasks
                  #task number will be displayed and please not that is it is not coming from the tasks.txt
                  print(f"""
                  TASK NO : {task_number_list}
                  User : {task_user}
                  Title : {task_title}
                  Task Description : {task_description}
                  Task Current Date : {task_current_date}
                  Task Due Date : {task_due_date}
                  Task Completed : {task_completion}
                  """)
                  #ask user for their option
      editTask = input(f"""
      PLEASE CHOOSE THE CORRECT OPTION
      [1] Would you like to mark the task as complete enter a 1
      [2] Would you like to edit the task enter a 2
      [3] Go back to the menu enter a -1
      """)
      if editTask == "1": # user selects option to update the status from No to Yes
            task_number = int(input("Please enter the task number? ")) #ask user for the task number
            task_number = task_number - 1 #since we start counting form 0 in the file as in the first line is technically 0 we will say task_number = task_number -1
            with open("tasks.txt",'r+') as f:
                  task_list = [i.strip().split(", ") for i in f.readlines()] # read the file as f and split the file by ", " and read eachline
                  #task_list will contain all the tasks in a list with a sublist e.g. [[line1 of task],[line 2 of task],[line 3 of task]]
            task_list[task_number][5] = "Yes" #change the status of the users task number from No to Yes
            print("your task has been updated from to a Yes")
            with open('tasks.txt', 'w') as fileinsert: #open the file tasks.txt as fileinsert
                  #write every sublist of list back into the file e.g. [[line1 of task],[line 2 of task],[line 3 of task]]
                  fileinsert.write("\n".join([', '.join([str(x) for x in item]) for item in task_list]))
      elif editTask == "2":
            #ask the username for update or the due date for update
            username_or_due_date_change = input(f"""
            [1] Would you like to update the username enter a 1
            [2] Would you like to update the due date enter a 2
            """)
            #if option 1 selected we will update the user name
            #UPDATE USER NAME
            if (username_or_due_date_change == "1"):
                  task_number = int(input("Please enter the task number? ")) #ask user for the task number
                  task_number = task_number - 1 #since we start counting form 0 in the file as in the first line is technically 0 we will say task_number = task_number -1
                  with open("tasks.txt",'r+') as f: # read the file as f and split the file by ", " and read eachline
                        task_list = [i.strip().split(", ") for i in f.readlines()] # read the file as f and split the file by ", " and read eachline
                        if task_list[task_number][5] == "Yes": #if the user has the status of completion set to yes
                              print("The task can only be edited if it has not yet been completed") #user cannot edit if task is complete
                              print_menu(username) #print the menu
                        elif task_list[task_number][5] == "No": #if the user task is still set to No we can update
                              new_username = input("Enter a new username ") #ask user for new username
                              old_user = task_list[task_number][0] #get the old user username from the task list
                              # WE ARE NOT DOING ANYTHING WITH OLD_USER IT IS PURELY USED FOR THE PRINT TO LET THE USER KNOW OF THEIR OLD USERNAME
                              task_list[task_number][0] = new_username #update the user name
                              print("user name has been updated from {} to {}".format(old_user,new_username)) #print a message to the client to let them know of the old username and the new username
                              with open('tasks.txt', 'w') as fileinsert: #open the file tasks.txt as fileinsert
                                    #write every sublist of list back into the file e.g. [[line1 of task],[line 2 of task],[line 3 of task]]
                                    fileinsert.write("\n".join([', '.join([str(x) for x in item]) for item in task_list]))
            #if option 2 selected we will update the due date
            #UPDATE DUE DATE
            elif (username_or_due_date_change == "2"):
                  task_number = int(input("Please enter the task number? ")) #ask user for the task number
                  task_number = task_number - 1 #since we start counting form 0 in the file as in the first line is technically 0 we will say task_number = task_number -1
                  with open("tasks.txt",'r+') as f:# read the file as f and split the file by ", " and read eachline
                        task_list = [i.strip().split(", ") for i in f.readlines()]# read the file as f and split the file by ", " and read eachline
                        if task_list[task_number][5] == "Yes": #if the user has the status of completion set to yes
                              print("The task can only be edited if it has not yet been completed") #user cannot edit if task is complete
                              print_menu(username)#print the menu
                        elif task_list[task_number][5] == "No":#if the user task is still set to No we can update
                              new_date = input("Enter a new Due Date ")#Enter the new due date
                              old_due_date = task_list[task_number][4] #get the old due date from the task list
                              # WE ARE NOT DOING ANYTHING WITH OLD_DUE_DATE IT IS PURELY USED FOR THE PRINT TO LET THE USER KNOW OF THEIR OLD USERNAME
                              task_list[task_number][4] = new_date #update the due_date
                              print("user name has been updated from {} to {}".format(old_due_date,new_date))#print a message to the client to let them know of the old due date and the new due date
                              with open('tasks.txt', 'w') as fileinsert: #open the file tasks.txt as fileinsert
                                    #write every sublist of list back into the file e.g. [[line1 of task],[line 2 of task],[line 3 of task]]
                                    fileinsert.write("\n".join([', '.join([str(x) for x in item]) for item in task_list]))
      elif editTask == "-1":# if user selects -1
            print_menu(username) #print the menu

#function to view the stats
def view_stats():
      file_tasks = open("tasks.txt", "r") #open tasks.txt
      line_count_tasks = 0 #set counter to 0
      for line in file_tasks: #for every line in the file
            if line != "\n": #if the does not have a "\n" count that line
                  line_count_tasks += 1 #increment the counter
      file_tasks.close() #close the file
      file_user = open("user.txt", "r") #open users.txt
      line_count_user = 0 #set counter to 0
      for line in file_user:#for every line in the file
            if line != "\n": #if the does not have a "\n" count that line
                  line_count_user += 1 #increment the counter
      file_user.close() #close the file
      #print the stats
      print(f"""
      Number of users: {line_count_user}
      Number of Tasks: {line_count_tasks}
      """)
      print_menu(username)
"""
FUNCTIONS: END
"""
"""
MAIN PROGRAM BEGIN
"""

#read the content of the file
user_file = open("user.txt",'r') #open the file and save it into user file variable
content_of_user_file = user_file.readlines() #read the content of each line of user.txt
content_of_user_file = [w.replace('\n', '') for w in content_of_user_file] #windows creates a "\n" in the file we need to remove this
login = False #login will be false as user has not logged in yet

#ask user for their credentials
while login == False: #while the user has not logged in yet
  username = input("Enter your username ") #ask user for their username
  password = input("Enter your password ") #ask user for their password

  for line in content_of_user_file:
        #go through each line in the variable content_of_user_file and split it up
        # e.g. admin, admin1
        #line[0] = admin
        #line[1] = adm1n
        line = line.split(", ")
        if username == line[0] and password == line[1]: #if user inputs for name and password match
              login = True #then they have logged in

  if login == False: #if their login is false
        print("Incorrect username or password") #incorrect user name or password entered
  user_file.seek(0) #bring the cursor of the file back to its original state

#print(login) Login is true at this point
print_menu(username)