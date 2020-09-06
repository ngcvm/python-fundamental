'''
Bai 7.5
@author: packkkk
'''
#Code goes here!!!

# tuple_a = tuple(int(i.strip()) for i in input("Input tuple a (separate by ','): ").split(','))
# tuple_b = tuple(int(i.strip()) for i in input("Input tuple b (separate by ','): ").split(','))

tuple_a = tuple(map(int, input("Input tuple a (separate by ','): ").split(',')))
tuple_b = tuple(map(int, input("Input tuple b (separate by ','): ").split(',')))

print('Tuple a: ', tuple_a)
print('Tuple b: ', tuple_b)
tuple_c = tuple(tuple_a + tuple_b)
print('Tuple c: ', tuple_c)
tuple_d = tuple(sorted(tuple_c))
print(type(tuple_d))
print('Tuple d: ', tuple_d)
print('Tuple_d[3] = ', tuple_d[3])
print('Last 3 elements of tuple d = ', tuple_d[-3:])