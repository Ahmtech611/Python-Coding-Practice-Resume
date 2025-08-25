Age = int(input("Enter your age please :"))

if(Age>=18):
    print("yes, you can cast vote.")
    print("Hope best for you 😊")

elif(Age>0 and Age<18):
    print("You cannot cast the vote because your age is below 18.")    

elif(Age==0):
    print("No, you are under age so you cannot cast the vote.")         

elif(Age<0):
    print("This age number is invald because you entered negative age number!")

else:
    print("No, you cannot cast the vote.")    