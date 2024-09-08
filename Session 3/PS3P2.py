#Input
LastName = input("Enter Last Name: ")
MidtermScore = float(input("Enter Midterm Score: "))
FinalExamScore = float(input("Enter Final Exam Score: "))

#Process
TotalExamScore = MidtermScore + FinalExamScore

#Output
print("Student: ", LastName)
print("Total points earned: ", TotalExamScore)