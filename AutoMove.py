# 简单的自动寻路逻辑
def simple(snake_x, snake_y, food_x, food_y, direction):
    if direction is None:
        if snake_x < food_x:
            direction = "right"
        if snake_x > food_x:
            direction = "left"
        else:
            if snake_y < food_y:
                direction = "down"
            elif snake_y > food_y:
                direction = "up"
    else:
        if direction == "left":
            if snake_x > food_x:
                direction = "left"
            elif snake_x == food_x:
                if snake_y > food_y:
                    direction = "up"
                elif snake_y < food_y:
                    direction = "down"
            else:
                direction = "up"
        elif direction == "right":
            if snake_x > food_x:
                direction = "up"
            elif snake_x < food_x:
                direction = "right"
            else:
                if snake_y > food_y:
                    direction = "up"
                elif snake_y < food_y:
                    direction = "down"
        elif direction == "up":
            if snake_x < food_x:
                direction = "right"
            elif snake_x > food_x:
                direction = "left"
            else:
                if snake_y < food_y:
                    direction = "left"
        elif direction == "down":
            if snake_x < food_x:
                direction = "right"
            elif snake_x > food_x:
                direction = "left"
            else:
                if snake_y > food_y:
                    direction = "left"
    return direction
