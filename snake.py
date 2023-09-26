import pygame
import random

# Initialize game window
pygame.init()
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Snake Game")

# Define pixel size of snake and food
PIXEL_SIZE = 20

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.body = [(x, y), (x-PIXEL_SIZE, y), (x-PIXEL_SIZE*2, y)]
        self.direction = "RIGHT"

    def move(self):
        if self.direction == "RIGHT":
            self.x += PIXEL_SIZE
        elif self.direction == "LEFT":
            self.x -= PIXEL_SIZE
        elif self.direction == "UP":
            self.y -= PIXEL_SIZE
        elif self.direction == "DOWN":
            self.y += PIXEL_SIZE
        self.body.insert(0, (self.x, self.y))
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self):
        if self.x < 0 or self.x >= WINDOW_SIZE[0]:
            return True
        if self.y < 0 or self.y >= WINDOW_SIZE[1]:
            return True
        for part in self.body[1:]:
            if self.x == part[0] and self.y == part[1]:
                return True
        return False

class Food:
    def __init__(self):
        self.x = random.randint(0, WINDOW_SIZE[0]//PIXEL_SIZE-1) * PIXEL_SIZE
        self.y = random.randint(0, WINDOW_SIZE[1]//PIXEL_SIZE-1) * PIXEL_SIZE

    def generate_new_position(self):
        self.x = random.randint(0, WINDOW_SIZE[0]//PIXEL_SIZE-1) * PIXEL_SIZE
        self.y = random.randint(0, WINDOW_SIZE[1]//PIXEL_SIZE-1) * PIXEL_SIZE

class Game:
    def __init__(self):
        self.snake = Snake(WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2)
        self.food = Food()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.snake.direction != "LEFT":
                    self.snake.direction = "RIGHT"
                elif event.key == pygame.K_LEFT and self.snake.direction != "RIGHT":
                    self.snake.direction = "LEFT"
                elif event.key == pygame.K_UP and self.snake.direction != "DOWN":
                    self.snake.direction = "UP"
                elif event.key == pygame.K_DOWN and self.snake.direction != "UP":
                    self.snake.direction = "DOWN"

    def update(self):
        self.snake.move()
        if self.snake.x == self.food.x and self.snake.y == self.food.y:
            self.snake.grow()
            self.food.generate_new_position()
        if self.snake.check_collision():
            pygame.quit()
            quit()

    def draw(self):
        screen.fill((0, 0, 0))
        for part in self.snake.body:
            pygame.draw.rect(screen, (255, 255, 255), (part[0], part[1], PIXEL_SIZE, PIXEL_SIZE))
        pygame.draw.rect(screen, (255, 0, 0), (self.food.x, self.food.y, PIXEL_SIZE, PIXEL_SIZE))
        pygame.display.update()

# Start game loop
game = Game()
while True:
    game.handle_input()
    game.update()
    game.draw()
    pygame.time.wait(100)

