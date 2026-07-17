import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

class Rect:
    def __init__(self, color, dims):
        self.color = color
        self.dims = dims

    def draw(self):
        pygame.draw.rect(screen, self.color, self.dims)

greenRect = Rect(green, (50, 20, 100, 100))
redRect   = Rect(red, (150, 200, 150, 150))
blueRect  = Rect(blue, (300, 400, 200, 200))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    greenRect.draw()
    redRect.draw()
    blueRect.draw()
    pygame.display.update()

pygame.quit()
