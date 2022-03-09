sal=int(input("enter the basic salary "))
if sal<=10000:
    hra=sal*3/4
    ta=sal*7/10
    print("the salary of the person is ",sal+hra+ta)
elif sal>10000 and sal<=20000:
    ta =hra=sal*4/5
    print("the salary of the person is ",sal+hra+ta)    
else :
    hra=sal*3/10
    ta=sal*19/20
    print("the salary of the person is ",sal+hra+ta)    