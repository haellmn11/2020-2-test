from random import sample

A = set(sample(list(range(1, 21)), 5))
B = set(sample(list(range(1, 21)), 5))

print('A = ', A)
print('B = ', B)
print()

print('A | B = {' + ', '.join(map(str, list(A | B))) + '}')
print('A & B = {' + ', '.join(map(str, list(A & B))) + '}')
print('A - B = {' + ', '.join(map(str, list(A - B))) + '}')
print('A ^ B = {' + ', '.join(map(str, list(A ^ B))) + '}')
 
