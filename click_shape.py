import pygame

pygame.init()

screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Growing Circles!!!!")
#screen color
screen.fill((154, 255, 255))

#color of circle
blue=(45, 30, 255)

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
mycir=Circle(blue,(300,300),50)

bgcolor=(255, 255, 255)
run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255, 255, 255))
            mycir.draw()
            pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONDOWN:
                    bgcolor=(154, 255, 255)
                    mycir.draw()
                    pygame.display.flip()
                    mycir.radius+=10
    screen.fill(bgcolor)
    mycir.draw()
    pygame.display.flip()#updates the circle and bg color on screen
    
pygame.quit()            
