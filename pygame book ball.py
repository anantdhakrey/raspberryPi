#from the book 'Pygame tutorial documentation, release 2019' by 'Raphael Holzer'

import pygame
from pygame.locals import * #it imports some 280 constants and instead of writing pygame.constant we can directly write constant

width=1920
height=1080
speed=[2,2]
RED=(255,0,0)
running=True


pygame.init()
screen=pygame.display.set_mode((width,height))
ball=pygame.image.load("ball.gif")
ballrect=ball.get_rect()

caption="GRAM 1.0"
pygame.display.set_caption(caption)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    ballrect=ballrect.move(speed)
    if ballrect.left<0 or ballrect.right>width:
        speed[0]= -speed[0]
    if ballrect.top<0 or ballrect.bottom>height:
        speed[1]=-speed[1]

    screen.fill(RED)
    pygame.display.update()
    pygame.display.flip()
    
pygame.quit()
