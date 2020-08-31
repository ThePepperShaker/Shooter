import pygame as pg 
from settings import * 

‚
# Create a function which supports rect and hit_rect interactions 
def collide_hit_rect(one,two):
    return one.hit_rect.colliderect(two.rect)

class Map: 
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f: 
            for line in f: 
                self.data.append(line.strip())
        # Width is simply the length of one of the lines         
        self.tilewidth = len(self.data[0])
        # Height is the length of the list 
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE 
        self.height = self.tileheight * TILESIZE 


class Camera: 
    '''
    Captures an offset to display the portion of the screen on which the player is centered. 
    Stop scrolling once the edge is in sight. 
    '''
    def __init__(self, width, height):
        # This rectangle tracks how far the offset should be
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width 
        self.height = height 
        
    def apply(self, entity):
        # move command shifts rectangle by the input amount
        return entity.rect.move(self.camera.topleft)
    
    def update(self, target):
        # Shift x, if player moves to the right, the offset should move to the left 
        x = -target.rect.centerx + int(WIDTH / 2)
        # Shift y 
        y = -target.rect.centery + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x) # left
        y = min(0, y) # top 
        x = max(-(self.width - WIDTH), x) # right 
        y = max(-(self.height - HEIGHT), y) # bottom 

        self.camera = pg.Rect(x, y, self.width, self.height)