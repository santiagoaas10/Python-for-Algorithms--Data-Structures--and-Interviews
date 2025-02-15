def reversal(str):
    wstring=str.strip()
    word=''
    words=[]
    wstring=wstring+' '
    for letter in wstring:
        if letter == ' ':

            if word!='' and word!=' ':
                words.append(word)
                word=''
                letter=' '
        
        if letter != '' and letter!=' ': 
            word+=letter

    reversed=''
    for word in words[::-1]:
        reversed=reversed+word+' '
    return reversed[:-1]


print(reversal('HOla a  todos jejejeje'))



