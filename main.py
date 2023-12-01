from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.keyboard import *
from variables import *
from init_assets import *
from game import *
from difficulty import *
from ranking import *

while True:
    
    pg.display.set_caption(f'Halloween Invaders - FPS: {clock.get_fps():.2f}')
    screen.set_background_color(0)
    sair.draw()
    ranking.draw()
    jogar.draw()
    dificuldade.draw()
    title.draw()

    current_mouse = pg.mouse.get_pressed()
    

    if mouse.is_over_object(jogar):
        jogar_bar.draw()
        if current_mouse[0] and not(last_mouse[0]):
            game_func(meter)

    elif mouse.is_over_object(dificuldade):
        dificuldade_bar.draw()
        if Mouse.is_button_pressed(mouse,1) and not(last_mouse[0]):
            meter = diff_func()

    elif mouse.is_over_object(ranking):
        ranking_bar.draw()
        if Mouse.is_button_pressed(mouse,1) and not(last_mouse[0]):
            rank_func()

    elif mouse.is_over_object(sair):
        sair_bar.draw()
        if Mouse.is_button_pressed(mouse,1) and not(last_mouse[0]):
            screen.close()

    last_mouse = current_mouse
    
    screen.update()