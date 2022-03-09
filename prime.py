n=int(input("enter the number"))
c=0
for i in range(2,n) :
    if n%i==0 :
        print(" NOT PRIME")
        break
else :
    print(" PRIME")