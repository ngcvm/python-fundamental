''' 
# Bai 5.2
@author: packkkk
'''
from bai8_modules import cal_bmi, eval_bmi

height = float(input('Input height (m): '))
weight = float(input('Input weight (kg): '))

bmi = cal_bmi(height, weight)
print ('BMI: ', bmi)
print(eval_bmi(bmi))