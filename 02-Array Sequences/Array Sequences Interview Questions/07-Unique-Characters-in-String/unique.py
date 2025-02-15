'''
## Problem
Given a string,determine if it is compreised of all unique characters. 
For example, the string 'abcde' has all unique characters and should return True. 
The string 'aabcde' contains duplicate characters and should return false.
'''

'''
def unique(string):

    dictio={}

    for letter in string: 
        if letter in dictio:
            dictio[letter]+=1
        else:
            dictio[letter]=1
        

    for letter in dictio:
        if dictio[letter]!=1:
            return False
    
    return True
'''
#print(unique('adkoe'))

def unico(string):
    seen = set()
    for i in string:
        if i in seen:
            return False
        else: 
            seen.add(i)
    return True

print(unico('hola'))