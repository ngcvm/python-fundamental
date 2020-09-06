'''
Bai 3.5
@author: packkkk

Result:
    Binary of x = 1111, Binary of y = 1100
    x & y = 1100
    x | y = 1111
    x ^ y = 0011
    ~x = 1...10000
    x << 2 = 111100
    x >> 2 = 0011
'''

x = 15
y = 12
print('Binary of x =', bin(x), ', Binary of y =', bin(y))
print('x & y =', bin(x & y))
print('x | y =', bin(x | y))
print('x ^ y =', bin(x ^ y))
print('~x =', bin(~x))
print('x << 2 =', bin(x << 2))
print('y >> 2 =', bin(y >> 2))