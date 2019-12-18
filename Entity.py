import mar_math
import pygame
class Entity(pygame.sprite.Sprite):
	def __init__(self, x, y, w, h, image):
		super().__init__()
		self.pos = mar_math.Vector2(x, y)
		self.image = image
		self.rect = pygame.Rect(x, y, w, h)
	def render(self, screen):
		screen.blit(self.image, self.rect)
