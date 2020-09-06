'''
Bai 5.5
@author: packkkk
'''
import math

def is_prime_number (num):
    if num < 2:
        return False
    else:
        counter = 2
        counter_guard = 0
        while counter <= math.sqrt(num):
            if num % counter == 0:
                counter_guard += 1
            counter += 1
        return True if counter_guard == 0 else False


def cal_A_B (num, mode = 'A'):
    if num < 1:
        return 0
    result = 0
    counter = 0
    while counter <= num:
        if mode == 'A':
            if counter % 2 != 0:
                result += counter
        else:
            if counter % 2 == 0:
                result += counter
        counter += 1
    return result

def cal_C (num):
    if num < 1:
        return 0
    result = 1
    counter = 1
    while counter <= num:
        result *= counter
        counter += 1
    return result

def cal_D (num):
    if num < 1:
        return 0
    result = 1
    counter = 1
    while counter <= num:
        if counter % 3 == 0:
            result *= counter
        counter += 1
    return result

def cal_E (num):
    if num < 1:
        return 0
    result = 0
    counter = 0
    while counter <= num:
        if is_prime_number(counter):
            result += counter
        counter += 1
    return result

number = int(input('Input number: '))

print('A = {}'.format(cal_A_B(number)))
print('B = {}'.format(cal_A_B(number, 'B')))
print('C = {}'.format(cal_C(number)))
print('D = {}'.format(cal_D(number)))
print('E = {}'.format(cal_E(number)))


