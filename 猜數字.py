guess=int(input('請輸入猜的數字(介於0~10之間)'))
import random
num=random.randint(1,10)
if(guess<0 or guess>10):
    print('請輸入猜的數字(介於0~10之間)')
elif(num==guess):
    print('猜對了')
else: 
    print('你猜錯了')
print('答案是',num) 