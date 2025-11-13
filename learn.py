import pygame as pg
import time

pg.init()
screen = pg.display.set_mode((1420, 710))
pg.display.set_caption("Gey Game")
icon = pg.image.load('C:/Users/user/Desktop/proglol/геймы/click royale/images/PYGAMEICON.jpg')
pg.display.set_icon(icon)

#lolimg = pg.image.load('click royale/images/PYGAMEICON.jpg')
bgimg = pg.image.load('imgs/bg1.jpg')
player_afk = pg.image.load('imgs/kris_afk.png')
walk_right = [
    pg.image.load('imgs/kris(1)r.png'),
    pg.image.load('imgs/kris(2)r.png'),
    pg.image.load('imgs/kris(1)r.png'),
    pg.image.load('imgs/kris(3)r.png')
]
walk_left = [
    pg.image.load('imgs/kris(1).png'),
    pg.image.load('imgs/kris(2).png'),
    pg.image.load('imgs/kris(1).png'),
    pg.image.load('imgs/kris(3).png')
]
walk_right_bool=False
walk_left_bool=False
walk_anim_k=0
player_pos=(200,400)


last_anim_time = time.time()
run = True
while run:
    screen.fill((0, 0, 0))
    screen.blit(bgimg, (0,0))

    current_time = time.time()

    if walk_right_bool:
        player_pos=[player_pos[0]+1,player_pos[1]]
        screen.blit(walk_right[walk_anim_k], tuple(player_pos))
        if current_time - last_anim_time >=0.2:
            if walk_anim_k == 3:
                walk_anim_k=0
            else: walk_anim_k+=1
            last_anim_time = current_time
    elif walk_left_bool:
        player_pos=[player_pos[0]-1,player_pos[1]]
        screen.blit(walk_left[walk_anim_k], tuple(player_pos))
        if current_time - last_anim_time >=0.2:
            if walk_anim_k == 3:
                walk_anim_k=0
            else: walk_anim_k+=1
            last_anim_time = current_time
    else:
        screen.blit(player_afk, player_pos)

    
    
    
    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                walk_right_bool=True
            if event.key == pg.K_a:
                walk_left_bool=True
        if event.type == pg.KEYUP:
            if event.key == pg.K_d:
                walk_right_bool=False
            if event.key == pg.K_a:
                walk_left_bool=False
    pg.display.update()

pg.quit()