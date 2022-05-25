#copy the even one file to other
f=open('filecopy.txt','w')
y=open('file.txt','r')
lst=y.readlines()
for i in range(len(lst)):
    if i%2==0:
        f.writelines(lst[i])
y.close 
f.close
