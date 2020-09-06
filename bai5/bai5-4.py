'''
Bai 5.4
@author: packkkk
'''

import math

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

number = int(input('Input number: '))

print ('{} {}'.format(number, 'is prime number!!!' if is_prime_number(number) else 'is not a prime number!!!'))

