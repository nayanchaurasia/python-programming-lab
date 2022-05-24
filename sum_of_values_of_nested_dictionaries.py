print("enter the length of dictionary ")
n=int(input())
sum=0
dct={}
for i in range(n):
    dctin={}
    print('enter the key')
    k=input()
    print('enter the number')
    num=int(input())
    sum+=num
    dctin[k]=num
    print('enter the key of this key value pair')
    key=input()
    dct[key]=dctin
print(dct)    
print("the sum of the values is ",sum)
