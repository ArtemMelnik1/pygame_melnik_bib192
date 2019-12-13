import pygame

from solution.Stopping import Stopping
from solution.static.static_data import StaticData


class Moving:
    def __init__(self):
        """
        Конструктор, хранятся основные переменные, координаты, изображения, музыка, надписи.
        """
        self.x1 = 0
        self.y1 = 650
        self.x2 = 0
        self.y2 = 0
        self.ax = 2000
        self.ay = 1500
        self.width = 88
        self.width2 = 150
        self.awidth = 40
        self.speed = 30
        self.speed2 = 50
        self.speed3 = 21
        self.count = 0
        self.lives = 3
        self.Right1 = True
        self.Strike = True
        self.items = [(720, 450, u'Play', (255, 255, 255), (255, 215, 0), 0),
                      (720, 490, u'Quit', (255, 255, 255), (255, 215, 0), 1)]
        self.win = pygame.display.set_mode((1440, 900))
        self.screen = pygame.Surface((1440, 900))
        self.info = pygame.Surface((1440, 30))
        pygame.display.set_caption("Spiderman Bros")
        pygame.mixer.music.load(StaticData.absolute_paths['Mitch Murder_-_Frantic Aerobics.mp3'])
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        self.sentence = pygame.font.SysFont('monospace', 25)
        self.game_over = pygame.font.SysFont('arial', 70)
        self.Fone = pygame.image.load(StaticData.absolute_paths['background.png'])
        self.Player = pygame.image.load(StaticData.absolute_paths['spoody.png'])
        self.Enemy = pygame.image.load(StaticData.absolute_paths['ghost.png'])
        self.Bomb = pygame.image.load(StaticData.absolute_paths['cherry.png'])
        self.Health = pygame.image.load(StaticData.absolute_paths['heart.png'])
        self.string = self.sentence.render('Points:' + str(self.count), 0, (255, 0, 0))
        self.game_over1 = self.game_over.render('Game over. Press SPACE to play again', 0, (0, 0, 0))

    def render(self, background, font, num_item):
        """
        Отрисовка надписи Play и Quit на экране, выбор цветов, местоположение надписей.
        """
        for i in self.items:
            if num_item == i[5]:
                background.blit(font.render(i[2], 1, i[4]), (i[0], i[1] - 40))
            else:
                background.blit(font.render(i[2], 1, i[3]), (i[0], i[1] - 40))

    def menu(self):
        """
        Меню, выбор шрифта, при подносе курсора или при нажатии клавиш up, down кнопки закрашиваются другим цветом,
        при нажатии левой кнопкой мыши  на Play происходит запуск игры, при нажатии Quit выход из нее.
        """
        done = True
        font_menu = pygame.font.Font(None, 50)
        item = 0
        while done:
            self.info.fill((0, 100, 200))
            self.screen.fill((0, 100, 200))

            mp = pygame.mouse.get_pos()
            for i in self.items:
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    item = i[5]
            self.render(self.screen, font_menu, item)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        if item > 0:
                            item -= 1
                    if e.key == pygame.K_DOWN:
                        if item == 0:
                            item += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if item == 0:
                        done = False
                    elif item == 1:
                        exit()
            self.win.blit(self.info, (0, 0))
            self.win.blit(self.screen, (0, 30))
            pygame.display.flip()

    def intersec(self):
        """
        Пересечение вишни и главного игрока, на вход идут координаты вишни, координаты игрока, размеры игрока, размеры вишни.
        """
        return self.ax > self.x1 - self.awidth and self.ax < self.x1 + self.width and self.ay > self.y1 - self.awidth and self.ay < self.y1 + self.width

    def healthes(self):
        """
        Появление количества единиц здоровья, можно изменить это количество, изменив self.lives.
        """
        self.shown = 0
        while self.shown != self.lives:
            self.shown += 1

    def DrawDisplay(self):
        """
        Обновление экрана, происходит при каждом перемещении любого предмета игры
        """
        self.win.blit(self.Fone, (0, 0))
        self.win.blit(self.Player, (self.x1, self.y1))
        self.win.blit(self.Enemy, (self.x2, self.y2))
        self.win.blit(self.Bomb, (self.ax, self.ay))
        self.win.blit(self.string, (0, 150))
        self.shown = 0
        self.x = 0
        while self.shown != self.lives:
            self.win.blit(self.Health, (self.x, 170))
            self.x += 25
            self.shown += 1
        pygame.display.update()

    def DrawDisplay2(self):
        """
        Обновление экрана при game over, поялвяется надпись 'Game over. Press SPACE to play again.'
        """
        self.win.blit(self.Fone, (0, 0))
        self.win.blit(self.Player, (self.x1, self.y1))
        self.win.blit(self.Enemy, (self.x2, self.y2))
        self.win.blit(self.Bomb, (self.ax, self.ay))
        self.win.blit(self.string, (0, 150))
        self.win.blit(self.game_over1, (245, 300))
        pygame.display.update()

    def routine(self):
        """
        Основная функция. Можно выйти из игры в процессе. Появляется здоровье. Происходит движение верхнего персонажа,
        которое не зависит от нажатых клавиш. Задаются его правая и левая границы,
        тогда он может двигаться, соответсвтенно, вправо и влево.
        Также происходит движение вишни, координата х зависит от местоположения верхнего персонажа.
        При пересечении главного игрока и вишни, координата y вишни становится первоначальной(сверху),
        координата х по прежнему зависит от местоположения верхнего персонажа, начисляются очки.
        Если координата y вишни вышла за пределы экрана, то она снова появляется сверху, отбавляются жизни.
        Далее вызывается функция game over, происходит обнуление очков, происходит обновление жизней,
        возвращаются изначальные положения всех предметов, музыка останавливается.
        Последнее - передвижение главного героя при помощи клавищ LEFT и RIGHT. Также задаются левая и правая границы.
        """
        self.menu()
        run = True
        while run:
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.healthes()

            if self.Right1:
                self.x2 += self.speed2
                if self.x2 > 1440 - self.width2:
                    self.x2 -= self.speed2
                    self.Right1 = False
            else:
                self.x2 -= self.speed2
                if self.x2 < 0:
                    self.x2 += self.speed2
                    self.Right1 = True
            if not self.Strike:
                self.Strike = True
                self.ax = self.x2
                self.ay = self.y2
            if self.intersec():
                self.Strike = False
                self.ay = -20
                self.ax = 2000
                self.count += 1
                self.string = self.sentence.render('Points:' + str(self.count), 0, (255, 0, 0))

            if not self.intersec() and self.ay > 879:
                self.lives -= 1

            if self.Strike:
                self.ay += self.speed3
                if self.ay > 900:
                    self.Strike = False
                    self.ay = -20
                    self.ax = 2000

            if self.lives <= 0:
                self.DrawDisplay2()
                pygame.mixer.music.stop()
                Stopping.gameover()
                self.x1 = 0
                self.y1 = 650
                self.x2 = 0
                self.y2 = 0
                self.lives = 3
                self.count = 0

                self.string = self.sentence.render('Points:' + str(0), 0, (255, 0, 0))

            buttons = pygame.key.get_pressed()
            if buttons[pygame.K_RIGHT] and self.x1 < 1440 - 150:
                self.x1 += self.speed
            if buttons[pygame.K_LEFT] and self.x1 > -20:
                self.x1 -= self.speed
            self.DrawDisplay()
