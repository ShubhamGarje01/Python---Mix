# in array we need to have all values of same data type
import array as arr
int_vals = arr.array('i', [2, 5, 3, -7, 8, 6]) #if we gave float value it will cause an error.
print(int_vals)
print("buffer_info:- ", int_vals.buffer_info()) #(memory address, no of elements)
print("Type_code:- ", int_vals.typecode) #data type of array
print()


float_vals = arr.array('f', [2.30, 2.5, 2.60, 2.9, 3.0])
print(float_vals)
print("buffer_info:- ", float_vals.buffer_info())
print("Type_code:- ", float_vals.typecode)
print()


char_vals = arr.array('u', ['a', 'b', 'c', 'D', 'e', 'f'])# cannot use trailling and leading space
print(char_vals)
print("buffer_info:- ", char_vals.buffer_info())
print("Type_code:- ", char_vals.typecode)
print()

#print whole array one-by-one
for i in int_vals:
    print(i)

for i in range(len(float_vals)):
    print(float_vals[i])

for i in range(6):
    print(char_vals[i])

#coping array with data type using for loop

new_arr = arr.array(int_vals.typecode, (i for i in int_vals))
# taking value and assignning it to new_arr variable.
# i before for is for taking value one by one and assign it to variable.
print("New Array:- ", new_arr)

new_arr2 = arr.array(int_vals.typecode, (i * i for i in int_vals))
print(new_arr2)

#printing array one-by-one using while loop

i = 0
while i < len(new_arr2):
    print(new_arr2[i])
    i+= 1

