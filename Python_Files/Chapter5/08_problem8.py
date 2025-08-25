dict2 = {}

Name1 = input("Enter your first name :")
Language1 = input("Enter your second name:")

dict2.update({Name1 : Language1})

Name2 = input("Enter your first name :")
Language2 = input("Enter your second name:")

dict2.update({Name2 : Language2})

Name3 = input("Enter your first name :")
Language3 = input("Enter your second name:")

dict2.update({Name3 : Language3})

print(dict2)
print(dict2.items())

# if the keys are same but are different then the latest updated value is assign to key