import spritesheet
import pygame
class ImageCutter:
	def __init__(self):
		self.runL = []
		self.runR = []
		self.jumpL = None
		self.jumpR = None
		self.duck = None
		self.stop = None
		self.idle = None
		self.flagPole = []
		self.runf = []
		self.jumpf = None
		self.duckf = None
		self.stopf = None
		self.idlef = None
		self.flagPolef = []
		self.runs = []
		self.jumps = None
		self.ducks = None
		self.stops = None
		self.idles = None
		self.flagPoles = []
		self.debris = None
		self.mario = spritesheet.spritesheet("images/characters.gif")
		self.objects = spritesheet.spritesheet("images/tiles.png")
		self.objects1 = spritesheet.spritesheet("images/blocks1.png")
		self.cutImage()
	def cutImage(self):
################# mario animation frames ######################
		idleRect = [(236, 0, 19, 32)]
		self.idle = self.mario.images_at(tuple(idleRect), (0,0,0,0))
		self.idle[0] = pygame.transform.scale(self.idle[0], (int(self.idle[0].get_rect().w * 2)\
		,int(self.idle[0].get_rect().h * 2)))

		self.idleR = [pygame.transform.flip(self.idle[0], True, False)]

		jumpRect = [(125, 0, 19, 35)]
		self.jumpL = self.mario.images_at(tuple(jumpRect), (0,0,0,0))
		self.jumpL[0] = pygame.transform.scale(self.jumpL[0], (int(self.jumpL[0].get_rect().w * 2)\
		,int(self.jumpL[0].get_rect().h * 2)))
		self.jumpR = [pygame.transform.flip(self.jumpL[0], True, False)]

		runRects = [(198, 0, 18, 32)]
		runRects.append((184, 0, 17, 32))
		runRects.append((164, 0, 18, 32))
		self.runL = self.mario.images_at(tuple(runRects), (0,0,0,0))

		for i in range(len(self.runL)):
			self.runL[i] = pygame.transform.scale(self.runL[i], (int(self.runL[i].get_rect().w * 2)\
		,int(self.runL[i].get_rect().h * 2)))

		self.runR = [pygame.transform.flip(image, True, False) for image in self.runL]

		duckRect = [(274, 0, 19, 32)]
		self.duck = self.mario.images_at(tuple(duckRect), (0,0,0,0))
		self.duck[0] = pygame.transform.scale(self.duck[0], (int(self.duck[0].get_rect().w * 2)\
		,int(self.duck[0].get_rect().h * 2)))


		stopRect = [(145, 0, 19, 32)]
		self.stop = self.mario.images_at(tuple(stopRect), (0,0,0,0))

		idleRectf = [(236, 125, 19, 32)]
		self.idlef = self.mario.images_at(tuple(idleRectf), (0,0,0,0))

		jumpRectsf = [(125,125, 19, 35)]
		self.jumpf = self.mario.images_at(tuple(jumpRectsf), (0,0,0,0))

		runRectsf = [(198, 125, 18, 32)]
		runRectsf.append((184, 125, 17, 32))
		runRectsf.append((164, 125, 18, 32))
		self.runf = self.mario.images_at(tuple(runRectsf), (0,0,0,0))

		duckRectf = [(274, 125, 19, 32)]
		self.duckf = self.mario.images_at(tuple(duckRectf), (0,0,0,0))

		stopRectf = [(145, 125, 19, 32)]
		self.stopf = self.mario.images_at(tuple(stopRectf), (0,0,0,0))

########################## other tiles ########################

		skyRect = [(48, 336, 16, 16)]
		self.sky = self.objects.images_at(tuple(skyRect), (0,0,0,0))

		brickRect = [(0, 0, 16, 16)]
		self.brick = self.objects.images_at(tuple(brickRect))
		self.brick[0] = pygame.transform.scale(self.brick[0], (int(self.brick[0].get_rect().w * 2)\
		,int(self.brick[0].get_rect().h * 2)))
		questionRect = [(384,0, 16, 16)]
		self.question = self.objects.images_at(tuple(questionRect))
		self.question[0] = pygame.transform.scale(self.question[0], (int(self.question[0].get_rect().w * 2)\
		,int(self.question[0].get_rect().h * 2)))
		questHitRect = [(432, 0, 16, 16)]
		self.question_hit = self.objects.images_at(tuple(questHitRect))
		self.question_hit[0] = pygame.transform.scale(self.question_hit[0], (int(self.question_hit[0].get_rect().w * 2)\
		,int(self.question_hit[0].get_rect().h * 2)))
		bricksRect = [(16, 0, 16, 16)]
		self.bricks = self.objects.images_at(tuple(bricksRect))
		self.bricks[0] = pygame.transform.scale(self.bricks[0] , (int(self.bricks[0].get_rect().w * 2)\
		,int(self.bricks[0].get_rect().h * 2)))

		debrisRect = [(68, 36, 8, 8)]
		debrisRect.append((68, 22, 8, 8))
		self.debris = self.objects1.images_at(tuple(debrisRect), (0,0,0,0))
		self.debris.append(pygame.transform.flip(self.debris[0], True, False))
		self.debris.append(pygame.transform.flip(self.debris[1], True, False))