'''
Bai 11-2
@author: packkkk
'''

# Code goes here

from bai11modules import read_report_file, check_file_exists

try:
    filename = input('Input filename: ')
    flag = 1
    while flag == 1:
        flag = int(input('0 (Any key). Exit, 1: Input file content: '))
        if (flag == 1):
            with open (filename, "w") as f:
                f.write (input ('Input content: '))
                f.close()
        else:
            read_report_file(filename)
            print('Exit!!!')
            break

except EOFError as error:
    print('Error: ', error)
