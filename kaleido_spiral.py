import turtle

from itertools import cycle
colors=cycle(['red','orange','yellow','green','blue','purple'])


def draw_circle(size,angle,shift):
    turtle,pencolor(next(colors))
    turtle,pencolor(next(colors))
    turtle,circle(size)
    turtle,right(angle)
    turtle,forwart(shift)
    draw_circle(size+5, angle+1,shift+1)


turtle,pencolor('black')
turtle,speed('fast')
turtle,pensize(40)
draw_circle(30,0,1)
