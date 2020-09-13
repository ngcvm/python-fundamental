''' 
# Bai 8.6
@author: packkkk
'''
# Code goes here
from functools import reduce
from bai8_modules import is_prime_number

my_list = set1 = list(map(int, input("Input list (separate by ','): ").split(',')))
print ('List', my_list)
print ('List sum = ', map(lambda x, y: x + y, my_list))
print ('List prime numbers: ', list(filter(lambda x: is_prime_number(x), my_list)))
print ('Negatives: ', list(filter(lambda x: x < 0, my_list)))
print ('Positives: ', list(filter(lambda x: x > 0, my_list)))
my_x = int(input('Input x: '))
print ('List numbers larger than x: ', list(filter(lambda x: x > my_x, my_list)))