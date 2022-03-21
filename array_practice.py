#sorting array in ascending order.
import array as arr

x_arr =  arr.array('i', [23, 45, 21, 11, 35, 9, 15])
print("Given Array:- ", x_arr)
print("Sorted Array:- ", sorted(x_arr))
print()

#Factorial of given number

import math as m
x = int(input("Enter value to find factorial:- "))
print("The factorial of",x,"is:- ", m.factorial(x))