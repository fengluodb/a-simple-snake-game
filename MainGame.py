import pygame
import config
import SnakeAndFood
import sys
import information
import time


# 游戏主功能类
class MainGame:
    def __init__(self):
        # 初始化贪吃蛇和食物，并设置生命的数量

        self.lives = config.lives
        self.food = SnakeAndFood.Food()
        self.snake = SnakeAndFood.Snake()
        self.mode = None

        # 模式1的关卡总需要的变量初始化
        self.level = 1
        self.add_speed = 0
        self.game_state = 1

        # 人机对战
        self.player = None
        self.computer = None
        self.state = None

    def startGame(self):
        # 开启游戏，其他功能均在此处开始执行
        while True:
            self.choose_mode()
            if self.mode == 1:
                self.normal_mode()
            elif self.mode == 2:
                self.test_mode()
            elif self.mode == 3:
                self.player_vs_computer()
            self.__init__()

    def choose_mode(self):
        # 选择游戏的模式
        information.choose_mode(screen)
        while self.mode is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.mode = 1
                    elif event.key == pygame.K_2:
                        self.mode = 2
                    elif event.key == pygame.K_3:
                        self.mode = 3

    def normal_mode(self):
        def display():
            # 显示正常模式下游戏时所有需要显示的内容
            screen.fill(config.black)

            self.show_snake_food_only()
            information.score(len(self.snake.body), screen)
            information.show_level(self.level, screen)
            information.show_lives_num(self.lives, screen)
            pygame.display.update()
            clock.tick(config.speed + self.add_speed)

        while self.lives:
            while self.snake.lives:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    else:
                        self.snake.move(self.food.x, self.food.y, event)
                self.snake.move(self.food.x, self.food.y)
                self.food.appear_or_disappear(self.snake.body)
                display()
                if len(self.snake.body) > self.level * 10:
                    self.level += 1
                    self.add_speed += 1
                    time.sleep(0.5)
                    information.pass_level(self.level, screen)
                    time.sleep(1)
                    self.snake = SnakeAndFood.Snake()
                    self.food = SnakeAndFood.Food()
            self.lives += -1
            if self.lives != 0:
                information.die_information(screen)
                while self.game_state:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            self.game_state = 0
                            self.snake = SnakeAndFood.Snake()
                            self.food = SnakeAndFood.Food()
                            break
                self.game_state = 1
        information.lose_information(screen)
        time.sleep(3)

    def test_mode(self):
        """用于测试贪吃蛇自动移动的算法
        用以改进人机对战
        """
        def display():
            screen.fill(config.black)
            self.show_snake_food_only()
            information.score(len(self.snake.body), screen)
            pygame.display.update()
            clock.tick(config.speed)

        while self.snake.lives:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.snake.auto_move(self.food.x, self.food.y)
            self.food.appear_or_disappear(self.snake.body)
            display()

    def player_vs_computer(self):
        """
        玩家对抗电脑，当一方出界或撞到对手，输，对方先达到二十分,输
        """

        def display():
            screen.fill(config.black)
            for i in self.player.body:
                pygame.draw.rect(screen, self.player.color, [i[0], i[1], self.player.size, self.player.size])
            for j in self.computer.body:
                pygame.draw.rect(screen, self.computer.color, [j[0], j[1], self.computer.size, self.computer.size])
            pygame.draw.rect(screen, self.food.color, [self.food.x, self.food.y, self.snake.size, self.snake.size])
            information.show_both_scores(len(self.player.body), len(self.computer.body), screen)
            pygame.display.update()
            clock.tick(config.speed)

        self.player = SnakeAndFood.MySnake()
        self.computer = SnakeAndFood.MySnake()
        self.computer.color = config.red
        while self.player.lives and self.computer.lives:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                else:
                    self.player.move_mend(self.food.x, self.food.y, event, self.computer.body)
            event = None
            self.player.move_mend(self.food.x, self.food.y, event, self.computer.body)
            self.computer.auto_move_mend(self.food.x, self.food.y, self.player.body)
            self.food.appear_or_disappear(self.player.body + self.computer.body)
            if len(self.player.body) >= 20:
                self.state = 1
                break
            elif len(self.computer.body) >= 20:
                self.state = 0
                break
            display()
        information.win_or_lose(self.player.lives, self.computer.lives, self.state, screen)
        time.sleep(2)

    def show_snake_food_only(self):
        for i in self.snake.body:
            pygame.draw.rect(screen, self.snake.color, [i[0], i[1], self.snake.size, self.snake.size])
        pygame.draw.rect(screen, self.food.color, [self.food.x, self.food.y, self.snake.size, self.snake.size])


if __name__ == '__main__':
    pygame.init()

    # initial the screen and speed
    screen = pygame.display.set_mode((config.width, config.height))
    pygame.display.set_caption('Snake Game by Yin Xing')
    clock = pygame.time.Clock()

    # 开始游戏
    game = MainGame()
    game.startGame()
