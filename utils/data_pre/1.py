import itertools
a = ['a','b','c']
b = itertools.permutations(a)
print(b)
for i in b:
    print(''.join(i))


b = [1,5,4,4,2,3]
print(set(b))