import turtle as t
t.shape('turtle') #arrow,turtle,circle,square,triangle,classic
t.colormode(255)
t.speed(0) #fastest is 0 else 1-10 where no. represents speed
t.pensize(5)
t.shapesize(2,2,2) 
#colors
t.pencolor("red")
t.pencolor((50,150,100)) #tuple rgb color mode works when colormode is set to 255
t.bgcolor('black')
i=1
t.fillcolor("yellow")
t.begin_fill()

while i<50:
    t.fd(200)
    t.rt(110)
    #t.fd(100)
    #t.lt(110)
    i=i+1
t.end_fill()
'''
t.write('Hello kids!')
t.clone()
t.fd(100)
t.dot(20,"red")
t.fd(100)

def turn(x,y):
    t.left(360)
t.onclick(turn)
#t.hideturtle()
#t.onclick(t.fd(50)) #NW
#t.onscreenclick(t.fd(50)) #NW
#t.reset()
#print('hello Harendra')
'''