import Layer
import Mario as m
import pygame
import ImageCutter as ic
import Entity
class LevelBuilder:
	def __init__(self):
		self.mario = None
		self.m_group = None
		self.entities = []
		self.images = ic.ImageCutter()
		self.total_width = 0
	# reads level and writes to the world
	def read(self, path):
		file = open(path, "r")
		level = "".join([s for s in file])
		level = level.split("\n")
		for i in range(len(level)):
			level[i] = list(level[i])
		b_w = 16
		b_h = 16
		isMario = False
		for i in range(len(level)):
			for j in range(len(level[0])):
				image = None
				if level[i][j] == "1":
					image = self.images.brick
					b_w = self.images.brick[0].get_width()
					b_h = self.images.brick[0].get_height()
				elif level[i][j] == "2":
					image = self.images.question
					b_w = self.images.question[0].get_width()
					b_h = self.images.question[0].get_height()
				elif level[i][j] == "3":
					image = self.images.bricks
					b_w = self.images.bricks[0].get_width()
					b_h = self.images.bricks[0].get_height()
				elif level[i][j] == "4":
					isMario = True
					self.mario = m.Mario(j*16, i*16)
					self.m_group = pygame.sprite.Group(self.mario)
				elif level[i][j] == "5":
					block = Entity.Entity(j*16, i*16, 16, 16, None)
					self.entities.append(block)
				if image != None and not isMario:
					block = Entity.Entity(j*b_w, i*b_h, b_w, b_h, image[0])
					self.entities.append(block)
				isMario = False
				self.total_width = len(level[0])*16

class LevelManager:
	def __init__(self, w, h, mario, entities, total_width):
		self.total_width = total_width
		self.w = w
		self.h = h
		self.mario = mario
		self.m_group = pygame.sprite.Group(self.mario)
		self.entities = entities
		self.images = ic.ImageCutter()
		self.background = Layer.Background(w, h)
		self.world_shift_x = self.world_shift_y = 0
		self.left_viewbox = int(w/2 - w/8)
		self.right_viewbox = int(w/2 + w/12)
	# updates all of the entities
	def update(self, dt):
		self.m_group.update(dt, self.entities)
		for entity in self.entities:
			entity.update(dt)
	# renders all of the entities
	def render(self, screen):
		self.background.render(screen)
		self.m_group.draw(screen)
		for entity in self.entities:
			entity.render(screen)
	# shifts the world by a certian amount
	def shift_world(self, shift_x, shift_y):
		self.world_shift_x += shift_x
		if self.world_shift_x > -16:
			self.left_viewbox = -16
		else:
			self.left_viewbox = int(self.w/2 - self.w/8)
		# add boundry for end of level
		for entity in self.entities:
			entity.rect.x += shift_x
	# math for scrolling
	def run_viewbox(self):
		if self.mario.rect.x <= self.left_viewbox:
			view_difference = self.left_viewbox - self.mario.rect.x
			self.mario.rect.x = self.left_viewbox
			self.shift_world(view_difference, 0)
		if self.mario.rect.x >= self.right_viewbox:
			view_difference = self.right_viewbox - self.mario.rect.x
			self.mario.rect.x = self.right_viewbox
			self.shift_world(view_difference, 0)

