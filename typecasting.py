var = 'program in working' #string
var2 = 412 #int
var3 = 69.69 #float
print("type of var:- ", type(var))
print("type of var2:- ", type(var2))
print("type of var3:- ", type(var3))

#string concat (every argument given in quotes is string)

a = 35
b = 15
print(a + b)
#output => 50
#Typecasting is nothing but changing data type of variable
a1 = "35"
b1 = "15"
print(a1 + b1) #same operation but diffrent output
#output => 3515

print(int(a1) + int(b1)) #--> typecasting from string to int for both variables
#output => 50

print(5 * "I am learning PYTHON.\n") #to print 1 statement multiple times

print(5 * str(int(a1) + int(b1))) #str coz we want to repeate the string not perform multiplication.
#converting string to int--addition--again into string--printing 5 times.
print(5 * (int(a1) + int(b1)))  #here multiplication happens string --> int --> addition --> mul by 5.

### user input ###
print("Enter Number: ")
var_in = input()
print("you have entered: ", var_in)

## addition input from user

print("enter 1st no.:- ")
var_a = input()
print("enter 2nd no.:- ")
var_b = input()
add = var_a + var_b
print("addition is:- ", add)
#output is concat of 2 input NOT addition

#for addition we need to do Typecasting.

add1 = int(var_a) + int(var_b) #TYPECASTING
print(add1) #OUTPUT--> addition of 2 numbers.


v = "2"
W = "8"
ans = int(v) * int(W)
print(ans) #output is multiplication.

