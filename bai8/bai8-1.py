'''
Bai 8.1
@author: packkkk
'''

ten_heaven_stemscyclical_terms = { 0: 'Canh', 1: 'Tan', 2: 'Nham', 3: 'Quy', 4: 'Giap', 5: 'At', 6: 'Binh', 7: 'Dinh', 8: 'Mau', 9: 'Ky' }
twelve_Earth_stermscyclical_terms = { 0: 'Than', 1: 'Dau', 2: 'Tuat', 3: 'Hoi', 4: 'Tý', 5: 'Suu', 6: 'Dan', 7: 'Mao', 8: 'Thin', 9: 'Tỵ', 10: 'Ngo', 11: 'Mui' }

def yearcheck(year):
    if len(str(year)) >= 1 and len(str(year)) <= 4: ## Check if year has between 1 to 4 numbers and return True.
        return True
    else:
        return False

def get_heaven_terms(year):
    return ten_heaven_stemscyclical_terms[year % 10]

def get_earth_terms(year):
    return twelve_Earth_stermscyclical_terms[year % 12]

birth_year = int(input('Input your birth year: '))

if yearcheck(birth_year) == False:
    raise Exception('Invalid year!!!')

print('{} - {}'.format(birth_year, get_heaven_terms(birth_year) + ' ' + get_earth_terms(birth_year)))