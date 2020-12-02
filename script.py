import os
import os.path
from os import path
import subprocess


def grep_options():
    print("The common one's are : [-i] -> ignore case")
    print("                       [-n] -> precede each matching line with a line number")
    print("                       [-v] -> to select non-matching lines")
    print("                       [-w] -> select lines containing matches that form whole words")
    print("                       [-x] -> exactly match the whole line ....etc")

def chmod_permissions():
    print("Below are the eight different permissions you can choose from")
    print("0 - none\n1 - execute only\m2 - wite only\n3 - write & execute\n4 - read only")
    print("5 - read & execute\n6 - read & write\n7 - read, write & execute\n")

print("\n1. Search for files")
print("2. Search for matching patterns in a file")
print("3. Generate a directory tree (upto 2 levels deep)")
print("4. Change permissions of a file/directory")
print("5. Exit\n")

choice = input ("Please select a command: ")
cmd_number = 0
log_file = open("log.txt", "a")

while choice != 5:
    if choice == 2:
        cmd_number += 1
        file_name = raw_input("\nEnter file name: ")
        if path.exists(file_name):
            grep_options()
            option = raw_input("Enter grep option (press enter for no option): ")
            pattern = raw_input('Search for this string: ')
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
            log_file.write(" Search Option: " + option + "\n")
            log_file.write(" Search Pattern: " + pattern + "\n\n")
            log_file.write(" " + output + "\n\n");
        print("-------------------x-------------------x-------------------x-------------------x-------------------")

    elif choice == 3:
        cmd_number += 1
        directory = raw_input("Enter the directory path: ")
        output_file = raw_input("Enter the output file name [with the .html extension and path]: ")
        cmd = "sh ./chavda_myScript.sh " + directory + " " + output_file
        os.system(cmd)
        log_file.write("Command " + str(cmd_number) + ": DIRECTORY TREE\n")
        log_file.write(" Directory path: " + directory + "\n")
        log_file.write(" Output file name (path): " + output_file + "\n\n")
        print("\nThe directory tree for " + directory + " is stored in " + output_file)
        print("-------------------x-------------------x-------------------x-------------------x-------------------")

    elif choice == 4:
        cmd_number += 1
        path = raw_input("\nEnter the directory/file path: ")
        chmod_permissions()
        perm = raw_input("Enter the permission you want to set in the form [user][group][other]: ")
        cmd = "chmod " + perm + " " + path
        os.system(cmd)
        log_file.write("Command " + str(cmd_number) + ": CHMOD\n")
        log_file.write(" Directory/File path: " + path + "\n")
        log_file.write(" Permission for the dir/file: " + perm + "\n\n")
        print("You have succefully changed the permission for " + path)
        print("-------------------x-------------------x-------------------x-------------------x-------------------")

    print("\n1. Search for files")
    print("2. Search for matching patterns in a file")
    print("3. Generate a directory tree (upto 2 levels deep)")
    print("4. Change permissions of a file/directory")
    print("5. Exit\n")
    choice = input ("Please select a command: ")

log_file.close()
