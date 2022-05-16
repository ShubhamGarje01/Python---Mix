#Que: Find out the common words from two strings using python

#Before comparing we need to get the unique words by deleting repeated words

def common_words():
    str01 = input("Enter 1st string\n")
    str02 = input("Enter 2nd string\n")
    print("Given String: ", str01, str02)
     # string.split() --> used to slit sentense into words
    s1 = str01.split()
    s2 = str02.split()
    print("splitting of strings: ", s1, s2)
    elist = [] 
    #usinf for loop and if condition we append duplicate elements in empty list
    for i in s1:
        if i in s2:
           elist.append(i)
    print("Common Words from String:", elist)
        

common_words()