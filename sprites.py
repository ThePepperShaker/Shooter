import pygame as pg
from settings import *
# Use vectors for a number of variables 
vec = pg.math.Vector2 

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        # store x and y velocity
        self.vel = vec(0, 0)
        # store the actual x and y position 
        self.pos = vec(x,y) * TILESIZE
        # rotation 
        self.rot = 0 
    
    def get_keys(self):
        self.rot_speed = 0 
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = PLAYER_ROT_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed = -PLAYER_ROT_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(-PLAYER_SPEED / 2, 0).rotate(-self.rot)
            


    def collide_with_walls(self, dir):
        if dir == 'x':
            # check for collision with walls 
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits: 
                if self.vel.x > 0: 
                    self.pos.x = hits[0].rect.left - self.rect.width 
                if self.vel.x < 0: 
                    self.pos.x = hits[0].rect.right 
                self.vel.x = 0 
                self.rect.x = self.pos.x 
        if dir == 'y':
            # check for collision with walls 
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits: 
                if self.vel.y > 0: 
                    self.pos.y = hits[0].rect.top - self.rect.height 
                if self.vel.y < 0: 
                    self.pos.y = hits[0].rect.bottom 
                self.vel.y = 0 
                self.rect.y = self.pos.y 


    def update(self):
        self.get_keys()
        # Update rotation - If rotate 360, change it back to 1
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        # Rotate the image - we have to keep track of new rect
        self.image = pg.transform.rotate(self.game.player_img, self.rot)
        # new rectangle 
        self.rect = self.image.get_rect()
        self.rect.center = self.pos 
        # Update position 
        self.pos += self.vel * self.game.dt
        # Check to see if the player collide with any wall - check on each axis 
        self.rect.centerx = self.pos.x 
        self.collide_with_walls('x')
        self.rect.centery = self.pos.y 
        self.collide_with_walls('y')


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    

