korean = ('정렬', '초보자', '내포', '사전')
english = ('sorting', 'novice', 'comprehension', 'dictionary')

find = input('찾을 단어 입력 ? ')
if find in korean:
    print(english[korean.index(find)])
else: print('단어를 찾을 수 없습니다.')
