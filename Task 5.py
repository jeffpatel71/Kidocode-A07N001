from turtle import *
jeff = Turtle()
jeff.shape('turtle')
jeff.speed(100)
colorBox=['green','yellow','blue','orange','purple']
for x in range(2):
    for y in range(5):
        jeff.color(colorBox[y])
        jeff.circle(100)
        jeff.left(360/10)
