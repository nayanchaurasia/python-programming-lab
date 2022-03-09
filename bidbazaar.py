'''big bazaar if shopping amt: then discount
   >25000         25percent
   10000-25000      10 per
   <10000           5 per    '''
n=int(input("enter the shopping amt\n"))
if n>25000:
    p=n/5
    print("the amount to be paid is ",n-p)

elif n>=10000 and n<=25000:
     p=n/10
     print("the amount to be paid is ",n-p)

else :
     p=n/20
     print("the amount to be paid is ",n-p)     