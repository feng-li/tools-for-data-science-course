
from random import choice
direction=['left','center','right']
score=[0,0]

for i in range(0,5):
    print('=== Round%d - You Kick! ===' %(i+1))
    print('Choose one side to shoot:') #选择一方向射门
    print('left,center,right')
    you = input()
    print('You kicked '+you)
    com = choice(direction)
    print('Computer saved '+com)
    if you!= com:
        print('Goal!!!')
        score[0] +=1#你得一分
    else:
        print('Oops...')
    print('Score: %d(you) - %d(com) \n' % (score[0],score[1]))

    print('=== Round%d - You Save! ===' %(i+1))
    print('Choose one side to save:') #选择一边救球
    print('left,center,right')
    you = input()
    print('You saved '+you)
    com = choice(direction) # 电脑随机选择射门方向
    print('Computer kicked '+com)
    if you==com:
        print('Saved!')
    else:
        print("Oops...")
        score[1] +=1 # 电脑得一分
    print('Score: %d(you) - %d(com) \n'%(score[0],score[1]))

if score[0]>score[1]:
    print('You win!')
elif score[0]<score[1]:
    print('You lose!')
else :
    print('打平了！！！')
    
