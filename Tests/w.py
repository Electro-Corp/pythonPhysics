"""
MAIN.py
Main file for particle sim. The library file is "particle.py"
"""

import pygame
import random
import math
#bg color
bgcol = (234, 212, 252)
(width, height) = (480, 360)
pygame.font.init()
myfont = pygame.font.SysFont('Sans Serif', 30)
#vars
drag = 0.999
elasticity = 0.75
gravity = (math.pi, 0.0005)
# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)
"""Init"""
colorchange = 0  #change color dependent on how many bounce? 0=off 1=on
#dimenzion/ windo
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('physics')


#def
def addVectors((angle1, length1), (angle2, length2)):
    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2
    angle = 0.5 * math.pi - math.atan2(y, x)
    length = math.hypot(x, y)
    return (angle, length)


def findPar(particles, x, y):
    for p in particles:
        if math.hypot(p.x - x, p.y - y) <= p.size:
            return p
    return None


def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.hypot(dx, dy)
    if dist < p1.size + p2.size:
        p1.hitamount += 1
        if colorchange == 1:

            p1.color = (0, (50 + p1.hitamount), 0)
        tangent = math.hypot(dy, dx) #atan2
        angle = 0.5 * math.pi - tangent
        angle1 = 2 / tangent - p1.angle
        angle2 = 2 / tangent + p2.angle
        speed1 = p2.speed * elasticity
        speed2 = p1.speed * elasticity
        (p1.angle, p1.speed) = (angle1, speed1)
        (p2.angle, p2.speed) = (angle2, speed2)
        p1.x += math.sin(angle)
        p1.y -= math.cos(angle)
        p2.x -= math.sin(angle)
        p2.y += math.cos(angle)


#Particle
class par():
    def __call__(self, (x, y), size, spot, hitamount):

        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 0, 255)
        self.thick = 50
        self.speed = 0.01
        self.angle = 0
        self.spot = spot
        self.hitamount = hitamount

    def __init__(self, (x, y), size, spot, hitamount):
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 0, 255)
        self.thick = 50
        self.speed = 0.01
        self.angle = 0
        self.spot = spot
        self.hitamount = hitamount

    def display(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size,
                           self.thick)

    def move(self):
        (self.angle, self.speed) = addVectors((self.angle, self.speed),
                                              gravity)
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= drag

    def __call__(self):
        print("called")

    #bounce function....
    def bounce(self):

        #print("i got hit ",self.hitamount)
        if self.x > width - self.size:
            self.x = 2 * (width - self.size) - self.x
            self.angle = -self.angle
            self.speed *= elasticity
        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle = -self.angle
            self.speed *= elasticity
        if self.y > height - self.size:
            self.y = 2 * (height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity
        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity


screen.fill(bgcol)

#random
number_of_particle = "d"
if (number_of_particle != "d"):
    number_of_particle = int(number_of_particle)
    mypar = []
    s = 1
    upper = input("Upper limit of size: ")
    lower = input("Lower input of size: ")
else:
    mypar = []
    s = 1
    number_of_particle = 25
    upper = 20
    lower = 10
for n in range(number_of_particle):
    size = random.randint(lower, upper)

    x = random.randint(size, width - size)
    y = random.randint(size, height - size)
    particle = par((x, y), size, s, 0)
    particle.speed = random.random()
    particle.angle = random.uniform(0, math.pi * 0.2)
    particle.spot = n

    mypar.append(particle)
#for par in mypar:
#  par.display()

pygame.display.flip()
selected_particle = None
clock = pygame.time.Clock()


# for adding more particle
def generatePar():
    number_of_particle = 1
    mypar = []
    s = 1
    for n in range(number_of_particle):
        size = random.randint(10, 20)

        x = random.randint(size, width - size)
        y = random.randint(size, height - size)
        #particle = par((x,y),size,s,0)
        #particle.speed = random.random()
        #particle.angle = random.uniform(0,math.pi*0.2)
        #particle.spot = n


        #mypar.append(particle)
def increaseSize(amount):
    (width, height) = (400 * amount, 300 * amount)
    screen = pygame.display.set_mode((width, height))


running = True
while running:
    key_to_function = {
        pygame.K_LEFT: (generatePar()),
        #pygame.K_EQUALS:   (increaseSize(1.3)),
        #pygame.K_MINUS: (increaseSize(0.3))
    }
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            (mouseX, mouseY) = pygame.mouse.get_pos()
            selected_particle = findPar(mypar, mouseX, mouseY)
            if selected_particle:

                selected_particle.color = (255, 0, 0)
        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_particle != None:
                selected_particle.color = (0, 0, 255)
            selected_particle = None
        elif event.type == pygame.KEYDOWN:
            if event.key in key_to_function:
                key_to_function[event.key]
                print("button used lol")

    if selected_particle:

        (mouseX, mouseY) = pygame.mouse.get_pos()
        dx = mouseX - selected_particle.x
        dy = mouseY - selected_particle.y
        selected_particle.angle = 0.5 * math.pi + math.atan2(dy, dx)
        selected_particle.speed = math.hypot(dx, dy) * 0.5

    screen.fill(bgcol)
    for par in mypar:
        par.move()
        par.display()
        par.bounce()
    for i, particle in enumerate(mypar):
        particle.move()
        particle.bounce()
    clock.tick()
    text = "FPS: " + str(clock.get_fps())
    textsurface = myfont.render(text, False, (0, 20, 0))
    text2 = myfont.render("Ball Physics 1.0", False, (0, 0, 0))
    if number_of_particle:
        #print("passed")
        try:
            numbertext = "Ball Selected: " + str(selected_particle.spot)
            number2 = "X: " + str(selected_particle.x) + " Y: " + str(
                selected_particle.y)
        except AttributeError:
            numbertext = "Ball Selected: None"
            number2 = "X:    Y: "

    else:
        numbertext = "None"
    text3 = myfont.render(numbertext, False, (0, 50, 0))
    xy = myfont.render(number2, False, (0, 50, 0))
    screen.blit(textsurface, (0, 20))
    screen.blit(text2, (0, 0))
    screen.blit(text3, (0, 40))
    screen.blit(xy, (0, 60))

    mouse = pygame.mouse.get_pos()
    for i, particle in enumerate(mypar):
        particle.move()
        particle.bounce()

        for particle2 in mypar[i + 1:]:

            collide(particle, particle2)
        particle.display()
    pygame.display.flip()
    screen.blit(textsurface, (0, 0))
