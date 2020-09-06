'''
Bai 4.4
@author: packkkk
'''


print ('''
    Consume ammount/month           Price         
    50kWh                           1484
    51 - 100kWh                     1533       
    101 - 200kWh                    1786
    201 - 300kWh                    2242
    301 - 400kWh                    2503
    From 401kWh                     2587 
''')


def cal_total (comsume_amount):
    if (comsume_amount <= 50):
        return consume_amount * 1484
    elif consume_amount > 50 and consume_amount < 101:
        return (50 * 1484) + (consume_amount - 50) * 1533
    elif consume_amount > 100 and consume_amount < 201:
        return (50 * 1484) + (50 * 1533) + (consume_amount - 100) * 1786
    elif consume_amount > 200 and consume_amount < 301:
        return (50 * 1484) + (50 * 1533) + (100 * 1786) + (consume_amount - 200) * 2242
    elif consume_amount > 300 and consume_amount < 401:
        return (50 * 1484) + (50 * 1533) + (100 * 1786) + (100 * 2242) + (consume_amount - 300) * 2503
    else:
        return (50 * 1484) + (50 * 1533) + (100 * 1786) + (100 * 2242) + (100 * 2503) + (consume_amount - 400) * 2587

consume_amount = int(input('Input comsum ammount (kw): '))

print ('Total : %.2f'%(cal_total(consume_amount)))

