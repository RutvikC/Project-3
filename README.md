# ECE 2524 - Project 3
## A Python script that helps the user perform some unix commands, but with a bit friendlier approach
---
Earlier me and my partner were going to work on this project, but due to some problems he had to drop this class. And because of that I had to scale down the project a bit. 

The project is about using some common UNIX commands via a python executable. I came up with a simple user-friendly application that allows the user to search for files, or words inside a specific file alongside some other UNIX commands like generating a directory-tree and changing file permissions.

Before running the script, one important thing to check for is the the python version on your machine. Just type the following command on your terminal and compare your python version with the one below:

```
$ python -V
Python 3.8.2
```

If the python version on your machine is Python 2.6 or higher than this script will not work on your machine. You need atleast 3.6 or higher for this script to run.

Now moving onto running the project3_script.py. Below is an example on how to run the script: First you will be asked to choose an option, here I have selected 1. Since I am searching for a file, I am asked for the search directory path next. After entering that I am aksed for any specific find options that I want to enter along with some examples. And then finally the script runs the 'find' command on the input parameters and the found files are displayed on the terminal.

```
$ python project3_script.py 

1. Search for files
2. Search for matching patterns in a file
3. Generate a directory tree (upto 2 levels deep)
4. Change permissions of a file/directory
5. Exit

Please select a command: 1

Enter the directory path: ../
The search common one's are : [-name/-iname *.jpg] -> search by name/ignore case
                              [-type f/d] -> search for file/directory
                              [-perm 744] -> search by permissions
                              [-size +10M] -> search by file size
                              [-user John] -> search by specific user
                              [-depth 2] -> search atleast specified levels deep ...etc
Enter the find option (press enter for no option): -name "text*" -size +6c

The following files were found in: 
 - ../text1.txt
 - ../Exercise 2/text1.txt
 - ../Exercise 2/text2.txt
 - ../text 2.txt
-------------------x-------------------x-------------------x-------------------x-------------------

```
You can choose any option you like (**except -exec**; the reason for not using that option is because it ends with {} \\; _in python '\' is treated as an escape character and so it adds an extra '\\;' while parsing the input and I couldn't find any other way to get around it_)

Continuing the example of choosing all the options with multiple variations in one session: (while choosing options from 2 to 4, you can get No such directory message on the terminal, which is likely that you don't have file permission to read. And so you need to go and manually change the file permissions, as there is no way this os.path() can bypass that error.)

```
1. Search for files
2. Search for matching patterns in a file
3. Generate a directory tree (upto 2 levels deep)
4. Change permissions of a file/directory
5. Exit

Please select a command: 2

Enter file name: ~/ECE-2524/mycontact.txt
The common one's are : [-i] -> ignore case
                       [-n] -> precede each matching line with a line number
                       [-v] -> to select non-matching lines
                       [-w] -> select lines containing matches that form whole words
                       [-x] -> exactly match the whole line ....etc
Enter grep options (press enter for no option): 
Search for this string (can use REGEX here): .com 

The following lines were found in /home/rutvik/ECE-2524/mycontact.txt:
 - aztecwrestling@google.com
 - andyM@google.com
 - Lawsonhawk@yahoo.com
 - daren103@yahoo.com
-------------------x-------------------x-------------------x-------------------x-------------------

1. Search for files
2. Search for matching patterns in a file
3. Generate a directory tree (upto 2 levels deep)
4. Change permissions of a file/directory
5. Exit

Please select a command: 2

Enter file name: ./mycontact.txt
The common one's are : [-i] -> ignore case
                       [-n] -> precede each matching line with a line number
                       [-v] -> to select non-matching lines
                       [-w] -> select lines containing matches that form whole words
                       [-x] -> exactly match the whole line ....etc
Enter grep options (press enter for no option): -i -n
Search for this string (can use REGEX here): "CA"

The following lines were found in ./mycontact.txt:
 - 4:Anaheim, CA 92807-1281
 - 14:La Habra, CA 90631
 - 15:Carl Hohl (aka Krazy Rabbit)
 - 21:Lakewood, CA 90713-2013
 - 29:Torrance, CA 90504
 - 36:Placentia, CA 90631
 - 44:Rosemead, CA 91770
-------------------x-------------------x-------------------x-------------------x-------------------
1. Search for files
2. Search for matching patterns in a file
3. Generate a directory tree (upto 2 levels deep)
4. Change permissions of a file/directory
5. Exit

Please select a command: 3

Enter the directory path: ~/ECE-2524/
Enter the output file name [with the .html extension and path]: ~/rutvik.html

The directory tree for /home/rutvik/ECE-2524/ is stored in ~/rutvik.html
-------------------x-------------------x-------------------x-------------------x-------------------

1. Search for files
2. Search for matching patterns in a file
3. Generate a directory tree (upto 2 levels deep)
4. Change permissions of a file/directory
5. Exit

Please select a command: 4

Enter the directory/file path: ~/ECE-2524/Project 2/Test_file3.cpp
Below are the eight different permissions you can choose from
0 - none
1 - execute only\m2 - wite only
3 - write & execute
4 - read only
5 - read & execute
6 - read & write
7 - read, write & execute

Enter the permission you want to set in the form [user][group][other]: 766
chmod: cannot access '/home/rutvik/ECE-2524/Project': No such file or directory
chmod: cannot access '2/Test_file3.cpp': No such file or directory
You have succefully changed the permission for /home/rutvik/ECE-2524/Project 2/Test_file3.cpp
-------------------x-------------------x-------------------x-------------------x-------------------

1. Search for files
2. Search for matching patterns in a file
3. Generate a directory tree (upto 2 levels deep)
4. Change permissions of a file/directory
5. Exit

Please select a command: 5

Your session has been logged into 'log.txt'
THANK YOU..!!

```
One thing you would notice, when the program execution ends it that there is a 'log.txt' file created in the current working directory. That file actually kept track of all the commands you ran from start to the end with the respective command numbers and also the found patterns for some of the commands along with the directory paths, file names, options, etc.
