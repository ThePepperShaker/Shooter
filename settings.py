import pygame as pg 
vec = pg.math.Vector2 

# define colors 
WHITE = (250, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

# Game settings 
WIDTH = 1024 
HEIGHT = 768 
FPS = 60 
TITLE = 'Tilemap Demo'
BGCOLOR = BROWN

# Tile settings 
TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE 

# Player settings 
PLAYER_HEALTH = 100
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250 
PLAYER_IMG = 'hitman1_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

# Weapon settings 
BULLET_IMG = 'bullet.png'
WEAPONS = {}
WEAPONS['pistol'] = {'bullet-speed':500,
                     'bullet-lifetime':1000,
                     'rate':300,
                     'kickback':200,
                     'spread':5,
                     'damage':10,
                     'bullet_size':'lg',
                     'bullet_count':1}
WEAPONS['shotgun'] = {'bullet-speed':400,
                     'bullet-lifetime':500,
                     'rate':900,
                     'kickback':300,
                     'spread':20,
                     'damage':5,
                     'bullet_size':'sm',
                     'bullet_count':12}
BULLET_SPEED = 500 
BULLET_LIFETIME = 1000 
BULLET_RATE = 150 
KICKBACK = 200 
GUN_SPREAD = 5
BULLET_DAMAGE = 20 

# Mob settings 
MOB_IMG = 'zombie1_hold.png'
MOB_SPEEDS = [150, 100, 100, 125, 150]
MOB_HIT_RECT = pg.Rect(0, 0 , 30, 30)
MOB_HEALTH = 100 
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50 
DETECT_RADIUS = 400

# Wall settings 
WALL_IMG = 'tileGreen_39.png'

# Effects 
MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png', 'whitePuff17.png', 'whitePuff18.png']
FLASH_DURATION = 40 
SPLAT = 'splat green.png'
DAMAGE_ALPHA = [i for i in range(0,255,25)]

# Layers 
WALL_LAYER = 1 
PLAYER_LAYER = 2 
BULLET_LAYER = 3 
MOB_LAYER = 2
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

# Items 
ITEM_IMAGES = {'health': 'health_pack.png', 
               'shotgun': 'obj_shotgun.png'}
HEALTH_PACK_AMOUNT = 20 
BOB_RANGE = 20
BOB_SPEED = 0.4

# Sounds 
# Background music
BG_MUSIC = 'espionage.ogg'
# WHen player gets hit sounds
PLAYER_HIT_SOUNDS = ['pain/8.wav', 'pain/9.wav','pain/10.wav', 'pain/11.wav']
ZOMBIE_MOAN_SOUNDS = ['brains2.wav', 'brains3.wav', 'zombie-roar-1.wav', 'zombie-roar-2.wav',
                      'zombie-roar-3.wav', 'zombie-roar-5.wav','zombie-roar-6.wav', 'zombie-roar-7.wav']
ZOMBIE_HIT_SOUNDS = ['splat-15.wav']
# Weapon sounds 
WEAPON_SOUNDS = {'pistol':['pistol.wav'],
                 'shotgun':['shotgun.wav']}
EFFECTS_SOUNDS = {'level_start':'level_start.wav',
                  'health_up': 'health_pack.wav',
                  'gun_pickup':'gun_pickup.wav'}

# RADAR 
RADAR_COLOR = LIGHTGREY
RADAR_WIDTH = 150 
RADAR_HEIGHT = 90 
BLIP_RADIUS = 2