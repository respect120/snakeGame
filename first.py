import pygame
import sys
import random
from pygame import Vector2

pygame.init()


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
        self.head_up = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load(
            '/Users/omaraldowir/Desktop/Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/body_bl.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('/Users/omaraldowir/Desktop/Graphics/eatingSound.mp3')

        self.crunch_sound = pygame.mixer.Sound('/Users/omaraldowir/Desktop/Graphics/eatingSound.mp3')

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if (previous_block.x == -1 and next_block.y == -1) or (
                            previous_block.y == -1 and next_block.x == -1):
                        screen.blit(self.body_tl, block_rect)
                    elif (previous_block.x == -1 and next_block.y == 1) or (
                            previous_block.y == 1 and next_block.x == -1):
                        screen.blit(self.body_bl, block_rect)
                    elif (previous_block.x == 1 and next_block.y == -1) or (
                            previous_block.y == -1 and next_block.x == 1):
                        screen.blit(self.body_tr, block_rect)
                    elif (previous_block.x == 1 and next_block.y == 1) or (previous_block.y == 1 and next_block.x == 1):
                        screen.blit(self.body_br, block_rect)

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

        # Wrap the snake's position around the edges of the screen
        self.body[0].x = self.body[0].x % cell_number
        self.body[0].y = self.body[0].y % cell_number

    def add_blocks(self, num_blocks):
        self.new_block = True
        for _ in range(num_blocks - 1):
            self.body.append(self.body[-1])

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)

# after finishing the game and the project DONE
class Stra:
    def __init__(self):
        self.visible = False
        self.randomize()

    def draw_stra(self):
        stra_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(stra_image, stra_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class TRAP:
    def __init__(self):
        self.randomize()

    def draw_trap(self):
        trap_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(trap_image, trap_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class WATER:
    def __init__(self):
        self.visible = False
        self.randomize()

    def draw_water(self):
        if self.visible:
            water_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
            screen.blit(water_image, water_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.water = WATER()
        self.stra = Stra()
        self.traps = []
        self.score = 0
        self.speed_multiplier = 1.0
        self.show_speed_increase_msg = False
        self.speed_increase_msg_end_time = 0

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.water.draw_water()
        self.stra.draw_stra()
        for trap in self.traps:
            trap.draw_trap()
        self.draw_score()

    def draw_score(self):
        score_text = str(self.score)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6,
                              apple_rect.height)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)

        if self.show_speed_increase_msg:
            speed_msg_surface = game_font.render("x2 Speed!", True, (255, 0, 0))
            speed_msg_rect = speed_msg_surface.get_rect(midleft=(bg_rect.left - 120, bg_rect.centery))
            screen.blit(speed_msg_surface, speed_msg_rect)

    def check_collision(self):
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
            if block == self.stra.pos:
                self.stra.randomize()

        if self.stra.pos == self.snake.body[0]:
            self.score += 2
            self.stra.randomize()
            self.snake.add_blocks(2)
            self.snake.play_crunch_sound()
            self.check_special_items()

        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_blocks(1)
            self.score += 1
            self.snake.play_crunch_sound()
            self.check_special_items()

        if self.water.visible and self.water.pos == self.snake.body[0]:
            self.water.visible = False
            self.snake.new_block = True
            self.speed_multiplier *= 1.5
            self.show_speed_increase_msg = True
            self.speed_increase_msg_end_time = pygame.time.get_ticks() + 3000  # Show message for 3 seconds
            pygame.time.set_timer(SPEED_RESET_EVENT, 3000)  # Set timer to reset speed after 3 seconds

    def check_special_items(self):
        if self.score % 10 == 0 and self.score != 0 and not self.water.visible:
            self.water.randomize()
            self.water.visible = True

        if self.score % 10 == 0 and self.score != 0 and not self.stra.visible:
            self.stra.randomize()
            self.stra.visible = True

        if (len(self.snake.body) - 3) % 5 == 0:
            trap = TRAP()
            while trap.pos in self.snake.body or any(trap.pos == t.pos for t in self.traps):
                trap.randomize()
            self.traps.append(trap)

    def check_fail(self):
        # Remove the wall collision check as it's handled in move_snake
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

        for trap in self.traps:
            if trap.pos == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()
        self.score = 0
        self.traps = []

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            for col in range(cell_number):
                if (row + col) % 2 == 0:
                    grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rect)


cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_size * cell_number))
apple = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/apple.png').convert_alpha()
water_image = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/BALL.png').convert_alpha()
trap_image = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/trap.png').convert_alpha()
stra_image = pygame.image.load('/Users/omaraldowir/Desktop/Graphics/stra.png').convert_alpha()

clock = pygame.time.Clock()
main_game = MAIN()
try:
    game_font = pygame.font.Font('/Users/omaraldowir/Desktop/font/PoetsenOne-Regular.ttf', 25)
except FileNotFoundError:
    print("Font file not found, using default font.")
    game_font = pygame.font.SysFont(None, 25)

SCREEN_UPDATE = pygame.USEREVENT
SPEED_RESET_EVENT = pygame.USEREVENT + 1  # Custom event for resetting speed

pygame.time.set_timer(SCREEN_UPDATE, int(150 / main_game.speed_multiplier))  # Adjust update speed

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
            pygame.time.set_timer(SCREEN_UPDATE, int(150 / main_game.speed_multiplier))  # Adjust update speed
        if event.type == SPEED_RESET_EVENT:
            main_game.speed_multiplier = 1.0  # Reset speed multiplier
            main_game.show_speed_increase_msg = False  # Hide speed increase message
            pygame.time.set_timer(SPEED_RESET_EVENT, 0)  # Stop the timer
            pygame.time.set_timer(SCREEN_UPDATE, int(150 / main_game.speed_multiplier))  # Adjust update speed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and main_game.snake.direction.y != 1:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and main_game.snake.direction.y != -1:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT and main_game.snake.direction.x != -1:
                main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT and main_game.snake.direction.x != 1:
                main_game.snake.direction = Vector2(-1, 0)

    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)  # Keep a consistent frame rate
