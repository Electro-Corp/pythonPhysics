# pythonPhysics
Basic Python physics library. 
Must have pygame installed. 
# How to: 
Sketon program is included.
<br>
    `for p in env.particles:
      pygame.draw.circle(screen, p.colour, (int(p.x), int(p.y)), p.size, p.thickness)`
      
 <br> The code above is required to render particles. 
 <br>
 `import particle as p`
 <br> ^ TO import
 
 <br>
 `env.addParticle(x=5, y=10, speed=1.5, angle=0.8, size=4, mass=1000)`
 <br> ^ Creating particle 
