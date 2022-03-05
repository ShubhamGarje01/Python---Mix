set_var = {"Iron Man", "Hulk", "Captain America", "Shaktiman"}
print(set_var)
print(type(set_var))
set_var.add("Spider Man")
print(set_var)

set_1 = {"captain marvel", "black widow", "she hulk"}
set_2 = {"spider man", "dr. strange", "black widow"}
print(set_2.difference(set_1)) #Present in set 2 but not in set 1
print(set_1.difference(set_2)) #present in set 1 but not in set 2

print(set_2.intersection(set_1)) # common elements in both sets
print(set_1.intersection(set_2)) # common elements in both sets
print(set_1.union(set_var)) #present in both sets or all elements of both sets


