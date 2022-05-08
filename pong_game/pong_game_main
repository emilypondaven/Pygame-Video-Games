import pygame, sys, random
import time
import math

def collision_checker(ball, rect):
    if ball.colliderect(rect):
        return True
    elif ball.centerx <= 20 or ball.centerx >= 1380:
        if ball.centery > rect.top and ball.centery < rect.bottom:
            return True

def show_score_right(score_right):
    score =  font.render(str(int(score_right)), True, (255, 255, 255))
    screen.blit(score, (300, 30))

def show_score_left(score_left):
    score =  font.render(str(int(score_left)), True, (255, 255, 255))
    screen.blit(score, (1100, 30))



def restart_button():
    res = font.render('Restart', True, (0, 0, 0))
    #res_rect = res.get_rect(center = (1380, 350))
    screen.blit(res, (1380, 350))


def start_text():
    text = beginning_font.render('Press space bar to start', True, (255, 255, 255))
    text_rect = text.get_rect(center = (700, 200))
    screen.blit(text, text_rect)

def middle_text():
    text = beginning_font.render('Press space bar to start...', True, (255, 255, 255))
    text_rect = text.get_rect(center = (700, 350))
    screen.blit(text, text_rect)

def difficultyLEVELS():
    # hard
    hard = difficulties_font.render('Easy', True, (255, 255, 255))
    hard_rect = hard.get_rect(center = (334, 650))
    screen.blit(hard, hard_rect)

    # medium
    medium = difficulties_font.render('Medium', True, (255, 255, 255))
    medium_rect = medium.get_rect(center = (700, 650))
    screen.blit(medium, medium_rect)

    # easy
    easy = difficulties_font.render('Hard', True, (255, 255, 255))
    easy_rect = easy.get_rect(center = (1066, 650))
    screen.blit(easy, easy_rect)


def easy_switch(easy, switchon, switchoff):
    if easy == False:
        screen.blit(switchon[0][0], switchon[0][1])
    if easy == True:
        screen.blit(switchoff[0][0], switchoff[0][1])

def medium_switch(medium, switchon, switchoff):
    if medium == False:
        screen.blit(switchon[1][0], switchon[1][1])
    if medium == True:
        screen.blit(switchoff[1][0], switchoff[1][1])

def hard_switch(hard, switchon, switchoff):
    if hard == False:
        screen.blit(switchon[2][0], switchon[2][1])
    if hard == True:
        screen.blit(switchoff[2][0], switchoff[2][1])


def first_switch(easy, medium, hard):
    if easy == True:
        screen.blit(switchon[0][0], switchon[0][1])
    if easy == False:
        screen.blit(switchoff[0][0], switchoff[0][1])
    if medium == True:
        screen.blit(switchon[1][0], switchon[1][1])
    if medium == False:
        screen.blit(switchoff[1][0], switchoff[1][1])
    if hard == True:
        screen.blit(switchon[2][0], switchon[2][1])
    if hard == False:
        screen.blit(switchoff[2][0], switchoff[2][1])

# initialise the pygame
pygame.init()


BLUE = (0, 0, 255)
#creating the screen (width by height)
screen = pygame.display.set_mode((1400, 700))

#speed
x_change = 4
y_change = 2

rec_speed = 8

# creates clock
clock = pygame.time.Clock()
x_pos = 350
y_pos = 350


# get pictures
yellow_ball = pygame.image.load('pong_work/yellow.png').convert_alpha()
yellow_ball_rect = yellow_ball.get_rect(center = (350, 350))

restart_button = pygame.image.load('pong_work/rectangle.png').convert_alpha()
restart_button = pygame.transform.scale(restart_button, (150, 60))
restart_button_rect = restart_button.get_rect(center = (1300, 650))

rectangle_right = pygame.image.load('pong_work/rectangle.png').convert_alpha()
rectangle_right = pygame.transform.scale(rectangle_right, (16, 128))
rectangle_right_rect = rectangle_right.get_rect(center = (1380, 350))

rectangle_left = pygame.image.load('pong_work/rectangle.png').convert_alpha()
rectangle_left = pygame.transform.scale(rectangle_left, (16, 128))
rectangle_left_rect = rectangle_left.get_rect(center = (20, 350))

switchon1 = pygame.image.load('pong_work/switch-on-2.png').convert_alpha()
switchon_rect = switchon1.get_rect(center = (232, 600))

switchoff1 = pygame.image.load('pong_work/switch-off.png').convert_alpha()
switchoff_rect = switchoff1.get_rect(center = (232, 600))

switchoff = []
list1 = []

switchon = []
list2 = []
y = 0
for i in range(3):
    switchoff_rect = switchoff1.get_rect(center = (334 + y, 600))
    list1.append(switchoff1)
    list1.append(switchoff_rect)
    switchoff.append(list1[(((i+1)*2)-2):((((i+1)*2)-2)+2)])

    switchon_rect = switchon1.get_rect(center = (334 + y, 600))
    list2.append(switchon1)
    list2.append(switchon_rect)
    switchon.append(list2[(((i+1)*2)-2):((((i+1)*2)-2)+2)])

    y += 366

print(switchon)
print(switchoff)

font = pygame.font.Font('freesansbold.ttf', 50)
beginning_font = pygame.font.Font('freesansbold.ttf', 70)
difficulties_font = pygame.font.Font('freesansbold.ttf', 30)

res = difficulties_font.render('Restart', True, (0, 0, 0))
res_rect = res.get_rect(center = (1300, 650))


right_change_up = 0
right_change_down = 0


left_change_up = 0
left_change_down = 0

rightdown = False
rightup = False

leftdown = False
leftup = False

# game variables
game_active = False
STARTOFGAME = True

left_win = False
right_win = False

left_or_right = ['right', 'left']

# score
score_right = 0
score_left = 0

# levels
easy = True
medium = False
hard = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() # shuts down game completely
        
        if event.type == pygame.KEYDOWN and game_active == True:
            if event.key == pygame.K_UP:
                right_change_up = -rec_speed
                rightup = True

            if event.key == pygame.K_DOWN:
                right_change_down = rec_speed
                rightdown = True
            
            if event.key == pygame.K_w:
                left_change_up = -rec_speed
                leftup = True
            if event.key == pygame.K_s:
                left_change_down = rec_speed
                leftdown = True
        

        if event.type == pygame.MOUSEBUTTONDOWN and game_active == False and STARTOFGAME == True:
            x,y = pygame.mouse.get_pos()
            if x>302 and x<366 and y>568 and y<632:
                if easy == False:
                    easy = True
                    medium = False
                    hard = False

                elif easy == True:
                    easy = False
                    medium = True

            if x>668 and x<732 and y>568 and y<632:
                if medium == False:
                    medium = True
                    easy = False
                    hard = False

                elif medium == True:
                    medium = False
                    easy = True
                    
            if x>1034 and x<1098 and y>568 and y<632:
                if hard == False:
                    hard = True
                    medium = False
                    easy = False

                elif hard == True:
                    hard = False
                    easy = True
        
        if event.type == pygame.MOUSEBUTTONDOWN and game_active == False and STARTOFGAME == False:
            x,y = pygame.mouse.get_pos()
            if x>1225 and x<1375 and y>620 and y<710:
                game_active = False
                STARTOFGAME = True
                easy = True
                medium = False
                hard = False
                left_win = False 
                right_win = False
                score_left = 0
                score_right = 0


        if event.type == pygame.KEYUP and game_active == False:
            if event.key == pygame.K_SPACE:
                STARTOFGAME = False
                if easy == True:
                    x_change = 3
                    y_change = 1
                    rec_speed = 4
                    add = 0
                if medium == True:
                    x_change = 4
                    y_change = 2
                    rec_speed = 6
                    add = 0.5
                if hard == True:
                    x_change = 7
                    y_change = 2
                    rec_speed = 10
                    add = 1

                if yellow_ball_rect.right == 1370:
                    yellow_ball_rect.right = 1365
                    x_change = -x_change
                    game_active = True

                elif yellow_ball_rect.left == 30:
                    yellow_ball_rect.left = 35
                    x_change += (-2*x_change)
                    game_active = True
                elif yellow_ball_rect.centerx == 700:
                    direction = random.choice(left_or_right)
                    if direction == 'left':
                        x_change = -x_change
                    if direction == 'right':
                        x_change += (-2*x_change)
                
                game_active = True


        if event.type == pygame.KEYUP and game_active == True:
            if event.key == pygame.K_UP: 
                if not rightdown:
                    right_change_up = 0
                rightup = False

            if event.key == pygame.K_DOWN:
                if not rightup:
                    right_change_down = 0
                rightdown = False
            
            if event.key == pygame.K_w: 
                if not leftdown:
                    left_change_up = 0
                leftup = False

            if event.key == pygame.K_s:
                if not leftup:
                     left_change_down = 0
                leftdown = False
        





    #0-255 each one is RGB - gives color to screen
    screen.fill((0,0,0))

    # collision checker

    
    # yellow ball movement
    if game_active == True:

        if yellow_ball_rect.top <= 0:
            y_change += (-2*y_change)

        if yellow_ball_rect.bottom >= 700:
            y_change = -y_change

        
        if yellow_ball_rect.right >= 1372:
            collision_right = collision_checker(yellow_ball_rect, rectangle_right_rect)
            if collision_right:
                yellow_ball_rect.right = 1370
                if rightup == True:
                    x_change = -x_change - add
                elif rightdown == True:
                    x_change = -x_change - add
                else:
                    x_change = -x_change

        
        if yellow_ball_rect.left <= 28:
            collision_left = collision_checker(yellow_ball_rect, rectangle_left_rect)
            if collision_left:
                yellow_ball_rect.left = 30
                if leftup == True:
                    x_change += (-2*x_change) + add
                elif leftdown == True:
                    x_change += (-2*x_change) + add
                else:
                    x_change += (-2*x_change)

        

        if yellow_ball_rect.left >= 1400:
            time.sleep(0.5)
            right_win = True
            score_right += 1
            game_active = False


        if yellow_ball_rect.right <= 0:
            time.sleep(0.5)
            left_win = True
            score_left += 1
            game_active = False
        
        
        yellow_ball_rect.centerx += x_change
        yellow_ball_rect.centery += y_change



        # rectangles movement
        if rectangle_right_rect.top <= 0:
            rectangle_right_rect.top = 7
        
        if rectangle_right_rect.bottom >= 700:
            rectangle_right_rect.bottom = 693
        
        if rectangle_left_rect.top <= 0:
            rectangle_left_rect.top = 7
        
        if rectangle_left_rect.bottom >= 700:
            rectangle_left_rect.bottom = 693
        

        rectangle_right_rect.centery += right_change_up
        rectangle_right_rect.centery += right_change_down

        rectangle_left_rect.centery += left_change_up
        rectangle_left_rect.centery += left_change_down




    if game_active == False:

        rectangle_right_rect.centery = 350
        rectangle_left_rect.centery = 350
        yellow_ball_rect.centery = 350

        right_change_up = 0
        right_change_down = 0
        left_change_up = 0
        left_change_down = 0

        if left_win == True:
            yellow_ball_rect.right = 1370
            middle_text()
        
        elif right_win == True:
            yellow_ball_rect.left = 30
            middle_text()
        
        elif left_win == False and right_win == False:
            yellow_ball_rect.centerx = 700
            start_text()
        
        if STARTOFGAME == False:
            screen.blit(restart_button, restart_button_rect)
            screen.blit(res, res_rect)
        
        elif STARTOFGAME:
            first_switch(easy, medium, hard)
            difficultyLEVELS()




    show_score_right(score_right)
    show_score_left(score_left)


    # draw all shapes
    screen.blit(rectangle_right, rectangle_right_rect)
    screen.blit(rectangle_left, rectangle_left_rect)
    
    screen.blit(yellow_ball, yellow_ball_rect)


    pygame.display.update()
    clock.tick(120) # frame rate - can run slower than this
