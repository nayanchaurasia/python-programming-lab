#using random modules
#user to guess the number and return in how many times he/she get it 
import random
count=0
value=random.randrange(0,1001)
#if using randint function then
#value=random.randint(0,1000)..........bez in randint both values are included
while 1:
    count+=1
    user=int(input('enter the number\t'))
    if user==value:
        print('YOU WON!!')
        print(f'your number of counts are {count}')
        break
    elif user>value:
        print('the value is too large')
    elif user<value:
        print('the value is too small')
        

