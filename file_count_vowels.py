y=open('file.txt','r')
lst=y.readlines()
v=['a','e','i','o','u','A','E','I','O','U']
vow=0
for i in lst:
    for j in i:
        if j in v :
            vow+=1
    
print('number of vowel in the file is    ',vow)
y.close