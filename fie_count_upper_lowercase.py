y=open('file.txt','r')
lst=y.readlines()
nol=len(lst)
noup=0
nolw=0
for i in lst:
    for j in i:
        if (j>='a' and j<'z') :
            nolw+=1
        if  (j>='A' and j<'Z'):
            noup+=1

print('number of upper case in the file is    ',noup)
print('number of loer case in the file is    ',nolw)

y.close