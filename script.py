import os
import os.path
from os import path
import subprocess


def grep_options():
    print("The common one's are : [-i] -> ignore case")
    print("                       [-n] -> precede each matching line with a line number")
    print("                       [-v] -> all lines, but only the ones that match ....etc")


print("\n1. Search for files")
print("2. Search for matching patterns in a file")
print("3. ")
print("4. Exit\n")

choice = input ("Please select a command: ")

while choice != 4:
    if choice == 2:
        file_name = raw_input("\nEnter file name: ")
        if path.exists(file_name):
            grep_options()
            option = raw_input("Enter grep option (press enter for no option): ")
            pattern = raw_input('Search for this string: ')
            if len(option) > 0:
                found = subprocess.Popen(["grep", option, pattern, file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, err = found.communicate()
            else:
                found = subprocess.Popen(["grep", pattern, file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, err = found.communicate()

            result = output.splitlines()
            print("\nThe following lines were found in " + file_name + ":")
            for i in result:
                print(" - " + i)

            write_to_log = raw_input("\nIf you want to write the searched results to a file enter 1: ");
            if write_to_log == 1:
                log_file_name = raw_input("Enter log file name: ");
                log_file = open(log_file_name, "a")
                log_file.write(output);
                log_file.close()
        else:
            print("This file does not exist: " + file_name)
        print("----------------------------------------------------------------------------------------------------")

    elif choice == 1:



    print("\n1. Search for files")
    print("2. Search for matching patterns in a file")
    print("3. Exit\n")
    choice = input ("Please select one of the above options: ")
