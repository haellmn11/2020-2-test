import random
lst = [random.randrange(1,99) for i in range(10)]
wlist = list(lst)
print('리스트 ', wlist)
wlist.sort()
print('정렬 리스트 ', wlist)
wlist.sort(reverse=True)
print('역순 리스트 ', wlist)
