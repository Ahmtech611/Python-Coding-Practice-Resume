Admin_Profile = {
    "Name" : "Demort",
    "Age" : 27,
    "Location" :"New Hampshire, Britain"   
    }

print(Admin_Profile.items())
#print(Admin_Profile.clear())
print(Admin_Profile)
print(Admin_Profile.get("Rollno"))
#print(Admin_Profile["Rollno"])

print(Admin_Profile.keys())

print(Admin_Profile.values())
print(Admin_Profile.update({"Name":"Openhemmer","Country":"Iran"}))
print(Admin_Profile)

# Here’s a complete list of commonly used **Python dictionary methods/functions** with short explanations:

# ---

# ### 🔹 **Basic Dictionary Methods**

# | Method                          | Description                                                                       |
# | ------------------------------- | --------------------------------------------------------------------------------- |
# | `dict.clear()`                  | Removes all items from the dictionary.                                            |
# | `dict.copy()`                   | Returns a shallow copy of the dictionary.                                         |
# | `dict.get(key, default)`        | Returns the value for `key` if `key` is in the dictionary, else `default`.        |
# | `dict.items()`                  | Returns a view object of (key, value) pairs.                                      |
# | `dict.keys()`                   | Returns a view object of all keys in the dictionary.                              |
# | `dict.values()`                 | Returns a view object of all values in the dictionary.                            |
# | `dict.pop(key[, default])`      | Removes specified key and returns the value. If key not found, returns `default`. |
# | `dict.popitem()`                | Removes and returns the last inserted (key, value) pair.                          |
# | `dict.update(other_dict)`       | Updates dictionary with key/value pairs from another dictionary.                  |
# | `dict.setdefault(key, default)` | Returns the value of a key. If not present, inserts key with `default` value.     |

# ---

# ### 🔹 **Creating and Initializing**

# | Method                        | Description                                                     |
# | ----------------------------- | --------------------------------------------------------------- |
# | `dict.fromkeys(seq[, value])` | Creates a new dictionary from keys in `seq` with given `value`. |

# ```python
# # Example:
# keys = ['a', 'b']
# d = dict.fromkeys(keys, 0)  # {'a': 0, 'b': 0}
# ```

# ---

# ### 🔹 **Other Useful Functions**

# | Function        | Description                                              |
# | --------------- | -------------------------------------------------------- |
# | `len(dict)`     | Returns the number of key-value pairs in the dictionary. |
# | `key in dict`   | Returns `True` if key is in the dictionary.              |
# | `del dict[key]` | Deletes a specific key from the dictionary.              |

# ---

# ### 🔹 **Example Dictionary Usage**

# ```python
# person = {
#     "name": "Ahmad",
#     "age": 20,
#     "skills": ["Python", "C++"]
# }

# # Access
# print(person.get("name"))        # Ahmad
# print(person["skills"])          # ['Python', 'C++']

# # Update
# person["age"] = 21
# person.update({"city": "Lahore"})

# # Add
# person["country"] = "Pakistan"

# # Delete
# person.pop("city")
# del person["skills"]

# # Loop
# for key, value in person.items():
#     print(key, value)
# ```

# ---

# Would you like a **PDF summary** of all dictionary methods with examples?

print(Admin_Profile.copy())
print(Admin_Profile.popitem())
print(Admin_Profile)
print(Admin_Profile.pop("Location"))
print(Admin_Profile)

print(Admin_Profile.setdefault("Location"))

Keys = ["a", "b", "c"]
Res = dict.fromkeys(Keys, 5)
print(Res)

del Admin_Profile["Age"]
print(Admin_Profile)
del Admin_Profile["Location"]
print(Admin_Profile)