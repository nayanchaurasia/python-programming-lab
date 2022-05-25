y=open('file.txt','r')
lst=y.readlines()
nol=len(lst)
now=0
noc=0
for i in lst:
    for j in i:
        if j==' ':
            now+=1

        if (j>='a' and j<'z') or (j>='A' and j<'Z'):
            noc+=1
    now+=1
print('number of line in the file is    ',nol)
print('number of words in the file is    ',now)
print('number of characters in the file is    ',noc)
y.close