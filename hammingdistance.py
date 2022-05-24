from msilib.schema import Binary


def ham():
    x=int(input("enter number:"))
    y=int(input("enter number:"))
    z=x^y
    c=0
    r=str(bin(z))
    
    for i in r:
        if i=='1':
            c=c+1
    print(c)        
ham()    