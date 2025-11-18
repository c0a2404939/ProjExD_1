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

    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        bg_rect.move_ip(-1, 0)
        screen.blit(bg_img, bg_rect)

        screen.blit(kk_img, [300, 200])

        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()