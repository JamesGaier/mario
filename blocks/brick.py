import sys,os
scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))
import Entity
import ImageCutter as ic
class Brick(Entity):
    def __init__(self, pos):
        self.rect.x = pos.x
        self.rect.y = pos.y
        self.image_cutter = ic.ImageCutter()
        self.image = self.image_cutter.brick[0]
        self.debris = self.image_cutter.debris[0]