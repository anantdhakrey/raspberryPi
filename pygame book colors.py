#from the book 'Pygame tutorial documentation, release 2019' by 'Raphael Holzer'

import pygame
from pygame.locals import * #it imports some 280 constants and instead of writing pygame.constant we can directly write constant

BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

YELLOW=(255,255,0)
CYAN=(0,255,255)
MAGENTA=(255,0,255)
GRAY=(127,127,127)
WHITE=(255,255,255)

pygame.init()
screen=pygame.display.set_mode((800,600))

caption="GRAM 1.0"
pygame.display.set_caption(caption)

background=GRAY
#define the key dictionary to avoid many if elses while changing the background
key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE,
            K_y:YELLOW,K_c:CYAN,K_m:MAGENTA,K_w:WHITE}
print(key_dict)

running= True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running=False
      
        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]

    screen.fill(background)
    pygame.display.update()
    
pygame.quit()
