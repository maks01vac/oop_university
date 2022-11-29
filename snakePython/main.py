import pygame
from random import randrange

W = 1200
H = 700
SIZE = 50

x, y = randrange(SIZE, W - SIZE, SIZE), randrange(SIZE, H - SIZE, SIZE)
apple = randrange(SIZE, W - SIZE, SIZE), randrange(SIZE, H - SIZE, SIZE)


length = 1
snake = [(x, y)]

x_head_snake = snake[-1][0] + 25
y_head_snake = snake[-1][1] + 25

x_left_eye, y_left_eye = -12.5 , 12.5
x_right_eye, y_right_eye = 12.5, -12.5

dx, dy = 0, 0
fps = 40

dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
score = 0

speed_count, snake_speed = 0, 10

pygame.init()
surface = pygame.display.set_mode([W, H])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
img = pygame.image.load('fon2.jpg')
game_over = pygame.image.load('game_over.png')

def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

while True:
    #surface.fill(pygame.Color('white'))

    surface.blit(img, (0,0))

    # fon_sound = pygame.mixer.Sound('fon_sound.wav')
    # fon_sound.play()
    # Отрисовка змейки и яблока

    [pygame.draw.rect(surface, pygame.Color(46, 86, 1), (i, j, SIZE - 2,SIZE - 2)) for i, j in snake]

    pygame.draw.line(surface, pygame.Color('brown'),(apple[0]+15,apple[1]),(apple[0]+19,apple[1]-17), 3)
    pygame.draw.ellipse(surface, pygame.Color('green'),(apple[0]+17,apple[1]-13, 20, 8))
    pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE))

    pygame.draw.circle(surface, pygame.Color('white'), (x_head_snake + x_right_eye, y_head_snake + y_right_eye), 9)
    pygame.draw.circle(surface, pygame.Color('white'), (x_head_snake + x_left_eye, y_head_snake - y_left_eye), 9)
    pygame.draw.circle(surface, pygame.Color('black'), (x_head_snake + x_right_eye, y_head_snake + y_right_eye), 4)
    pygame.draw.circle(surface, pygame.Color('black'), (x_head_snake + x_left_eye, y_head_snake - y_left_eye), 4)


    # Показ счетчика

    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    surface.blit(render_score, (5, 5))

    # Движение змейки

    speed_count += 1
    if not speed_count % snake_speed:
        x += dx * SIZE
        y += dy * SIZE
        snake.append((x, y))
        snake = snake[-length:]
        x_head_snake = snake[-1][0] + 25
        y_head_snake = snake[-1][1] + 25

    # Поедание яблока
    bite_apple_sound = pygame.mixer.Sound('bite_apple.wav')

    if snake[-1] == apple:
        apple = randrange(SIZE, W - SIZE, SIZE), randrange(SIZE, H - SIZE, SIZE)
        bite_apple_sound.play()
        length += 1
        score += 1
        snake_speed -= 1
        snake_speed = max(snake_speed, 4)

    # Конец игры

    GO_sound = pygame.mixer.Sound('go.wav')

    if x < 0 or x > W - SIZE or y < 0 or y > H - SIZE or len(snake)!=len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            surface.blit(game_over, (0,0))
            GO_sound.play(5)
            pygame.display.flip()
            close_game()

    pygame.display.flip()
    clock.tick(fps)
    close_game()

    # Логика управления
    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        if dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
            x_left_eye, y_left_eye = -12.5 , 12.5
            x_right_eye, y_right_eye = 12.5, -12.5

    elif key[pygame.K_s]:
        if dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True, }            
            x_left_eye, y_left_eye = 12.5 , -12.5
            x_right_eye, y_right_eye = -12.5, 12.5

    elif key[pygame.K_a]:
        if dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
            x_left_eye, y_left_eye = -12.5 , 12.5
            x_right_eye, y_right_eye = -12.5, 12.5

    elif key[pygame.K_d]:
        if dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True, }
            x_left_eye, y_left_eye = 12.5 , 12.5
            x_right_eye, y_right_eye = 12.5, 12.5

   

