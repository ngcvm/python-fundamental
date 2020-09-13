import math

def cal_bmi(height, weight):
    return weight / (height * height)

def eval_bmi(bmi):
    if bmi < 18.5:
        return 'Too thin!!!'
    elif bmi < 25:
        return 'Normal'
    else:
        return 'Too fat!!!'

# Rewrite 5.2
def cal_S(n, x):
    return math.pow((x**2 + 1), n)
    
# Rewrite 5.3
def cal_A(n, x):
    return (x**2 + x + 1)**n + math.pow((x*x - x + 1), n)

# Rewrite 5.4
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

###### bai8-4
def add_list(original_list):
    if not isinstance(original_list, list):
        raise Exception('List type is required!')
    new_el = input('Input new element: ')
    original_list.append(new_el)
    return original_list

def cal_list_sum(original_list):
    if not isinstance(original_list, list):
        raise Exception('List type is required!')
    return sum(original_list)

def occurences(original_tuple, x):
    if not isinstance(original_tuple, tuple):
        raise Exception('Tuple type is required!')
    return original_tuple.count(x) if original_tuple.count(x) != 0 else 0

def print_dictionary(dictonary):
    if not isinstance(dictonary, dict):
        raise Exception('Tuple type is required!')
    for key, value in dictonary.items():
        print('{}: {} \n'.format(key, value))

def search_dictionary(dictionary, key_search):
    if not isinstance(dictionary, dict):
        raise Exception('Tuple type is required!')
    print (dictionary[key_search]) if dictionary.get(key_search) else print('Cannot find this word')

def add_dictionary(dictionary, key_insert, value_insert):
    if not isinstance(dictionary, dict):
        raise Exception('Tuple type is required!')
    dictionary[key_insert] = value_insert
    return dictionary

###### bai8-5
PI = math.pi

s_circle = lambda r: PI * math.pow(r, 2)
p_circle = lambda r: 2 * r * PI
s_rectangle = lambda l, w: l * w
p_rectangle = lambda l, w: (l + w) * 2