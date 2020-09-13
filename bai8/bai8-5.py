'''
Bai 8.5
@author: packkkk
'''
import math
PI = math.pi

s_circle = lambda r: PI * math.pow(r, 2)
p_circle = lambda r: 2 * r * PI
s_rectangle = lambda l, w: l * w
p_rectangle = lambda l, w: (l + w) * 2

r = float(input('Input circle radius: '))
l = float(input('Input rectangle length: '))
w = float(input('Input rectangle width: '))

print('S circle = ', s_circle(r))
print('P circle = ', p_circle(r))
print('S rectangle = ', s_rectangle(l, w))
print('S rectangle = ', p_rectangle(w=w, l=l))