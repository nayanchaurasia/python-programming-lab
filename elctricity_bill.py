n=int(input("enter the no. of unit of elctricity bill"))
b=0
s=0
if n>250:
    s=n-250
    n=250
    x=s*1.75  #rupees
    b+=x
if  n>150 and n<=250:
    s=n-150
    n=150
    x=s*1.2  # rupees
    b+=x
if n>50 and n<=150:
    s=n-50
    n=50
    x=s*0.5  #rupees
    b+=x
if n<=50:
    x=n*0.2  #rupees
    b+=x    

print ("the elctricity bill is of rupees",b)