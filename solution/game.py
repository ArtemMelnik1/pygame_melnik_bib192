import pygame
pygame.init()
win = pygame.display.set_mode((1440, 900))
pygame.display.set_caption("Spiderman Bros")
sentence = pygame.font.SysFont('monospace', 25)
game_over = pygame.font.SysFont('arial', 70)

Fone = pygame.image.load('../items/background.png')
Player = pygame.image.load('../items/spoody.png')
Enemy = pygame.image.load('../items/ghost.png')
Bomb = pygame.image.load('../items/cherry.png')
Health = pygame.image.load('../items/heart.png')

x1 = 0
y1 = 650
x2 = 0
y2 = 0
ax= 2000
ay= 1500
width = 88
width2 = 150
awidth = 40
speed = 30
speed2 = 50
speed3 = 21
count = 0
lives = 3
Right1 = False
Strike = False

string = sentence.render('Points:'+str(count), 0, (255, 0, 0))
game_over1 = game_over.render('Game over. Press SPACE to play again', 0, (0, 0, 0))

def healthes():
    global lives
    shown = 0
    while shown != lives:
        shown += 1

def intersec(ax, ay, x1, y1, awidth, width):
    if ax > x1 - awidth and ax < x1+ width and ay > y1 - awidth and ay < y1 + width:
        return 1
    else:
        return 0

def gameover():
    stop = True
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            stop = False


def DrawDisplay():
    win.blit(Fone, (0, 0))
    win.blit(Player, (x1, y1))
    win.blit(Enemy, (x2, y2))
    win.blit(Bomb, (ax, ay))
    win.blit(string, (0, 150))
    global lives
    shown = 0
    x = 0
    while shown != lives:
        win.blit(Health, (x, 170))
        x += 25
        shown += 1

    pygame.display.update()

def DrawDisplay2():
    win.blit(Fone, (0, 0))
    win.blit(Player, (x1, y1))
    win.blit(Enemy, (x2, y2))
    win.blit(Bomb, (ax, ay))
    win.blit(string, (0, 150))
    win.blit(game_over1, (245, 300))
    pygame.display.update()

run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    healthes()

    if Right1:
        x2 += speed2
        if x2 > 1440 - width2:
            x2 -= speed2
            Right1 = False
    else:
        x2 -= speed2
        if x2 < 0:
            x2 += speed2
            Right1 = True
    if Strike == False:
        Strike = True
        ax = x2
        ay = y2

    if intersec(ax, ay, x1, y1, awidth, width):
        Strike = False
        ay = -20
        ax = 2000
        count += 1
        string = sentence.render('Points:' + str(count), 0, (255, 0, 0))

    if intersec(ax, ay, x1, y1, awidth, width) == False and ay > 879:
        lives -= 1

    if Strike:
        ay += speed3
        if ay > 900:
            Strike = False
            ay = -20
            ax = 2000

    if lives <= 0:
        DrawDisplay2()
        gameover()
        x1 = 0
        y1 = 650
        x2 = 0
        y2 = 0
        lives = 3
        count = 0

        string = sentence.render('Points:' + str(0), 0, (255, 0, 0))




    buttons = pygame.key.get_pressed()
    if buttons[pygame.K_RIGHT] and x1 < 1440 - 150:
        x1 += speed
    if buttons[pygame.K_LEFT] and x1 > -20:
        x1 -= speed
    DrawDisplay()
