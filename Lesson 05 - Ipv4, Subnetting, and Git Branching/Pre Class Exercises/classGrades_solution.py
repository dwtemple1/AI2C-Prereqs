#Create a program to help track students and their grades.
#First ask how many students are in the class
#For each student, ask their name, and their grade (from 1 to 100)
#Display the class average
#Display the highest grade
#Display the lowest grade

#BONUS:  Display the highest scorer

number_of_students = int(input("How many students are in your class?  "))

student_list = []
grade_list = []
highest_grade = 0
lowest_grade = 100

for __ in (range(number_of_students)):
    student_name = input("What is the student's name?  ")
    grade = int(input("What is the students grade?  "))
    student_list.append(student_name)
    grade_list.append(grade)
    if grade > highest_grade:
        highest_grade = grade
    elif grade < lowest_grade:
        lowest_grade = grade
    

    
average = sum(grade_list)/number_of_students
highest_index = grade_list.index(highest_grade)
highest_scorer = student_list[highest_index]

print("The average is", average)
print("The lowest grade is",lowest_grade)
print("The highest grade is", highest_grade)
print(highest_scorer, "scored the highest!")

