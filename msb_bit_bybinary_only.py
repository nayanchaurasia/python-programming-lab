n=int(input("enter the number\n"))
x= bin(n)
#y=x%10
#print("the most probabile bit of a give number " ,n , "is ",y)

c= n&1
print("the msb of the ",n,"is",c)