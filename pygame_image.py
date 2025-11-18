import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_rect = bg_img.get_rect()

    bg_img2 = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img2, True, False)

    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rect = kk_img.get_rect()
    kk_rect.center = 300, 200
    

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_w]:
            kk_rect.move_ip((0, -1))
        if key_lst[pg.K_a]:
            kk_rect.move_ip((-1, 0))
        if key_lst[pg.K_s]:
            kk_rect.move_ip((0, 1))
        if key_lst[pg.K_d]:
            kk_rect.move_ip((1, 0))

        screen.blit(kk_img, kk_rect)


        pg.display.update()
        tmr += 1        
        clock.tick(400)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()