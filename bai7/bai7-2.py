''' 
# Bai 5.2
@author: packkkk
'''

the_list = []
break_input = 1
while break_input == 1:
    the_list.append(int(input('Input value: ')))
    break_input = int(input('Do you want to add more value? 0 (or anykey): No and 1: Yes'))

x = int(input('Input x: '))

print('List: ', list(the_list))
print('Sum of list: ', sum(the_list))
print('%i appear %i in the list'%(x, the_list.count(x))) if (x in the_list) else print('%i is not in the list')
print('%x is the largest value in the list' % (x)) if (max(the_list) == x) else print('{} is not the largest value in the list \nNumber(s) that larger than {}: {}'.format(x, x, [i for i in the_list if i > x]))