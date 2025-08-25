p1 = "Click this!"
p2 = "Chance of winning"
p3 = "Buy now"
p4 = "Make lot money"

message = input("Enter your comment here : ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam.")

else:
    print("This comment is not spam.")

