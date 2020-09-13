''' 
# Bai 8.3
@author: packkkk
'''

from bai8_modules import cal_S, cal_A, is_prime_number

n = int(input('Input n: '))
x = float(input('Input x: '))
print('S = (x*x + 1)^n = %.2f'%(cal_S(n, x)))
print ('A = (x^2 + x + 1)^n + (x^2 - x +1)^n = {}'.format(cal_A(n, x)))
number = int(input('Input number: '))
print ('{} {}'.format(number, 'is prime number!!!' if is_prime_number(number) else 'is not a prime number!!!'))
