d={}
m=1
n=int(input('enter the number of key value pair'))
for i in range(n):
    k=input('enter the key')
    v=eval(input("enter the numeric value"))
    d.update({k:v})
    m*=v
print('the multipliction of the numeric values of the dicitionary is {}'.format(m))