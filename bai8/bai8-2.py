''' 
# Bai 5.2
@author: packkkk
'''

def cal_bmi(height, weight):
    return weight / (height * height)

def eval_bmi(bmi):
    if bmi < 18.5:
        return 'Too thin!!!'
    elif bmi < 25:
        return 'Normal'
    else:
        return 'Too fat!!!'

height = float(input('Input height (kg): '))
weight = float(input('Input weight (m): '))

bmi = cal_bmi(height, weight)
print ('BMI: ', bmi)
print(eval_bmi(bmi))