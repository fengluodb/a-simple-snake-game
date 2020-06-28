import sys
import random
import pygame

# initial pygame module
pygame.init()

# set width and height
width = 600
height = 600

# initial the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game by DB')

# initial the speed
clock = pygame.time.Clock()
speed = 15

# the color
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)


class Snake(object):
    def __init__(self):
        # the snake parameter
        self.x = width / 2
        self.y = height / 2
        self.x_change = 0
        self.y_change = 0
        self.list = [[self.x, self.y]]
        self.len = len(self.list)
        self.block = 10
        self.direction = None
        self.state = True
        self.score = 0

    def display(self):
        for i in self.list:
            pygame.draw.rect(screen, blue, [i[0], i[1], self.block, self.block])

    def direction_state(self, event):
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT) and (self.direction != "right"):
                self.x_change = - 10
                self.y_change = 0
                self.direction = "left"
            elif (event.key == pygame.K_RIGHT) and (self.direction != "left"):
                self.x_change = 10
                self.y_change = 0
                self.direction = "right"
            elif (event.key == pygame.K_UP) and (self.direction != "down"):
                self.x_change = 0
                self.y_change = -10
                self.direction = "up"
            elif (event.key == pygame.K_DOWN) and (self.direction != "up"):
                self.x_change = 0
                self.y_change = 10
                self.direction = "down"

    def move(self):
        self.x += self.x_change
        self.y += self.y_change
        self.list.append(list((self.x, self.y)))
        if len(self.list) > self.len:
            del self.list[0]

        if self.x >= width or self.x < 0 or self.y >= height or self.y < 0:
            self.state = False

        if [self.x, self.y] in self.list[:-1]:
            self.state = False


class Food(object):
    def __init__(self):
        self.block = 10
        self.x = round(random.randrange(0, width - self.block) / 10.0) * 10.0
        self.y = round(random.randrange(0, height - self.block) / 10.0) * 10.0

    def recreate(self):
        self.x = round(random.randrange(0, width - self.block) / 10.0) * 10.0
        self.y = round(random.randrange(0, height - self.block) / 10.0) * 10.0

    def display(self):
        pygame.draw.rect(screen, red, [self.x, self.y, self.block, self.block])


def text_display(x):
    pygame.font.init()
    my_font = pygame.font.Font(None, 30)
    text_image = my_font.render("Score:{}".format(x), True, white)
    screen.blit(text_image, (20, 20))


def Main():
    while True:
        snake = Snake()
        food = Food()
        while snake.state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                snake.direction_state(event)
            snake.move()
            if snake.x == food.x and snake.y == food.y:
                snake.len += 1
                snake.score += 1
                food.recreate()
                while [food.x, food.y] in snake.list:
                    food.recreate()

            screen.fill(black)
            snake.display()
            food.display()
            text_display(snake.score)
            pygame.display.update()
            clock.tick(speed)
        sys.exit()


if __name__ == '__main__':
    Main()
