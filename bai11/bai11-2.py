'''
Bai 11-1
@author: packkkk
'''

# Code goes here
import os
from bai11modules import read_report_file, check_file_exists
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

try:
    filename = input('Input filename: ')
    file = open(os.path.join(CURRENT_DIR, filename), 'r')
    content = file.read()
    read_report_file(filename)
    file.close()
except EOFError as error:
    print('Error: ', error)
    