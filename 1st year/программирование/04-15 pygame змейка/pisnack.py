import pygame
import time
import random
import tkinter
from tkinter import *
from tkinter import messagebox
pygame.init()

pygame.mixer.music.load("untitled.wav")

pygame.mixer.pre_init(44100, -16, 1, 512)
eat = pygame.mixer.Sound('pop.wav')
hit = pygame.mixer.Sound('al.wav')

#используемые в коде цвета 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
dis_width = 1280
dis_height = 720
field = pygame.image.load('bckgr (2).jpg')
field = pygame.transform.scale(field,(dis_width,dis_height))

#инициализация экрана
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('змея')
dis.blit(field, (0,0))
 
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("verdana", 35)

#инициализация главного меню
root = Tk()
root.geometry("500x350")
root.resizable(0,0)

def Your_score(score):
    value = score_font.render("Ваш счет: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    pygame.draw.rect(dis,red,[snake_list[-1][0],snake_list[-1][1], snake_block, snake_block])
    for x in snake_list[:-1]:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    pygame.mixer.music.play(loops=-1, start=0.0,fade_ms = 20)
    game_over = False
    game_close = False
    music_of_game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    #генерация еды
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        dis.blit(field, (0,0))

        while game_close == True: #действие при столкновении
            dis.fill(black)
            if music_of_game_close == True:
                hit.play(loops=0)
                pygame.mixer.music.stop()
                music_of_game_close = False
            message("Вы проиграли.", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: #выход из игры
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c: #перезапуск игры
                        gameLoop()
        
        if game_over == True:
            hit.play()

        for event in pygame.event.get(): #перемещение змейки
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x1_change != snake_block:
                        x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    if x1_change != -snake_block:
                        x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    if y1_change != snake_block:
                        y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    if y1_change != -snake_block:
                        y1_change = snake_block
                    x1_change = 0
                break

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #детектор столкновения
            game_close = True
            music_of_game_close = True
        x1 += x1_change
        y1 += y1_change

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) #создание змейки
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
                music_of_game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        
        pygame.display.update()

        if x1 == foodx and y1 == foody: #рост змейки
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            eat.play()
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

def start_game():
    root.destroy()
    gameLoop()

#открытие главного меню
root.title('Главное меню')
Label(root, text='Привет. Вот правила игры:', font="Arial 14").grid(row=0, sticky=W, pady=5, padx=10)
Label(root, text='\tКормите свою змейку, чтобы она росла', font="Arial 12").grid(row=1, sticky=W, pady=5, padx=10)
Label(root, text='\tНе приближайтесь к стене ', font="Arial 12").grid(row=2, sticky=W, pady=5, padx=10)
Label(root, text='\tНе пытайтесь пройти сквозь себя,', font="Arial 12").grid(row=3, sticky=W, pady=5, padx=10)
Label(root, text='иначе игра завершится.', font="Arial 14").grid(row=4, sticky=W, pady=5, padx=10)

Label(root, text='В таком случае нажмите С, чтобы сыграть по-новой', font="Arial 14").grid(row=6, sticky=W, pady=10, padx=10)
Label(root, text='или Q, чтобы выйти из игры. Удачи!', font="Arial 14").grid(row=7, sticky=W, pady=0, padx=10)

but = Button(root, text='Начать игру', font="couriernew 14", command=start_game)
but.grid(row=9, sticky=E+W, pady=10, padx=10)
root.mainloop()

gameLoop()