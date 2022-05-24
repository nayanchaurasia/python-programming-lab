#using random modules
#user has to guess the number within 10 turns and return the score of him 
#left chances==score of him
import random
count=10
value=random.randint(0,100)
while count:
    count-=1
    user=int(input('enter the number\t'))
    if user==value:
        print('YOU WON!!')
        print(f'your score is {count}{chr(128526)*2}')
        break
    elif user>value:
        print('the value is too large')
    elif user<value:
        print('the value is too small')
    print(f'chances left {count}')
else :
    print(f'YOU LOSE{chr(128559)*2}')
        

