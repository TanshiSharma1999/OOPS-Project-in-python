import pgzrun
import random

WIDTH = 600
HEIGHT = 600
TITLE = "Shape Drawer"

class Shape:
    def draw(self):
        pass

# Rectangle class
class Rectangle(Shape):
    def __init__(self):
        w = 200
        h = 100
        x = random.randint(0, WIDTH - w)
        y = random.randint(0, HEIGHT - h)
        self.rect = Rect((x, y), (w, h))
        self.color = "RED"

    def draw(self):
        screen.draw.filled_rect(self.rect, self.color)

# Circle class
class Circle(Shape):
    def __init__(self):
        self.radius = 50
        x = random.randint(self.radius, WIDTH - self.radius)
        y = random.randint(self.radius, HEIGHT - self.radius)
        self.pos = (x, y)
        self.color = "BLUE"

    def draw(self):
        screen.draw.filled_circle(self.pos, self.radius, self.color)

# Line class
class Line(Shape):
    def __init__(self):
        self.start = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.end = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.color = "GREEN"

    def draw(self):
        screen.draw.line(self.start, self.end, self.color)

# Store shapes
shapes = []

def draw():
    screen.clear()
    for shape in shapes:
        shape.draw()

def on_key_down(key):
    if key == keys.R:
        shapes.append(Rectangle())
    elif key == keys.C:
        shapes.append(Circle())
    elif key == keys.L:
        shapes.append(Line())

pgzrun.go()