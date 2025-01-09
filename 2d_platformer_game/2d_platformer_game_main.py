import pygame, sys, random
import time


def flip(player):
    if type(player) == list:
        for i in range(len(player)):
            player[i] = pygame.transform.flip(player[i],True, False)

        return player
    
    else:
        player = pygame.transform.flip(player,True, False)

        return player

def boundaries(player, grass_block, width, height):

    if player.left <= 0:
        player.left += 10
    if player.right >= width-32:
        player.right -= 10
    if player.top <= 0:
        player.top += 10
    if player.bottom >= height:
        player.bottom -= 10
    
    if player.colliderect(grass_block):
        if grass_block.collidepoint((player.left, player.bottom - v)) and grass_block.collidepoint((player.centerx, player.bottom - v)) or grass_block.collidepoint((player.centerx, player.bottom - v)) and grass_block.collidepoint((player.right, player.bottom - v)):
            player.bottom = grass_block.top - 1
        elif grass_block.collidepoint(player.topleft) and grass_block.collidepoint(player.midtop) or grass_block.collidepoint(player.midtop) and grass_block.collidepoint(player.topright):
            player.top = grass_block.bottom + 1
        elif grass_block.collidepoint(player.topleft) and grass_block.collidepoint(player.midleft) or grass_block.collidepoint(player.midleft) and grass_block.collidepoint(player.bottomleft):
            player.left = grass_block.right + 2
        elif grass_block.collidepoint(player.topright) and grass_block.collidepoint(player.midright) or grass_block.collidepoint(player.midright) and grass_block.collidepoint(player.bottomright):
            player.right = grass_block.left - 2


    
    return player
    
def number_check(n):
    if n > 8:
        return 3
    else:
        return int(n)

def generate_character():
    global my_spritesheetRUNNING, my_spritesheetNORMAL, my_spritesheetJUMP, my_spritesheetFALL, my_spritesheetDOUBLEJUMP
    character = ['Mask_Dude','Ninja_Frog','Pink_Man','Virtual_Guy']
    character = random.choice(character)
    if character == 'Mask_Dude':
        my_spritesheetRUNNING = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Mask_Dude/Run(32x32).png')
        my_spritesheetNORMAL = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Mask_Dude/Idle(32x32).png')
        my_spritesheetJUMP = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Mask_Dude/Jump(32x32).png')
        my_spritesheetFALL = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Mask_Dude/Fall(32x32).png')
        my_spritesheetDOUBLEJUMP = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Mask_Dude/DoubleJump(32x32).png')

    if character == 'Ninja_Frog':
        my_spritesheetRUNNING = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Ninja_Frog/Run(32x32).png')
        my_spritesheetNORMAL = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Ninja_Frog/Idle(32x32).png')
        my_spritesheetJUMP = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Ninja_Frog/Jump(32x32).png')
        my_spritesheetFALL = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Ninja_Frog/Fall(32x32).png')
        my_spritesheetDOUBLEJUMP = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Ninja_Frog/DoubleJump(32x32).png')

    if character == 'Pink_Man':
        my_spritesheetRUNNING = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Pink_Man/Run(32x32).png')
        my_spritesheetNORMAL = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Pink_Man/Idle(32x32).png')
        my_spritesheetJUMP = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Pink_Man/Jump(32x32).png')
        my_spritesheetFALL = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Pink_Man/Fall(32x32).png')
        my_spritesheetDOUBLEJUMP = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Pink_Man/DoubleJump(32x32).png')

    if character == 'Virtual_Guy':
        my_spritesheetRUNNING = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Virtual_Guy/Run(32x32).png')
        my_spritesheetNORMAL = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Virtual_Guy/Idle(32x32).png')
        my_spritesheetJUMP = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Virtual_Guy/Jump(32x32).png')
        my_spritesheetFALL = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Virtual_Guy/Fall(32x32).png')
        my_spritesheetDOUBLEJUMP = Spritesheet('2d_platformer_game_work/Free/Main_Characters/Virtual_Guy/DoubleJump(32x32).png')

def player_generator():
    player = []
    player.append(my_spritesheetNORMAL.get_sprite(0,0,32,32))
    player.append(my_spritesheetJUMP.get_sprite(0,0,32,32))
    player.append(my_spritesheetFALL.get_sprite(0,0,32,32))
    for i in range(6):
        i = i*32
        player.append(my_spritesheetDOUBLEJUMP.get_sprite(i,0,32,32))

    for i in range(len(player)):
        player[i] = pygame.transform.scale(player[i], (64, 64))
    
    return player

def runningplayer_generator():
    running_player = []
    for i in range(12):
        i = i*32
        running_player.append(my_spritesheetRUNNING.get_sprite(i,0,32,32))
        i = int(i/32)
        running_player[i] = pygame.transform.scale(running_player[i], (64, 64))

    return running_player

def generate_background():
    background = pygame.image.load('2d_platformer_game_work/Free/Background/Brown.png').convert()
    return background

def paste_background(b):
    j = 0
    for j in range(11):
        j = j*64
        for i in range(22):
            i = i*64
            screen.blit(b, (i, j))
        
def generate_platform():
    global my_spritesheetTERRAIN
    my_spritesheetTERRAIN = Spritesheet('2d_platformer_game_work/Free/Terrain/Terrain (16x16).png')

def terrains():
    global grass_block, grass_block_rect, grass_block_large, grass_block_large_rect, dirt_block, dirt_block_rect, max
    max = 10
     # one block
    grass_block = my_spritesheetTERRAIN.get_sprite(96,0,48, 48)
    grass_block = pygame.transform.scale(grass_block, (144, 144))
    grass_block_rect = []
    for i in range(max):
        grass_block_rect.append(grass_block.get_rect(center = (140,567)))


    """ size = 44
    grass_block_large = my_spritesheetTERRAIN.get_sprite(98,2,size, size)
    grass_block_large = pygame.transform.scale(grass_block_large, (size*3, size*3))
    grass_block_large_rect = []

    size1 = 5
    for i in range(size1):
        grass_block_large_rect.append(grass_block_large.get_rect(center = (size*3/2,567)))
    
    for i in range(len(grass_block_large_rect) - 1):
        grass_block_large_rect[i+1].centerx = grass_block_large_rect[i].centerx + (size*3)
        grass_block_large_rect[i+1].centery = grass_block_large_rect[i].centery """



    """ dirt_block = my_spritesheetTERRAIN.get_sprite(96,32,48, 16)
    dirt_block = pygame.transform.scale(dirt_block, (144, 48))
    dirt_block_rect = dirt_block.get_rect(center = (500,615))

    grass_block = my_spritesheetTERRAIN.get_sprite(96,0,48, 16)
    grass_block = pygame.transform.scale(grass_block, (144, 48))
    grass_block_rect = grass_block.get_rect(center = (500,567)) """

def check_collision():
    if player_rect.bottom >= ground_level[0] and player_rect.bottom <= ground_level[0] + 11:
        if player_rect.right >= ground_level[1].left + 15 and player_rect.left <= ground_level[1].right - 15:
            return True
        else:
            return False

def ground_levelgg():
    ontop = False
    for i in range(len(grass_block_rect)):
        if player_rect.bottom >= grass_block_rect[i].top-1 and player_rect.bottom <= grass_block_rect[i].bottom:
            if player_rect.right >= grass_block_rect[i].left + 5 and player_rect.left <= grass_block_rect[i].right - 5:
                ontop = True
                return grass_block_rect[i]
    
    if ontop == False:
        return ground_level[1]

def move_grass_block():

    if left_down:
        for i in range(len(grass_block_rect)):
            grass_block_rect[i].centerx += 10

    elif right_down:
        for i in range(len(grass_block_rect)):
            grass_block_rect[i].centerx -= 10


    # if grass_block_rect[0].left <= 0:
    #     grass_block_rect.append(grass_block.get_rect(center = (grass_block_rect[len(grass_block_rect)-1].centerx + 280, grass_block_rect[0].centery)))
    

    
    return grass_block_rect

def re_do_grass_blocks():

    grass_block_rect.clear()
    for i in range(max):
        grass_block_rect.append(grass_block.get_rect(center = (140,567)))

    
    for i in range(max-1):
        grass_block_rect[i+1].centerx = grass_block_rect[i].centerx + 280
        grass_block_rect[i+1].centery = grass_block_rect[i].centery -50


    

# initialise the pygame
# pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512)
pygame.init()

SCREENWIDTH = 1400
SCREENHEIGHT = 700
#creating the screen (width by height)
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

# creates clock
clock = pygame.time.Clock()

class Spritesheet:

    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()

    def get_sprite(self,x,y,w,h):
        global sprite
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet, (0,0), (x,y,w,h))
        return sprite



# terrain
generate_platform()
background = generate_background()
terrains()

for i in range(len(grass_block_rect) - 1):
    grass_block_rect[i+1].centerx = grass_block_rect[i].centerx + 280
    grass_block_rect[i+1].centery = grass_block_rect[i].centery - 20




# get character images

generate_character()

player = player_generator()
player_rect = player[0].get_rect(center = (140,grass_block_rect[0].top-200))
running_player = runningplayer_generator()




# game variable
stop = True

playerX_change = 0
left_down = False
right_down = False

direction = 'right'
jump = False
falling = True
doublejump = False
gravity = 5
v = -30

number = 0
player_num = 0
player_movement = 0
player_vel = -15
ground_level = []
ground_level.append(grass_block_rect[0].top - 1)
ground_level.append(grass_block_rect[0])

num = 0
double_jump_times = 0
num_jump = 0
falling_jump = False
add_block = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # shuts down game completely
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_down=True
                if direction != 'left':
                    running_player = flip(running_player)
                    player = flip(player)
                direction = 'left'
            if event.key == pygame.K_RIGHT:
                right_down=True
                if direction != 'right':
                    running_player = flip(running_player)
                    player = flip(player)
                direction = 'right'

            if event.key == pygame.K_SPACE and num_jump == 1 and doublejump == False and double_jump_times == 0:
                falling = False
                doublejump = True
                jump = False
                number = 3
                player_movement = v
                double_jump_times = 1
            
            elif event.key == pygame.K_SPACE and jump == False and doublejump == False and double_jump_times == 0:
                falling = False
                player_num = 1
                jump = True
                player_movement = v
                num_jump = 1


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if not right_down and stop:
                    playerX_change = 0
                left_down=False
                flipping_time = False

            if event.key == pygame.K_RIGHT:
                if not left_down and stop:
                    playerX_change = 0
                right_down=False
                flipping_time = False
    

    paste_background(background)

    if left_down:
        if player_rect.centerx >= 700:
            playerX_change = -10
        elif grass_block_rect[0].left >= 68:
            playerX_change = -10
        else:
            # move terrain
            grass_block_rect = move_grass_block()
            playerX_change = 0
    elif right_down:
        if grass_block_rect[9].right <= 1332:
            playerX_change = 10
        elif player_rect.centerx <= 700:
            playerX_change = 10
        else: 
            # move terrain
            grass_block_rect = move_grass_block()
            playerX_change = 0
    


    #chooses ground_level
    ground_level[1] = ground_levelgg()
    ground_level[0] = ground_level[1].top - 1
    
    
    #jumping
    if jump:
        if player_movement >= 0:
            jump = False
            falling = True
        else:
            player_rect.centery += player_movement 
            player_movement += gravity
            player_rect = boundaries(player_rect, ground_level[1], SCREENWIDTH, SCREENHEIGHT)

    elif doublejump:        
        if player_movement >= 0:
            doublejump = False
            falling = True
        else:
            player_rect.centery += player_movement 
            player_movement += gravity
            number += 1
            player_num = number_check(number)
            player_rect = boundaries(player_rect, ground_level[1], SCREENWIDTH, SCREENHEIGHT)

        
    if falling == True:
        if check_collision() == True:
            num_jump = 0
            double_jump_times = 0
            player_num = 0
            player_movement = 0
            
        else:
            player_num = 2
            player_movement -= gravity
            player_rect.centery -= player_movement




    # respawn
    if player_rect.top >= SCREENHEIGHT:
        re_do_grass_blocks()
        player_rect.bottom = ground_level[0] - 200
        player_rect.centerx = grass_block_rect[0].centerx
        player_movement = 0
        player_num = 0
        double_jump_times = 0
        jump = False
        doublejump = False


    # running
    player_rect = boundaries(player_rect, ground_level[1], SCREENWIDTH, SCREENHEIGHT)

    if left_down or right_down:
        num += 1
        stop = False

        if num > 11:
            num = 0

        if player_rect.centerx >= 700 or player_rect.centerx <= 700:
            player_rect.centerx += playerX_change
        if jump == False and doublejump == False and check_collision() == True:
            screen.blit(running_player[num], player_rect)
        else:
            screen.blit(player[player_num], player_rect)

    else:
        screen.blit(player[player_num], player_rect)
    
    

    

    for i in range(len(grass_block_rect)):
        screen.blit(grass_block, grass_block_rect[i])
    



    time.sleep(0.05)

    pygame.display.update()
    clock.tick(120) # frame rate - can run slower than this
