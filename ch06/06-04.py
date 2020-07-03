import random
lst=[]
for i in range(20):
    player1=random.sample(['가위','바위','보오'],1)[0]
    player2=random.sample(['가위','바위','보오'],1)[0]
    lst.append([player1, player2])
print('*'*23)
print('{}     {}     {}'.format('철수','영희','승자'))
print('*' * 23)

cnt1, cnt2, cnt3 = 0, 0, 0
for i in lst:
    if i[0]=='가위':
        if i[1]=='가위':
            cnt3+=1
            result='비김 '+ str(cnt3)
            
        elif i[1]=='바위':
            cnt2+=1
            result='영희 '+ str(cnt2)
            
        else:
            cnt1+=1
            result='철수 '+ str(cnt1)
            
    elif i[0]=='바위':
        if i[1]=='가위':
            cnt1+=1
            result='철수 '+ str(cnt1)
            
        elif i[1]=='바위':
            cnt3+=1
            result='비김 '+ str(cnt3)
            
        else:
            cnt2+=1
            result='영희 '+ str(cnt2)
            
    else:
        if i[1]=='가위':
            cnt2+=1
            result='영희 '+ str(cnt2)
            
        elif i[1]=='바위':
            cnt1+=1
            result='철수 '+ str(cnt1)
            
        else:
            cnt3+=1
            result='비김 '+ str(cnt3)
    print('{}\t{}\t{}'.format(i[0],i[1],result))
    
print()
print('총 게임 회수:', len(lst))
print('철수 승률', cnt1/len(lst))
print('영희 승률', cnt2/len(lst))

