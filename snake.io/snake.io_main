import pygame, sys, random
import time
import random

from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP


def dir1(x_change,y_change):
    if x_change < 0:
        return 'left'
    if x_change > 0:
        return 'right'
    if y_change < 0:
        return 'up'
    if y_change > 0:
        return 'down'

def dir(x,y):
    x_change = x[1] - x[0]
    y_change = y[1] - y[0]
    if x_change < 0:
        return 'left'
    if x_change > 0:
        return 'right'
    if y_change < 0:
        return 'up'
    if y_change > 0:
        return 'down'

def collidecheck(apple, snake_head_rect):
    if snake_head_rect.colliderect(apple):
        return False
    else:
        return True

def placementcheckerX(x, direction):
    if direction == 'down':
        return x
    elif direction == 'up':
        return x
    elif direction == 'right':
        x_value = x-34
        return x_value
    elif direction == 'left':
        x_value = x+34
        return x_value

def placementcheckerY(y, direction):
    if direction == 'down':
        return y-34
    elif direction == 'up':
        y_value = y+34
        return y_value
    elif direction == 'right':
        return y
    elif direction == 'left':
        return y

def reverse(length):
    list4 = []
    for i in range(length):
        list4.insert(0, i)
    return list4

def collision_with_itself_checker(snakes):
    found = 0
    for body in range(len(snakes)-2):
        body += 2
        if snakes[0][1].colliderect(snakes[body][1]):
            found += 1

    if found >= 1:
        return True
    elif found == 0:
        return False

def check_taken(snakes, apple_rect, scores_rect):
    found = 0
    for block in range(len(snakes)-1):
        if snakes[block][1].colliderect(apple_rect):
            found += 1
    
    if scores_rect.colliderect(apple_rect):
        found += 1
    
    if found >= 1:
        return True
    elif found == 0:
        return False
    
def snake_body_moveY(snake_head_direction):
    if snake_head_direction == 'left':
        return 0
    if snake_head_direction == 'right':
        return 0
    if snake_head_direction == 'up':
        return -2
    if snake_head_direction == 'down':
        return 2

def snake_body_moveX(snake_head_direction):
    if snake_head_direction == 'left':
        return -2
    if snake_head_direction == 'right':
        return 2
    if snake_head_direction == 'up':
        return 0
    if snake_head_direction == 'down':
        return 0

def score_button():
    res = font.render('Score: ' + str(int(Score)), True, (20, 130, 100))
    #res_rect = res.get_rect(center = (1380, 350))
    screen.blit(res, (19, 670))

def highscore_button():
    res = font.render('Highscore: ' + str(int(Highscore)), True, (20, 130, 100))
    #res_rect = res.get_rect(center = (1380, 350))
    screen.blit(res, (19, 705))

def highscore_increase(Highscore, Score):
    if Score > Highscore:
        Highscore = Score
    
    return Highscore


pygame.init()


#creating the screen (width by height)
screen = pygame.display.set_mode((760, 760))


game_active = True
bg_surface = pygame.image.load('snake_work/images/background_image.PNG').convert()

# snake body
snake = pygame.image.load('snake_work/images/snake.png').convert_alpha()
length = 0
snakes = []
list1 = list()
snake_direction = []

snake_rect = snake.get_rect(center = (399, 399))
list1.append(snake)
list1.append(snake_rect)
snakes.append(list1)

snakes_direction = ['down']



snake_head_direction = []
turning = False
# apple
apple = pygame.image.load('snake_work/images/snake.png').convert_alpha()
apple_rect = snake.get_rect(center = (380, 380))

# snake_movement
snakex_change = 0
snakey_change = 0
first = True

left_down = False
right_down = False
up_down = False
down_down = False

# game variables
clock = pygame.time.Clock()
apple_exist = False

# Text
font = pygame.font.Font('freesansbold.ttf', 25)

# scores
Score = -1
Highscore = 0
scores_rect = pygame.Rect(5, 651, 218, 104)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # shuts down game completely


        if event.type == pygame.KEYDOWN and game_active == True:
            if event.key == pygame.K_LEFT:
                snakey_change = 0
                snakex_change = -2
                if first == True:
                    snake_head_direction.append('left')


            if event.key == pygame.K_RIGHT and game_active == True:
                snakey_change = 0
                snakex_change = 2
                if first == True:
                    snake_head_direction.append('right')

            if event.key == pygame.K_UP and game_active == True:
                snakex_change = 0
                snakey_change = -2
                if first == True:
                    snake_head_direction.append('up')

            if event.key == pygame.K_DOWN and game_active == True:
                snakex_change = 0
                snakey_change = 2
                if first == True:
                    snake_head_direction.append('down')




    
    if snakex_change != 0 or snakey_change != 0:
        first = False

        #first snake movement
        snake_head_past_direction = snakes_direction[0]
        snakes_direction[0] = dir1(snakex_change, snakey_change)
        if snake_head_past_direction != snakes_direction[0]:
            snake_head_direction.append(snakes_direction[0])
            if (snake_head_direction[0] == 'up' and snake_head_direction[1] == 'down') or (snake_head_direction[0] == 'down' and snake_head_direction[1] == 'up'):
                time.sleep(0.5)
                game_active = False
            if (snake_head_direction[0] == 'right' and snake_head_direction[1] == 'left') or (snake_head_direction[0] == 'left' and snake_head_direction[1] == 'right'):
                time.sleep(0.5)
                game_active = False

        

        if len(snake_head_direction) >= 2:
            if snake_head_direction[1] == 'right' or snake_head_direction[1] == 'left':
                if (snakes[0][1].centery-19) % 38 == 0:
                    
                    snake_head_direction.pop(0)
                    turning = False
                else:
                    turning = True

            elif snake_head_direction[1] == 'up' or snake_head_direction[1] == 'down':
                if (snakes[0][1].centerx-19) % 38 == 0:
                    snake_head_direction.pop(0)
                    turning = False
                else:
                    turning = True
        

        if turning == True:
            snakes[0][1].centery += snake_body_moveY(snake_head_direction[0])
            snakes[0][1].centerx += snake_body_moveX(snake_head_direction[0])
            
        


        if turning == False:
            snakes[0][1].centerx += snakex_change
            snakes[0][1].centery += snakey_change



        if len(snakes_direction) >= 2:
            for i in range(length-1):
                i += 1

                if i == 1:
                    if snakes[i][1].centerx == snakes[i-1][1].centerx or snakes[i][1].centery == snakes[i-1][1].centery:
                        x = []
                        y = []
                        x.append(snakes[i][1].centerx)
                        y.append(snakes[i][1].centery)
                        snakes[i][1].centery += snake_body_moveY(snake_head_direction[i-1])
                        snakes[i][1].centerx += snake_body_moveX(snake_head_direction[i-1])
                        x.append(snakes[i][1].centerx)
                        y.append(snakes[i][1].centery)
                        snakes_direction[i] = dir(x, y)


                    else:
                        snakes[i][1].centery += snake_body_moveY(snakes_direction[i])
                        snakes[i][1].centerx += snake_body_moveX(snakes_direction[i])


                else:
                    if snakes[i][1].centerx == snakes[i-1][1].centerx or snakes[i][1].centery == snakes[i-1][1].centery:
                        x = []
                        y = []
                        x.append(snakes[i][1].centerx)
                        y.append(snakes[i][1].centery)
                        snakes[i][1].centery += snake_body_moveY(snakes_direction[i-1])
                        snakes[i][1].centerx += snake_body_moveX(snakes_direction[i-1])
                        x.append(snakes[i][1].centerx)
                        y.append(snakes[i][1].centery)
                        snakes_direction[i] = dir(x, y)


                    else:
                        snakes[i][1].centery += snake_body_moveY(snakes_direction[i])
                        snakes[i][1].centerx += snake_body_moveX(snakes_direction[i])


    # snake movement
    if snakes[0][1].right >= 760:
        time.sleep(0.5)
        game_active = False
    if snakes[0][1].top <= 0:
        time.sleep(0.5)
        game_active = False
    if snakes[0][1].bottom >= 760:
        time.sleep(0.5)
        game_active = False
    if snakes[0][1].left <= 0:
        time.sleep(0.5)
        game_active = False

    #obstacle detection - apple
    if apple_exist == True:
        apple_exist = collidecheck(apple_rect, snakes[0][1])
    
    if apple_exist == False:
        Score += 1
        length += 1
        if length >= 2:
            length_of_list = len(snakes)
            x_positioncurrent = placementcheckerX(snakes[length_of_list-1][1].centerx, snakes_direction[(length_of_list - 1)])
            y_positioncurrent = placementcheckerY(snakes[length_of_list-1][1].centery, snakes_direction[(length_of_list - 1)])
            snake_rect = snake.get_rect(center = (x_positioncurrent, y_positioncurrent))
            list1 = list()
            list1.append(snake)
            list1.append(snake_rect)
            snakes.append(list1)

            snakes_direction.append(snakes_direction[(length_of_list - 1)])


        apple_rect.centerx = random.randrange(57, 703, 38)
        apple_rect.centery = random.randrange(57, 703, 38)
        check_collision_first = check_taken(snakes, apple_rect, scores_rect)
        while check_collision_first == True:
            apple_rect.centerx = random.randrange(57, 703, 38)
            apple_rect.centery = random.randrange(57, 703, 38)
            check_collision_first = check_taken(snakes, apple_rect, scores_rect)

        apple_exist = True
    


    #checks collision

    collisionITSELF = collision_with_itself_checker(snakes)
    if collisionITSELF:
        time.sleep(0.5)
        game_active = False


    screen.blit(bg_surface, (0,0))


    #screen grid
    positiv = 0
    nega = 0
    
    for i in range(10):
        for i in range(10):
            pygame.draw.rect(screen, (40,200,6), pygame.Rect(nega, positiv, 38,38))
            positiv += 76
        positiv = 38
        nega += 38
        for i in range(10):
            pygame.draw.rect(screen, (40,200,6), pygame.Rect(nega, positiv, 38,38))
            positiv += 76
        positiv = 0
        nega += 38
    



    if game_active == False:
        Score = -1
        snakes.clear()
        
        snake = pygame.image.load('snake_work/images/snake.png').convert_alpha()
        length = 0
        snakes = []
        list1 = list()
        snake_direction = []

        snake_rect = snake.get_rect(center = (399, 399))
        list1.append(snake)
        list1.append(snake_rect)
        snakes.append(list1)

        snakes_direction = ['down']

        snake_head_direction = []
        turning = False

        # snake_movement
        snakex_change = 0
        snakey_change = 0
        first = True

        left_down = False
        right_down = False
        up_down = False
        down_down = False

        # game variables
        apple_exist = False

        game_active = True


    pygame.draw.rect(screen, (255,0,0), apple_rect)

    pygame.draw.rect(screen, (230,255,180), scores_rect)

    screen.blit(apple,apple_rect)

    Highscore = highscore_increase(Highscore, Score)

    score_button()
    highscore_button()

    for i in reverse(length):
        pygame.draw.rect(screen, (0,255,0), snakes[i][1])
        screen.blit(snakes[i][0], snakes[i][1])


    pygame.display.update()
    clock.tick(120) # frame rate - can run slower than this

