import random
score=0
while True:
    
    num = int(input('Enter any number between 1 to 10\nto exit enter 0\n'))
    if(num==0):
        print('your score is {}'.format(score))
        break
        
    random_num = random.randint(1, 10)
    if num == random_num:
        score+=2
        print('\U0001f600')
    else:
        score-=1
        print('\u2639\uFE0F')