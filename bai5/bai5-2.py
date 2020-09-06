''' 
# Bai 5.2
@author: packkkk
'''

n = int(input('Input n: '))
x = float(input('Input x: '))
result = 0
index = 1
while index < n:
    if (index == 1):
        result += (x*x + 1)
    else:
        result *= (x*x + 1)
    index += 1

print('S = (x*x + 1)^n = %.2f'%(result))