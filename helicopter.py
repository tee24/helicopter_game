import pygame

graphics = [pygame.image.load(f"images\helicopter_{i}.png") for i in range(1,9)]
blowUp = [pygame.image.load(f"images\\frame000{i}.png") if i < 10 else pygame.image.load(f"images\\frame00{i}.png") for i in range(0,71)]

class Helicopter(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.width = 70
		self.height = 30
		self.speed = 1 * (self.y - 100)*0.05
		self.hitbox = (self.x + 3, self.y - 3, self.width, self.height + 6)
		self.alive = True
		self.step = 0
		self.explosion = 0

	def draw(self, win):
		if self.alive:
			if self.step + 1 >= 24:
				self.step = 0
			self.hitbox = (self.x + 5, self.y - 3, self.width + 10, self.height + 6)
			win.blit(graphics[self.step//3], (self.x, self.y))
			self.step += 1
		else:
			if self.explosion < 71:
				if self.y < 400:
					win.blit(blowUp[self.explosion], (self.x, self.y))
				else:
					win.blit(blowUp[self.explosion], (self.x, 370))
				self.explosion += 1

	def hit(self):
		self.alive = False

	def reset(self):
		self.alive = True
		self.x = 100
		self.y = 200
		self.explosion = 0
		self.step = 0
