print("enter the number of players ")
n=int(input())
dct={}
sum=0
for i in range(n):
    print('enter the name of a player')
    p=input()
    print('enter the runs scored by him')
    s=int(input())
    dct[p]=s
    sum+=s
print('the total score made by the {} players are {}'.format(n,sum))    

