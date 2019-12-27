import sys, pygame
import time
import Mario as m
import Input as inp
import Layer
import scene
import mar_math
BLACK = 0, 0, 0
WHITE = 255, 255, 255

SIZE = (640, 640)
MAX_FPS = 60
TIMESTEP = 1000/MAX_FPS
def main():

	pygame.init()
	screen = pygame.display.set_mode(SIZE)

	levelBuilder = scene.LevelBuilder()
	levelBuilder.read("levels/1-1.txt")

	levelManager = scene.LevelManager(SIZE[0], SIZE[1], levelBuilder.mario, levelBuilder.entities,\
					levelBuilder.total_width)

	clock = pygame.time.Clock()
	lastTime = 0
	dt = 0

	playing = True
	accumulator = 0
	while playing:
		dt = clock.tick(60)
		accumulator += dt
		if accumulator > TIMESTEP:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			screen.fill(BLACK)
			levelManager.update(TIMESTEP)

			levelManager.run_viewbox()
			levelManager.render(screen)


			pygame.display.flip()
			accumulator -= TIMESTEP

if __name__ == "__main__":
	main()