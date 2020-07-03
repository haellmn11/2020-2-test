def togallon(liter):
    return liter * 0.264
def toliter(gallon):
    return gallon * 3.785

num = int(input('번호 선택 1. 갤론 => 리터 2. 리터 => 갤론 >> '))

if num == 1:
    change = float(input('변환할 갤론은? '))
    total = toliter(change)
    print('{:0.2f} 갤론 == {:0.2f} 리터'.format(change, total))
    
elif num == 2:
    change = float(input('변환할  리터는? '))
    total = togallon(change)
    print('{:0.2f} 리터 == {:0.2f} 갤론'.format(change, total))

