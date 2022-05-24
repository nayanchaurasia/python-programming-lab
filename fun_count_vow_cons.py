def count_vow_cons(word):
    v=0
    c=0
    for i in word:
        if i in "aeiou":
            v+=1
        elif i>='a'or i<='z':
            c+=1
    return v,c
        #RETURNS IN TUPLE FORMATE
st=input('enter the word\n')
st1=st.lower()
x=count_vow_cons(st1)
print(x)
print(f'the vowel count is {x[0]} and ther consonent count is {x[1]}')
