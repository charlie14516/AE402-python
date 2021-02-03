n=0
people=int(input('請輸入班上人數'))
scorelist=[]
namelist=[]
scoresum=0
highest=0
lowest=100
highestname=''
lowestname=''
while n<people:
    name=input('請輸入名稱')
    score=int(input('請輸入數學分數'))
    scorelist.append(score)
    namelist.append(name)
    n=n+1

for i in range(people):
    scoresum=scoresum+scorelist[i]
    if(scorelist[i]>highest):
        highest=scorelist[i]
        highestname=namelist[i]
    elif(scorelist[i]<lowest):
        lowest=scorelist[i]
        lowestname=namelist[i]
print('最高分:',highest,highestname)
print('最低分:',lowest,lowestname)
print('平均:',scoresum/people) 