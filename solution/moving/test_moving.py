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

    def test_intersec5(self):
        self.move.ax = 100
        self.move.width = 50
        self.move.x1 = 200
        self.move.awidth = 10
        self.move.ay = 400
        self.move.y1 = 400
        self.assertEqual(self.move.intersec(), False)

    def test_intersec6(self):
            self.move.ax = 50
            self.move.width = 500
            self.move.x1 = 10
            self.move.awidth = 200
            self.move.ay = 600
            self.move.y1 = 300
            self.assertEqual(self.move.intersec(), True)

    def test_intersec7(self):
            self.move.ax = 190
            self.move.width = 90
            self.move.x1 = 200
            self.move.awidth = 20
            self.move.ay = 320
            self.move.y1 = 340
            self.assertEqual(self.move.intersec(), False)

    def test_intersec8(self):
        self.move.ax = 700
        self.move.width = 20
        self.move.x1 = 710
        self.move.awidth = 15
        self.move.ay = 450
        self.move.y1 = 445
        self.assertEqual(self.move.intersec(), True)

    def test_intersec9(self):
        self.move.ax = 400
        self.move.width = 10
        self.move.x1 = 200
        self.move.awidth = 20
        self.move.ay = 900
        self.move.y1 = 900
        self.assertEqual(self.move.intersec(), False)

    def test_intersec10(self):
        self.move.ax = 0
        self.move.width = 1
        self.move.x1 = 0
        self.move.awidth = 1
        self.move.ay = 0
        self.move.y1 = 0
        self.assertEqual(self.move.intersec(), True)

    def test_intersec11(self):
        self.move.ax = 100
        self.move.width = 700
        self.move.x1 = 50
        self.move.awidth = 5
        self.move.ay = 200
        self.move.y1 = 400
        self.assertEqual(self.move.intersec(), False)

    def test_intersec12(self):
        self.move.ax = 50
        self.move.width = 200
        self.move.x1 = 70
        self.move.awidth = 30
        self.move.ay = 567
        self.move.y1 = 570
        self.assertEqual(self.move.intersec(), True)

    def test_intersec13(self):
        self.move.ax = 30
        self.move.width = 30
        self.move.x1 = 250
        self.move.awidth = 30
        self.move.ay = 390
        self.move.y1 = 448
        self.assertEqual(self.move.intersec(), False)

    def test_intersec14(self):
        self.move.ax = 400
        self.move.width = 30
        self.move.x1 = 500
        self.move.awidth = 101
        self.move.ay = 300
        self.move.y1 = 310
        self.assertEqual(self.move.intersec(), True)

    def test_intersec15(self):
        self.move.ax = 567
        self.move.width = 3
        self.move.x1 = 100
        self.move.awidth = 1
        self.move.ay = 150
        self.move.y1 = 150
        self.assertEqual(self.move.intersec(), False)

    def test_lives1(self):
        self.move.lives = 5
        self.move.healthes()
        self.assertEqual(self.move.shown, 5)

    def test_lives2(self):
        self.move.lives = 20
        self.move.healthes()
        self.assertEqual(self.move.shown, 20)

unittest.main()
