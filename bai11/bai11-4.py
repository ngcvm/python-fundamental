'''
Bai 11-2
@author: packkkk
'''

# Code goes here

from bai11modules import read_report_file, check_file_exists, read_file, file_path

try:
    filename = input('Input filename: ')
    flag = 1
    while flag == 1:
        flag = int(input('0 (Any key). Exit, 1: Input file content: '))
        if (flag == 1):
            with open (file_path(filename), "a", encoding='utf-8') as f:
                f.write (input ('Input content: ') + "\n")
                f.close()
        else:
            read_report_file(filename)
            print('Exit!!!')
            break
except Exception as error:
    print('Error: ', error)
