dct={'name':'nayan','section':'s','cpi':9.25,'rolln':36}
dct1=list(dct.keys())
dct2=list(dct.values())
dct1.sort()
print(dct1)
print(dct2)
out=dct.copy()
for i in dct1:
    x=dct.pop(i)
    dct[i]=x
print(dct)    

