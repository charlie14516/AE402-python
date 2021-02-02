import random
num=random.randint(1,10)
condition=True
while condition:
    guess=int(input('請輸入猜的數字(介於0~10之間)'))
    if(guess<0 or guess>10):
        print('請輸入猜的數字(介於0~10之間)')
    elif(num==guess):
        print('你猜對了')
        condition=False
    else:
        print('你猜錯了')