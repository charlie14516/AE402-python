math_score=input('請輸入數學成績')
english_score=input('請輸入英文成績')
math_score=int(math_score)
english_score=int(english_score)
if(english_score>=90 and math_score>=90):
    print('有禮物')
elif(english_score<60 and math_score<60):
    print('要處罰')
else:
    print('再加油')