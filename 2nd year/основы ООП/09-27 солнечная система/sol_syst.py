from dataclasses import dataclass
from math import *

import pygame as pg

@dataclass
class Planet:
    x = y = 700
    boost = 100
    i = 0

    __n: any
    __r: any
    __V: any
    __speed: any

    def draw(self):
        angle = self.i * pi / (self.__speed * self.boost)
        self.x = int((self.__r * 160 * cos(angle)) + sun_1)
        self.y = int((self.__r * 140 * sin(angle)) + sun_2)
        self.i += 3
        image = pg.image.load(planet_pics[self.__n - 1])
        size = (self.__V * 30, self.__V * 30)
        image = pg.transform.scale(image, size)
        screen.blit(image, (self.x, self.y))

    def angle_return(self):
        return round((self.i * 3.14 / (self.__speed * 200) / 3.14 * 180) % 360, 2)

def file_read(title):
    a = []
    b = open(title, 'r').readlines()
    for line in b:
        a.append([x for x in line.split()])
    return a

width = 1280
height = 720
fps = 30
sun_1 = width / 2
sun_2 = height / 2

pg.init()
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Sol system")
clock = pg.time.Clock()

f1 = pg.font.SysFont('serif', 36)
white = (255, 255, 255)

bg = pg.image.load('bckgr__3_.jpg')
sun_pic = pg.image.load('sun.png')

planets = file_read('Planet list.txt')
kk = []
for i in planets:
    kk.append(Planet(int(i[1]), float(i[2]), float(i[3]), float(i[4])))

global planet_pics
planet_pics = ['merc.png', 'ven.png', 'earth.png', 'mars.png', 'jup.png', 'sat.png', 'uran.png', 'nept.png']

def gameloop():
    running = True
    while running:
        clock.tick(fps)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.blit(bg, (0, 0))
        screen.blit(sun_pic, (sun_1-85,sun_2-100))

        for a in range(0, 1):
            for i in range(len(planets)):
                kk[i].draw()

        pg.display.update()
    pg.quit()

gameloop()
