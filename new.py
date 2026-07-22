import pygame
from random import randint
pygame.init()

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Growing Circles-2!!!!")
#screen color
screen.fill((154, 255, 255))

#color of circle
blue=(0,0,0)

#class is a blueprint
class Circle:
    #property
    def __init__(self,color,pos,radius):
        self.color=color
        self.pos=pos
        self.radius=radius
        self.bg=screen
    #method
    def draw(self):
        pygame.draw.circle(
            self.bg,
            self.color,
            self.pos,
            self.radius
            
        )
mycir=Circle(blue,(300,300),10)
r=randint(0,255)
g=randint(0,255)
b=randint(0,255)
bgcolor=(r, g, b)
run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            r=randint(0,255)
            g=randint(0,255)
            b=randint(0,255)
            screen.fill((r, g, b))
            mycir.draw()
            pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONUP:
                    r=randint(0,255)
                    g=randint(0,255)
                    b=randint(0,255)
                    bgcolor=(r, g, b)
                    mycir.draw()
                    pygame.display.flip()
                    mycir.radius+=10
    screen.fill(bgcolor)
    mycir.draw()
    pygame.display.flip()#updates the circle and bg color on screen
    
pygame.quit()            