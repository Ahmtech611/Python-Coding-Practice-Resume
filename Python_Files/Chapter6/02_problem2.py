Marks1 = int(input("Enter Your marks in Subject1 : "))
Marks2 = int(input("Enter Your marks in Subject2 : "))
Marks3 = int(input("Enter Your marks in Subject3 : "))

total_Percentage = (((Marks1 + Marks2 + Marks3)/300)*100)

if((total_Percentage >= 40) and (Marks1>=33) and (Marks2>=33) and (Marks3>=33)):
    print("Congratulations, you are passed 🥰", total_Percentage)

else:
    print("Ooh, you are fail 😟. Try next time", total_Percentage)
