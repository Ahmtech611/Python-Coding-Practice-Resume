# Here we learn about the tuples in Python :

tuple1 = ("Jakarta", "Romania", "Serbia", "Macedonia", "Bosnia", "Austria", "Germany", "France", "Spain", "Netherlands", "Sweden", "Norvey", "Denmark")
print(tuple1)
print(tuple1[3])
tuple2 = ("Rome", "England","Wales","Ireland", "Scotland","Washington","NewYork","Los-Angles","Texas")
res_MainTuple = tuple1 + tuple2
print(res_MainTuple)
print(res_MainTuple.count("Serbia"))
res_MainTuple = res_MainTuple * 6
print(res_MainTuple)
print(res_MainTuple.count("Rome"))
print(res_MainTuple.index("Serbia"))
print(res_MainTuple.count("Serbia"))
print(res_MainTuple[3:7])
# min() and max() operations/functions in tuple :
tuple3 = (34,89,75,43,56,90,12,63)
min_Val = min(tuple3)
print(min_Val)
max_Val = max(tuple3)
print(max_Val)
# length or size of tuple :
print(len(res_MainTuple))
# membership operation on tuple :
print("Macedonia" in res_MainTuple)
print("Brussals" in res_MainTuple)
# Unpacking operation/function on Tuple :
a, b, c, d, e, f, g, h = tuple3
print(a, b, c, d, e, f, g, h)
print(d)
print(tuple3)
print(res_MainTuple.index("Bosnia"))