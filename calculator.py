n1=int(input("enter the first number\n"))
op=str(input("enter S for subtraction,A for addition ,M for multiplication,R for remainder and D for divison\n"))
n2=int(input("enter the second number\n"))
if op=="A":
    print(n1+n2)
elif op=="S":
    print(n1-n2)
elif op=="M":
    print(n1*n2)
elif op=="D":
    print(n1/n2)
elif op=="r" :
    print(n1%n2)    
else :
    print("INVALID OPERATION")    