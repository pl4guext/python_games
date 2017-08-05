# coding=utf-8
import time

try:
    import pygame
except Exception, e:
    print 'FAILED TO IMPORT PYGAME: ',e
    exit(1)


try:
    from config import *
    from app.pygame_tools.image_tools import *
except Exception, e:
    print 'FAILED TO IMPORT INNER TOOLS: ',e
    exit(1)







def __init__():
    global x, y, x_speed, conf, game, color, window_size, flag_end, mario_img, x_ball, y_ball, x_speed_ball, y_speed_ball

    conf = env_variables()
    game = game_variables()
    color = colors()
    window_size = conf.window_size
    x = conf.center_x
    y = conf.center_y
    x_ball = 20
    y_ball = 20
    x_speed = 0
    x_speed_ball = game.x_speed_ball
    y_speed_ball = game.y_speed_ball
    flag_end = False
    mario_img = pygame.image.load('app/static/images/mario.png')
    mario_img = pygame.transform.scale(mario_img, game.object_size)








def mario(_x, _y):
    gameDisplay.blit(mario_img, (_x,_y))


def event_handler():
    global flag_end, x_speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            flag_end = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -game.x_speed
            if event.key == pygame.K_RIGHT:
                x_speed = game.x_speed
            if event.key == pygame.K_ESCAPE:
                flag_end = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0


def on_draw():
        gameDisplay.fill(color.white)
        mario(x,y)
        pygame.draw.circle(gameDisplay, color.red, (x_ball, y_ball), game.ball_rad) 
        pygame.display.update()

def update_pos():
    global x
    if (x + x_speed + game.object_w) < conf.width  and (x + x_speed) > 0:
        x = x + x_speed

def update_ball():
    global x_ball, y_ball, x_speed_ball, y_speed_ball

    if (x_ball + x_speed_ball + game.ball_rad) > conf.width or (x_ball + x_speed_ball - game.ball_rad) < 0:
        x_speed_ball = -x_speed_ball
    
    if (y_ball + y_speed_ball + game.ball_rad) > conf.height  or (y_ball + y_speed_ball - game.ball_rad) < 0:
        y_speed_ball = -y_speed_ball
    
    x_ball = x_ball + x_speed_ball
    y_ball = y_ball + y_speed_ball

def text_objects(text, font):
    TextSurface = font.render(text, True, color.black)
    return TextSurface, TextSurface.get_rect()

def show_message(text):
    largeText = pygame.font.Font('freesansbold.ttf', 80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (conf.center_x,conf.center_y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(0.5)


def check_collision():
    if abs(x-x_ball)<game.ball_rad and abs(y-y_ball)<game.ball_rad:
        show_message("CRASHHH")




if __name__ == "__main__":

    __init__()

    pygame.init()
    gameDisplay = pygame.display.set_mode( window_size )
    pygame.display.set_caption('Titulo')
    clock = pygame.time.Clock()

    while not flag_end:
        event_handler()
        update_pos()
        update_ball()


        on_draw()
        check_collision()

        clock.tick(60) # fps

    pygame.quit()
    quit()