Set = {0,1,2,3,"Hermoiny Granger"}
print(Set)
Set1 = {0,1,1,1,2,3,"Ron Weasly"}
print(Set1)
Set1.add("Graco Malfoy")
print(Set1)
print(Set1.clear())
print(Set1)

Set2 = set()
print(Set2)
Set3 = {"Graco Malfoy","Romnos",67,90,75}
print(Set3.copy())
print(Set3.pop())
print(Set3)

# Here's a complete list of **Python set operations and functions** you can use:

# ---

# ## 🔹 **Creating Sets**

# ```python
# my_set = {1, 2, 3}
# my_set = set([1, 2, 3])
# ```

# ---

# ## 🔹 **Basic Set Functions**

# | Function        | Description                                | Example                   |
# | --------------- | ------------------------------------------ | ------------------------- |
# | `add()`         | Adds an element                            | `my_set.add(4)`           |
# | `remove()`      | Removes an element (Error if not found)    | `my_set.remove(2)`        |
# | `discard()`     | Removes an element (No error if not found) | `my_set.discard(2)`       |
# | `pop()`         | Removes a random element                   | `my_set.pop()`            |
# | `clear()`       | Removes all elements                       | `my_set.clear()`          |
# | `copy()`        | Returns a shallow copy                     | `new_set = my_set.copy()` |
# | `len()`         | Returns the number of elements             | `len(my_set)`             |
# | `in` / `not in` | Checks membership                          | `3 in my_set`             |

# ---

# ## 🔹 **Set Operations**

# ### 🔸 Mathematical Set Operations

# | Operation                | Symbol | Description                     | Example                                |                     |     |
# | ------------------------ | ------ | ------------------------------- | -------------------------------------- | ------------------- | --- |
# | `union()`                | \`     | \`                              | Combines elements from both sets       | `a.union(b)` or \`a | b\` |
# | `intersection()`         | `&`    | Common elements                 | `a.intersection(b)` or `a & b`         |                     |     |
# | `difference()`           | `-`    | Elements in A but not B         | `a.difference(b)` or `a - b`           |                     |     |
# | `symmetric_difference()` | `^`    | Elements in A or B but not both | `a.symmetric_difference(b)` or `a ^ b` |                     |     |

# ---

# ## 🔹 **Set Comparison**

# | Method         | Description                             | Example           |
# | -------------- | --------------------------------------- | ----------------- |
# | `issubset()`   | True if A is subset of B                | `a.issubset(b)`   |
# | `issuperset()` | True if A is superset of B              | `a.issuperset(b)` |
# | `isdisjoint()` | True if sets have no elements in common | `a.isdisjoint(b)` |

# ---

# ## 🔹 **Update Methods (in-place operations)**

# | Method                          | Description                           | Example                            |
# | ------------------------------- | ------------------------------------- | ---------------------------------- |
# | `update()`                      | Adds elements from another set        | `a.update(b)`                      |
# | `intersection_update()`         | Keeps only common elements            | `a.intersection_update(b)`         |
# | `difference_update()`           | Removes elements found in another set | `a.difference_update(b)`           |
# | `symmetric_difference_update()` | Keeps only elements not in both       | `a.symmetric_difference_update(b)` |

# ---

# ## 🔹 Example

# ```python
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print(a.union(b))                 # {1, 2, 3, 4, 5, 6}
# print(a.intersection(b))          # {3, 4}
# print(a.difference(b))            # {1, 2}
# print(a.symmetric_difference(b))  # {1, 2, 5, 6}
# ```

# ---

# Would you like a **PDF version** of this list or a **YouTube Shorts format** for learning?

# Union funtion :

set4 = {0, "Tent",89,45}

set5 = {13, "Bird", 78,56}

print(set4.union(set5))

print(set5.union(set4))

print(Set2)

print(set4.union(Set2))

print(Set2.union(set5))

#Intersection :

print(set4.intersection(set5))

print(set5.intersection(Set2))

set6 ={12, "loop", 56.78, 46}

set7 ={34, "Hagwarts", 67.98, 46,12}

print(set6.intersection(set7))

#Difference :

print(set6.difference(set7))

print(set7.difference(set6))

set4.discard(45)

print(set4)

set4.remove(89)

print(set4)

