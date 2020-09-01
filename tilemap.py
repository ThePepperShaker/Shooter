import pygame as pg 
from settings import * 
import pytmx

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

class TiledMap: 
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth 
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm 
    
    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid 
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer: 
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, 
                                            y * self.tmxdata.tileheight))

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface 

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
        # applies to sprites 
        # move command shifts rectangle by the input amount
        return entity.rect.move(self.camera.topleft)
    
    def apply_rect(self, rect):
        # Applies to rectangle
        # Takes a rectangle instead of a sprite. and returns the rectangle moved by camera offset 
        return rect.move(self.camera.topleft)
    
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