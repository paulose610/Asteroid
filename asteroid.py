import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):
        self.position+=self.velocity*dt
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return None

        log_event('asteroid_hit!!')
        rand_ang = random.uniform(20,50)
        vel1 = self.velocity.rotate(rand_ang)
        vel2 = self.velocity.rotate(-rand_ang)
        new_rad = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x,self.position.y,new_rad)
        a1.velocity = vel1 * 1.2
        a2 = Asteroid(self.position.x,self.position.y,new_rad)
        a2.velocity = vel2 * 1.2
        self.kill()


