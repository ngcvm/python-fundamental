'''
Bai 6.4
@author: packkkk
'''

n = int(input('Input n: '))
x = float(input('Input x: '))

print ('A = (x^2 + x + 1)^n + (x^2 - x +1)^n = {}'.format(pow(x**2 + x + 1, n) + pow(x**2 - x + 1, n)))

