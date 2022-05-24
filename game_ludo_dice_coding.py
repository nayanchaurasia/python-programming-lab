import random
print('enter N for ending the rolling dice')
while 1:
    x=random.randrange(0,7)
    print(x)
    #to hold the screen we will take the input
    y=input('enter for the next value of dice').lower()
    if y=='n':
        break