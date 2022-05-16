#Que: Find out the common letters from two strings using python

#Before comparing we need to get the unique letters by deleting repeated letters


def common_letters():
    str01 = input("Enter First String\n")   
    str02 = input("Enter Second String\n")
    print("Givet word is: ", str01,   str02)

    #to delete duplicate letters we need to pass the string to sets
    s1 = set(str01)
    s2 = set(str02)
    print("Word into sets: ", s1, s2)

    # using & (AND) operator we will print which present in both sets
    print("Common lettre in both words are: ", s1 & s2)

common_letters()
