#we have rabit and chiken in the farmhouse in whch the head count of them is 72 and there leag count is 200
#find how many rabit and chickens are there
head=72
#head=int(input("enter the toal number of head" ))
leg=200
#leg=int(input("enter the total number of leg"))
lr=4
#lr=int(input("enter the number of legs one rabit has"))
lc=2
#lc=int(input("enter the number of legs one chicken has"))
c=(lr*head-leg)/(lr-lc)
r=head-c

print("the number of rabits are %d"%r)
print("the number of chickens are %d"%c)