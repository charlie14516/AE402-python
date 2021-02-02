math_score=input('請輸入數學成績')
english_score=input('請輸入英文成績')
math_score=int(math_score)
english_score=int(english_score)
if((math_score>=90 and english_score>=90) or math_score==100 or english_score==100):
    print('可得獎學金')
else:
    print('無法得獎學金')
    