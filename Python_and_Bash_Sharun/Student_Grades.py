Student_Grades = {"Isaki": "A", "Vaidy": "A+", "Sharun": "A"}

#Student_Name = input("Enter Your Name -")
#New_Grade = input("Enter Your Grade -")

#Student_Grades[Student_Name] = New_Grade

#print("Updated Student Grades:")
#print(Student_Grades)

Student_Name = input("Enter the student name: ")

if Student_Name in Student_Grades:
    print('Student found')
    print("Grade:", Student_Grades[Student_Name])

else:
    print('Student not found!')