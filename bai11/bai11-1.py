'''
Bai 11-1
@author: packkkk
'''

# Code goes here

import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
try:
    name = input('Input filename: ')
    file = open(os.path.join(CURRENT_DIR, name), 'r')
    content = file.read()
    print('File content: \n', content)
    file.close()
except EOFError as error:
    print('Error: ', error)