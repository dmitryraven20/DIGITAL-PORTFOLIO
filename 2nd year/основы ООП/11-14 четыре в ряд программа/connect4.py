import pygame as pg
import time

border = 10
c_size = 60

red = (255,0,0)
yellow = (255,205,0)
white = (255,255,255)

class Board():
    x, y = 800, 520

    def place_piece(l,x,y):
        for i, line in enumerate(circles):
            for j, circle in enumerate(line):
                if circle.rect.collidepoint((x, y)):
                    current_j = -1
                    while current_j + 1 < len(line) and circles[i][current_j+1].color == white:
                        current_j += 1
                    if current_j >= 0:
                        color = Game.next_turn()
                        circle = circles[i][current_j]
                        if l:
                            circle.recolize(color)

class Piece(pg.sprite.Sprite):
    def __init__(self, i: int, j: int, size: int):
        super().__init__()
        self.color = white
        self.image = pg.Surface((size, size))
        self.image.fill(self.color)
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (border + (c_size + border) * i, border + (c_size + border) * j)

    def recolize(self,color):
        self.color = color
        self.image.fill(color)

ii = 0
class Game():
    def next_turn():
        global ii
        ii = ii + 1
        if ii % 2 == 0:
            color = red
            message("Ходит желтый игрок  ", yellow)
        else:
            color = yellow
            message("Ходит красный игрок", red)
        return color

    def generate_field():
        for i in range(0, 6):
            line = []
            for j in range(0, 6):
                circle_group.add(Piece(i, j, c_size))
                line.append(circle_group.sprites()[-1])
            circles.append(line)

    def reset(det):
        det = False
        time.sleep(2)
        gameloop()

pg.init()
field = pg.image.load('bckgr (2).jpg')
screen = pg.display.set_mode((Board.x,Board.y))
pg.display.set_caption('четверка')
screen.blit(field, (0,0))
clock = pg.time.Clock()

circle_group = pg.sprite.Group()
circles = []

f1 = pg.font.SysFont('centurygothic', 30)
f2 = pg.font.SysFont('arialnarrow', 30)
text2 = f1.render('Нажмите C, чтобы сбросить игровое поле', 1, (250,250,230),(20,20,30))
text2_1 = f1.render('или же Q, чтобы выйти из игры', 1, (250,250,230),(20,20,30))

def message(msg, color):
    mesg = f2.render(msg, True, color,(40,45,50))
    screen.blit(mesg, (440,340))

# def check_row(color):
#     t = 0
#     for i, line in enumerate(circles):
#         for j, circle in enumerate(line):
#             current_j = -1
#             circle = circles[i][current_j]
#             if circle.color == color:
#                 t = t + 1
#                 if t == 4:
#                     message("Игра завершена", color)
#             else:
#                 t = 0

def gameloop():
    Game.generate_field()
    
    is_running = True
    while is_running:
        clock.tick(60)
        screen.blit(text2, (10,440))
        screen.blit(text2_1, (10,470))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    is_running = False
                elif event.key == pg.K_c:
                    Game.reset(is_running)

            elif event.type == pg.MOUSEBUTTONDOWN:
                (x, y) = pg.mouse.get_pos()
                l,_,_ = pg.mouse.get_pressed()

                Board.place_piece(l,x,y)

        circle_group.draw(screen)
        pg.display.flip()

gameloop()
