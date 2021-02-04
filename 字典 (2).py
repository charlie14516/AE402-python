d={}


print('#########################')
print('#歡迎使用寬的英文字典')
print('#Welcome to the kuan English dictionary' )

while True:  
    print('=>')
    print('1.建立字典')
    print('2.列出所有單字')
    print('3.英翻中')
    print('4.中翻英')
    print('5.測驗學習成果')
    print('6.離開系統')
    
    sel=input('請輸入欲直行選項')
    if sel=='1':
        while True:
            voc=input('請輸入新單字(按0跳出)')
            if voc == '0':
                break
            if voc not in d:
                m=input('輸入文字解釋')
                d[voc]=m
            else:
                print('單字已存在')
    elif sel =='2':
        lk=sorted(d)
        for item in lk:
            print(item,'的中文是',d[item])
    elif sel =='3':
        voc=input('輸入要調查的英文單字(按0跳出)')
        if voc == '0':
            break
        if voc in d:
            print(d[voc])
        else:
            print('我的字典每有這個單字')
    elif sel =='4':
        got=False
        ch=input('輸入要調查的中文單字(按0跳出)')
        if ch == '0':
            break
        for k,v in d.items():
            if ch == v:
                print(ch,'的英文是',k)
                got=True
        if not got:
            print('抱歉找不到')
    elif sel =='5':
        score=0
        print('這次測驗的滿分是',len(d))
        ans=input()
        for k,v in d.items():
            print(v,'')
            if ans==k:
                score+=1
                print('你答對了!你現在的分數是',score)
            else:
                print('你答錯了!你現在的分數是',score)
    elif sel == 6:
        break
    else:
        print('輸入錯誤，請重新輸入。')
        
            
            
                