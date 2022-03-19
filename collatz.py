#the collatz sequence drawing
from turtle import *

shape('turtle')
pensize(5)
pencolor('red')
bgcolor('black')


def collatz(a):
    if a%2==0:
        return(a//2)
    else:
        return(3*a+1)

no=500
collatzno=no

#screen dimensions
xmax=950
xmin=-950
ymax=500
ymin=-500


a=0
while not collatzno==1:
    collatzno=collatz(collatzno)
    if collatzno%2==0:
        rt(90)
    else:
        lt(90)
    fd(collatzno)
    if pos()[0]>xmax and pos()[0]<xmin and pos
    
    a+=1

print('program finsihed. Total numbers to reach one: ',a)