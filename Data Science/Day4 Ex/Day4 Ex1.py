#Create csv file (Name, ID, GPA)
#Read the csv file
#Store the GPA in List --> Make it alone another Table
#GPA = [] for the Student
#Calculate the average of GPA
#Read the infotmation of new-student of it --> input fron user
#Insert new GPA in 3rd place in the list

import pandas as pd

dataFrame = pd.read_csv(r"C:\Users\PC\Downloads\Data Science\Exercise\Student.csv")

print("Students Data:\n",dataFrame)
print("_______________________________\n")

gpa= dataFrame["GPA"].tolist()

print("GPA List:",gpa)
print("_______________________________\n")

Average_GPA = sum(gpa) / len(gpa)

print("Average GPA:",Average_GPA)
print("_______________________________\n")

# Read information for the new student from the user
new_id = int(input("Enter new student's ID: "))
new_name = input("Enter new student's name: ")
new_gpa = float(input("Enter new student's GPA: "))

gpa.insert(2,new_gpa)

# Update the DataFrame with the new student
new_student = pd.DataFrame({"ID": [new_id], "Name": [new_name], "GPA": [new_gpa]})
dataFrame = pd.concat([dataFrame.iloc[:2], new_student, dataFrame.iloc[2:]]).reset_index(drop=True)

print("New student information added.\n",dataFrame)





