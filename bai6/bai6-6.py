''' 
# Bai 6.6
@author: packkkk
'''

import re

s = str(input('Input s: '))
s_sub = str(input('Input s_sub: '))
s_find = str(input('Input s_find: '))
s_replace = str(input('Input s_replace: '))

temp_list = list(s)
temp_list[0] = temp_list[0].upper()

print ('String s: ', s)
print ('String s with whitespace strip: ', s.strip())
print ('String s start with first character uppercase: ', ''.join(temp_list))
print ('Number of s_sub string appears in string s: ', s.count(s_sub))
print ('String s after find and replace "{}" with "{}": {}'.format(s_find, s_replace, s.replace(s_find, s_replace)))
