d={}
x=int(input('enter the number of keys'))
for i in range(x):
    y=input("enter the key")
    d[y]={}
    k=input()
    v=int(input("enter the values"))
    d[y].update({k:v})
print(d)