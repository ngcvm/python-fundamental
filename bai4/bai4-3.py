'''
Bai 4.3
@author: packkkk
'''

print ('''
    Vehicle type            Open door price (vnd/0.8km)         Under 31km (vnd/km)         From 31th km (vnd/km)
    4                       11000                               15300                       12100
    7                       12000                               16100                       13800
''')


available_vehicles = (4, 7)
fees = {
    4: {
        'open_door': 11000,
        'first_30km': 15300,
        'from_31km': 12100
    },
    7: {
        'open_door': 12000,
        'first_30km': 16100,
        'from_31km': 13800
    }
}

def cal_wait_time_fee (travel_distance, wait_time):
    return 0 if wait_time <=5 else 750 * (wait_time - 5)
    
def cal_travel_fee (vehicle_type, travel_distance):
        if (travel_distance <= 0.8):
            return fees[vehicle_type]['open_door']
        elif (travel_distance > 0.8 and travel_distance < 31):
            return fees[vehicle_type]['open_door'] + ((travel_distance - 0.8) * fees[vehicle_type]['first_30km'])
        else:
            return fees[vehicle_type]['open_door'] +  ((31 - 0.8) * fees[vehicle_type]['first_30km']) + ((travel_distance - 31) * fees[vehicle_type]['from_31km'])

vehicle = int(input('Type of vehicle: '))
if (vehicle in available_vehicles):
    travel_distance = float(input('Travel distance (km): '))
    wait_time = int(input('Input wait time (round to minute): '))
    wait_time_fee = cal_wait_time_fee(travel_distance, wait_time)
    travel_fee = cal_travel_fee(vehicle, travel_distance)
    print ('Wait time fee = %.2f'%(wait_time_fee))
    print ('Travel fee = %.2f'%(travel_fee))
    print ('Wait time fee = %.2f + %.2f = %.2f'%(travel_fee, wait_time_fee, travel_fee + wait_time_fee))
else:
    print('Vehicle not found!!!')



