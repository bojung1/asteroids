import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid (CircleShape):
	def __init__ (self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius, 2)


	def update(self, dt):
		self.position += (self.velocity * dt) 

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			randomangle = random.uniform(20,50)
			assvel1 = self.velocity.rotate(randomangle)
			assvel2 = self.velocity.rotate(-randomangle)
			new_rad = self.radius - ASTEROID_MIN_RADIUS

			new_ass1 = Asteroid(self.position.x, self.position.y, new_rad)
			new_ass2 = Asteroid(self.position.x, self.position.y, new_rad)
			new_ass1.velocity = assvel1 * 1.2
			new_ass2.velocity = assvel2 * 1.2 



