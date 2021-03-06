"""
PARTICLE.py
This is the library file that is needed to be included inorder to use particle physics.
"""

import pygame, math, random
drag = 0.999
elasticity = 0.75
gravity = (math.pi,0.002)
(width,height) = (624,468)
"""Init"""
colorchange = 1 #change color dependent on how many bounce? 0=off 1=on
def addVectors((angle1, length1), (angle2, length2)):
  x = math.sin(angle1)*length1 +math.sin(angle2)*length2
  y = math.cos(angle1)*length1 +math.cos(angle2)*length2
  angle = 0.5*math.pi -math.atan2(y,x)
  length = math.hypot(x,y)
  return(angle, length)

def findPar(particles, x, y):
    for p in particles:
        if math.hypot(p.x-x, p.y-y) <= p.size:
            return p
    return None

def collide(p1,p2):
  dx = p1.x - p2.x
  dy = p1.y -p2.y
  dist = math.hypot(dx,dy)
  if dist <p1.size + p2.size:
    p1.hitamount += 1
    if colorchange == 1:
      
      p1.color = (0,(50+p1.hitamount),0)
    tangent = math.atan2(dy,dx)
    angle = 0.5*math.pi+tangent
    angle1 = 2*tangent  -p1.angle
    angle2 = 2*tangent - p2.angle
    speed1 = p2.speed*elasticity 
    speed2 = p1.speed*elasticity
    (p1.angle,p1.speed) = (angle1,speed1)
    (p2.angle,p2.speed) = (angle2,speed2)
    p1.x += math.sin(angle)
    p1.y -= math.cos(angle)
    p2.x -= math.sin(angle)
    p2.y += math.cos(angle)
  
  
    
#Particle
class par():
  def __init__(self, (x,y),size,spot,hitamount):
    self.x = x
    self.y = y
    self.size = size
    self.color = (0,0,255)
    self.thick = 50
    self.speed = 0.01
    self.angle = 0
    self.spot = spot
    self.hitamount = hitamount
  def display(self):
    #pygame.draw.circle(screen,self.color,(self.x,self.y),self.size,self.thick)
    pass
  def move(self):
    (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
    self.x += math.sin(self.angle) * self.speed
    self.y -= math.cos(self.angle) * self.speed
    self.speed *=drag
    

  #bounce function....
  def bounce(self):

    print("i got hit ",self.hitamount)
    if self.x > width - self.size:
      self.x = 2 *(width -self.size) -self.x
      self.angle = -self.angle
      self.speed *= elasticity
    elif self.x < self.size:
      self.x = 2* self.size -self.x
      self.angle = -self.angle
      self.speed *= elasticity
    if self.y > height - self.size:
      self.y = 2 *(height -self.size) -self.y
      self.angle = math.pi -self.angle
      self.speed *= elasticity
    elif self.y < self.size:
      self.y = 2* self.size -self.y
      self.angle = math.pi - self.angle
      self.speed *= elasticity

mypar = []

class envi:
  def __init__(self,(width,height)):
    self.width = width
    self.height = height
    self.particles = []

    self.color = (255,255,255)
    self.elasticity = 0.75
  def addParticle(self, n=1, **kargs):
    for i in range (n):
      size = kargs.get('size', random.randint(10,20))
      mass = kargs.get('mass', random.randint(100,10000))
      x = kargs.get('x',random.uniform(size, self.width-size))
      y = kargs.get('y',random.uniform(size,self.height-size))
      p = par((x,y),size,0,4)
      p.speed = kargs.get('speed',random.random())
      p.angle = kargs.get('angle', random.uniform(0, math.pi*2))
      self.particles.append(p)
  def bounce(self,particle):
  
      print("i got hit ",particle.hitamount)
      if particle.x > width - particle.size:
        particle.x = 2 *(width -particle.size) -particle.x
        particle.angle = -particle.angle
        particle.speed *= elasticity
      elif particle.x < particle.size:
        particle.x = 2* particle.size -particle.x
        particle.angle = -particle.angle
        particle.speed *= elasticity
      if particle.y > height - particle.size:
        particle.y = 2 *(height -particle.size) -particle.y
        particle.angle = math.pi -particle.angle
        particle.speed *= elasticity
      elif particle.y < particle.size:
        particle.y = 2* particle.size -particle.y
        particle.angle = math.pi - particle.angle
        particle.speed *= elasticity    
      
  def update(self):
    for i, particle in enumerate(self.particles):
        particle.move()
        self.bounce(particle)
        for particle2 in self.particles[i+1:]:
            collide(particle, particle2)

  