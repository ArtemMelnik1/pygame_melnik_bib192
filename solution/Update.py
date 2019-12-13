import pygame
from solution.moving.Moving import Moving
class Update:
    def DrawDisplay(self):
        self.win.blit(self.Fone, (0, 0))
        self.win.blit(self.Player, (self.x1, self.y1))
        self.win.blit(self.Enemy, (self.x2, self.y2))
        self.win.blit(self.Bomb, (self.ax, self.ay))
        self.win.blit(self.string, (0, 150))
        self.lives
        self.shown = 0
        self.x = 0
        while self.shown != self.lives:
            self.win.blit(self.Health, (self.x, 170))
            self.x += 25
            self.shown += 1
        pygame.display.update()

    def DrawDisplay2(self):
        self.win.blit(self.Fone, (0, 0))
        self.win.blit(self.Player, (self.x1, self.y1))
        self.win.blit(self.Enemy, (self.x2, self.y2))
        self.win.blit(self.Bomb, (self.ax, self.ay))
        self.win.blit(self.string, (0, 150))
        self.win.blit(self.game_over1, (245, 300))
        pygame.display.update()