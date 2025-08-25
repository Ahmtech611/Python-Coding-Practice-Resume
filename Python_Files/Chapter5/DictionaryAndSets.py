#Dictionaries :
Admin_Profile = {
    "Name" : "Demort",
    "Age" : 27,
    "Location" :"New Hampshire, Britain"   
    }

print(Admin_Profile)
print(Admin_Profile["Name"])
print(Admin_Profile["Age"])
print(Admin_Profile["Location"])
print(type(Admin_Profile))
print(type(Admin_Profile["Name"]))
print(type(Admin_Profile["Age"]))

Admin_Profile["Age"] = 14

print(Admin_Profile)
print(Admin_Profile["Age"])

# We should prefer Dictionaries for such a characteristics and assigning values in curly brakets :

# We can code this dictionary terminology in terms of List :
List = [["Name", "Morphious"],["Age", 33],["Address","Bermigam,UK"]]

print(List)
print(List[0])