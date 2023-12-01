from init_assets import *

def rank_func():
    confirm_menu_sfx.play()

    while True:
        screen.set_background_color(0)


        f = open("score.txt", "r+")

        scores = f.readlines()
        scorelist = []

        for i in range(int(len(scores)/2)):
            scorelist.append((scores[i*2][:-1],int(scores[i*2 + 1])))
        ranklist = sorted(scorelist, key=lambda i: -i[1])

        for i in range(12):
            f = open("score.txt", "r")
            name  = ranklist[i][0]
            score = str(ranklist[i][1])
            name, rect = RANK_FONT.render(name, (255, 255, 255))
            Window.screen.blit(name, (screen.width/2 -144, screen.height*(i*1.2+4)/20))
            score, rect = RANK_FONT.render(score, (255, 255, 255))
            Window.screen.blit(score, (screen.width/2 +64, screen.height*(i*1.2+4)/20))

        for i in range(12):
            position_dict = {0: '1st', 1: '2nd', 2: '3rd', 3: '4th', 
                             4: '5th', 5: '6th', 6: '7th', 7: '8th', 
                             8: '9th', 9: '10th', 10: '11th', 11: '12th', }
            position = position_dict[i]
            position, rect = RANK_FONT.render(position, (255, 255, 255))
            Window.screen.blit(position, (screen.width/2 -256, screen.height*(i*1.2+4)/20))

        ranking2.draw()
        keys = pg.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            break

        screen.update()