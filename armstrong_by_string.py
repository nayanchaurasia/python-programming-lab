s=input('enter the number')
n=int(s)
sum=0
y=len(s)
for i in s:
    sum+=pow(int(i),y)
if sum==n:
    print('ARMSTRONG')    
else:
    print('NOT ARMSTRONG') 
