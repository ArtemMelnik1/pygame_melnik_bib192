import unittest
from unittest import TestCase

import pygame

from solution.absolute_path import AbsolutePath
from solution.moving.Moving import Moving
from solution.static.static_data import StaticData


class TestMoving(TestCase):
    def setUp(self) -> None:
        StaticData.items_path = '../../items'
        AbsolutePath.routine()
        pygame.init()
        self.move = Moving()


class TestInit(TestMoving):
    def test_intersec1(self):
        self.move.ax = 400
        self.move.width = 88
        self.move.x1 = 400
        self.move.awidth = 40
        self.move.ay = 650
        self.move.y1 = 650
        self.assertEqual(self.move.intersec(), True)

    def test_intersec2(self):
        self.move.ax = 46
        self.move.width = 88
        self.move.x1 = 500
        self.move.awidth = 40
        self.move.ay = 200
        self.move.y1 = 650
        self.assertEqual(self.move.intersec(), False)

    def test_intersec3(self):
        self.move.ax = 38
        self.move.width = 76
        self.move.x1 = 837
        self.move.awidth = 29
        self.move.ay = 387
        self.move.y1 = 653
        self.assertEqual(self.move.intersec(), False)

    def test_intersec4(self):
        self.move.ax = 308
        self.move.width = 300
        self.move.x1 = 250
        self.move.awidth = 100
        self.move.ay = 467
        self.move.y1 = 445
        self.assertEqual(self.move.intersec(), True)

    def test_lives1(self):
        self.move.lives = 5
        self.move.healthes()
        self.assertEqual(self.move.shown, 5)

    def test_lives2(self):
        self.move.lives = 20
        self.move.healthes()
        self.assertEqual(self.move.shown, 20)

unittest.main()