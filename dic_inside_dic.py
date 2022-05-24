print("enter the number ")
n=int(input())
dct={}
for i in range(n):
    print('enter the key')
    k=input()
    print('enter the number')
    num=int(input())
    dct[k]=num
print(dct)
keyin=input('enter the key of inside dictionary')
print("enter the number of the dictionary to be added inside the dictionary")
n1=int(input())
dctin={}
for i in range(n1):
    print('enter the key in string formate')
    k1=input()
    print('enter the number')
    num1=int(input())
    dctin[k1]=num1
dct[keyin]=dctin
print(dct)

