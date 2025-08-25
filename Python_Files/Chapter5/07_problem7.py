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

#If the keys are different but their values are same then their are no issues, this is possible.