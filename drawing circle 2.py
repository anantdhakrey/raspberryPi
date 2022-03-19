from turtle import *
import random

ht()
speed(0)
color('red')
bgcolor('black')
pensize(2)
colors=['red','blue','green','yellow','cyan','pink']

r=200
angle=7

for i in range(200):
    circle(r)
    color(random.choice(colors))
    #r=r-5
    lt(angle)
    rotation=i*angle
    if rotation==360:
        angle=5