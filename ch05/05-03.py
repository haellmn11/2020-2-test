str = 'HelloPython!'

print("+ 012345678901")
print(" ", str)
print("- 210987654321")

str = list(str)

while True:
    one, two, three = map(int, input('슬라이스[?:?:?] 3개 입력 >> ').split())
    if one == 0 and two == 0 and three == 0:
        break
    print(str[one:two:three])
print("************** 종료 **************")
