import os
import os.path
import getpass
from os import path
import subprocess

# This functions just prints out some common grep options used, so that
# the user has something to refer on how to use it
def grep_options():
    print("The common one's are : [-i] -> ignore case")
    print("                       [-n] -> precede each matching line with a line number")
    print("                       [-v] -> to select non-matching lines")
    print("                       [-w] -> select lines containing matches that form whole words")
    print("                       [-x] -> exactly match the whole line ....etc")

# This functions just prints out some common find options used with some
# examples, so that the user has something to refer on how to use it
def find_options():
    print("The search common one's are : [-name/-iname *.jpg] -> search by name/ignore case")
    print("                              [-type f/d] -> search for file/directory")
    print("                              [-perm 744] -> search by permissions")
    print("                              [-size +10M] -> search by file size")
    print("                              [-user John] -> search by specific user")
    print("                              [-depth 2] -> search atleast specified levels deep ...etc")

# This functions just prints out all the file/directory permissions that
# the user can set.
def chmod_permissions():
    print("Below are the eight different permissions you can choose from")
    print("0 - none\n1 - execute only\m2 - wite only\n3 - write & execute\n4 - read only")
    print("5 - read & execute\n6 - read & write\n7 - read, write & execute\n")

# Function that prints out the menu onto the terminal
def menu():
    print("\n1. Search for files")
    print("2. Search for matching patterns in a file")
    print("3. Generate a directory tree (upto 2 levels deep)")
    print("4. Change permissions of a file/directory")
    print("5. Exit\n")

# From here on starts the main function
# Firstly a menu is displayed to the user, of all the things that can
# be done using this script, and then the user is asked to select one of
# those options
menu()
choice = eval(input("Please select a command: "))

# keeps track of the command number for the log_file
# the log_file keep track of the commands that the user
# used in a given session
cmd_number = 0
log_file = open("log.txt", "a") #
log_file.write("***** START OF PROGRAM *****\n\n")

# This while loops keeping going until the user enters 5, which is the
# command number to exit
while choice != 5:

    # If statement for finding files/directory. The user is initially asked for
    # the directory path to search for files. Then find_options() is called,
    # which displays the common find options, and the user is asked to enter
    # the desired the option. Since the user can add multiple options altogether
    # I split the option string and store it into another variable of list. Also
    # the user can enter some options with single or double qoutes, so I replace
    # all types of quotes before splitting, so that there are no descrepancies.
    # Now, I am using subprocess.Popen() command to run all the UNIX commands in
    # this script. As the command takes a list of strings as input arguments
    # I pass the list of string (cmd) to which I appended 'find', 'path' and the
    # 'options'; to the subprocess, which runs and the result is stored into
    # a variable, which then used for proccessing the terminal as well as the
    # log_file output
    if choice == 1:
        cmd_number += 1 #incrementing command number
        cmd = ['find']
        dir_path = input("\nEnter the directory path: ")
        dir_path = dir_path.replace("~", "/home/"+getpass.getuser())
        find_options()
        cmd.append(dir_path)
        option = input("Enter the find option (press enter for no option): ")

        # writing the find parameters to the log_file in a formatted way
        log_file.write("Command " + str(cmd_number) + ": FIND\n")
        log_file.write(" Search Path: " + dir_path + "\n")
        log_file.write(" Search Options: " + option + "\n\n")

        option = option.replace("'", "")
        option = option.replace('"', '')
        cmd = cmd + option.split()
        found = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = found.communicate()

        result = output.splitlines() # splitting the output by '\n' to easily
                                     #format the terminal output

        print("\nThe following files were found in: ")
        for i in result:
            print(" - " + i.decode()) # printing to terminal
            log_file.write(" - " + i.decode() + "\n"); # writing to log_file

        log_file.write("----------\n\n")
        print("-------------------x-------------------x-------------------x-------------------x-------------------")

    # else-if statement for searching string inside a file. This works in the
    # same way as the if-statement above. The only thing different is that
    # the user enters grep-options and search strings in 2 different input()'s
    # Since we are searching inside a file, I check if the file exists or not
    # by using os.path.exists() method. If the file is not present, I print an
    # error message for the same.
    elif choice == 2:
        cmd_number += 1
        file_name = input("\nEnter file name: ")
        log_file.write("Command " + str(cmd_number) + ": GREP\n")
        log_file.write(" Search File: " + file_name + "\n")

        # Since relative paths don't work very well with Python, I conver that
        # to absolute path and then continue.
        file_name = file_name.replace("~", "/home/"+getpass.getuser())
        if os.path.exists(file_name):
            grep_options()
            option = input("Enter grep options (press enter for no option): ")
            pattern = input('Search for this string (can use REGEX here): ')

            #writing the grep params to log_file
            log_file.write(" Search Options: " + option + "\n")
            log_file.write(" Search Pattern: " + pattern + "\n\n")

            cmd = ['grep']
            if len(option) > 0: # if the user enters the options
                pattern = pattern.replace("'", "")
                pattern = pattern.replace('"', '')
                cmd.extend(option.split())
                cmd.append(pattern)
                cmd.append(file_name)
                found = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, err = found.communicate()
            else: # if the user does not enter any option
                found = subprocess.Popen(['grep', pattern, file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, err = found.communicate()

            result = output.splitlines()
            print(("\nThe following lines were found in " + file_name + ":"))
            for i in result:
                print(" - " + i.decode())
                log_file.write(" - " + i.decode() + "\n")
        else:
             print("This file does not exist: " + file_name)
             log_file.write(" This file does not exist: " + file_name + "\n")

        log_file.write("----------\n\n")
        print("-------------------x-------------------x-------------------x-------------------x-------------------")

    # else-if statement for generating a directory tree. Here I am using the
    # my original bash-script from Project-1, to generate the tree. I ask for
    # all the input arguments that the original script required from the user
    # and append them together into a string which has the call to 'sh' and the
    # script-file name. One thing that is different is that I am using os.system()
    # to run my tree_script. There is no particular output to the terminal except
    # informing the user about the tree-directory and where is it stored.
    elif choice == 3:
        cmd_number += 1
        directory = input("\nEnter the directory path: ")
        log_file.write("Command " + str(cmd_number) + ": DIRECTORY TREE SCRIPT\n")
        log_file.write(" Directory path: " + directory + "\n")

        # Since relative paths don't work very well with Python, I conver that
        # to absolute path and then continue.
        directory = directory.replace("~", "/home/"+getpass.getuser())
        if os.path.exists(directory):
            output_file = input("Enter the output file name [with the .html extension and path]: ")
            cmd = "sh ./chavda_myScript.sh " + directory + " " + output_file
            os.system(cmd)
            log_file.write(" Output file name (path): " + output_file + "\n----------\n\n")
            print("\nThe directory tree for " + directory + " is stored in " + output_file)

        else:
            print("No such directory")
            log_file.write(" No such directory: " + directory + "\n")
            log_file.write("----------\n\n")

        print("-------------------x-------------------x-------------------x-------------------x-------------------")

    # else-if statement for chainging file/directory permissions. This one is
    # pretty similar to above one as well. The user is asked for a file or
    # directory path, and then asked for the permission s/he wants to set.
    # The user is also displayed a list of all the permissions in number format
    # on the terminal. All these inputs from the user is then ran, and the
    # terminal as well as the log_file are updated with the info about the
    # permissions of the file.
    elif choice == 4:
        cmd_number += 1
        dir_path = input("\nEnter the directory/file path: ")
        log_file.write("Command " + str(cmd_number) + ": CHMOD\n")
        log_file.write(" Directory/File path: " + dir_path + "\n")

        # Since relative paths don't work very well with Python, I conver that
        # to absolute path and then continue.
        dir_path = dir_path.replace("~", "/home/"+getpass.getuser())
        if os.path.exists(dir_path):
            chmod_permissions()
            perm = input("Enter the permission you want to set in the form [user][group][other]: ")
            cmd = "chmod " + perm + " " + dir_path
            os.system(cmd)
            log_file.write(" Permission for the dir/file: " + perm + "\n----------\n\n")
            print("You have succefully changed the permission for " + dir_path)
        else:
            print("This file does not exist: " + dir_path)
            log_file.write(" This file does not exist: " + dir_path + "\n")
            log_file.write("----------\n\n")

        print("-------------------x-------------------x-------------------x-------------------x-------------------")

    # Print the menu again as one of the command was selected and now is complete
    menu()
    choice = eval(input ("Please select a command: "))

# end-while loop

# Lastly after exiting, the log_file is closed and a thank you message is printed
log_file.write("***** END OF PROGRAM *****\n\n")
log_file.close()
print("\nYour session has been logged into 'log.txt'")
print("THANK YOU..!!")
