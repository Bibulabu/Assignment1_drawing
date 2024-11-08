from turtle import *


speed(20)
bgcolor('black')
lt(120)

for x in range(18):
    for y in range(4):
        pencolor('red')
        pensize(5)
        fd(100)
        rt(90)
    pencolor('orange')
    pensize(3)
    rt(20)
    circle(100)
    pencolor('yellow')
    pensize(2)
    circle(130)

done()
