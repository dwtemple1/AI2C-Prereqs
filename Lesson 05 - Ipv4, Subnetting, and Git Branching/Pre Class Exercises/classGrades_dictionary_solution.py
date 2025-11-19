#Create a program to help track students and their grades.
#First ask how many students are in the class
#For each student, ask their name, and their grade (from 1 to 100)
#Display the class average
#Display the highest grade
#Display the lowest grade

#BONUS:  Display the highest scorer

#Note:  This solution only shows how to display the highest scorer using a dictionary.  Class average, highest grade, and lowest grade would be found
#are omitted to make the code more readable.  Those would be found the same way as shown in the classGrades_solution.py file


#Get the number of students
students = int(input("How many students are in the class?  "))

#Build the student dictionary with a for loop
student_dictionary = {}
for __ in range(students):
    name = input("What is the student's name?  ")
    grade = int(input("What is the students' grade?"))
    student_dictionary[name] = grade

#Find the max value in the dictionary
max = max(student_dictionary.values())

#Use a for loop and .items() method to interrogate keys and values together
for key, value in student_dictionary.items():
    if value == max:
        max_scorer = key
        print(max_scorer)

#Note -- if two people score the same high score, both will be printed because we have a print statement on line 27.  If we added
#a print statement later (outside of the for loop), you would only see the last person in the for loop who scored the highest.
#Alternatively, you could initialize an empty list before the for loop, and you could build a max_scorers list to show ties.


