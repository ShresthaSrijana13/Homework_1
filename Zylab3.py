# Srijana Shrestha
# 1918305
lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
agave_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n\n'))

print('Lemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lemon_juice_cups), 'cup(s) lemon juice')
print('{:.2f}'.format(water_cups), 'cup(s) water')
print('{:.2f}'.format(agave_nectar_cups), 'cup(s) agave nectar\n')

required_servings = float(input('How many servings would you like to make?\n\n'))
print('Lemonade ingredients - yields', '{:.2f}'.format(required_servings), 'servings')
print('{:.2f}'.format(lemon_juice_cups * required_servings/servings), 'cup(s) lemon juice')
print('{:.2f}'.format(water_cups * required_servings/servings), 'cup(s) water')
print('{:.2f}'.format(agave_nectar_cups * required_servings/servings), 'cup(s) agave nectar\n')

print('Lemonade ingredients - yields', '{:.2f}'.format(required_servings), 'servings')
print('{:.2f}'.format((lemon_juice_cups * required_servings/servings)/16), 'gallon(s) lemon juice')
print('{:.2f}'.format((water_cups * required_servings/servings)/16), 'gallon(s) water')
print('{:.2f}'.format((agave_nectar_cups * required_servings/servings)/16), 'gallon(s) agave nectar')
