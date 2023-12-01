from init_assets import *
meter = 1.5


def diff_func():
    global meter 
    confirm_menu_sfx.play()
    last_mouse = (0,0,0)

    while True:
        pgkeys = pg.key.get_pressed()
        

        current_mouse = pygame.mouse.get_pressed()

        if pgkeys[K_ESCAPE]:
            return meter
                
        screen.set_background_color(0)
        facil.draw()
        medio.draw()
        dificil.draw()

        if mouse.is_over_object(facil) or meter == 1:
            facil_bar.draw()
            if mouse.is_over_object(facil) and Mouse.is_button_pressed(mouse,1) and meter != 1 and not(last_mouse[0]):
                meter = 1
                select_menu_sfx.play()

        if mouse.is_over_object(medio) or meter == 1.5:
            medio_bar.draw()
            if mouse.is_over_object(medio) and Mouse.is_button_pressed(mouse,1) and meter != 1.5 and not(last_mouse[0]):
                meter = 1.5
                select_menu_sfx.play()

        if mouse.is_over_object(dificil) or meter == 2:
            dificil_bar.draw()
            if mouse.is_over_object(dificil) and Mouse.is_button_pressed(mouse,1) and meter != 2 and not(last_mouse[0]):
                meter = 2
                select_menu_sfx.play()


        last_mouse = current_mouse

        screen.update()