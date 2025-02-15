'''
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space. 
The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
'''


def compress(string):
    newstr=''
    contador=0
    n=len(string)
    string+=' '
    j=0
    elemen_an=string[0]
    for i in string:
        if elemen_an != i :
            newstr=newstr+elemen_an+str(contador)
            contador=0
        contador+=1
        elemen_an=i
        #j+=1
    return newstr

print(compress('A '))

        

