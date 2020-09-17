'''
Bai 11-2
@author: packkkk
'''

# Code goes here

from bai11modules import write_csv, read_telephobe_csv

try:
    filename = input('Input filename: ')
    flag = 1
    content_list = []
    while flag == 1:
        flag = int(input('0 (Any key). Exit, 1: Input file content: '))
        if (flag == 1):
            content = input('Input content: (Split by ","): ')
            content_list.append(map(str, content.split(',')))
        else:
            write_csv(filename, content_list)
            read_telephobe_csv(filename)
            content = []
            print('Exit!!!')
            break
except Exception as error:
    print('Error: ', error)


