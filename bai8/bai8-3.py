''' 
# Bai 8.3
@author: packkkk
'''
import math

# Rewrite 5.2
def cal_S(n, x):
    return math.pow((x**2 + 1), n)
    
# Rewrite 5.3
def cal_A(n, x):
    return (x**2 + x + 1)**n + math.pow((x*x - x + 1), n)

# Rewrite 5.4
def is_prime_number (num):
    if (num < 2):
        return False
    else:
        counter = 2
        counter_guard = 0
        while counter <= math.sqrt(num):
            if num % counter == 0:
                counter_guard += 1
            counter += 1
        return True if counter_guard == 0 else False

n = int(input('Input n: '))
x = float(input('Input x: '))
print('S = (x*x + 1)^n = %.2f'%(cal_S(n, x)))
print ('A = (x^2 + x + 1)^n + (x^2 - x +1)^n = {}'.format(cal_A(n, x)))
number = int(input('Input number: '))
print ('{} {}'.format(number, 'is prime number!!!' if is_prime_number(number) else 'is not a prime number!!!'))
