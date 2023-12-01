from PPlay.sprite import *
from init_assets import *
from random import randint

enemy_offset = (screen.width/2) - 240

def spawn_enemies():
    enemy_list = []
    for i in range(10):
        enemy_list.append(Sprite("art/Enemy1.png"))
        enemy_list[i].set_position((48*i)+enemy_offset,(screen.height*4/24)+(16*(-1)**i))

    for i in range(10,20):
        enemy_list.append(Sprite("art/Enemy2.png"))
        enemy_list[i].set_position((48*(i-10))+enemy_offset,(screen.height*6/24)+(16*(-1)**i))

    for i in range(20,30):
        enemy_list.append(Sprite("art/Enemy3.png"))
        enemy_list[i].set_position((48*(i-20))+enemy_offset,(screen.height*8/24)+(16*(-1)**i))

    for i in range(30,40):
        enemy_list.append(Sprite("art/Enemy2.png"))
        enemy_list[i].set_position((48*(i-30))+enemy_offset,(screen.height*10/24)+(16*(-1)**i))

    for i in range(40,50):
        enemy_list.append(Sprite("art/Enemy1.png"))
        enemy_list[i].set_position((48*(i-40))+enemy_offset,(screen.height*12/24)+(16*(-1)**i))

    return enemy_list





shooting_delay = False
enemy_delay = False
speed = 8
bobbing = 4
bobcounter = 0

def game_func(meter):
    confirm_menu_sfx.play()
    
    global shooting_delay
    global enemy_delay
    global speed
    global bobbing
    global bobcounter
    global lost
    global enemy_box
    global enemy_timer
    global timer
    global animation_timer_enemy
    global animation_timer_laser
    global animation_enemy_flag
    global animation_laser_flag
    global enemy_shooting_delay
    global enemy_laser
    global enemy_shooting_timer
    global enemy_laser_timer
    global score

    score                  = 0
    HP                     = 5 - meter*2 # Determina quantas vidas o jogador terá, pela dificuldade
    score_decay            = 0
    collision_range_down   = False
    collision_range_top    = screen.height*12/24 + 32
    collision_range_bottom = screen.height*4/24
    shields                = []
    immunity               = False
    shield_count           = round(3 - meter)
    lost_counter           = 0
    go_to_points           = False
    go_to_menu             = False
    enemy_list             = spawn_enemies()


    for i in range(shield_count):
        for j in range(3):
            shields.append((Sprite("art/shield_unit.png"), (screen.width*1/8-40)+(j*28), screen.height-128+(i*28)))
 
        for i in range(shield_count):
            for j in range(3):
                shields.append((Sprite("art/shield_unit.png"), (screen.width*3/8-40)+(j*28), screen.height-128+(i*28)))

    for i in range(shield_count):
        for j in range(3):
            shields.append((Sprite("art/shield_unit.png"), (screen.width*5/8-40)+(j*28), screen.height-128+(i*28)))
    
    for i in range(shield_count):
        for j in range(3):
            shields.append((Sprite("art/shield_unit.png"), (screen.width*7/8-40)+(j*28), screen.height-128+(i*28)))










    lasers = []
    enemy_lasers = []
    
    dead_enemies = []
    dead_lasers = []
    animation_enemy_flag = True
    animation_timer_enemy = 0
    animation_laser_flag = True
    animation_timer_laser = 0
    enemy_shooting_delay = True
    enemy_shooting_timer = 2500
    enemy_laser = True
    enemy_laser_timer = 0
    i_frames = 0
    round_timer = 0
    win_flag = False
    username = ""

    move_delay = 400
    lost = False

    player.set_position(WIDTH/2,HEIGHT-40)

    




    while True:
        clock.tick(60)
        pgkeys = pg.key.get_pressed()
        pg.display.set_caption(f'Space Invaders - FPS: {clock.get_fps():.2f}')

        score_decay += 1

        if score_decay >= 5 and score != 0 and lost == False and len(enemy_list) > 0:
            score -= 1
            score_decay = 0



        if pgkeys[K_ESCAPE]:
            enemy_list = []
            break


        # MOVEMENT #

        if pgkeys[K_LEFT]:
            player.x -= 6
        elif pgkeys[K_RIGHT]:
            player.x += 6
        
        if player.x > WIDTH - (4+player.width):
            player.x = WIDTH - (4+player.width)
        elif player.x < 4:
            player.x = 4












        # LASER #

        if pgkeys[K_SPACE] and shooting_delay == False:
            shooting_delay = True
            timer = pg.time.get_ticks()
            shoot_sfx.play()
            lasers.append(Sprite("art/shot.png"))
            lasers[-1].set_position(player.x+24,player.y-8)

        if shooting_delay == True and pg.time.get_ticks() - timer >= 300*meter:
            shooting_delay = False





        # ENEMY LASER #

        if enemy_shooting_delay == False and len(enemy_list) > 0:
            shooter = randint(0,len(enemy_list)-1)
            enemy_shooting_delay = True
            enemy_shooting_timer = pg.time.get_ticks()
            enemy_shoot_sfx.play()
            enemy_lasers.append(Sprite("art/shot.png"))
            enemy_lasers[-1].set_position(enemy_list[shooter].x,enemy_list[shooter].y)

        if enemy_shooting_delay == True:
            if pg.time.get_ticks() - enemy_shooting_timer >= 2000+(randint(0,10)*100)-(meter*600): 
                enemy_shooting_delay = False






        # ENEMIES #

        if enemy_delay == False:
            enemy_delay = True
            enemy_timer = pg.time.get_ticks()

            for i in enemy_list:
                i.x += speed
                i.y += bobbing
                bobcounter += 1
                if bobcounter >= len(enemy_list):
                    bobcounter = 0
                    bobbing *= -1

            for i in enemy_list:
                if i.x < 8 or i.x > (screen.width-32):
                    i.x -= speed
                    speed *= -1

                    for j in enemy_list:
                        j.y += 32
                        collision_range_down = True

                        if j.y > screen.height-56:
                            lost = True
                    break
        
        if collision_range_down == True:
            collision_range_top += 32
            collision_range_bottom += 32
            collision_range_down = False










        # COLLISION #

        for i in enemy_list:
            for j in lasers:
                if j.y <= collision_range_top and j.y >= collision_range_bottom:  # Checa se o laser está dentro da faixa onde os inimigos se encontram
                    if (j.x > i.x and j.x < (i.x+i.width)):
                        if (j.y > i.y and j.y < (i.y+i.height)):
                            animation_timer_enemy = pg.time.get_ticks()
                            animation_enemy_flag = False
                            lasers.remove(j)                        
                            enemy_list.remove(i)
                            explosion_sfx.play()
                            move_delay -= 2
                            score += 75 + meter*25
                            dead_enemies.append((Sprite("art/dead_enemy.png"),i.x,i.y))
                elif j.y <= 8:
                    animation_timer_laser = pg.time.get_ticks()
                    animation_laser_flag = False
                    lasers.remove(j)
                    explosion_sfx.play()
                    dead_lasers.append((Sprite("art/laser_dead.png"),(j.x - 18),j.y))


        # SHIELD COLLISION #

        for i in shields:


            for j in lasers:
                if (j.x > i[1] and j.x < (i[1]+24)):
                    if (j.y > i[2] and j.y < (i[2]+24)):
                        explosion_sfx.play()
                        shields.remove(i)
                        lasers.remove(j)


            for j in enemy_lasers:
                if (j.x+2 > i[1] and j.x-2 < (i[1]+24)):
                    if (j.y+j.height > i[2] and j.y+j.height < (i[2]+24)):
                        explosion_sfx.play()
                        shields.remove(i)
                        enemy_lasers.remove(j)


        # PLAYER COLLISION #

        for j in enemy_lasers:
            if (j.x > player.x and j.x < player.x+player.width) and immunity == False:
                if (j.y+j.height > player.y and j.y+j.height < player.y+player.height):
                    death_sfx.play()
                    HP -= 1
                    immunity = True
                    player.x = screen.width/2
                    i_frames = 240
                    enemy_lasers.remove(j)
                    if HP == 0:
                        lost = True











        if pg.time.get_ticks() - animation_timer_enemy >= 250 and animation_enemy_flag == False:
            dead_enemies = []
            animation_enemy_flag = True
        if pg.time.get_ticks() - animation_timer_laser >= 250 and animation_laser_flag == False:
            dead_lasers = []
            animation_laser_flag = True

        if enemy_delay == True and pg.time.get_ticks() - enemy_timer >= move_delay/meter:
            enemy_delay = False











        # DRAW SCREEN #

        screen.set_background_color(0)

        deathbar.draw()

        for i in shields:
            i[0].set_position(i[1],i[2])
            i[0].draw()


        for i in lasers:
            i.y -= 12
            i.draw()

        for i in enemy_lasers:
            i.y += 4*meter
            i.draw()

        for i in enemy_list:
            i.draw()

        for i in dead_enemies:
            i[0].set_position(i[1],i[2])
            i[0].draw()
        for i in dead_lasers:
            i[0].set_position(i[1],i[2])
            i[0].draw()
        
        if i_frames > 0:
            i_frames -= 1

        
        if i_frames > 225:
            player.draw()
        elif i_frames > 210:
            pass
        elif i_frames > 195:
            player.draw()
        elif i_frames > 180:
            pass
        elif i_frames > 165:
            player.draw()
        elif i_frames > 150:
            pass
        elif i_frames > 135:
            player.draw()
        elif i_frames > 120:
            pass
        elif i_frames > 105:
            player.draw()
        elif i_frames > 90:
            pass
        elif i_frames > 75:
            player.draw()
        elif i_frames > 60:
            pass
        elif i_frames > 45:
            player.draw()
        elif i_frames > 30:
            pass
        elif i_frames > 15:
            player.draw()
        elif i_frames > 0:
            pass

        if i_frames == 0:
            player.draw()
            immunity = False




        if lost == True:
            enemy_shooting_delay = True
            shooting_delay = True

            if lost_counter == 1:
                go_to_points = True

            if lost_counter == 0 and go_to_points == False:
                lost_counter = 120

            elif lost_counter > 0:
                lost_counter -= 1
                
                screen.set_background_color(0)
                game_over_art.draw()






            # INPUT SCREEN#


            


            while go_to_points == True:
                screen.set_background_color(0)

                current_mouse = pg.mouse.get_pressed()
                keys = pg.key.get_pressed()
                name.draw()

                user_text, rect = SCORE_FONT.render(username, (255, 255, 255))
                Window.screen.blit(user_text, (screen.width/2 -96, screen.height/2))

                if len(username) != 3:
                    if keys[pygame.K_a] and not(last_key[pygame.K_a]):
                        username += 'A'
                    elif keys[pygame.K_b] and not(last_key[pygame.K_b]):
                        username += 'B'
                    elif keys[pygame.K_c] and not(last_key[pygame.K_c]):
                        username += 'C'
                    elif keys[pygame.K_d] and not(last_key[pygame.K_d]):
                        username += 'D'
                    elif keys[pygame.K_e] and not(last_key[pygame.K_e]):
                        username += 'E'
                    elif keys[pygame.K_f] and not(last_key[pygame.K_f]):
                        username += 'F'
                    elif keys[pygame.K_g] and not(last_key[pygame.K_g]):
                        username += 'G'
                    elif keys[pygame.K_h] and not(last_key[pygame.K_h]):
                        username += 'H'
                    elif keys[pygame.K_i] and not(last_key[pygame.K_i]):
                        username += 'I'
                    elif keys[pygame.K_j] and not(last_key[pygame.K_j]):
                        username += 'J'
                    elif keys[pygame.K_k] and not(last_key[pygame.K_k]):
                        username += 'K'
                    elif keys[pygame.K_l] and not(last_key[pygame.K_l]):
                        username += 'L'
                    elif keys[pygame.K_m] and not(last_key[pygame.K_m]):
                        username += 'M'
                    elif keys[pygame.K_n] and not(last_key[pygame.K_n]):
                        username += 'N'
                    elif keys[pygame.K_o] and not(last_key[pygame.K_o]):
                        username += 'O'
                    elif keys[pygame.K_p] and not(last_key[pygame.K_p]):
                        username += 'P'
                    elif keys[pygame.K_q] and not(last_key[pygame.K_q]):
                        username += 'Q'
                    elif keys[pygame.K_r] and not(last_key[pygame.K_r]):
                        username += 'R'
                    elif keys[pygame.K_s] and not(last_key[pygame.K_s]):
                        username += 'S'
                    elif keys[pygame.K_t] and not(last_key[pygame.K_t]):
                        username += 'T'
                    elif keys[pygame.K_u] and not(last_key[pygame.K_u]):
                        username += 'U'
                    elif keys[pygame.K_v] and not(last_key[pygame.K_v]):
                        username += 'V'
                    elif keys[pygame.K_w] and not(last_key[pygame.K_w]):
                        username += 'W'
                    elif keys[pygame.K_x] and not(last_key[pygame.K_x]):
                        username += 'X'
                    elif keys[pygame.K_y] and not(last_key[pygame.K_y]):
                        username += 'Y'
                    elif keys[pygame.K_z] and not(last_key[pygame.K_z]):
                        username += 'Z'

                if keys[pygame.K_BACKSPACE] and not(last_key[pygame.K_BACKSPACE]) and len(username) > 0:
                    username = username[:-1]

                if len(username) == 3:
                    if keys[pygame.K_SPACE]:
                        pass


                last_key = keys

                if mouse.is_over_object(done):
                    done_bar.draw()
                    if Mouse.is_button_pressed(mouse,1) and not(last_mouse[0]):
                        f = open("score.txt", "a")
                        f.write(f"\n{username}\n{score}")
                        go_to_menu = True
                        break
                done.draw()
                last_mouse = current_mouse

                screen.update()



        if go_to_menu == True:
            break









        if len(enemy_list) == 0:

            if win_flag == False:
                round_timer = 120
                win_flag = True

            if round_timer > 0:
                victory_art.draw()
                round_timer -= 1
            
            if round_timer == 0 and win_flag == True:
                enemy_list = spawn_enemies()
                collision_range_down   = False
                collision_range_top    = screen.height*12/24 + 32
                collision_range_bottom = screen.height*4/24

        if len(enemy_list) != 0:
            win_flag = False
            
        

        score_text, rect = FONT.render(f'score: {int(score)}', (255, 255, 255))
        Window.screen.blit(score_text, (50, 50))


        if HP > 1:
            heart1.draw()
        if HP > 2:
            heart2.draw()

        screen.update()