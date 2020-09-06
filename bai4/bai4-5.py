'''
Bai 4.5
@author: packkkk
'''

print(''' 
    Room ID         Room name                   Price/night         From 2 - 3 nights                  Over 4 nights

    1               Standard                    1,260,000           Discount 25(%) on 1 night          Discount 30(%) on 1 night
    2               Superior Garden View        1,550,000
    3               Superior Ocean View         1,830,000
    4               Garden View Bungalow        1,830,000
    5               Pool View Bungalow          2,120,000
    6               Family Room                 2,120,000
    7               Beach Front Bungalow        2,540,000
    8               VIP sea view                4,800,000

''')

rooms_and_price = { 1: 1260000, 2: 1550000, 3: 1830000, 4: 1830000, 5: 2120000, 6: 2120000, 7: 2540000, 8: 4800000 }

def cal_total (room_type, nights):
    if (nights < 2):
        return rooms_and_price[room_type]
    elif nights > 1 and nights < 4:
        return (rooms_and_price[room_type] - ( rooms_and_price[room_type] * 25 / 100 )) * nights
    else:
        return (rooms_and_price[room_type] - ( rooms_and_price[room_type] * 30 / 100 )) * nights


def main ():
    room_type = int(input('Input room type: '))
    if room_type < 1 or room_type > len(rooms_and_price):
        print('Sorry, we don\'t have this room type!!!')
        return
    nights = int(input('Input number of nights: '))
    if nights < 1:
        print('Are you serious!!!')
        return
    print ('Total : %.2f'%(cal_total(room_type, nights)))

main()

