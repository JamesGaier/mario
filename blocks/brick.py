import sys,os
import pygame
scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))
import Entity
class Brick(Entity.Entity):
    def __init__(self, pos, images):
        super().__init__(pos[0], pos[1], images.bricks[0].get_rect().w,\
        images.bricks[0].get_rect().h, images.bricks[0])
        self.image_cutter = images
        self.image = self.image_cutter.bricks[0]
        self.debris_rects = []
        self.debris = self.image_cutter.debris
        for debris in self.debris:
            self.debris_rects.append(pygame.Rect(self.rect.x, self.rect.y,\
            self.rect.w, self.rect.h))
        self.hit = False
        self.vel = -3
        self.gravity = 0.5
        self.org_pos = self.pos.y
    def update(self, dt, mario):
        delta = float(dt)/1000
        hit = self.rect.bottom == mario.rect.top\
            and self.rect.left-self.rect.w+7 <= mario.rect.left\
            and self.rect.right+self.rect.w-6 >= mario.rect.right
        if hit:
            self.hit = True
        if self.hit:
            self.anim_rect.y +=  int(self.vel)
            self.vel += self.gravity
            if self.anim_rect.y >= self.org_pos:
                self.anim_rect.y = self.org_pos
                self.vel = -3
                self.hit = False

    def render(self, screen):
        '''
        if the block is hit run the animation then delete once the
        particles are out of bounds.
        '''
        screen.blit(self.image, self.anim_rect)
