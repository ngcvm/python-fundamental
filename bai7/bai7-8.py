''' 
# Bai 7.7
@author: packkkk
'''

#Code goes here!!!
dictionary = {}

task = 1

def print_dictionary():
    print('Eng-Vi Dictionary'.center(50, '='))
    print('English - Vietnamese')
    print('*Number of words: ', len(dictionary))
    for english, vietnamese in dictionary.items():
        print('{} - {}'.format(english, vietnamese))  

while task > 0:
    print('*'.center(50, '*'))
    task = int(input('How can I help you? 0: Exit; 1: Read dictionary; 2: Search; 3: Add; 4: Remove\n'))
    print(('Executing task %i'%task).center(50, '*'))
    if task == 1:
        print_dictionary()
    elif task == 2:
        word = input('Input word: ')
        print('"{}" means "{}" in Vietnamese'.format(word, dictionary[word])) if word in dictionary.keys() else print('There is no word in dictionary ', word)
    elif task == 3:
        word_eng = input('Input word: ')
        word_vi = input('Input vietnamese meaning: ')
        dictionary[word_eng] = word_vi
        print_dictionary()
    elif task == 4:
        word = input('Input word: ')
        if word not in dictionary.keys():
            print('There is no word in dictionary ', word)
        else:
            del dictionary[word]
            print_dictionary()
    else:
        print('Exit!!!')