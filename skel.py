"""
Basic Example on how to use E2D Particle 
"""

import pygame
import particle as p

pygame.display.set_caption('E2D Particle Skeleton')
(width, height) = (624,468)
screen = pygame.display.set_mode((width, height))
running = True
env = p.envi((width, height))
env.addParticle(x=5, y=10, speed=1.5, angle=0.8, size=4, mass=1000)
screen.fill(env.color)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          
    for p in env.particles:
      pygame.draw.circle(screen, p.color, (int(p.x), int(p.y)), p.size, p.thick)
      env.update()
      

    pygame.display.flip()
    screen.fill(env.color)
    env.update()
