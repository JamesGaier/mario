import Layer
import Mario as m
import pygame
import ImageCutter as ic
import Entity
class LevelBuilder:
	def __init__(self, w, h):
		self.w = w
		self.h = h
		self.background = Layer.Background(w, h)
		self.mario = None
		self.m_group = None
		self.entities = []
		self.images = ic.ImageCutter()
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
					self.mario = m.Mario(j*20, i*32)
					self.m_group = pygame.sprite.Group(self.mario)
				if image != None and not isMario:
					print(i*b_h)
					block = Entity.Entity(j*b_w, i*b_h, b_w, b_h, image[0])
					self.entities.append(block)
				isMario = False		
	def update(self, dt):
		self.m_group.update(dt, self.entities)
		for entity in self.entities:
			entity.update(dt)
	def render(self, screen):
		self.background.render(screen)
		self.m_group.draw(screen)
		for entity in self.entities:
			entity.render(screen)
