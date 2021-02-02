import random
num=random.randint(1,10)
condition=1
while condition<6:
    guess=int(input('請輸入猜的數字(介於0~10之間)'))
    if(guess<0 or guess>10):
        print('請輸入猜的數字(介於0~10之間)')
    elif(num==guess):
        print('你猜對了')
        print('你猜了',condition,'次')
    elif(guess>num):
        print('太大')
        print('你猜了',condition,'次')
        condition=condition+1
    else:
        print('太小')
        print('你猜了',condition,'次')   
        condition=condition+1    
print('你輸了')
print('答案是',num)    
    
  