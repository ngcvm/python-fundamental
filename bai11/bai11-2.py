'''
Bai 11-1
@author: packkkk
'''

# Code goes here
from bai11modules import read_report_file, read_file

try:
    filename = input('Input filename: ')
    content = read_file(filename)
    read_report_file(filename)
except Exception as error:
    print('Error: ', error)
    