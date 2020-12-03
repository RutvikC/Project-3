import os
import os.path
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

# This functions just prints out some common find options used, so that
# the user has something to refer on how to use it
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

# From here on starts the main function
# Firstly a menu is displayed to the user, of all the things that can
# be done using this script
print("\n1. Search for files")
print("2. Search for matching patterns in a file")
print("3. Generate a directory tree (upto 2 levels deep)")
print("4. Change permissions of a file/directory")
print("5. Exit\n")

choice = input("Please select a command: ")
cmd_number = 0
log_file = open("log.txt", "a")
log_file.write("***** START OF PROGRAM *****\n\n")

while choice != 5:
    if choice == 1:
        cmd_number += 1
        cmd = ['find']
        dir_path = raw_input("\nEnter the directory path: ")
        find_options()
        cmd.append(dir_path)
        option = raw_input("Enter the find option (press enter for no option): ")
        option = option.replace("'", "")
        option = option.replace('"', '')
        cmd = cmd + option.split()
        found = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = found.communicate()
        result = output.splitlines()
        print("\nThe following files were found in: ")
        for i in result:
            print(" - " + i)

        log_file.write("Command " + str(cmd_number) + ": FIND\n")
        log_file.write(" Search Path: " + dir_path + "\n")
        log_file.write(" Search Options: " + option + "\n\n")
        for i in result:
            log_file.write(" " + i + "\n");
        log_file.write("----------\n\n")

    elif choice == 2:
        cmd_number += 1
        file_name = raw_input("\nEnter file name: ")
        if os.path.exists(file_name):
            grep_options()
            option = raw_input("Enter grep options (press enter for no option): ")
            pattern = raw_input('Search for this string (can use REGEX here): ')
            cmd = ['grep']
            if len(option) > 0:
                cmd.extend(option.split())
                cmd.append(pattern)
                cmd.append(file_name)
                found = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, err = found.communicate()
            else:
                found = subprocess.Popen(['grep', pattern, file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, err = found.communicate()

            result = output.splitlines()
            print("\nThe following lines were found in " + file_name + ":")
            for i in result:
                print(" - " + i)

            log_file.write("Command " + str(cmd_number) + ": GREP\n")
            log_file.write(" Search File: " + file_name + "\n")
            log_file.write(" Search Options: " + option + "\n")
            log_file.write(" Search Pattern: " + pattern + "\n\n")
            for i in result:
                log_file.write(" " + i + "\n");
            log_file.write("----------\n\n")

        else:
             print("This file does not exist: " + file_name)
        print("-------------------x-------------------x-------------------x-------------------x-------------------")

    elif choice == 3:
        cmd_number += 1
        directory = raw_input("\nEnter the directory path: ")
        output_file = raw_input("Enter the output file name [with the .html extension and path]: ")
        cmd = "sh ./chavda_myScript.sh " + directory + " " + output_file
        os.system(cmd)
        log_file.write("Command " + str(cmd_number) + ": DIRECTORY TREE SCRIPT\n")
        log_file.write(" Directory path: " + directory + "\n")
        log_file.write(" Output file name (path): " + output_file + "\n----------\n\n")
        print("\nThe directory tree for " + directory + " is stored in " + output_file)
        print("-------------------x-------------------x-------------------x-------------------x-------------------")

    elif choice == 4:
        cmd_number += 1
        dir_path = raw_input("\nEnter the directory/file path: ")
        chmod_permissions()
        perm = raw_input("Enter the permission you want to set in the form [user][group][other]: ")
        cmd = "chmod " + perm + " " + dir_path
        os.system(cmd)
        log_file.write("Command " + str(cmd_number) + ": CHMOD\n")
        log_file.write(" Directory/File path: " + dir_path + "\n")
        log_file.write(" Permission for the dir/file: " + perm + "\n----------\n\n")
        print("You have succefully changed the permission for " + dir_path)
        print("-------------------x-------------------x-------------------x-------------------x-------------------")

    print("\n1. Search for files")
    print("2. Search for matching patterns in a file")
    print("3. Generate a directory tree (upto 2 levels deep)")
    print("4. Change permissions of a file/directory")
    print("5. Exit\n")
    choice = input ("Please select a command: ")
log_file.write("***** END OF PROGRAM *****\n\n")
log_file.close()
