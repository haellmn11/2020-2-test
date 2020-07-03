sports = ['축구', '야구', '농구', '배구']
num = [11, 9, 5, 6]

temp = sports[0:4]

for i in range(4):
    temp.insert(i * 2 + 1, num[i])
print("메소드 insert()로 팀원 수 삽입")
print(temp)
print()

for i in range(1, 8, 2):
    sports.insert(i, '')
print("메소드 insert()로 '' 삽입")
print(sports)
print()

sports[1::2] = num
print("슬라이스 sports[1::2]에 num을 대입")
print(sports)
