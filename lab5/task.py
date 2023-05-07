import pygame
from pygame.draw import *
from random import randint

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball:
    def __init__(self, screen, x, y, radius, color, speed, lifetime):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.lifetime = lifetime

    def draw(self):
        """Отрисовка шара"""
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def update(self):
        """
        Обновление координат шара и его направления
        :return: True, если шар ещё не исчез, иначе False
        """
        self.x += self.speed[0]
        self.y += self.speed[1]

        # Отражение от стенок
        if self.x - self.radius < 0 or self.x + self.radius > WINDOW_WIDTH:
            self.speed[0] = -self.speed[0]
        if self.y - self.radius < 0 or self.y + self.radius > WINDOW_HEIGHT:
            self.speed[1] = -self.speed[1]

        self.lifetime -= 1
        return self.lifetime > 0


class Game:
    def __init__(self):
        self.score = 0
        self.balls = []
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.boop_sound = pygame.mixer.Sound("boop.wav")
        self.high_score = 0
        self.time_left = 2 * 60 * 60  # 2 минуты
        self.started = False
        self.load_high_score()

    def restart(self):
        """Перезапуск игры"""
        self.high_score = max(self.high_score, self.score)
        self.score = 0
        self.balls = []
        self.time_left = 2 * 60 * 60
        self.started = False
        self.save_high_score()

    def load_high_score(self):
        """Загрузка рекорда из файла"""
        try:
            with open("high_score.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            pass

    def save_high_score(self):
        """Сохранение рекорда в файл"""
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def new_ball(self):
        """Создание нового шара"""
        radius = randint(10, 50)
        x = randint(10 + radius, WINDOW_WIDTH - radius - 10)
        y = randint(10 + radius, WINDOW_HEIGHT - radius - 10)
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        speed = [randint(-7, 7), randint(-7, 7)]
        lifetime = randint(120, 240)
        ball = Ball(self.screen, x, y, radius, color, speed, lifetime)
        self.balls.append(ball)

    def delete_ball(self, ball):
        """Удаление шара"""
        self.balls.remove(ball)

    def check_click(self, x, y):
        """
        Проверка попадания по шару
        :param x: координата x клика
        :param y: координата y клика
        """
        for ball in self.balls:
            if (x - ball.x) ** 2 + (y - ball.y) ** 2 <= ball.radius ** 2:
                self.delete_ball(ball)
                self.score += 1
                self.boop_sound.play()
                return

    def game_loop(self):
        """Основной цикл игры"""
        # инициализация переменных
        finished = False
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 36)

        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.started:
                        # Запуск игры
                        self.started = True
                    # Проверка попадания по шару
                    self.check_click(*event.pos)

            if not self.started:
                # Отрисовка экрана
                self.screen.fill(BLACK)
                text = font.render("Click to start", True, WHITE)
                self.screen.blit(text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 20))
                pygame.display.update()
                continue

            # Создание нового шара с вероятностью 1/20
            if randint(1, 20) == 1:
                self.new_ball()

            # Отрисовка экрана
            self.screen.fill(BLACK)

            # old_balls = self.balls

            for ball in self.balls:
                if not ball.update():
                    self.delete_ball(ball)

            for ball in self.balls:
                ball.draw()

            text = font.render(f"Score: {self.score}", True, WHITE)
            self.screen.blit(text, (10, 10))

            text = font.render(f"High score: {self.high_score}", True, WHITE)
            self.screen.blit(text, (10, 40))

            text = font.render(f"Time left: {self.time_left // 60}", True, WHITE)
            self.screen.blit(text, (10, 70))

            self.time_left -= 1
            if self.time_left <= 0:
                self.restart()

            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.game_loop()
