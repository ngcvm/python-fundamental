'''
Bai 7.4
@author: packkkk
'''

the_tuple = tuple(input('Input tuple (separate by ","): ').split(','))
the_tuple = tuple([i.strip() for i in the_tuple])
print('Tuple: ', the_tuple)

positive_index = int(input('Input positive index   (from 0 to 9): '))
negative_index = int(input('Input negative index   (from -1 to -9): '))
if positive_index < 0 or positive_index > 9:
    raise Exception('Positive index cannot exceed the range 0 - 9')
if negative_index > -1 or negative_index <-9:
    raise Exception('Negative index cannot exceed the range -9 - -1')

s_find = input('Input string to find: ')
print(type(the_tuple))
print ('Tuple[%i] = %s'%(positive_index, the_tuple[positive_index]))
print ('Tuple[%i] = %s'%(negative_index, the_tuple[negative_index]))
print ('%s appears %i times in the tuple'%(s_find, the_tuple.count(s_find)))

