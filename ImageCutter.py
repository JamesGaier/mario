import spritesheet
class ImageCutter:
	def __init__(self):
		self.run = []
		self.jump = None
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
		self.mario = spritesheet.spritesheet("images/characters.gif")
		self.objects = spritesheet.spritesheet("images/tiles.png")
		self.cutImage()
	def cutImage(self):
		
################# mario animation frames ######################
		idleRect = [(236, 0, 19, 32)]
		self.idle = self.mario.images_at(tuple(idleRect), (0,0,0,0))

		jumpRect = [(125, 0, 19, 35)]
		self.jump = self.mario.images_at(tuple(jumpRect), (0,0,0,0))

		runRects = [(198, 0, 18, 32)]
		runRects.append((184, 0, 17, 32))
		runRects.append((164, 0, 18, 32))
		self.run = self.mario.images_at(tuple(runRects), (0,0,0,0))
		
		duckRect = [(274, 0, 19, 32)]
		self.duck = self.mario.images_at(tuple(duckRect), (0,0,0,0))

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

		questionRect = [(384,0, 16, 16)]
		self.question = self.objects.images_at(tuple(questionRect))
		
		bricksRect = [(16,0, 16, 16)]
		self.bricks = self.objects.images_at(tuple(bricksRect))