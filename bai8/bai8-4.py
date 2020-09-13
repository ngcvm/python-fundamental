'''
Bai 8.4
@author: packkkk
'''

from bai8_modules import add_list, cal_list_sum, occurences, print_dictionary, search_dictionary, add_dictionary

# def add_list(original_list):
#     if not isinstance(original_list, list):
#         raise Exception('List type is required!')
#     new_el = input('Input new element: ')
#     original_list.append(new_el)
#     return original_list

# def cal_list_sum(original_list):
#     if not isinstance(original_list, list):
#         raise Exception('List type is required!')
#     return sum(original_list)

# def occurences(original_tuple, x):
#     if not isinstance(original_tuple, tuple):
#         raise Exception('Tuple type is required!')
#     return original_tuple.count(x) if original_tuple.count(x) != 0 else 0

# def print_dictionary(dictonary):
#     if not isinstance(dictonary, dict):
#         raise Exception('Tuple type is required!')
#     for key, value in dictonary.items():
#         print('{}: {} \n'.format(key, value))

# def search_dictionary(dictionary, key_search):
#     if not isinstance(dictionary, dict):
#         raise Exception('Tuple type is required!')
#     print (dictionary[key_search]) if dictionary.get(key_search) else print('Cannot find this word')

# def add_dictionary(dictionary, key_insert, value_insert):
#     if not isinstance(dictionary, dict):
#         raise Exception('Tuple type is required!')
#     dictionary[key_insert] = value_insert
#     return dictionary

def main():
    original_list = ['dog', 'cat', 'bear', 'ant']
    original_tuple = ('Ty', 'Suu', 'Dan', 'Dan')
    original_dict = {'bear': 'gau', 'ant': 'kien'}
    task = 1
    while task > 0:
        print('*'.center(50, '*'))
        task = int(input('How can I help you? 0: Exit; 1: Add list; 2: Calculate list sum; 3: Count occurencies in tuple; 4: Print dictionary; 5: Search dictionary; 6: Add dictionary\n'))
        print(('Executing task %i'%task).center(50, '*'))
        if task == 1:
            item = input('Input new item: ')
            original_list.append(item)
        elif task == 2:
            print('Sum of list: ', cal_list_sum(original_list))
        elif task == 3:
            item = input('Input item to find occurence: ')
            print('{} appear {} times in the tuple: '.format(item, occurences(original_tuple, item)))
        elif task == 4:
            print_dictionary(original_dict)
        elif task == 5:
            search_key = input('Input word to search: ')
            search_dictionary(original_dict, search_key)
        elif task == 6:
            dict_key = input('Input word: ')
            dict_value = input('Input meaning: ')
            add_dictionary(original_dict, dict_key, dict_value)
        else:
            print('Exit!!!')        

main()


