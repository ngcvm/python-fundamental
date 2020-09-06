'''
Bai 3.4
@author: packkkk

Result:
    x = 10, y = 4
    x==y is: False
    x!=y is: True
    x>y is: True
    x = 8, y = 9
    x>=y is: False
    x< y is: True
    x<=y is: True
'''

x = 10
y = 4
print('x = %d, y = %d'%(x,y))
equivelence = x==y
print('x==y is', equivelence)
equivelence = x!=y
print('x!=y is', equivelence)
equivelence = x>y
print('x>y is', equivelence)
x = 8
y = 9
print('x = %d, y = %d'%(x,y))
equivelence = x>=y
print('x>=y is', equivelence)
equivelence = x<y
print('x<y is', equivelence)
equivelence = x<=y
print('x<=y is', equivelence)