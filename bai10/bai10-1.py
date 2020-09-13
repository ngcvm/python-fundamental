'''
Bai 10-1
@author: packkkk
'''

# Code goes here
from bai10_modules import cal_avg

x = int(input('Input x: '))
y = int(input('Input y: '))

try:
    print('A = %.2f'%(cal_avg(x, y)))
except ZeroDivisionError as error:
    print('Error: divisor must be <> 0')
