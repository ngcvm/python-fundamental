'''
Bai 7.1
@author: packkkk
'''

animals = list(input('Input list of animals (separate by ","): ').split(','))
animals = [i.strip() for i in animals]
animal2find = str(input('I want to find: '))
print('Animals: ', list(animals))
print('Number of animals: ', len(animals))
print ('There is a (an) %s in list of animals'%animal2find) if (animal2find in animals) else print ('There isn\'t any %s in the list of animal'%animal2find)



