import math
lenght = int(input('lenght>>'))
degrees = int(input('angle>>'))
angle = math.pi*degrees/180
height = lenght*math.sin(angle)
print(round(height))
