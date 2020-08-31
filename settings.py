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

# Gun settings 
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 500 
BULLET_LIFETIME = 1000 
BULLET_RATE = 150 
KICKBACK = 200 
GUN_SPREAD = 5
BULLET_DAMAGE = 20 

# Mob settings 
MOB_IMG = 'zombie1_hold.png'
MOB_SPEED = 100
MOB_HIT_RECT = pg.Rect(0, 0 , 30, 30)
MOB_HEALTH = 100 
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20

# Wall settings 
WALL_IMG = 'tileGreen_39.png'

