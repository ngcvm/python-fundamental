'''
Bai 11-2
@author: packkkk
'''

# Code goes here

from bai11modules import write_file

try:
    filename = input('Input filename: ')
    content = input('Input file content: ')
    write_file(filename, content)
except Exception as error:
    print('Error: ', error)
