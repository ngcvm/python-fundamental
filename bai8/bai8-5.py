'''
Bai 8.5
@author: packkkk
'''
from bai8_modules import s_circle, p_circle, s_rectangle, p_rectangle

r = float(input('Input circle radius: '))
l = float(input('Input rectangle length: '))
w = float(input('Input rectangle width: '))

print('S circle = ', s_circle(r))
print('P circle = ', p_circle(r))
print('S rectangle = ', s_rectangle(l, w))
print('S rectangle = ', p_rectangle(w=w, l=l))