#Project: CIS 177 WEEK 15 FINAL PROJECT
#Project Location: projects\cis177\Week15Project
#File: StudentClass.py
#Purpose: This is the file containing the student class definition for the Week 15 Final Project
#         This file is used in Week15FinalProject.py       
#Revision: 1.0 / 8 MAY 2017
#Created: 8 MAY 2017
#Author: Rick Miller <rick@rickthegeek.com>

class Student(object):
    """This is a class for the student object for CIS 177 Week 15 final project"""

    def __init__(self,firstName ='UNKNOWN',lastName = 'UNKNOWN',gpa = 0,major='Undeclared'):
        self.firstName = firstName
        self.lastName = lastName
        self.gpa = float(gpa)
        self.major = major

    def __str__(self):
        return 'First Name: %s\nLast Name: %s\nGPA: %.2f\nMajor: %s' % (self.firstName, self.lastName, self.gpa, self.major)
