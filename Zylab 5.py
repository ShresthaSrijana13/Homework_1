# Srijana Shrestha
# 1918305
print('Davy\'s auto shop services')
Services = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12,
    '-': 0
}
print('Oil change -- $' + str(Services['Oil change']))
print('Tire rotation -- $' + str(Services['Tire rotation']))
print('Car wash -- $' + str(Services['Car wash']))
print('Car wax -- $' + str(Services['Car wax']) + '\n')

service_1 = input('Select first service:\n')
service_2 = input('Select second service:\n\n')

print('Davy\'s auto shop invoice\n')
if service_1 != '-' and service_2 != '-':
    print('Service 1:', service_1 + ',', '$' + str(Services[service_1]))
    print('Service 2:', service_2 + ',', '$' + str(Services[service_2]) + '\n')

else:
    if service_1 == '-' and service_2 == '-':
        print('Service 1: No service')
        print('Service 2: No service')

    elif service_1 == '-':
        print('Service 1: No service')
        print('Service 2:', service_2 + ',', '$' + str(Services[service_2]) + '\n')

    else:
        print('Service 1:', service_1 + ',', '$' + str(Services[service_1]))
        print('Service 2: No service' + '\n')

print('Total:', '$' + str(Services[service_1] + (Services[service_2])))
