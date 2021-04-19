import math
def collistion(r1, x1, y1, r2, x2, y2):
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    if distance < r1+r2:
        return True
    else:
        return False

one_r,one_x,one_y=map(eval, input('>>').split())
two_r,two_x,two_y=map(eval, input('>>').split())
print(collistion(one_r,one_x,one_y,two_r,two_x,two_y))
