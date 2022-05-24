# YOU HAVE TO ENTER TWO LIST AND MADE A 3RD LIST SUCH THAT THE TWO ELEMENTS OF THE TWO LISTS
#IN SAME POSITION ARE PAIRED IN THE TUPLE INSIDE THE LIST
l1=[1,2,3,4,5]
l2=[5,4,3,2,1]
l3=[0 for i in range(len(l1))]
c=0
for i in l1:
    com_to_tup=lambda a,b:(a,b)
    l3[c]=com_to_tup(i,l2[c])
    c+=1
print(l3)