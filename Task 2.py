from turtle import *
jeff = Turtle()
jeff.shape('turtle')
jeff.color('green')
jeff.speed(10)
def pentagon(size):
    for x in range(5):
        jeff.forward(size)
        jeff.left(360/5)

def jump(x,y):
    jeff.penup()
    jeff.goto(x,y)
    jeff.pendown()

pentagon(50)
jump(150,0)
pentagon(50)
jump(300,0)
pentagon(50)
jump(450,0)
pentagon(50)
jump(600,0)
