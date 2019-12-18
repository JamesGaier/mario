import pygame
import Entity
import ImageCutter as ic
class Background(Entity.Entity):
	def __init__(self, w, h, x=0, y=0, image=None):
		super().__init__(x, y, w, h, image)
		
		self.images = ic.ImageCutter()
		self.sky = self.images.sky[0]
	def render(self,screen):
		bg_buffer = pygame.Surface((screen.get_width(), screen.get_height()))
		for x in range(self.pos.x, self.rect.w, 16):
			for y in range(self.pos.y, self.rect.h, 16):
				skyRect = self.sky.get_rect()
				skyRect.x = x
				skyRect.y = y
				bg_buffer.blit(self.sky, skyRect)
		screen.blit(bg_buffer, (0,0))
