import random
i=0
while (i<10):
    num= (random.randint(0,10))
    
     
    def action(num):
        if (num==0):
         print('{} = break'.format(num))
        elif(num>0 and num<8 ):
            print('{}=car is acclerated' .format(num)) 

        else:
            print('{}=break are applied' .format(num))
    i+=1       
    action(num)