# global modules
import sys,os
import pygame

# modules that are outside the folder
scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))
import Entity
class Question(Entity.Entity):
    def __init__(self, pos, images):
        super().__init__(pos[0], pos[1], images.question[0].get_rect().w,\
         images.question[0].get_rect().h,images.question[0])
        self.image_cutter = images
        self.image = self.image_cutter.question[0]
        self.hit_image = self.image_cutter.question_hit[0]
        self.hit = False
        self.vel = -3
        self.gravity = 0.5
        self.org_pos = self.rect.y
    def update(self, dt, mario):
        delta = float(dt)/1000
        hit = self.rect.bottom == mario.rect.top\
            and self.rect.left-self.rect.w+15 <= mario.rect.left\
            and self.rect.right+self.rect.w-13 >= mario.rect.right
        if hit:
            self.hit = True
        if self.hit:
            self.image = self.hit_image
            self.anim_rect.y +=  int(self.vel)
            self.vel += self.gravity
            if self.anim_rect.y >= self.org_pos:
                self.anim_rect.y = self.org_pos
                self.vel = 0
                self.hit = False
    def render(self, screen):
        screen.blit(self.image, self.anim_rect)



