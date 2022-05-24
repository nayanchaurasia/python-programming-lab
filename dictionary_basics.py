#dct={1:5,2:10,3:15}
#out={}
#for i in dct:
 #       out[i]=dct[i]+10
#print(out)
#ALTERNATIVE WAY
dct={1:5,2:10,3:15}
out={i:dct[i]+10 for i in dct }
print(out)
#this this also known as dictinary comphrehension 
