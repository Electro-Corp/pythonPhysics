"""
Basic Example on how to use E2D Particle 
"""

import pygame
import particle as p
import random 
pygame.display.set_caption('E2D Particle Skeleton')
(width, height) = (624,468)
screen = pygame.display.set_mode((width, height))
running = True
env = p.envi((width, height))
for i in range(10):
  env.addParticle(x=random.randint(0,100), y=random.randint(0,100), speed=1.5, angle=0.8, size=4, mass=1000)
screen.fill(env.color)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          
    for p in env.particles:
      pygame.draw.circle(screen, (0,0,255), (int(p.x), int(p.y)), p.size, p.thick)
      env.update()
      

    pygame.display.flip()
    screen.fill(env.color)
    env.update()
