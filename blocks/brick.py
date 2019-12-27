import sys,os
import pygame
scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))
import Entity
from ImageCutter import *
class Brick(Entity.Entity):
    def __init__(self, pos):
        super().__init__(pos[0], pos[1], 16, 16, ImageCutter().bricks[0])
        self.image_cutter = ImageCutter()
        self.image = self.image_cutter.bricks[0]
        self.debris_rects = []
        self.debris = self.image_cutter.debris
        for debris in self.debris:
            self.debris_rects.append(pygame.Rect(self.rect.x, self.rect.y,\
            self.rect.w, self.rect.h))
        self.hit = False
    def update(self, dt, mario):
        self.hit = self.rect.bottom == mario.rect.top\
                    and self.rect.left-self.rect.w <= mario.rect.left\
                    and self.rect.right+self.rect.w >= mario.rect.right
        if self.hit:
            pass

    def render(self, screen):
        '''
        if the block is hit run the animation then delete once the
        particles are out of bounds.
        '''
        if not self.hit:
            screen.blit(self.image, self.rect)
        else:
            for debris in self.debris:
                screen.blit(debris, self.rect)
