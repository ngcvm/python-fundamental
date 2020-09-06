'''
Bai 6.5
@author: packkkk
'''
import math

print ('Calculate ax^2 + bx +c = 0')

a = float(input('Input a: '))
b = float(input('Input b: '))
c = float(input('Input c: '))

if a == 0:
    if b == 0:
        print('Equation has no root!!!') if c != 0 else print ('Equation has unlimit root!!!')
    else:
        print ('Equation has root: x = ', -c/b)
else:
    delta = b*b - (4*a*c)
    if delta < 0:
        print('Equation has no root!!!')
    elif delta == 0:
        print ('Equation has two root: x1 = x2 = ', -1 * (b / (2 * a)))
    else:
        print ('Equation has two separate root: x1 = {}; x2 = {}'.format((-b + math.sqrt(delta)) / (2*a), (-b - math.sqrt(delta)) / (2*a)))

