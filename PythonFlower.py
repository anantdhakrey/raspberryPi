import turtle as t
i=0
len=300
deg=170
t.speed(0)
t.pencolor('red')
#t.fillcolor('yellow')
t.begin_fill()
while i<50:
    t.fd(len)
    t.rt(deg)
    i+=1
t.end_fill()