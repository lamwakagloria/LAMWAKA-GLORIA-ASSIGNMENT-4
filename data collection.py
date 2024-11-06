#lists
#sets
#tupples
#diction

#xtics
#-mutable
#-index
#-item

#LISTS
studentNames =["Brenda", "Patricia", "Phiona", "Anita"] #strings
marks = [80,56,78,90] #,intergers
data = ["Brenda", 90, "kamokya"]

#Access the whole list
print("\nWhole list..\t")
print(studentNames, type( studentNames))

#Accessing list items
#indexes (positives indexes)
print('\n...positive indexes...\t')
print(studentNames[0]) # first item
print(studentNames[1]) # second item
print(studentNames[2]) # third item

#indexes (negative indexes)
print('\n...negative indexes...\t')
print(studentNames[-3]) #first item
print(studentNames[-2]) #second item
print(studentNames[-1]) #third item

#Adding new items to the list - Appending 
print('\n...append lists...\t')
studentNames.append("michelle")
print(studentNames)

#insert
print('\n..insert lists...\t')
studentNames.insert(2,"faith")
print(studentNames)

#Assignment
#Print Patricia, Faith, Phiona and Anita
#Add Masha at the 4th position
#Update the name Phiona to Aladina
#Display the length of the students list
#Print all students names using a for loop
#Calculate the total marks for the students marks variable and the answer is 304

#No 1
print("\nNo.1\t")
print(studentNames[1])
print(studentNames[2])
print(studentNames[3])
print(studentNames[4])

#No.2
print('\nNo.2\t')

studentNames.insert(3,"masha")
print(studentNames)

#No.3
print('\nNo.3\t')
studentNames[4]="Aladina"
print(studentNames)

#No.4
print('\nNo.4\t')

print(len(studentNames))

#No.5
print('\nNo.5\t')

for studentname in studentNames:
    print(studentname)

#No.6
print('\nNo.6\t')

Total_marks=sum(marks)
print(f"The total_marks for students variables is {Total_marks}")
