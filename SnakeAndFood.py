# 定义游戏中的对象，贪吃蛇和食物。

import config
import pygame
import random
import AutoMove


# 贪吃蛇对象
class Snake:
    def __init__(self):
        # 初始化贪吃蛇的位置
        self.x = config.snake_x
        self.y = config.snake_y
        self.x_change = 0
        self.y_change = 0

        # 定义贪吃蛇的大小颜色
        self.size = config.size
        self.color = config.blue

        # 初始化贪吃的身体 、移动时的方向及状态
        self.body = [(self.x, self.y)]
        self.direction = None
        self.lives = 1

    def move(self, food_x, food_y, event=None):
        # 控制贪吃蛇在屏幕上移动，并且判断是否死亡
        if event is not None:
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

        # 贪吃蛇移动，并判断是否撞到墙或自己
        self.x += self.x_change
        self.y += self.y_change
        self.die_or_live(food_x, food_y)

    def auto_move(self, food_x, food_y):
        self.direction = AutoMove.simple(self.x, self.y, food_x, food_y, self.direction)
        if self.direction == "left":
            self.x += -10
        elif self.direction == "right":
            self.x += 10
        elif self.direction == "up":
            self.y += -10
        elif self.direction == "down":
            self.y += 10
        self.die_or_live(food_x, food_y)

    def die_or_live(self, food_x, food_y, opponent=None):
        if self.x < 0 or self.y < 0 or self.x > config.width or self.y > config.height:
            self.lives = 0
        elif (self.x, self.y) in self.body and len(self.body) > 1:
            self.lives = 0
        else:
            if self.x == food_x and self.y == food_y:
                self.body.append((self.x, self.y))
            else:
                self.body.append((self.x, self.y))
                del self.body[0]
        if opponent is not None:
            if (self.x, self.y) in opponent and len(self.body) > 1:
                self.lives = 0


# 食物对象
class Food:
    def __init__(self):
        # 初始化食物的位置并定义了颜色
        self.x = round(random.randrange(0, config.width - config.size) / 10.0) * 10.0
        self.y = round(random.randrange(0, config.height - config.size) / 10.0) * 10.0
        self.color = config.green

    def appear_or_disappear(self, snake_body):
        # 当食物被贪吃蛇吃到后，消失，并且不会重生在贪吃蛇中
        if (self.x, self.y) in snake_body:
            self.x = round(random.randrange(0, config.width - config.size) / 10.0) * 10.0
            self.y = round(random.randrange(0, config.height - config.size) / 10.0) * 10.0
            self.appear_or_disappear(snake_body)


class MySnake(Snake):
    """
    对Snake的修改版，以适应人机对战的情况
    """

    def __init__(self):
        super().__init__()

    def move_mend(self, food_x, food_y, event=None, opponent=None):
        if event is not None:
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

        # 贪吃蛇移动，并判断是否撞到墙或自己
        self.x += self.x_change
        self.y += self.y_change
        self.die_or_live(food_x, food_y, opponent)

    def auto_move_mend(self, food_x, food_y, opponent=None):
        self.direction = AutoMove.simple(self.x, self.y, food_x, food_y, self.direction)
        if self.direction == "left":
            self.x += -10
        elif self.direction == "right":
            self.x += 10
        elif self.direction == "up":
            self.y += -10
        elif self.direction == "down":
            self.y += 10
        self.die_or_live(food_x, food_y, opponent)
