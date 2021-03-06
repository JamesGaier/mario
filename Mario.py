import pygame
import Input as inp
import time
import Entity

class Mario(Entity.Entity):
	def __init__(self, x, y, image, images):
		super().__init__(x,y,image.get_rect().w,image.get_rect().h, image)
		self.w = image.get_rect().w
		self.h = image.get_rect().h
		self.images = images
		self.index = 0
		self.animation_time = 0.1
		self.current_time = 0
		self.animation_frames = len(self.images.runL)
		self.current_frame = 0
		self.x_speed = 230
		self.y_speed = 550
		self.gravity = 15
		self.vel = pygame.Vector2(0, 0)
		self.jumpPressed = False
		self.onGround = False
		self.direction = "L"
		self.currentDirection = "L"
	def update(self, dt, entities):
		delta_time = float(dt)/1000
		# if the player pressed z move faster
		if inp.Input().keyFired(pygame.K_z):
			self.x_speed = 275
		else:
			self.x_speed = 230

		# input on the x-axis
		self.vel.x = inp.Input().horizontal()*self.x_speed*delta_time

		# flips mario depending on the direction mario is moving

		if self.currentDirection != self.direction:
			if self.currentDirection == "L":
				self.image = self.images.idle[0]
			elif self.currentDirection == "R":
				self.image = self.images.idleR[0]
			self.direction = self.currentDirection




		# make ground check to check if player hasn't fallen off platform
		# input on the y-axis
		if self.jumpPressed != inp.Input().vertical():
			self.jumpPressed = not self.jumpPressed
			if self.onGround and self.jumpPressed:
				if self.direction == "L":
					self.image = self.images.jumpL[0]
				elif self.direction == "R":
					self.image = self.images.jumpR[0]
				self.vel.y += (-inp.Input().vertical()*self.y_speed)*delta_time
				self.onGround = False
		else:
			self.vel.y += self.gravity*delta_time

		# code for animations
		self.current_time += delta_time
		if self.current_time >= self.animation_time:
			if self.vel.x < 0  and self.currentDirection == "L" \
				and self.onGround:
				self.current_time = 0
				self.index = (self.index + 1) % len(self.images.runL)
				self.image = self.images.runL[int(self.index)]
			elif self.vel.x > 0 and self.currentDirection == "R"\
				and self.onGround:
				self.current_time = 0
				self.index = (self.index + 1) % len(self.images.runR)
				self.image = self.images.runR[int(self.index)]
			else:
				if self.onGround:
					if self.currentDirection == "L":
						self.image = self.images.idle[0]
					elif self.currentDirection == "R":
						self.image = self.images.idleR[0]


		# seperating the movement into x and y movement
		if self.vel.x != 0:
			self.move_single_axis(int(self.vel.x), 0, entities, delta_time)
		if self.vel.y != 0:
			self.move_single_axis(0, int(self.vel.y), entities, delta_time)



	def move_single_axis(self, dx, dy, entities, dt):
		# move
		self.rect.x += dx
		self.rect.y += dy

		#collision detection
		hit_list = pygame.sprite.spritecollide(self, entities, False)
		for entity in hit_list:
			if not entity.static:
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
					self.stop_rising(dt)




	# pushes mario down after hitting a block
	def stop_rising(self, dt):
		self.vel.y += 0.5*self.y_speed*dt

	# what happens when mario hits the ground after jumping
	def land(self, dt):

		self.vel.y = 0

		self.onGround = True

		if self.vel.x < 0 and self.direction != "L":
			self.vel.x = -1 * self.x_speed * dt
			self.currentDirection = "L"
		elif self.vel.x < 0 and self.direction == "L":
			self.vel.x = -1 * self.x_speed * dt

		if self.vel.x > 0 and self.direction != "R":
			self.vel.x = self.x_speed * dt
			self.currentDirection = "R"
		elif self.vel.x > 0 and self.direction == "R":
			self.vel.x = self.x_speed * dt