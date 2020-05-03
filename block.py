import pygame

graphic = pygame.transform.scale(pygame.image.load('images\\asteroidBrown.png'), (90, 110))

class Block(object):
	def __init__(self, y):
		self.x = 700
		self.y = y
		self.height = 70
		self.width = 100
		self.visible = True
		self.movable = True
		self.hitbox = (self.x -3, self.y -3, self.width + 6, self.height + 6)
		self.step = 0

	def draw(self, win):
		if self.x + self.width < 0:
			self.visible = False
		if self.movable:
			self.x -= 5
		self.hitbox = (self.x - 3, self.y + 10, self.width, self.height + 20)
		win.blit(graphic, (self.x, self.y))
