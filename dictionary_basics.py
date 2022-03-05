#dictionary syntax --> {key:value_for_key, key2:value_for_key2}

dict1 = {1:'sam', 2:'rushya', 3:'vaishu'}
print(dict1)
print(dict1[3])
print(dict1.get(1))
#print(dict1[4])--> will throw error because 4 not exist in dict
print(dict1.get(4)) #--> will not throw error
print(dict1.get(4, 'Not Found'))
print(dict1.get(1, 'Not Found'))
##List to dict conversion
l1 = ['sam', 'rushya', 'vaishu']
l2 = ['python', 'java', 'dumb']

dictf = dict(zip(l1, l2)) #put 2 list in zip and do the typecasting of zip
print(dictf)
print(dictf['sam'])

dictf['shruti'] = 'dumb2' #adding new element to dictionary
print(dictf)

del dictf['rushya']  #deleting from dictionary.
print(dictf)
############################################################

prog = {'JS':'Atom', 'Python':['Pycharm', 'sublime', 'vs code'], 'C':'Turbo C', 
        'Java':{'Java SE':'Netbeans', 'Java EE': 'Eclips'}}
        #passing list in dictionary --> python
        #passing dict in dictionary --> java

print(prog)

print("JavaScript:", prog['JS'])
print(prog['Python'])
print(prog['Python'][1])
print(prog['Java']['Java EE'])


