#observer pattern
import pygame
import time
class Input:
	def __init__(self):
		self.move_ticks = 0
		self.keys = pygame.key.get_pressed()
	def horizontal(self):
		if self.keys[pygame.K_d]:
			if self.move_ticks == 0:
				self.move_ticks = 20
				return 1
		if self.keys[pygame.K_a]:
			if self.move_ticks == 0:
				self.move_ticks = 20
				return -1
		if self.move_ticks > 0:
			self.move_ticks -= 1
		return 0
	def vertical(self):
		if self.keys[pygame.K_x]:
			if self.move_ticks == 0:
				self.move_ticks = 20
				return 1
		if self.move_ticks > 0:
			self.move_ticks -= 1

		return 0
	def keyFired(self, key):
		return self.keys[key]