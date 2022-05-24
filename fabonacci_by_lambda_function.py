
n=int(input('enter the number of terms u want in '))
x=0
y=1
for  i in range(n):
    print(x,end=" ")
    s1=lambda a,b:a+b
    z=s1(x,y)
    y=x
    x=z


