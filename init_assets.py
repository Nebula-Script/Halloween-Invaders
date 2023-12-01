from PPlay.sprite import *
from variables import *

xcenter = screen.width/2
FONT = pygame.freetype.Font("art/minecraft.ttf", 24)
RANK_FONT = pygame.freetype.Font("art/minecraft.ttf", 48)
SCORE_FONT = pygame.freetype.Font("art/minecraft.ttf", 96)

#-----------------------#
# MAIN SCREEN
#-----------------------#

title       = Sprite("art/title.png")
jogar       = Sprite("art/botJogar.png")
dificuldade = Sprite("art/botDificuldade.png")
ranking     = Sprite("art/botRanking.png")
ranking2    = Sprite("art/botRanking.png")
sair        = Sprite("art/botSair.png")

jogar_bar       = Sprite("art/barraJogar.png")
dificuldade_bar = Sprite("art/barraDificuldade.png")
ranking_bar     = Sprite("art/barraRanking.png")
sair_bar        = Sprite("art/barraSair.png")

title_x, title_y = xcenter-title.width/2,       screen.height/8
jogar_x, jogar_y = xcenter-jogar.width/2,       screen.height*4/8
diff_x, diff_y   = xcenter-dificuldade.width/2, screen.height*5/8
rank_x, rank_y   = xcenter-ranking.width/2,     screen.height*6/8
rank2_x, rank2_y = xcenter-ranking.width/2,     screen.height/12
sair_x, sair_y   = xcenter-sair.width/2,        screen.height*7/8

title.set_position(title_x, title_y)

jogar.set_position(jogar_x, jogar_y)
jogar_bar.set_position(jogar_x, jogar_y)

dificuldade.set_position(diff_x, diff_y)
dificuldade_bar.set_position(diff_x, diff_y)

ranking.set_position(rank_x, rank_y)
ranking2.set_position(rank2_x, rank2_y)
ranking_bar.set_position(rank_x, rank_y)

sair.set_position(sair_x, sair_y)
sair_bar.set_position(sair_x, sair_y)


#-----------------------#
# DIFFICULTY SCREEN
#-----------------------#

facil   = Sprite("art/1.png")
medio   = Sprite("art/2.png")
dificil = Sprite("art/3.png")

facil_bar   = Sprite("art/barraNum.png")
medio_bar   = Sprite("art/barraNum.png")
dificil_bar = Sprite("art/barraNum.png")

facil_x, facil_y     = xcenter-facil.width/2,   screen.height*1/5
medio_x, medio_y     = xcenter-medio.width/2,   screen.height*2/5
dificil_x, dificil_y = xcenter-dificil.width/2, screen.height*3/5


facil.set_position(facil_x, facil_y)
facil_bar.set_position(facil_x, facil_y)

medio.set_position(medio_x, medio_y)
medio_bar.set_position(medio_x, medio_y)

dificil.set_position(dificil_x, dificil_y)
dificil_bar.set_position(dificil_x, dificil_y)



#-----------------------#
# GAME
#-----------------------#

player = Sprite("art/Player.png")
heart1 = Sprite("art/heart.png")
heart2 = Sprite("art/heart.png")
heart1.set_position(screen.width-64,40)
heart2.set_position(screen.width-112,40)

game_over_art = Sprite("art/gameover.png")
game_over_art.set_position((screen.width/2)-(game_over_art.width/2),(screen.height/2)-(game_over_art.height/2))
victory_art   = Sprite("art/win.png")
victory_art.set_position((screen.width/2)-(victory_art.width/2),(screen.height/2)-(victory_art.height/2))
deathbar      = Sprite("art/deathbar.png")
deathbar.set_position(0,screen.height-40)


#-----------------------#
# RANKING
#-----------------------#

name     = Sprite("art/name.png")
done     = Sprite("art/botDone.png")
done_bar = Sprite("art/barraDone.png")

name_x, name_y = xcenter-name.width/2, screen.height*2/8
done_x, done_y = xcenter-name.width/2, screen.height*7/8


name.set_position(name_x, name_y)
done.set_position(done_x, done_y)
done_bar.set_position(done_x, done_y)

score = 0
f = open("score.txt", "r+")

scores = f.readlines()
scorelist = []

for i in range(int(len(scores)/2)):
    scorelist.append((scores[i*2][:-1],int(scores[i*2 + 1])))
ranklist = sorted(scorelist, key=lambda i: -i[1])


#-----------------------#
# AUDIO
#-----------------------#

shoot_sfx        = pygame.mixer.Sound("audio/laserShoot.ogg")
explosion_sfx    = pygame.mixer.Sound("audio/explosion.ogg")
enemy_shoot_sfx  = pygame.mixer.Sound("audio/enemylaser.ogg")
death_sfx        = pygame.mixer.Sound("audio/dead.ogg")
select_menu_sfx  = pygame.mixer.Sound("audio/powerUp.ogg")
confirm_menu_sfx = pygame.mixer.Sound("audio/blipSelect.ogg")