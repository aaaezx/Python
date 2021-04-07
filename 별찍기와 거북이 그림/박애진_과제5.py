for i in range(1, 6):
    for j in range(5-i):
        print(' ', end="")
    for k in range(1, i*2, 1):
        print('*', end="")
    print('')

import turtle
t = turtle.Pen()
t.shape('turtle')
t.left(180)
for i in range(1, 6):
    t.left(72)
    t.circle(50, steps=5)
