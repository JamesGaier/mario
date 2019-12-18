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
		self.y_speed = 500
		self.gravity = 100
		self.vel = mar_math.Vector2(0, 0)
		self.jumpPressed = False
		self.onGround = False
		self.direction = 1
	def update(self, dt, entities):
		delta_time = float(dt)/1000


		if inp.Input().keyFired(pygame.K_z):
			self.x_speed = 300
		else:
			self.x_speed = 200
		self.vel.x = inp.Input().horizontal()*self.x_speed*delta_time

		
		if self.jumpPressed != inp.Input().vertical():
			self.jumpPressed = not self.jumpPressed
			if self.onGround and self.jumpPressed:
				self.vel.y += (-inp.Input().vertical()*self.y_speed)*delta_time
				self.onGround = False
		if not self.onGround:
			self.vel.y += int(self.gravity*delta_time)
		else:
			self.vel.y = 0
		
		
		
		
		print(self.vel.x, self.vel.y)

		
		
		if self.vel.x != 0:
			self.move_single_axis(int(self.vel.x), 0, entities, delta_time)
		if self.vel.y != 0:
			self.move_single_axis(0, int(self.vel.y), entities, delta_time)

		
	def move_single_axis(self, dx, dy, entities, dt):
				
		self.rect.x += dx
		self.rect.y += dy

		hit_list = pygame.sprite.spritecollide(self, entities, False)
		for entity in hit_list:
			rect = entity.rect
			if dx > 0:
				self.rect.right = rect.left
			if dx < 0:
				self.rect.left = rect.right
			if dy > 0:
				self.rect.bottom = rect.top
				self.land(dt)
			if dy < 0:
				self.rect.top = rect.bottom
		


		'''
		self.current_time += float(dt)/1000
		if self.current_time >= self.animation_time:
			self.current_time = 0
			self.index = (self.index + 1) % len(self.anim.run)
			self.image = self.anim.run[int(self.index)]
		'''
		
	def land(self, dt):
		

		self.vel.y = 0

		self.onGround = True
		

		if self.vel.x < 0:
			self.vel.x = -1 * self.x_speed * dt
			
		
		if self.vel.x > 0:
			self.vel.x = self.x_speed * dt
		
		self.onGround = True