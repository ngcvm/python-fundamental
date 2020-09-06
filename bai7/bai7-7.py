''' 
# Bai 7.7
@author: packkkk
'''

#Code goes here!!!
tel_book = {}

task = 1

def print_tel_book():
    print('Tel book'.center(50, '='))
    print('Name - Phone number')
    for contact_name, phone_num in tel_book.items():
        print('{} - {}'.format(contact_name, phone_num))  

while task > 0:
    print('*'.center(50, '*'))
    task = int(input('How can I help you? 0: Exit; 1: Read telephone book; 2: Search; 3: Add; 4: Remove\n'))
    print(('Executing task %i'%task).center(50, '*'))
    if task == 1:
        print_tel_book()
    elif task == 2:
        name = input('Input name: ')
        print('{} has phone number: {}'.format(name, tel_book[name])) if name in tel_book.keys() else print('There is no contact about ', name)
    elif task == 3:
        name = input('Input name: ')
        phone_num = input('Input phone number: ')
        tel_book[name] = phone_num
        print_tel_book()
    elif task == 4:
        name = input('Input name: ')
        if name not in tel_book.keys():
            print('There is no contact about ', name)
        else:
            del tel_book[name]
            print_tel_book()
    else:
        print('Exit!!!')