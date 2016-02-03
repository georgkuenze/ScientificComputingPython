# -*- coding: utf-8 -*-
"""
Created on Sat Aug 01 18:50:45 2015

@author: Georg
"""

# Function to read in student data and create data dictionary
def load(studentfile):
    infile = open(studentfile, 'r')
    data = {}
    for line in infile:
        i = line.find('Name:')
        if i != -1:            # There follows really a name after 'Name:'
            words = line.split(':')
            name = words[1][1:-1]
            #name = ' '.join(words[1:])
        
        elif line.isspace():   # Line is a blank line
            continue
        
        else:                  # This must be a course line
            words = line.split()
            grade = words[-1]
            credit = int(words[-2])
            semester = ' '.join(words[-4:-2])
            course_name = ' '.join(words[:-4])
            data[name] = []
            data[name].append({'title': course_name, 'semester': semester,
                               'credit': credit, 'grade': grade})
    infile.close()
    return data

# Function to calculate average grade
def average_grade(data, name):
    grade2number = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
    number2grade = {grade2number[grade]: grade for grade in grade2number}
    
    summe = 0; weights = 0
    
    for course in data[name]:
        weight = course['credit']
        grade = course['grade']
        summe += weight*grade2number[grade]
        weights += weight
    avg = summe/float(weights)
    return number2grade[round(avg)]

# Function to sort dinctionary according to surname
def sort_name(name1, name2):
    last_name1 = name1.split()[-1]
    last_name2 = name2.split()[-1]
    if last_name1 < last_name2:
        return -1
    elif last_name1 > last_name2:
        return 1
    else:
        return 0

# Name of input data file
studentfile = 'students.dat'

# Make data dictionary
data = load(studentfile)

# Loop over name in data dictionary and calculate average grade
for name in sorted(data, sort_name):
    avg_grade = average_grade(data, name)
    print "%13s: %s" % (name, avg_grade)