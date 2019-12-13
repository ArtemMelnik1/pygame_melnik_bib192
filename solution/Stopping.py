import pygame


class Stopping:
    @staticmethod
    def gameover():
        """"
        Остановка игры при проигрыше, когда заканчиваются жизни.
        Останавливается движение персонажей, при нажатии space игра возобновляется.
        """
        stop = True
        while stop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                stop = False
                pygame.mixer.music.play(-1)
