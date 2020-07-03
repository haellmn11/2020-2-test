import math
import statistics

def fact(n):
    return math.factorial(n)

def stat(lst):
    return [statistics.median(lst), sum(lst)/len(lst),
            statistics.variance(lst),statistics.stdev(lst)]

print(1, '! = ', math.factorial(1))
print(6, '! = ', math.factorial(6))
print(11, '! = ', math.factorial(11))
print(16, '! = ', math.factorial(16))
print('\n')


if __name__=='__main__':
    mid = [80,99,77,65,92,74,82]
    print(mid)
    print('중앙값: {0:.2f}'.format(stat(mid)[0]))
    print('중앙값: {0:.2f}'.format(stat(mid)[1]))
    print('중앙값: {0:.2f}'.format(stat(mid)[2]))
    print('중앙값: {0:.2f}'.format(stat(mid)[3]))
