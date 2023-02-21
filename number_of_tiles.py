#write a pyton program to display the required number of tiles for the floor
import math
lf=eval(input("enter the length of floor "))
bf=eval(input("enter the breadth of floor "))
area_f=lf*bf
lt=eval(input("enter the length of tiles "))
bt=eval(input("enter the length of tiles "))
area_t=lt*bt
tile=math.ceil(area_f/area_t)
print(f'number of tiles required {tile}')
#-(-area_f//area_t))
