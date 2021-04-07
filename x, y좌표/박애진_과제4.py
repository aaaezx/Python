import math

def points(x, y, x1, y1):
        return (y1-y)/(x1-x), math.sqrt(math.pow(x1-x,2)+math.pow(y1-y,2))

a, b, c, d=map(int, input('points>> ').split())
if(a!=c):
    slope, distance=points(a,b,c,d)
    print('The slope is', slope, 'and the distance is', distance)

else:
    result=math.sqrt(math.pow(d-b,2))
    print('The slope is infinity and the distance is', result)

