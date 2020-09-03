# Game Development with Pygame video series - Tile Based Game
# Art from kenney - https://kenney.nl/assets/topdown-shooter

import pygame as pg
import sys
from settings import *
from sprites import *
from os import path
from tilemap import * 

# HUD function 
def draw_player_heath(surf, x,y, pct):
    if pct < 0: 
        pct = 0 
    BAR_LENGTH = 100 
    BAR_HEIGHT = 20 
    fill = pct * BAR_LENGTH 
    outline_rect = pg.Rect(x,y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x,y, fill, BAR_HEIGHT)
    if pct > 0.6:
        col = GREEN 
    elif pct > 0.3:
        col = YELLOW 
    else: 
        col = RED 
    pg.draw.rect(surf, col, fill_rect)
    pg.draw.rect(surf,WHITE, outline_rect, 2)

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        # Set the repeat rate
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        # location of .py files 
        # define some folders where files are stored 
        game_folder = path.dirname('__file__')
        img_folder = path.join(game_folder, 'img')
        map_folder = path.join(game_folder, 'maps')
        self.map = TiledMap(path.join(map_folder, 'level1_pls.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        # load the player image sprite 
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        # load the wall image sprite
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        # Resize the image to the appropriate size 
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))
        # load the mob image sprite 
        self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
        # load the bullet image sprite 
        self.bullet_img = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
        # load the gun flashes 
        self.gun_flashes = []
        for img in MUZZLE_FLASHES:
            self.gun_flashes.append(pg.image.load(path.join(img_folder, img)).convert_alpha())
        # load items 
        self.item_images = {}
        for item in ITEM_IMAGES:
            self.item_images[item] = pg.image.load(path.join(img_folder, ITEM_IMAGES[item])).convert_alpha()
    
    def new(self):
        # initialize all variables and do all the setup for a new game
        # Set layers for each group
        self.all_sprites = pg.sprite.LayeredUpdates()
        # Walls group 
        self.walls = pg.sprite.Group()
        # Mobs group 
        self.mobs = pg.sprite.Group()
        # Bullet group 
        self.bullets = pg.sprite.Group()
        # Items group 
        self.items = pg.sprite.Group()
        # spawn walls from map.txt file 
        # enumerate returns the index and the item of a list
        # for row, tiles in enumerate(self.map.data):
        #     # enumerate on each string
        #     for col, tile in enumerate(tiles):
        #         if tile == '1':
        #             Wall(self, col, row)
        #         # If there is a 'p' on the map, spawn a player
        #         if tile == 'P':
        #             self.player = Player(self, col, row)
        #         # If there is a 'M' on the map, spawn a mob 
        #         if tile == 'M':
        #             self.mob = Mob(self, col, row)
        for tile_object in self.map.tmxdata.objects: 
            object_center = vec(tile_object.y + tile_object.width / 2, 
                                tile_object.y + tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = Player(self, object_center.x, object_center.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'zombie':
                Mob(self,object_center.x, object_center.y)
            if tile_object.name in ['health']:
                Item(self,object_center,tile_object.name)
        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False 


    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            # Divide by 1000 as we want dt in seconds, not milliseconds
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        # mob hits player 
        hits = pg.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
        for hit in hits: 
            self.player.health -= MOB_DAMAGE
            hit.vel = vec(0,0)
            if self.player.health <= 0: 
                self.playing = False
        if hits:
            self.player.pos += vec(MOB_KNOCKBACK, 0).rotate(-hits[0].rot)

        # bullets kill mobs 
        hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True)
        for hit in hits:
            hit.health -= BULLET_DAMAGE 
            hit.vel = vec(0,0)
        

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        pg.display.set_caption('{:.2f}'.format(self.clock.get_fps()))
        # self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        # Draw the grid 
        # self.draw_grid()
        for sprite in self.all_sprites:
            if isinstance(sprite, Mob):
                sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.draw_debug:
                pg.draw.rect(self.screen, GREEN, self.camera.apply_rect(sprite.hit_rect),1)
        if self.draw_debug:
            for wall in self.walls: 
                pg.draw.rect(self.screen, GREEN, self.camera.apply_rect(wall.rect),1)
        # HUD functions 
        draw_player_heath(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_h:
                    self.draw_debug = not self.draw_debug

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()