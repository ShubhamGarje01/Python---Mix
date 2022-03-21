#take array values from user.
import array as arr
arr_in = arr.array('i', []) #declaring empty array

n = int(input("Hey user, enter the length of array:- "))

for i in range(n):
    x = int(input("enter next value:- "))
    arr_in.append(x) #appending x value in empty array
print(arr_in)
    
#searching for index number of user input MANUALLY
ch = int(input("which number you want to search:- "))
if ch not in arr_in:
    print("Number is Not in Array")
else:
    k = 0 #setting counter so we can find index.
    for e in arr_in:
        if e == ch:
            print(k)
            break
        k+=1

#searching for index number of user input using function

print(arr_in.index(ch))
