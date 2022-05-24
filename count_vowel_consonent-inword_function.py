#funtion of vowel
def vow(word):
    '''this function calculates the number of vowels'''
    vowel=['a','e','i','o','u','A','E','I','U','O']
    vow=0
    for i in word:
        if i in vowel:
            vow+=1
    return vow
#funtion of consonent 
def con(word):
    '''this function calculates the no of consonent in a word '''
    con=0
    if ' ' in word :
        for i in word:
            ascii=ord(i)
            vowel=['a','e','i','o','u','A','E','I','U','O']
            if ((ascii>=65 and ascii<=90) or(ascii>=95 and ascii <=122)) and i not in vowel:
                con+=1
        return con
    else:    
        return len(word)-vow(word)
#main code
st=input('enter the word\n')
print(f'the number of vowels in a word {st} are {vow(st)}')
print(f'the number of consonents in a word {st} are {con(st)}')