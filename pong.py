# Configuration constants
MENU_WIDTH, MENU_HEIGHT = 1000, 1000
GAME_WIDTH, GAME_HEIGHT = 1600, 1000

# Параметры ракеток
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 2

# Параметры мяча
BALL_SIZE = 50
BALL_SPEED = 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
LIME = (150, 235, 100)
GRAY = (128, 128, 128)

WINDOW_CAPTION = 'pong game, ёпт'

# import dependencies
import pygame
import sys
from tkinter.messagebox import showinfo
from pygame.locals import *
import csv


class INPUTBOX():
    def __init__(self, x, y, width, height):
        self.border = Rect(x, y, width, height)
        self.rect = Rect(x+5, y+5, width-10, height-10)
        self.font = pygame.font.Font(None, 72)
        self.text_rect = (x+5, y + height//2 - self.font.get_height()//2)
        self.state = False
        self.text = ''
        self.clear_button = BUTTON(x+width, y, height, height, 'очистить', False, WHITE, 26)
        self.use_button = BUTTON(x+width+height+5, y, height, height, 'принять', False, LIME, 26)

    def draw_inputbox(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)
        text_surf = self.font.render(self.text, True, BLACK)
        screen.blit(text_surf, self.text_rect)
        self.clear_button.draw_button(screen)
        self.use_button.draw_button(screen)
    
    def draw_border(self, screen, color):
        pygame.draw.rect(screen, color, self.border)



class BUTTON():
    def __init__(self, x, y, width, height, text, state, color, font_size):
        self.rect = Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.font_size = font_size
        
        self.state = state
        if self.state == True:
            self.font = pygame.font.Font(None, self.font_size)
            self.text_surf = self.font.render(self.text, True, self.color)
        else:
            self.font = pygame.font.Font(None, self.font_size)
            self.text_surf = self.font.render(self.text, True, self.color)

        self.text_rect = (x + width//2 - self.text_surf.get_width()//2, y + height//2 - self.text_surf.get_height()//2)

    def draw_button(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect)
        screen.blit(self.text_surf, self.text_rect)

    def change_state(self, screen):
        if self.state == True:
            self.font = pygame.font.Font(None, self.font_size)
            self.text_surf = self.font.render(self.text, True, YELLOW)
        else:
            self.font = pygame.font.Font(None, self.font_size)
            self.text_surf = self.font.render(self.text, True, WHITE)
        
        self.draw_button(screen)



class MENU():
    def __init__(self):
        pygame.init()
        self.width = MENU_WIDTH
        self.height = MENU_HEIGHT
        pygame.display.set_caption(WINDOW_CAPTION)
        pygame.display.set_icon(pygame.image.load('icon.png'))
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.menu_buttons = {
            'pc_game': BUTTON(self.width//2-300, 200, 600, 100, 'START VS PC', False, WHITE, 72),
            'user_game': BUTTON(self.width//2-300, 400, 600, 100, 'START VS USER', False, WHITE, 72),
            'statistics': BUTTON(self.width//2-300, 600, 600, 100, 'VEIW STATISTICS', False, WHITE, 72),
            'exit': BUTTON(self.width//2-300, 800, 600, 100, 'QUIT', False, WHITE, 72)
        }

        self.settings_buttons = {
            'time': BUTTON(self.width//4-200, 200, 300, 100, 'TIME', True, YELLOW, 72),
            'score_limit': BUTTON(self.width//4*3-90, 200, 300, 100, 'SCORE', False, WHITE, 72),
            'start': BUTTON(self.width//4*3-90, self.height-150, 300, 100, 'START', False, LIME, 72),
            'back': BUTTON(self.width//4-200, self.height-150, 300, 100, 'BACK', False, WHITE, 72)
        }

        self.inputbox = INPUTBOX(50, 500, 550, 100)

        self.gametype = 'time'
        self.opponent = 'pc'
        self.gamevalue = 0
        

    def draw_menu(self):
        self.screen.fill(GRAY)
        for button in self.menu_buttons:
            self.menu_buttons[button].draw_button(self.screen)
        pygame.display.flip()
        
        while True:
                for event in pygame.event.get():
                    # Обработка закрытия приложения
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        print('Exit...')
                        pygame.quit()
                        sys.exit()
                    # Обработка нажатия на кнопки
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.menu_buttons['pc_game'].rect.collidepoint(event.pos):
                            print('pc_game')
                            self.opponent = 'pc'
                            self.draw_gamesettings()
                        elif self.menu_buttons['user_game'].rect.collidepoint(event.pos):
                            print('user_game')
                            self.opponent = 'user'
                            self.draw_gamesettings()
                        elif self.menu_buttons['statistics'].rect.collidepoint(event.pos):
                            self.draw_stats()
                            print('statistics')
                        elif self.menu_buttons['exit'].rect.collidepoint(event.pos):
                            print('Exit...')
                            pygame.quit()
                            sys.exit()
                        else:
                            print('missclick')
    
    def draw_stats(self):
        # self.screen.fill(GRAY)
        with open('statistics.csv', 'r', newline='') as csvfile:
            stats = []
            csv_reader = csv.reader(csvfile)
            # Чтение и вывод содержимого файла
            for row in csv_reader:
                stats.append(row)
        print(stats)

    def draw_gamesettings(self):
        self.screen.fill(GRAY)
        self.inputbox.draw_inputbox(self.screen)

        descriptions = {
            'time': 'Укажите время игры (в секундах)',
            'score_limit': 'Укажите количество очков'
        }

        description_font = pygame.font.Font(None, 48)
        description_surf = description_font.render(descriptions['time'], True, WHITE)
        self.screen.blit(description_surf, (50, 450))

        for button in self.settings_buttons:
            self.settings_buttons[button].draw_button(self.screen)
        pygame.display.flip()

        while True:
                for event in pygame.event.get():
                    # Обработка закрытия приложения
                    if event.type == pygame.QUIT:
                        print('Exit...')
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.draw_menu()

                    elif event.type == pygame.KEYDOWN and self.inputbox.state:
                        if event.key == K_BACKSPACE:
                            self.inputbox.text = self.inputbox.text[:-1]
                        elif event.key == K_RETURN:
                            if self.inputbox.text.isdigit():
                                self.gamevalue = int(self.inputbox.text)
                            else:
                                self.inputbox.text = ''
                                showinfo(title='ОшибОчка', message='Некорректное значение')
                            print(self.gamevalue)
                        else:
                            self.inputbox.text += event.unicode
                        self.inputbox.draw_inputbox(self.screen)


                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.settings_buttons['time'].rect.collidepoint(event.pos):
                            self.gametype = 'time'
                            description_font = pygame.font.Font(None, 48)
                            description_surf = description_font.render(descriptions['time'], True, WHITE)
                            pygame.draw.rect(self.screen, GRAY, (50, 450, 800, 50))
                            self.screen.blit(description_surf, (50, 450))
                            self.settings_buttons['time'].state = True
                            self.settings_buttons['score_limit'].state = False
                            self.settings_buttons['time'].change_state(self.screen)
                            self.settings_buttons['score_limit'].change_state(self.screen)

                        elif self.settings_buttons['score_limit'].rect.collidepoint(event.pos):
                            self.gametype = 'score_limit'
                            description_font = pygame.font.Font(None, 48)
                            description_surf = description_font.render(descriptions['score_limit'], True, WHITE)
                            pygame.draw.rect(self.screen, GRAY, (50, 450, 800, 50))
                            self.screen.blit(description_surf, (50, 450))
                            self.settings_buttons['time'].state = False
                            self.settings_buttons['score_limit'].state = True
                            self.settings_buttons['time'].change_state(self.screen)
                            self.settings_buttons['score_limit'].change_state(self.screen)
                        elif self.settings_buttons['start'].rect.collidepoint(event.pos):
                            if self.inputbox.text != '' and not self.gamevalue == 0:
                                print('start')
                                game = GAME(self.gametype, self.gamevalue, self.opponent)
                                game.loop()

                            else:
                                showinfo(title='ОшибОчка', message='Некорректное значение')
                        elif self.settings_buttons['back'].rect.collidepoint(event.pos):
                            self.draw_menu()
                            print('back')
                        
                        if self.inputbox.rect.collidepoint(event.pos):
                            self.inputbox.state = True
                            self.inputbox.draw_border(self.screen, LIME)
                        elif self.inputbox.use_button.rect.collidepoint(event.pos):
                            if self.inputbox.text.isdigit():
                                self.gamevalue = int(self.inputbox.text)
                            else:
                                self.inputbox.text = ''
                                showinfo(title='ОшибОчка', message='Некорректное значение')
                            print(self.gamevalue)
                        elif self.inputbox.clear_button.rect.collidepoint(event.pos):
                            self.inputbox.text = ''
                            self.gamevalue = 0
                            print(self.gamevalue)
                        else:
                            self.inputbox.state = False
                            self.inputbox.draw_border(self.screen, GRAY)
                            print(self.gametype, self.opponent, self.gamevalue)

                self.inputbox.draw_inputbox(self.screen)
                pygame.display.flip()
                pygame.display.update()


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
        try:
            with open('statistics.csv', 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(value)
                            
            with open('statistics.csv', 'r', newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                data = list(csv_reader)
                # Сортировка данных по третьему элементу
                sorted_data = sorted(data, key=lambda x: x[2])
                sorted_data = sorted_data[::-1]

            # Запись отсортированных данных обратно в CSV файл
            with open('statistics.csv', 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerows(sorted_data)
        except:
                with open('statistics.csv', 'a', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow(value)



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
 


class GAME():
    def __init__(self, gametype, gamevalue, opponent):
        pygame.init()
        self.width = GAME_WIDTH
        self.height = GAME_HEIGHT
        pygame.display.set_caption(WINDOW_CAPTION)
        pygame.display.set_icon(pygame.image.load('icon.png'))
        self.game_screen = pygame.display.set_mode((self.width, self.height))
        self.game_screen.fill(LIME)
        self.default_font = pygame.font.Font(None, 72)
        self.game_end_font = pygame.font.Font(None, 256)
        self.start_time = pygame.time.get_ticks()//1000
        self.gametype = gametype
        self.gamevalue = gamevalue
        self.opponent = opponent

        if self.gametype != 'time':
            self.timer = 0
        else:
            self.timer = self.gamevalue

        self.paddle1 = PADDLE(50, self.height//2 - PADDLE_HEIGHT//2, PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_SPEED)
        self.paddle2 = PADDLE(self.width - PADDLE_WIDTH - 50, self.height//2 - PADDLE_HEIGHT//2, PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_SPEED)
        self.ball = BALL(self.width//2 - BALL_SIZE//2, self.height//2 - BALL_SIZE//2, BALL_SIZE, BALL_SPEED)

        self.score_text = self.default_font.render(f'{self.paddle1.score}:{self.paddle2.score}', True, WHITE)
        self.game_screen.blit(self.score_text, (GAME_WIDTH//2 - self.score_text.get_width()//2, 20))

        self.timer_text = self.default_font.render(f'{self.timer//60}:{self.timer%60}', True, WHITE)
        self.game_screen.blit(self.timer_text, (GAME_WIDTH//2 - self.score_text.get_width()//2, GAME_HEIGHT-100))

        pygame.display.flip()
        

    def change_timer(self):
        if self.gametype == 'time':
            self.timer = self.gamevalue - pygame.time.get_ticks()//1000 + self.start_time
        else:
            self.timer = pygame.time.get_ticks()//1000 - self.start_time

    def update_board(self):
        self.game_screen.fill(LIME)
        self.ball.move(self.paddle1, self.paddle2)
        pygame.draw.rect(self.game_screen, WHITE, self.paddle1.rect)
        pygame.draw.rect(self.game_screen, WHITE, self.paddle2.rect)
        pygame.draw.ellipse(self.game_screen, WHITE, self.ball.rect)
        self.score_text = self.default_font.render(f'{self.paddle1.score}:{self.paddle2.score}', True, WHITE)
        self.game_screen.blit(self.score_text, (GAME_WIDTH//2 - self.score_text.get_width()//2, 20))
        self.timer_text = self.default_font.render(f'{self.timer//60}:{self.timer%60}', True, WHITE)
        self.game_screen.blit(self.timer_text, (GAME_WIDTH//2 - self.score_text.get_width()//2, GAME_HEIGHT-100))
        pygame.display.flip()
        

    def loop(self):
        print(self.gametype, self.gamevalue, self.opponent)
        while True:
            for event in pygame.event.get():
                # Обработка закрытия приложения
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    menu = MENU()
                    menu.draw_menu()
                    break           
                
            # Управление ракетками
            keys = pygame.key.get_pressed()
            self.paddle1.move_left(keys)
            self.paddle2.move_right(keys, self.opponent, self.ball.rect)


            self.change_timer()

            # Проверка условий окончания игры
            if self.gametype == 'time' and self.timer == 0:
                if self.opponent == 'user' and max(self.paddle1.score, self.paddle2.score)!=0: 
                    score = self.gamevalue//max(self.paddle1.score, self.paddle2.score)*10
                    if self.paddle1.score >= self.paddle2.score:
                        winner = 1
                    else:
                        winner = 2
                    stat_write = STAT_MENU(score, self.gamevalue, winner)
                    stat_write.draw_statmenu()
                else:
                    self.game_screen.fill(LIME)
                    text = self.game_end_font.render('GAME ENDED', True, WHITE)
                    self.game_screen.blit(text, (self.width//2-text.get_width()//2, self.height//2-text.get_height()//2))
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    menu = MENU()
                    menu.draw_menu()
                    break

            else:
                if self.paddle1.score == self.gamevalue or self.paddle2.score == self.gamevalue:
                    if self.opponent == 'user':
                        score = self.timer//self.gamevalue*10
                        if self.paddle1.score >= self.paddle2.score:
                            winner = 1
                        else:
                            winner = 2
                        stat_write = STAT_MENU(score, self.timer, winner)
                        stat_write.draw_statmenu()
                    else:
                        self.game_screen.fill(LIME)
                        text = self.game_end_font.render('GAME ENDED', True, WHITE)
                        self.game_screen.blit(text, (self.width//2-text.get_width()//2, self.height//2-text.get_height()//2))
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        menu = MENU()
                        menu.draw_menu()
                        break

            self.update_board()            


class STAT_MENU():
    def __init__(self, score, time, winner):
        pygame.init()
        self.width = MENU_WIDTH
        self.height = MENU_HEIGHT
        pygame.display.set_caption(WINDOW_CAPTION)
        pygame.display.set_icon(pygame.image.load('icon.png'))
        self.stat_screen = pygame.display.set_mode((self.width, self.height))
        self.stat_screen.fill(GRAY)
        self.default_font = pygame.font.Font(None, 144)
        self.score = score
        self.winner = winner
        self.time = time
        self.name_box = INPUTBOX(10, 200, 600, 100)
        self.exit_button = BUTTON(self.width//2-300, self.height-200, 600, 150, 'Exit without saving', False, WHITE, 72)
        pygame.display.flip()
        
    
        

    def draw_statmenu(self):
        self.stat_screen.fill(GRAY)
        self.name_box.draw_inputbox(self.stat_screen)
        text = self.default_font.render(f'Winner: player {self.winner}', True, WHITE)
        self.stat_screen.blit(text, (self.width//2-text.get_width()//2,20))
        self.exit_button.draw_button(self.stat_screen)
        print(self.score, self.winner)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    menu = MENU()
                    menu.draw_menu()
                    break       

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.name_box.rect.collidepoint(event.pos):
                        self.name_box.state = True
                        self.name_box.draw_border(self.stat_screen, LIME)

                    elif self.name_box.use_button.rect.collidepoint(event.pos):
                        try:
                            with open('statistics.csv', 'a', newline='') as csvfile:
                                csv_writer = csv.writer(csvfile)
                                csv_writer.writerow([self.name_box.text, self.time, self.score])
                            
                            with open('statistics.csv', 'r', newline='') as csvfile:
                                csv_reader = csv.reader(csvfile)
                                data = list(csv_reader)

                            # Сортировка данных по третьему элементу
                            sorted_data = sorted(data, key=lambda x: x[2])
                            sorted_data = sorted_data[::-1]

                            # Запись отсортированных данных обратно в CSV файл
                            with open('statistics.csv', 'w', newline='') as csvfile:
                                csv_writer = csv.writer(csvfile)
                                csv_writer.writerows(sorted_data)
                        except:
                            with open('statistics.csv', 'a', newline='') as csvfile:
                                csv_writer = csv.writer(csvfile)
                                csv_writer.writerow([self.name_box.text, self.time, self.score])
                        text = self.default_font.render('WRITED!', True, WHITE)
                        self.stat_screen.blit(text, (self.width//2 - text.get_width()//2, 320))
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        menu = MENU()
                        menu.draw_menu()
                        break    

                    elif self.name_box.clear_button.rect.collidepoint(event.pos):
                        self.name_box.text = ''
                    
                    elif self.exit_button.rect.collidepoint(event.pos):
                        menu = MENU()
                        menu.draw_menu()
                        break    
                    else:
                        self.name_box.state = False
                        self.name_box.draw_border(self.stat_screen, GRAY)

                elif event.type == pygame.KEYDOWN and self.name_box.state:
                        if event.key == K_BACKSPACE:
                            self.name_box.text = self.name_box.text[:-1]
                        elif event.key == K_RETURN:
                            name = self.name_box.text
                        else:
                            self.name_box.text += event.unicode
                self.name_box.draw_inputbox(self.stat_screen) 
            pygame.display.flip() 
                

if __name__ == '__main__':
    menu = MENU()
    menu.draw_menu()
