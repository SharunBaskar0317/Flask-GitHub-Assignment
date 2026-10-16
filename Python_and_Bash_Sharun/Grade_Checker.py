Score = int(input("Enter Your Score \n"))

if Score >= 90:
    Grade = "A"

elif Score >= 80:
    Grade = "B"

elif Score >= 70:
    Grade = "C"

elif Score >= 60:
    Grade = "D"

else:
    Grade = "F"

print("Your Grade is", Grade)