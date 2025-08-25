dict = {
         "Ahmad Ali" : "Python",
         "Faizan Rajpoot" : "Cpp",
         "Shameem-u-Rehan" : "JavaScript"
    }

print(dict.keys())
print(dict.values())

print(dict)

print(dict.copy())

print(dict.items())

print(dict["Ahmad Ali"])
print(dict["Faizan Rajpoot"])
print(dict["Shameem-u-Rehan"])

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