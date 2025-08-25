start_iterater = 1

i = 1

ending_iterater = int(input("Enter your ending index[limit] :"))

tableVal = int(input("Enter the number on which you want : "))

while(start_iterater<=ending_iterater):
    print("Hello World!", start_iterater)
    if(i<=1000):
        print(f"{tableVal} x {i} = {tableVal*i}")
        i+=1
        
    start_iterater+=1
        


print("This program sounds good!")