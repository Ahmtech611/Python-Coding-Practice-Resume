list1 = ["Apple","Banana",34.098,655,True,False]

#list1.clear()
print(list1)
list1.append("Fast")
list1.insert(1,78.9)
list1.insert(2,"Apple")
list1.insert(2,456)
list1.append("Alexy")
val1 = list1[0]
val2 = list1[1]
val3 = list1[2]
val4 = list1[3]
val5 = list1[4]
print(val1)
print(val2)
print(val3)
print(val4)
print(val5)
print(list1)
print(list1[0])
print(list1[2])
print(list1[1])
print(list1[3])
print(list1[4])
print(list1[6])
print(list1[8])
print(list1[10])

print(f"The pop(removed) value of this list1[2] list is: {list1.pop(2)}")
print(list1)
print(list1[2])

list2 = [23,78,89,98,12,45,67]

list2.sort()
print(list2)

list2.reverse()
print(list2)

list2.extend("high")
print(list2)

print(list2[2:5])#Returns piece of code or slice from one index to ending index although the ending index is not included:
