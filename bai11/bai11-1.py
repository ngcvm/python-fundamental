'''
Bai 11-1
@author: packkkk
'''

# Code goes here

import os
from bai11modules import read_file

try:
    name = input('Input filename: ')
    content = read_file(name)
    print('File content: \n', content)
except EOFError as error:
    print('Error: ', error)
except Exception as error:
    print (error)