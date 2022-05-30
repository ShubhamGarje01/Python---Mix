#Que - find the frequncy words in given string in dictionary format

def words_freq():
 
    str01 = input("Enter string: ")
    print(str01)
    temp = str01.split()
    # string.split() --> used to slit sentense into words
    print(temp)

    empty_dict = {}

    for i in temp:
        if i not in empty_dict.keys(): # taking splitted words askeys of dictionary
            empty_dict[i] = 0 #start value of dict is 0, as soon as word appears in dict we increament
        empty_dict[i] = empty_dict[i] + 1
    print(empty_dict)

words_freq()