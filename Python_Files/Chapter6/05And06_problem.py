# Problem no 5:
list_Names = ["ahmad ali", "AISHA", "Faizan rajpoot", "Shameem-u-Rehan"]

list_Names.append("Rome")

print(list_Names)

enteredNames = input("Enter your name please : ")

if(((enteredNames).capitalize() in list_Names) or ((enteredNames).upper() in list_Names) or ((enteredNames).lower() in list_Names)):
    print("Yes, your name exist in list.")

else:
    print("No, your name is not exit in the list.")

# Problem no 6:

Marks = int(input("Enter your marks please : "))

if((Marks<=100) and (Marks>=90)):
    print("Your grade is Ex!")
elif((Marks<90) and (Marks>=80)):
    print("Your grade is A")
elif((Marks<80) and (Marks>=70)):
    print("Your grade is B")
elif((Marks<70) and (Marks>=60)):
    print("Your grade is C")
elif((Marks<60) and (Marks>=50)):
    print("Your grade is D")
elif(Marks<50):
    print("Your grade is F")

print("Your Marks are : ", Marks)

