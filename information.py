import pygame
import config


# 在屏幕上显示当前得分
def score(num, screen):
    pygame.font.init()
    my_font = pygame.font.Font(None, 30)
    text_image = my_font.render("Score:{}".format(num - 1), True, config.white)
    screen.blit(text_image, (20, 20))


# 游戏开始时，提醒用户如何选择模式
def choose_mode(screen):
    screen.fill(config.black)
    pygame.font.init()
    my_font = pygame.font.Font(None, 30)
    text0 = my_font.render("Choose the mode you want", True, config.white)
    text1 = my_font.render("1.Normal mode: Please press 1", True, config.white)
    text2 = my_font.render("2.Test mode for algorithm: Please press 2", True, config.white)
    text3 = my_font.render("3.Player vs Computer: Please press 3", True, config.white)
    screen.blit(text0, (100, 100))
    screen.blit(text1, (100, 140))
    screen.blit(text2, (100, 180))
    screen.blit(text3, (100, 210))
    pygame.display.update()


def show_level(num, screen):
    pygame.font.init()
    my_font = pygame.font.Font(None, 30)
    text_image = my_font.render("Level:{}".format(num), True, config.white)
    screen.blit(text_image, (200, 20))


def pass_level(num, screen):
    screen.fill(config.black)
    pygame.font.init()
    my_font = pygame.font.Font(None, 30)
    text_image = my_font.render("Congratulation! You passed Level{}".format(num), True, config.white)
    screen.blit(text_image, (100, 200))
    pygame.display.update()


def die_information(screen):
    screen.fill(config.black)
    pygame.font.init()
    my_font = pygame.font.Font(None, 30)
    text0 = my_font.render("You are died! ", True, config.white)
    text1 = my_font.render("Please press ang button to play the level again", True, config.white)
    screen.blit(text0, (200, 200))
    screen.blit(text1, (60, 300))
    pygame.display.update()


def show_lives_num(num, screen):
    pygame.font.init()
    my_font = pygame.font.Font(None, 30)
    text_image = my_font.render("Lives:{}".format(num), True, config.white)
    screen.blit(text_image, (400, 20))


def lose_information(screen):
    screen.fill(config.black)
    pygame.font.init()
    my_font = pygame.font.Font(None, 60)
    text_image = my_font.render("You lose!", True, config.red)
    screen.blit(text_image, (200, 200))
    pygame.display.update()


def win_or_lose(player, computer, information, screen):
    screen.fill(config.black)
    pygame.font.init()
    my_font = pygame.font.Font(None, 60)
    if player == 0:
        text_image = my_font.render("You lose!", True, config.red)
    elif computer == 0:
        text_image = my_font.render("You win!", True, config.red)
    else:
        if information == 1:
            text_image = my_font.render("You win!", True, config.red)
        else:
            text_image = my_font.render("You lose!", True, config.red)
    screen.blit(text_image, (200, 200))
    pygame.display.update()


def show_both_scores(player_score, computer_score, screen):
    pygame.font.init()
    my_font = pygame.font.Font(None, 30)
    text1 = my_font.render("Score of Player:{}".format(player_score - 1), True, config.white)
    text2 = my_font.render("Score of Computer:{}".format(computer_score - 1), True, config.white)
    screen.blit(text1, (20, 20))
    screen.blit(text2, (360, 20))
