import os
import sys
import pygame as pg
import random


WIDTH, HEIGHT = 1600, 900
os.chdir(os.path.dirname(os.path.abspath(__file__)))


mv = {pg.K_UP:(0, -5),
      pg.K_DOWN:(0, 5),
      pg.K_LEFT:(-5, 0),
      pg.K_RIGHT:(5, 0)}

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_file = pg.image.load("fig/3.png")
    kk_img = pg.transform.rotozoom(kk_file, 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    bomb = pg.Surface((20, 20))
    bomb.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb, (255, 0, 0), (10, 10), 10)
    bb_rct = bomb.get_rect()
    bb_rct.center = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    vx, vy = 5, 5

    dire = {(0, -5):pg.transform.rotozoom(kk_file, -90, 2.0),
        (5, -5):pg.transform.rotozoom(kk_file, -135, 2.0),
        (0, -5):pg.transform.rotozoom(kk_file, -90, 2.0),
        (5, 0):pg.transform.flip(kk_file, True, False),
        (5, 5):pg.transform.rotozoom(kk_file, 135, 2.0),
        (0, 5):pg.transform.rotozoom(kk_file, 90, 2.0),
        (-5, 5):pg.transform.rotozoom(kk_file, 45, 2.0),
        (-5, 0):pg.transform.rotozoom(kk_file, 0, 2.0),
        (-5, -5):pg.transform.rotozoom(kk_file, -45, 2.0),
        }

    clock = pg.time.Clock()
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        screen.blit(bg_img, [0, 0])

        if kk_rct.colliderect(bb_rct):
            return

        key_lst = pg.key.get_pressed()
        # print(key_lst)
        sum_mv = [0, 0]

        for k, v in mv.items():
            if key_lst[k]:
                sum_mv[0] += v[0]
                sum_mv[1] += v[1]

                kk_img = dire[tuple(sum_mv)]


        bb_rct.move_ip(vx, vy)
        yoko, tate = check_bound(bb_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        screen.blit(bomb, bb_rct)

        kk_rct.move_ip(sum_mv)
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(kk_img, kk_rct)

        pg.display.update()
        tmr += 1
        clock.tick(50)

def check_bound(obj_rct: pg.Rect) ->tuple[bool, bool]:
    W, H =True, True

    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        W = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        H = False

    return W, H

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
