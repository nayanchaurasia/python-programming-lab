d1={'name':'nayan','section':'s','roll':36}
d2={'phone':'9696460855','landline':15425871}
for i in d2:
    d1.update({i:d2[i]})
print(d1)
print(d2)