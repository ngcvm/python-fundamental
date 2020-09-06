'''
Bai 4.1
@author: packkkk
'''

a, b, c, d = list(map(int, input('Input a, b, c, d: ').split()))

print ('a, b, c, d = {} {} {} {}'.format(a, b, c, d))

max = min = a

if b > a:
    max = b
else:
    min = b

if c > a:
    max = b
else:
    min = b

if d > a:
    max = d
else:
    min = d

print ('Max = {}'.format(max))
print ('Min = {}'.format(min))