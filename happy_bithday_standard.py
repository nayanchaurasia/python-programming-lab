from fileinput import close
# w inside the open denoted the permission grant for the open to write inside the file
#see the difference of all the f.write output
f=open('happybirthday','w')
f.write('happy birthday\n')
f.write('god bless u')
f.write('have a good day  ')
f.write('where is the PARTY!!!!!????')
f=close