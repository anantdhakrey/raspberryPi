import pygame

pygame.init()
screen=pygame.display.set_mode((600,500))
'''
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(255,0,255),pygame.Rect(300,300,20,20))
    pygame.display.flip()
    '''
while True:
    for event in pygame.event.get():
        print(event)
ctrl-C    