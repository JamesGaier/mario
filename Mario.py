import pygame
import ImageCutter as ic
import mar_math
import Input as inp
import time
import Entity
class Mario(Entity.Entity):
	def __init__(self, x, y):
		super().__init__(x,y,20,32, ic.ImageCutter().idle[0])
		self.w = 20
		self.h = 32
		self.images = ic.ImageCutter()
		self.index = 0
		self.animation_time = 0.1
		self.current_time = 0
		self.animation_frames = len(self.images.run)
		self.current_frame = 0
		self.x_speed = 200
		self.y_speed = 900
		self.gravity = 100
		self.vel = mar_math.Vector2(0, 0)
		self.jumpPressed = False
		self.onGround = False
	def update(self, dt, entities):
		delta_time = float(dt)/1000


		if inp.Input().keyFired(pygame.K_z):
			self.x_speed = 300
		else:
			self.x_speed = 200
		self.vel.x = int(inp.Input().horizontal()*self.x_speed*delta_time)

		
		if self.jumpPressed != inp.Input().vertical():
			self.jumpPressed = not self.jumpPressed
			if self.onGround and self.jumpPressed:
				self.vel.y += int((-inp.Input().vertical()*self.y_speed)*delta_time)
				self.onGround = False
		else:
			self.vel.y += int(self.gravity*delta_time)

		
		self.pos.x += self.vel.x
		self.pos.y += self.vel.y
		
		
		

		'''
		# temp collision
		if self.pos.y > 608:
			self.pos.y = 608
			self.vel.y = 0
			self.onGround = True
		'''

		
		
		self.rect.x = self.pos.x
		self.rect.y = self.pos.y


	

		


		'''
		self.current_time += float(dt)/1000
		if self.current_time >= self.animation_time:
			self.current_time = 0
			self.index = (self.index + 1) % len(self.anim.run)
			self.image = self.anim.run[int(self.index)]
		'''
	def collision(self, entities):
		for entity in entities:
			e_rect = entity.rect
			if self.rect.x < e_rect.x + e_rect.width\
			and self.rect.x + self.rect.width > e_rect.x\
			and self.rect.y < e_rect.y + e_rect.height\
			and self.rect.y + self.rect.height > e_rect.y:
				return True
		return False

