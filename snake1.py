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


# define the main function
def Main():
    # the snake parameter
    snake_x = width / 2
    snake_y = height / 2
    snake_x_change = 0
    snake_y_change = 0
    snake_list = [[snake_x, snake_y]]
    snake_len = len(snake_list)
    snake_block = 10
    snake = Snake()

    # initial the food
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # initial game state
    game_state = True

    # initial the direction
    direction = None

    # score
    score = 0

    while True:
        while game_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_LEFT) & (direction != "right"):
                        snake_x_change = - 10
                        snake_y_change = 0
                        direction = "left"
                    elif (event.key == pygame.K_RIGHT) & (direction != "left"):
                        snake_x_change = 10
                        snake_y_change = 0
                        direction = "right"
                    elif (event.key == pygame.K_UP) & (direction != "down"):
                        snake_x_change = 0
                        snake_y_change = -10
                        direction = "up"
                    elif (event.key == pygame.K_DOWN) & (direction != "up"):
                        snake_x_change = 0
                        snake_y_change = 10
                        direction = "down"

            snake_x += snake_x_change
            snake_y += snake_y_change
            snake_list.append(list((snake_x, snake_y)))
            if len(snake_list) > snake_len:
                del snake_list[0]

            if snake_x >= width or snake_x < 0 or snake_y >= height or snake_y < 0:
                game_state = False

            if [snake_x, snake_y] in snake_list[:-1]:
                game_state = False
            screen.fill(black)
            snake.display(snake_list, snake_block)
            pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])
            text_display(score)
            pygame.display.update()
            if snake_x == food_x and snake_y == food_y:
                food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
                snake_len += 1
                score += 1
            clock.tick(speed)
        print(score)
        sys.exit()


def text_display(x):
    pygame.font.init()
    my_font = pygame.font.Font(None, 30)
    text_image = my_font.render("Score:{}".format(x), True, white)
    screen.blit(text_image, (20, 20))


class Snake(object):
    def __init__(self):
        # the snake parameter
        pass

    def display(self, snake_list_1, snake_block_1):
        for i in snake_list_1:
            pygame.draw.rect(screen, blue, [i[0], i[1], snake_block_1, snake_block_1])


if __name__ == '__main__':
    Main()
