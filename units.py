import pygame
from pygame.locals import *

class PADDLE:
    def __init__(self, x, y, height, width, speed):
        self.score = 0
        self.speed = speed
        self.height = height
        self.default_rect = Rect(x, y, width, self.height)
        self.rect = self.default_rect.copy()
    
    def move_left(self, keys):
        if keys[pygame.K_w] and not self.rect.y <= 0:
            self.rect.y = self.rect.y - self.speed
        elif keys[pygame.K_s] and not self.rect.y >= GAME_HEIGHT - self.rect.h:
            self.rect.y = self.rect.y + self.speed
    
    def move_right(self, keys, opponent, ball_rect):
        if opponent != 'pc':
            if keys[pygame.K_UP] and not self.rect.y <= 0:
                self.rect.y -= self.speed
            elif keys[pygame.K_DOWN] and not self.rect.y >= GAME_HEIGHT - self.rect.h:
                self.rect.y += self.speed
        else:
            if ball_rect.y + ball_rect.h//2 >= self.rect.y + self.rect.h//2:
                self.rect.y += self.speed
            else:
                self.rect.y -= self.speed

def write_statistics(value):
    with open('statistics.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(value)
                            
    with open('statistics.csv', 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        data = list(csv_reader)
        # Сортировка данных по третьему элементу
        sorted_data = sorted(data, key=lambda x: int(x[2]))
        sorted_data = sorted_data[::-1]

    # Запись отсортированных данных обратно в CSV файл
    with open('statistics.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(sorted_data)
    return sorted_data


class BALL:
    def __init__(self, x, y, size, speed):
        self.size = size
        self.default_rect = Rect(x, y, self.size, self.size)
        self.rect = self.default_rect.copy()
        self.direction = [speed, speed]

    def move(self, paddle1, paddle2):
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]

        if self.rect.y <= 0 or self.rect.y >= GAME_HEIGHT - self.size:
            self.direction[1] *= -1
        elif Rect.colliderect(self.rect, paddle1.rect):
            self.direction[0] *= -1
            self.rect.x += self.direction[0]
        elif Rect.colliderect(self.rect, paddle2.rect):
            self.direction[0] *= -1
            self.rect.x += self.direction[0]

        if self.rect.x <= 0:
            paddle2.score += 1
            paddle1.rect = paddle1.default_rect.copy()
            paddle2.rect = paddle2.default_rect.copy()
            self.rect = self.default_rect.copy()

        elif self.rect.x + self.size >= GAME_WIDTH:
            paddle1.score += 1
            paddle1.rect = paddle1.default_rect.copy()
            paddle2.rect = paddle2.default_rect.copy()
            self.rect = self.default_rect.copy()
 