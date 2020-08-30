import pygame as pg
from settings import *
from tilemap import collide_hit_rect
# Use vectors for a number of variables 
vec = pg.math.Vector2 

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        # Define the hit rect for collisions separately 
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
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
            # check for collision with walls if moving in the x direction
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits: 
                if self.vel.x > 0: 
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2
                if self.vel.x < 0: 
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2
                self.vel.x = 0 
                self.hit_rect.centerx = self.pos.x 
        if dir == 'y':
            # check for collision with walls if moving in y direction
            hits = pg.sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits: 
                if self.vel.y > 0: 
                    self.pos.y = hits[0].rect.top - self.hit_rect.height /2
                if self.vel.y < 0: 
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.width / 2
                self.vel.y = 0 
                self.hit_rect.centery = self.pos.y 


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
        # Check to see if the player collide with any wall - check on each axis on the hit rect
        self.hit_rect.centerx = self.pos.x 
        self.collide_with_walls('x')
        self.hit_rect.centery = self.pos.y 
        self.collide_with_walls('y')
        self.rect.center = self.hit_rect.center

class Mob(pg.sprite.Sprite):
    '''
    Defines all the mobs and their movement and actions
    '''
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.pos = vec(x,y) * TILESIZE
        self.rect.center = self.pos
        self.rot = 0 
    
    def update(self):
        # Need to find out where the player is and rotate towards that position
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1,0))
        # rotate that image by the angle self.rot
        self.image = pg.transform.rotate(self.game.mob_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos 

class Wall(pg.sprite.Sprite):
    '''
    Class for all wall sprites 
    '''
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    



