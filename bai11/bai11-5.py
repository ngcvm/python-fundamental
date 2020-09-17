'''
Bai 11-2
@author: packkkk
'''

# Code goes here

from bai11modules import read_csv

try:
    filename = input('Input filename: ')
    read_csv(filename)
except EOFError as error:
    print('Error: ', error)
