print("enter the number ")
n=int(input())
dct={}
for i in range(n):
    dctin={}
    print('enter the key')
    k=input()
    print('enter the number')
    num=int(input())
    dctin[k]=num
    print('enter the key of this key value pair')
    key=input()
    dct[key]=dctin
print(dct)
