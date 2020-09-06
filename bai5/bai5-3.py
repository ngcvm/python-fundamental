'''
Bai 5.3
@author: packkkk
'''


n = int(input('Input n: '))
x = float(input('Input x: '))

def cal(expression, n):
    counter = 0
    result = 0
    while counter < n:
        if counter == 0:
            result += expression
        else:
            result *= expression
        counter += 1
    return result

print ('A = (x^2 + x + 1)^n + (x^2 - x +1)^n = {}'.format(cal(x**2 + x + 1, n) + cal(x**2 - x + 1, n)))



