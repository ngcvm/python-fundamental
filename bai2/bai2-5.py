# Bai 2.5
# author: packkkk

interest_rate = float(input('Input interest rate: '))
money_amount = float(input('Input money amount: '))
months =  float(input('Input time (month(s)): '))

profit = (money_amount * months) * (interest_rate / 100 / 12)
cap_n_prof = money_amount + profit

print ('Profit: {} (currency unit)'.format(profit))
print ('Capital + Profit: {} (currency unit)'.format(cap_n_prof))