import pygame

from solution.absolute_path import AbsolutePath
from solution.moving.Moving import Moving


class Main:
    @staticmethod
    def mainest():
        """
        Основная функция которая открывает и запускает игру.
        """
        AbsolutePath.routine()
        pygame.init()
        main = Moving()
        main.routine()
