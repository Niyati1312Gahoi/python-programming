#write a python program to calculate the distance between two coordinate
x1=eval(input("enter first x coordinate"))
y1=eval(input("enter first y coordinate"))
x2=eval(input("enter second x coordinate"))
y2=eval(input("enter second y coordinate"))

dis=((x2-x1)**2 + (y2-y1)**2)**.5
print(f'distance between {x1,y1} and {x2,y2} is {dis}')
