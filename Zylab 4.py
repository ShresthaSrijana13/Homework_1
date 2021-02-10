# Srijana Shrestha
# 1918305
import math
wall_height = float(input('Enter wall height (feet):\n'))
wall_width = float(input('Enter wall width (feet):\n'))
wall_area = int(wall_height * wall_width)
print('Wall area:', wall_area, 'square feet')

paint_needed = (wall_area/350)
print('Paint needed:', '{:.2f}'.format(paint_needed), 'gallons')


Gallons_paint_needed = math.ceil(paint_needed)
print('Cans needed:', Gallons_paint_needed, 'can(s)\n')

paint_Color = input('Choose a color to paint the wall:\n')

paint_colors_cost = {
   'red': 35,
   'blue': 75,
   'green': 23
}


print('Cost of purchasing', paint_Color, 'paint: $' + str(paint_colors_cost[paint_Color]))















