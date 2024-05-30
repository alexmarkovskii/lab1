import unittest
from unittest.mock import patch
from pong import BALL, PADDLE, write_statistics
import pygame

# Константы, необходимые для тестов
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 2

BALL_SIZE = 50
BALL_SPEED = 4

height = 1000
width = 1600

class TestBallMovement(unittest.TestCase):
    # Создаем игровые объекты, необходимые для проверки отскоков мяча
    paddle1 = PADDLE(50, height//2 - PADDLE_HEIGHT//2, PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_SPEED)
    paddle2 = PADDLE(width - PADDLE_WIDTH - 50, height//2 - PADDLE_HEIGHT//2, PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_SPEED)
    ball = BALL(width//2 - BALL_SIZE//2, height//2 - BALL_SIZE//2, BALL_SIZE, BALL_SPEED)
    # проверка обработки столкновения с правой ракеткой
    def test_collision_with_rigth_plate(self):
        # Размещаем мяч рядом с правой ракеткой
        self.ball.rect.x = width - PADDLE_WIDTH - 50 - BALL_SIZE - 3
        self.ball.rect.y = height//2 - PADDLE_HEIGHT//2
        # Запускаем движение мяча
        self.ball.move(self.paddle1, self.paddle2)
        # Проверяем изменение направления после столкновения
        self.assertEqual(self.ball.direction[0], -BALL_SPEED)

    # проверка обработки столкновения с левой ракеткой
    def test_collision_with_left_plate(self):
        # Размещаем мяч рядом с левой ракеткой
        self.ball.rect.x = 50 + PADDLE_WIDTH + 3
        self.ball.rect.y = height//2 - PADDLE_HEIGHT//2
        # Меняем направление движения мяча в сторону левой ракетки
        self.ball.direction[0] = - self.ball.direction[0]
        # Запускаем движение мяча
        self.ball.move(self.paddle1, self.paddle2)
        # Проверяем изменение направления после столкновения
        self.assertEqual(self.ball.direction[0], BALL_SPEED)

    def test_collision_with_upper(self):
        # Размещаем мяч рядом с верхней границей
        self.ball.rect.x = 100
        self.ball.rect.y = 3
        # Меняем направление мяча в сторону верхней границы
        self.ball.direction[1] = - self.ball.direction[1]
        # Запускаем движение мяча
        self.ball.move(self.paddle1, self.paddle2)
        # Проверяем изменение направления после столкновения
        self.assertEqual(self.ball.direction[1], BALL_SPEED)

    def test_collision_with_lower(self):
        # Размещаем мяч рядом с верхней границей
        self.ball.rect.x = 100
        self.ball.rect.y = height - BALL_SIZE - 3
        # Запускаем движение мяча
        self.ball.move(self.paddle1, self.paddle2)
        # Проверяем изменение направления после столкновения
        self.assertEqual(self.ball.direction[1], -BALL_SPEED)
    
    def test_paddle1_score(self):
        # Размещаем мяч рядом с правой границей
        previous_score = self.paddle1.score
        self.ball.rect.x = width - BALL_SIZE
        self.ball.rect.y = 300
        # Меняем направление мяча в сторону правой границы
        self.ball.direction[0] = BALL_SPEED
        # Запускаем движение мяча
        self.ball.move(self.paddle1, self.paddle2)
        # Проверяем начисление очков первому пользователю
        self.assertEqual(self.paddle1.score, previous_score + 1)

    def test_paddle2_score(self):
        # Размещаем мяч рядом с левой границей
        previous_score = self.paddle2.score
        self.ball.rect.x = 3
        self.ball.rect.y = 300
        # Меняем направление мяча в сторону левой границы
        self.ball.direction[0] = -BALL_SPEED
        # Запускаем движение мяча
        self.ball.move(self.paddle1, self.paddle2)
        # Проверяем начисление очков второму пользователю
        self.assertEqual(self.paddle1.score, previous_score + 1)


class TestPaddleMovement(unittest.TestCase):
    # Создаем игровые объекты, необходимые для проверки движения ракетки
    paddle1 = PADDLE(50, height//2 - PADDLE_HEIGHT//2, PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_SPEED)
    paddle2 = PADDLE(width - PADDLE_WIDTH - 50, height//2 - PADDLE_HEIGHT//2, PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_SPEED)
    def test_up_direcrion_l(self):
        start_position = self.paddle1.rect.y
        # Иммитируем нажатие на клавишу W
        keys = {pygame.K_w: True, pygame.K_s: False}
        self.paddle1.move_left(keys)
        self.assertEqual(self.paddle1.rect.y, start_position-self.paddle1.speed)

    def test_down_direcrion_l(self):
        start_position = self.paddle1.rect.y
        # Иммитируем нажатие на клавишу S
        keys = {pygame.K_w: False, pygame.K_s: True}
        self.paddle1.move_left(keys)
        self.assertEqual(self.paddle1.rect.y, start_position+self.paddle1.speed)

    def test_upper_border(self):
        # Устанавливаем позицию раекетки на верхнюю границу
        self.paddle1.rect.y = 0
        previous_position = self.paddle1.rect.y
        # Иммитируем нажатие на клавишу W
        keys = {pygame.K_w: True, pygame.K_s: False}
        # Запускаем движение ракетки
        self.paddle1.move_left(keys)
        # Проверяем, что ракетка не изменила свое положение
        self.assertEqual(self.paddle1.rect.y, previous_position)

    def test_lower_border(self):
        # Устанавливаем позицию раекетки на нижнюю границу
        self.paddle1.rect.y = height - self.paddle1.rect.h
        previous_position = self.paddle1.rect.y
        # Иммитируем нажатие на клавишу S
        keys = {pygame.K_w: False, pygame.K_s: True}
        # Запускаем движение ракетки
        self.paddle1.move_left(keys)
        # Проверяем, что ракетка не изменила свое положение
        self.assertEqual(self.paddle1.rect.y, previous_position)


if __name__ == '__main__':
    unittest.main()