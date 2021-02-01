score=input('請輸入成績')
score=int(score)
if(not(score>0 and score<100)):
    print('請輸入介於0~100之間的數字')
elif(score>=90):
    print('a')
elif(score>=80):
    print('b')
elif(score>=70):
    print('c')
elif(score>=60):
    print('d')
else:
    print('e')