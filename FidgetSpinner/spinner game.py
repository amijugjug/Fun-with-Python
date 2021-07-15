from turtle import *

state = {'turn' : 0}
def draw_spinner():
    clear()
    angle = state['turn'] / 10
    right(angle)
    forward(100)
    dot(120,'red')
    back(100)
    right(120)
    forward(100)
    dot(120,'green')
    back(100)
    right(120)
    forward(100)
    dot(120,'blue')
    back(100)
    right(120)
    update()

def animate_spinner():
    if state['turn']>0:
        state['turn'] -= 1
    draw_spinner()
    ontimer(animate_spinner,20)

def flick():
    state['turn'] += 10

setup(420,420,370,0)
hideturtle()
tracer(False)
width(20)
onkey(flick,'space')
listen()
animate_spinner()
done()
