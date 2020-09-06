''' 
# Bai 7.6
@author: packkkk
'''

set1 = set(map(int, input("Input set 1 (separate by ','): ").split(',')))
set2 = set(map(int, input("Input set 2 (separate by ','): ").split(',')))

print ('Set 1: ', set1)
print ('Set 2: ', set2)
print ('Set 1 has {} elements, sum of them = {}'.format(len(set1), sum(set1)))
print ('Set 2 has {} elements, sum of them = {}'.format(len(set2), sum(set2)))
print ('Min set 1 = {}, Max set 1 = {}'.format(min(set1), max(set1)))
print ('Min set 2 = {}, Max set 2 = {}'.format(min(set2), max(set2)))
print ('Pop set 1: ', set1.pop())
print ('Set 1 after pop: ', set1)
print ('Set 1 union Set 2: ', set1 | set2)
print ('Set 1 intersect Set 2: ', set1 & set2)
print ('Set 1, Set 2 symmetric difference: ', set1 ^ set2)
print ('Set 1 asc sorted: ', sorted(set1))
print ('Set 2 desc sorted: ', sorted(set2, reverse=True))
