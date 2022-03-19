from turtle import *
pensize(2)

ht()
bgcolor('black')
speed(0)
totangle=0
#shape("turtle")
#shapesize(10,10)

for i in range(150):
    pensize(5)
    pencolor('green')
    circle(100)
    pensize(2)
    lt(3)
    pencolor('white')
    circle(150)
    lt(3)
    pencolor('orange')
    circle(200)
    lt(3)
    totangle+=3
    print(totangle)
    if totangle>180:
        break
    
   