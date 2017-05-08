#Project: CIS 177 WEEK 15 FINAL PROJECT
#Project Location: projects\cis177\Week15Project
#File: Week15FinalProject.py
#Purpose: This is an implementation of a student information system for XYZ Community college
#         for Week 15 - the final project of the year       
#         NOTE: The program depends on StudentClass.py
#Revision: 1.0 / 8 MAY 2017
#Created: 8 MAY 2017
#Author: Rick Miller <rick@rickthegeek.com>



nextAvailableStudentNumber = 10000 # This is the next available student number, We want 5 digit numbers so init it to 10000 (and it is a global)

import StudentClass

currentStudents = {} # This will be the dictionary of the studentIDs and student records

def addStudent(studentDict, Student, newStudentNumber):
    # This routine will actuallt add the given student record to the given dict. 
    # Also, we will increment the next available student number here
    global nextAvailableStudentNumber
    studentDict[newStudentNumber] = Student
    nextAvailableStudentNumber += 1

def printAll(studentDict):
    # This routine will simply step through all the records in the given dict, print the ID, then print the record for the ID
    # Note: If there are no students in the dict, tell the user and do nothing.
    if len(studentDict) > 0:
        print('Printing list of all students:')
        for ID, Student in studentDict.items():
            print('\nStudent ID:', ID) # Print a black line before each student record, for neatness
            print(Student)
    else:
        print('No students on file. Please add some students, then try again!')

def addNewStudent(studentDict):
    global nextAvailableStudentNumber
    newStudentNumber = nextAvailableStudentNumber
    print('Add a new student - new ID will be', newStudentNumber)
    myNewStudent = StudentClass.Student()
    myNewStudent.firstName = input('Student\'s first name: ')
    myNewStudent.lastName = input('Students\'s last name: ')
    myNewStudent.gpa = float(input('Student\'s GPA: '))
    myNewStudent.major = input('Student\'s major: ')
    print('\nAbout to create this student with ID', newStudentNumber)
    print(myNewStudent)
    isOK = input('Add this student? ')[0].lower()
    if isOK == 'y':
        addStudent(currentStudents, myNewStudent, newStudentNumber)
        print('Student',newStudentNumber,'added!')
        print('The next available ID is:', nextAvailableStudentNumber)
    else:
        print('Cancelled!')

def findStudentByID(studentDict):
    # This function will accept an input to pass to findStudent(). Note, that
    # I would have combined this function and the findStudent function into one, but
    # the spec called for a function called findStudent with two paramaters.
    # So, this function just gets the second paramater to pass to findStudent
    try:
        idToFind=int(input('Please enter the student ID to find -> '))
        findStudent(studentDict, idToFind)
    except ValueError:
        print('Sorry, student IDs are numbers only. Returning to main menu.')

def largeGPA(studentDict):
    # This function will look through the given dictionary
    # and will print the information with the highest GPA
    # We will look at each student ID in turn, and if the
    # student's GPA is higher than the previous student's GPA
    # then we will note that student's ID. If the studetnt's GPA
    # is not higher than the GPA for the student on file, then
    # we will skip to the next student record. Once we have checked
    # all the students in the dict, the student with the highest GPA
    # will be the one we recorded, and then we will print that student's info
    # Note: If there are no students in the given dict, we will let the user know
    # and then do nothing
    if len(studentDict) > 0:
        highestGPA = 0.0 # This is where we will store the highest GPA we found so far
        highestGPAStudentID = 0 # This is where we will store the ID of the highest GPA found so far
        for studentID in studentDict: # Check each student's record in the given dict
            if studentDict[studentID].gpa > highestGPA: # if the GPA for the current student ID is higher than the one we found so far...
                highestGPAStudentID = studentID # ... store their ID as the highest GPA we found so far...
                highestGPA = studentDict[studentID].gpa # ... then record their GPA as the highest GPA we found so far...
        print('\nStudent with the highest GPA is:') # now tell the user the student with the highest GPA
        print('Student ID:',highestGPAStudentID) # NOTE: If there are two or more students with the highest GPA (as in if the highest GPA is 3.5)
        print(studentDict[highestGPAStudentID]) # and more than student has that GPA, this function will return the student with the highest ID
        # I would have created a list of students with sharing the highest GPA, but, the spec just said to print the student with the highest GPA...
    else:
        print('No students on file. Please add some students, then try again!')

def updateGPA(idToUpdate, studentDict, gpa):
    # This function will check if the idToUpdate is in the dict, and if it is
    # then we will update that record with the GPA given. If the ID does not exist,
    # we will tell the user that no changes were made.
    if idToUpdate in studentDict.keys():
        studentDict[idToUpdate].gpa = gpa
        print('Student ID',idToUpdate,'updated to',gpa)
    else:
        print('ID not found, no changes made.')

def askAndUpdateGPA(studentDict):
    # This routine is a wrapper for the updateGPA functuion. It will
    # ask the user for the ID of the student to update, and the new GPA, then
    # pass that info to the updateGPA function. Again, I would have combined them
    # all into one function, but, the spec is the spec.... :)
    # Note: If there are no students in the given dict, tell the user, and do nothing.
    if len(studentDict) > 0:
        try: # If the user enters something other than a number, these statements will cause an exception so we want to handle it
            idToUpdate = int(input('Please enter the ID for the student you want to update -> ')) # Convert the entry to an int, because the dict keys are ints
            newGPA = float(input('Please enter the new GPA for the student -> ')) # and convert this entry to a float, because thats what's in the dict
            updateGPA(idToUpdate, studentDict, newGPA) # finally, we update the dict with the new GPA
        except ValueError:  # user enters something other than a number, or nothing at all...
            print('Sorry, I was expecting a number, No action taken.')
    else:
        print('No students on file. Please add some students, then try again!')

def findStudent(studentDict, idToFind):
    # In this function we are given the dict and the id, so we are going to see if the
    # student ID exists in the dictionary. If it does, then we will print the student record
    # if not, we will tell the user that the ID entered is not on file.
    if idToFind in studentDict.keys():
        print('Information for student ID:', idToFind)
        print(studentDict[idToFind])
    else:
        print('Sorry, that ID is not on file.')

def findGPA(studentDict, GPA):
    # This routine will step through the given studentDict and will create a list
    # of the student IDs where the gpa is equal or higher to the given gpa, and at
    # the end, the list of the students will be printed.
    gpasToPrint = [] # This will be our list of students we will need to print
    for studentID in studentDict:
        if studentDict[studentID].gpa >= GPA: # if the current student's GPA is higher than the GPA we are looking for...
            gpasToPrint.append(studentID) # ...add it to the list
    if len(gpasToPrint) > 0: # If the list is not empty, print the list
        for studentId in gpasToPrint: # step through the each entry in our list
            print('Student ID:', studentId) # print the ID
            print(studentDict[studentId]) # and the student record for that ID
    else: # we didn't find any students meeting the criteria so tell the user
        print('No students found with a GPA equal to or higher than', GPA)

def askGPAsToFind(studentDict):
    # This is a wrapper for the findGPA function. We will ask the user for the
    # GPA to find, and then we will give that to findGPA function which will print
    # the list of students with a GPA higher or equal to the GPA given.
    # NOTE: As always, if the given dict is empty, tell the user and do nothing...
    if len(studentDict) > 0:
        try: # If the uer enters a non-numeric entry, or nothing at all, we want to handle it gracefully...
            gpaToFind = float(input('Please enter the GPA to find. Students with a GPA higher than\nor equal to the given GPA will be printed. -> '))
            findGPA(studentDict, gpaToFind) # convert the user's entry to a float, then call the findGPA function to actually look for the GPAs
        except ValueError: # User entered a non-numeric entry or nothing at all...
            print('Sorry, I was looking for a number. No action taken.\n')
    else:
        print('No students on file. Please add some students, then try again!') 

def findMajor(studentDict, major):
    # This function will search through the given studentDict for each student with
    # a major equal to the given major. Note that for when comparing, all the comparisions
    # will be done in lower case, so that if a student's major is entered as MATH, Math, or math,
    # or even MaTh, the search will match. Each studen ID will be added to a list, then
    # the students in the list will be printed.
    foundStudents = [] # This is where we will keep the students we find
    for studentID in studentDict:
        if studentDict[studentID].major.lower() == major.lower(): # compare the lowercase version of the major in the current student record to the lowercase version of the given major
            foundStudents.append(studentID) # If they match, add it to the list
    if len(foundStudents) > 0: # If we found any students, print the list of the students we found...
        print('Found the following students:')
        for studentID in foundStudents: # Loop through the list
            print('Student ID:', studentID) # ...and print each student's ID...
            print(studentDict[studentID]) # ...and their record
    else: # Nobody found with that major, so tell the user
        print('Sorry. No students found with major', major)

def askMajorToFind(studentDict):
    # This is a wrapper for the findMajor function. Here we will ask for the major to find
    # and pass the given dict and the major to the findMajor function
    # Also, this is where we check if the given dict is empty. if it is, we tell the user and then do nothing
    if len(studentDict) > 0:
        majorToFind = input('\nFind all students with which major? ')
        findMajor(studentDict, majorToFind)
    else:
        print('No students on file. Please add some students, then try again!')

def updateMajor(studentDict, idnumber, major):
    # This routine will update the record by the given idnumber in the given studentDict,
    # with the given major. Once done, the user will be told it has been update, and 
    # if the idnumber isn't found, the user will be told that no action was taken.
    if idnumber in studentDict.keys():
        studentDict[idnumber].major = major
        print('Record updated! New record for student',idnumber)
        print(studentDict[idnumber])
    else:
        print('ID not found. No action taken.\n')

def askIDToUpdateMajor(studentDict):
    # This routine will ask what student to update, and the new major, then will
    # send that info to the updateMajor function which will handle the actual updating
    # of the student record in the dictionary.
    # Note: If there are no entries in the given dict, tell the user and do nothing.
    if len(studentDict) > 0:
        try: # If the user enters a non-numeric entry, or nothing at all, we want to handle it gracefully...
            idToUpdate = int(input('What student ID would you like to upate? ')) # Find out what student ID we want to update, convert it to an int
            majorToUpdate = input('Please enter the new major -> ') # and find out what major we want that student to have
            updateMajor(studentDict, idToUpdate, majorToUpdate) # Note: There is no checking for what major is entered. Since it is a string, the user can enter anything and it wll be the new major
        except ValueError: # User entered a non-numeric entry, or nothing at all so tell the user
            print('Sorry, all Student IDs are a five digit number. No action taken.')
            print('Returning to the main menu.')
    else:
        print('No students on file. Please add some students, then try again!')


def showMenu():
    # This function simply shows the user the main menu
    print('\nXYZ Community College Student Management System')
    print('-----------------------------------------------')
    print('A - Add student')
    print('F - Find student by ID')
    print('G - Find the student with the highest GPA')
    print('L - List all students with a GPA equal to or higher than a given GPA')
    print('M - Update a student\'s major')
    print('P - Print a list of all students')
    print('U - Update a student\'s GPA')
    print('R - Find all students with a given majo(R)')
    print('Z - Clear database and add example student data to database (debug!)')
    print('Q - Quit')

def addExampleStudents(studentDict):
    # This function will empty out, then add a few example students to the given studentDict
    # This is primarily a debug functions, but, I'm leaving it in so the user doesn't need
    # to add a bunch of students for testing.
    studentDict.clear() # Clear the database
    # Now, let's add some example students
    addStudent(studentDict, StudentClass.Student('Rick', 'Miller', 3.55, 'Engineering'), nextAvailableStudentNumber)
    addStudent(studentDict, StudentClass.Student('Steve', 'Miller', 2.51, 'Basketweaving'), nextAvailableStudentNumber)
    addStudent(studentDict, StudentClass.Student('John', 'Doe', 2.01, 'Chemistry'), nextAvailableStudentNumber)
    addStudent(studentDict, StudentClass.Student('Harry', 'Potter', 3.95, 'Magic'), nextAvailableStudentNumber)
    addStudent(studentDict, StudentClass.Student('Ron', 'Weaseley', 3.21, 'Magic'), nextAvailableStudentNumber)
    addStudent(studentDict, StudentClass.Student('Kent', 'Dorfman', 0.01, 'Chemistry'), nextAvailableStudentNumber)
    print('Database cleared and example students added!')


# *** MAIN PROGRAM BEGINS HERE ***
# First, show the user the menu
showMenu()

userInput =''
# Repeat the following until the user enters 'q'
while userInput != 'q':
    try:
        userInput = input('\nMain Menu: Enter your choice (? for menu) -> ')[0].lower()
        if userInput == 'a':
            addNewStudent(currentStudents)
        elif userInput == 'p':
            printAll(currentStudents)
        elif userInput == 'f':
            findStudentByID(currentStudents)
        elif userInput == 'g':
            largeGPA(currentStudents)
        elif userInput == 'l':
            askGPAsToFind(currentStudents)
        elif userInput == 'u':
            askAndUpdateGPA(currentStudents)
        elif userInput == 'm':
            askIDToUpdateMajor(currentStudents)
        elif userInput == 'z':
            addExampleStudents(currentStudents)
        elif userInput == 'r':
            askMajorToFind(currentStudents)
        elif userInput == 'q':
            pass # Do nothing here, we just want to exit the loop.
        else:
            showMenu()
    except IndexError: # user entered an empty string, or something weird happened so show them the menu.
        showMenu()

# If the user entered 'q', we end up here, so it's the end of the program, so tell the user
print('End of program.')