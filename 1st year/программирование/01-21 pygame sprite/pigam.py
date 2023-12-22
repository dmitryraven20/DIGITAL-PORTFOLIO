import pygame
from pygame import key
from random import randint
#from tkinter import *
#from tkinter import messagebox

pygame.init()

field = pygame.image.load('bckgr.jpg')

MOVE_CONST = 10
WIDTH = 50
HEIGHT = 100
#Tk().wm_withdraw()

window_width = 1280
window_height = 720 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('plr.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        #self.rect.x += 5
        if self.rect.left > window_width:
            self.rect.right = 0

class Enemies(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('enem.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedy = randint(5,10)
        self.rect.right = randint(0, window_width)
    
    def update(self):
        if self.rect.bottom > window_height:
            self.rect.top = 0
            self.rect.right = self.rect.right = randint(0,window_width)
            self.speedy = randint(1,10)

        self.rect.top += self.speedy

fps = 30
global on_lose

#Точки спауна игрока и врагов
on_lose = False
def start(player, enemies):
    on_lose = False
    player.rect.left = window_width//2 - 100
    player.rect.top = window_height - 100
    for enemy in enemies:
        enemy.speedy = randint(1,5)
        enemy.rect.top = randint(-200,-100)
        #enemy.image.fill((0,0,0))

#Инициализация экрана
screen = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("inspired by star conflict")
screen.blit(field, (0,0))

#Отсчет времени
f1 = pygame.font.Font(None, 40)
counter = 0
clock = pygame.time.Clock()
text1 = f1.render(str(counter), True, (240,248,200))

time_delay = 1000
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event,time_delay)

#Добавление текста
f2 = pygame.font.Font(None, 36)
text2 = f2.render('Нажмите R, чтобы перезапустить игру', 1, (250,250,230))
text2_1 = f2.render('или же Q, чтобы выйти из игры', 1, (250,250,230))

all_sprites = pygame.sprite.Group()
player = Player()
player.rect.left = window_width//2 - 100
player.rect.top = window_height - 100

enemies = [Enemies() for i in range(10)]

#Генерация спрайтов
all_sprites.add(player)
all_sprites.add(enemies)
start(player, enemies)

running = True
on_lose = False

while running:
    clock.tick(fps)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == timer_event:
            counter += 1
            text1 = f1.render(str(counter), True, (240,240,200))
        
    keys = pygame.key.get_pressed()

    #Управление игроком
    if not on_lose:
        if keys [pygame.K_LEFT]:
            player.rect.left -= MOVE_CONST
        if keys [pygame.K_RIGHT]:
            player.rect.right += MOVE_CONST
        if keys [pygame.K_UP]:
            player.rect.top -= MOVE_CONST
        if keys [pygame.K_DOWN]:
            player.rect.bottom += MOVE_CONST
    
    #Кнопка перезапуска
    if keys[pygame.K_r]:
        on_lose = False
        start(player,enemies)
        counter = -1
    
    #Кнопка выхода
    if keys[pygame.K_q]:
        on_lose = False
        running = False
        
    #Определение столкновения
    for enemy in enemies:
        if player.rect.colliderect(enemy.rect):
            on_lose = True
            #enemy.image.fill((255,0,0))

    if on_lose:
        for enemy in enemies:
            enemy.speedy = 0
            #if counter <= 5:
            #    messagebox.showinfo('Вы не справились')
            #    break
            #elif counter <= 10:
            #    messagebox.showinfo('Терпимо')
            counter = -1

    all_sprites.update()
    screen.blit(field, (0,0))
    screen.blit(text1, (10,90))
    screen.blit(text2, (10,20))
    screen.blit(text2_1, (10,50))

    all_sprites.draw(screen)
    pygame.display.flip()