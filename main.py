import pygame as pg
pg.init()
screen=pg.display.set_mode((400,500))
while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
    pg.display.flip()
            