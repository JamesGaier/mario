import mar_math
import pygame
#from ImageCutter import *
class Entity(pygame.sprite.Sprite):
	def __init__(self, x, y, w, h, image):
		super().__init__()
		self.pos = mar_math.Vector2(x, y)
		self.image = image
		#self.image_cutter = ImageCutter()
		self.rect = pygame.Rect(x, y, w, h)
		self.anim_rect = pygame.Rect(x, y, w, h)
		self.static = False
	def render(self, screen):
		if self.image != None:
			screen.blit(self.image, self.rect)
	def update(self, dt, mario=None):
		pass
