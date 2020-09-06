''' 
# Bai 7.3
@author: packkkk
'''
import math

def is_prime_number (num):
    if (num < 2):
        return False
    else:
        counter = 2
        counter_guard = 0
        while counter <= math.sqrt(num):
            if num % counter == 0:
                counter_guard += 1
            counter += 1
        return True if counter_guard == 0 else False

arth_mean_cal = lambda l: sum(l) / len(l)

the_list = []
break_input = 1
while break_input == 1:
    the_list.append(int(input('Input value: ')))
    break_input = int(input('Do you want to add more value? 0 (or anykey): No and 1: Yes'))

negative_nums = [num for num in the_list if num < 0]
positive_nums = [num for num in the_list if num > 0]

print('List: ', list(the_list))
print('Prime numbers in list: ', [i for i in the_list if is_prime_number(i)])
print('Negative numbers in list: ', negative_nums)
print('Positive numbers in list: ', positive_nums)
print('Arithmetic mean of all negative and positive number in the list is: %.2f, %.2f'%(arth_mean_cal(negative_nums), arth_mean_cal(positive_nums)))
print('Max number: %i, Min number: %i'%(max(the_list), min(the_list)))
temp_list = the_list[:] #or the_list.copy() or copy.copy(the_list) or copy.deepcopy(the_list)
the_list.sort()
print('Sort asc with list.sort(): ', the_list)
print('Sort asc with sorted(): ', sorted(temp_list))