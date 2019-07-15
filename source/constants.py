
DEBUG = False
PLAYER_START_X = 110
PLAYER_START_y = 540

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

ORIGINAL_CAPTION = "Super Mario Bros"

## COLORS ##
#                R    G    B
GRAY         = (100, 100, 100)
NAVYBLUE     = ( 60,  60, 100)
WHITE        = (255, 255, 255)
RED          = (255,   0,   0)
GREEN        = (  0, 255,   0)
FOREST_GREEN = ( 31, 162,  35)
BLUE         = (  0,   0, 255)
SKY_BLUE     = ( 39, 145, 251)
YELLOW       = (255, 255,   0)
ORANGE       = (255, 128,   0)
PURPLE       = (255,   0, 255)
CYAN         = (  0, 255, 255)
BLACK        = (  0,   0,   0)
NEAR_BLACK   = ( 19,  15,  48)
COMBLUE      = (233, 232, 255)
GOLD         = (255, 215,   0)

BGCOLOR = WHITE


SIZE_MULTIPLIER = 2.5
BRICK_SIZE_MULTIPLIER = 2.69
BACKGROUND_MULTIPLER = 2.679
GROUND_HEIGHT = SCREEN_HEIGHT - 62

#STATES FOR ENTIRE GAME
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'load screen'
TIME_OUT = 'time out'
GAME_OVER = 'game over'
LEVEL = 'level'

#MAIN MENU CURSOR STATES
PLAYER1 = 'mario game'
PLAYER2 = 'luigi game'

#GAME INFO DICTIONARY KEYS
COIN_TOTAL = 'coin total'
SCORE = 'score'
TOP_SCORE = 'top score'
LIVES = 'lives'
CURRENT_TIME = 'current time'
LEVEL_STATE = 'level state'
LEVEL_NUM = 'level num'
CAMERA_START_X = 'camera start x'
PLAYER_NAME = 'player name'
PLAYER_MARIO = 'mario'
PLAYER_LUIGI = 'luigi'
PLAYER_DEAD = 'player dead'

#MAP COMPONENTS
MAP_IMAGE = 'image_name'
MAP_MAPS = 'maps'
SUB_MAP = 'sub_map'
MAP_GROUND = 'ground'
MAP_PIPE = 'pipe'
PIPE_TYPE_NONE = 0
PIPE_TYPE_IN = 1
PIPE_TYPE_OUT = 2
PIPE_TYPE_HORIZONTAL = 3
MAP_STEP = 'step'
MAP_BRICK = 'brick'
BRICK_NUM = 'brick_num'
TYPE_NONE = 0
TYPE_COIN = 1
TYPE_STAR = 2
MAP_BOX = 'box'
TYPE_MUSHROOM = 3
TYPE_FIREFLOWER = 4
TYPE_FIREBALL = 5
TYPE_LIFEMUSHROOM = 6
MAP_ENEMY = 'enemy'
ENEMY_TYPE_GOOMBA = 0
ENEMY_TYPE_KOOPA = 1
ENEMY_TYPE_FLY_KOOPA = 2
ENEMY_TYPE_PIRANHA = 3
ENEMY_RANGE = 'range'
MAP_CHECKPOINT = 'checkpoint'
ENEMY_GROUPID = 'enemy_groupid'
MAP_INDEX = 'map_index'
CHECKPOINT_TYPE_ENEMY = 0
CHECKPOINT_TYPE_FLAG = 1
CHECKPOINT_TYPE_CASTLE = 2
CHECKPOINT_TYPE_MUSHROOM = 3
CHECKPOINT_TYPE_PIPE = 4
CHECKPOINT_TYPE_PIPE_UP = 5
CHECKPOINT_TYPE_MAP = 6	#go to another map
MAP_FLAGPOLE = 'flagpole'
FLAGPOLE_TYPE_FLAG = 0
FLAGPOLE_TYPE_POLE = 1
FLAGPOLE_TYPE_TOP = 2
MAP_SLIDER = 'slider'
HORIZONTAL = 0
VERTICAL = 1
VELOCITY = 'velocity'
MAP_COIN = 'coin'

#COMPONENT COLOR
COLOR = 'color'
COLOR_TYPE_ORANGE = 0
COLOR_TYPE_GREEN = 1
COLOR_TYPE_RED = 2

#BRICK STATES
RESTING = 'resting'
BUMPED = 'bumped'
OPENED = 'opened'

#MUSHROOM STATES
REVEAL = 'reveal'
SLIDE = 'slide'

#Player FRAMES
PLAYER_FRAMES = 'image_frames'
RIGHT_SMALL_NORMAL = 'right_small_normal'
RIGHT_BIG_NORMAL = 'right_big_normal'
RIGHT_BIG_FIRE = 'right_big_fire'

#PLAYER States
STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
FLY = 'fly'
SMALL_TO_BIG = 'small to big'
BIG_TO_FIRE = 'big to fire'
BIG_TO_SMALL = 'big to small'
FLAGPOLE = 'flag pole'
WALKING_TO_CASTLE = 'walking to castle'
END_OF_LEVEL_FALL = 'end of level fall'
IN_CASTLE = 'in castle'
DOWN_TO_PIPE = 'down to pipe'
UP_OUT_PIPE = 'up out of pipe'

#PLAYER FORCES
PLAYER_SPEED = 'speed'
WALK_ACCEL = 'walk_accel'
RUN_ACCEL = 'run_accel'
JUMP_VEL = 'jump_velocity'
MAX_Y_VEL = 'max_y_velocity'
MAX_RUN_SPEED = 'max_run_speed'
MAX_WALK_SPEED = 'max_walk_speed'
SMALL_TURNAROUND = .35
JUMP_GRAVITY = .31
GRAVITY = 1.01

#LIST of ENEMIES
GOOMBA = 'goomba'
KOOPA = 'koopa'
FLY_KOOPA = 'fly koopa'
PIRANHA = 'piranha'

#GOOMBA Stuff
LEFT = 'left'
RIGHT = 'right'
JUMPED_ON = 'jumped on'
DEATH_JUMP = 'death jump'

#KOOPA STUFF
SHELL_SLIDE = 'shell slide'

#FLAG STATE
TOP_OF_POLE = 'top of pole'
SLIDE_DOWN = 'slide down'
BOTTOM_OF_POLE = 'bottom of pole'

#FIREBALL STATE
FLYING = 'flying'
BOUNCING = 'bouncing'
EXPLODING = 'exploding'