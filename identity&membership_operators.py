#Identity Operators
#used to check whether memory address is similar or not

x = 11
print("Memory location :- ",id(x))
y = 10
print("Memory location :- ",id(y))
print("x is y -->", x is y)
print("x is not y -->", x is not y)
# is & is not are identity operators
# if x and y have same memory address location then true else false

a = "Python"
print("Memory Location :- ", id(a))
b = "Python"
print("Memory Location :- ", id(b))
print("a is b -->", a is b)
print("a is not b -->", a is not b)

l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5]
print("Memory location:- ", id(l1))
print("Memory location:- ", id(l2))
print("l1 is l2 -->", l1 is l2)
print("l1 is not l2 -->", l1 is not l2)
# l1 is not = to l2 because list has diffrent memory locations

## Membership Operators
# it is used to test whether a value or variable is found in sequence or not

# in & not in

list_a = [1, 2, 33, "Python", 69.69]
print("1 in list:-", 1 in list_a)
print("Python in list:- ","Python" in list_a)
print("100 in list:- ", 100 in list_a)
print("100 not in list:- ", 100 not in list_a)