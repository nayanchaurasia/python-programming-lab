n=int(input("enter the number\n"))
c=0
for i in range(1,n+1) :
    if n%i==0 :
         c+=1

print("no. of divisor are :%d"%(c))    
