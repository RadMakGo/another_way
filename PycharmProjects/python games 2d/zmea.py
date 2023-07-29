import random

import pygame, sys


width = 600
height = 400
FPS = 20
size = 20
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0,)
white = (255, 255, 255)

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)
speed = 20

pygame.init()

sc = pygame.display.set_mode((width,height))
pygame.display.set_caption('snake game')
clock = pygame.time.Clock()

def add_parts_of_snake(snake,snake_tail,head):
    update = [-size * x for x in head]
    if len(snake_tail) == 0:
        snake_tail.append(snake.move(update[0], update[1]))
    else:
        snake_tail.append(snake_tail[len(snake_tail)-1].move(update[0], update[1]))
def draw_snake(snake,snake_tail, head):
    tmp = snake.move(0,0)   
    head_speed = [speed * x for x in head]
    snake.move_ip(head_speed[0], head_speed[1])
    pygame.draw.rect(sc, green, snake)
    if len(snake_tail) == 0:
        return
    for i in range(0,len(snake_tail) -1):
        snake_tail[len(snake_tail)  -1 -i] = snake_tail[len(snake_tail) - 2 - i]
        pygame.draw.rect(sc, blue, snake_tail[len(snake_tail)-1 -i])
    snake_tail[0] = tmp
    pygame.draw.rect(sc,blue,snake_tail[0])


def make_new_apple():
    apple_x = random.randint(0, width - size)
    apple_y = random.randint(0, height - size)
    apple = pygame.Rect(apple_x, apple_y, size, size)
    return apple
def finish():
    pygame.quit()
    sys.exit(0)

def main(FPS):
    appple = pygame.image.load('pixil-frame-0.png')
    score = 0
    snake = pygame.Rect(width / 2, height / 2, size, size)
    head = up
    apple = make_new_apple()
    snake_tail = []
    fontscore = pygame.font.Font('sniper/scootchover-sans.ttf', 24)
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                finish()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and head != right:

                    head = left
                if event.key == pygame.K_RIGHT and head != left:

                    head = right
                if event.key == pygame.K_UP and head != down:

                    head = up
                if event.key == pygame.K_DOWN and head != up:

                    head = down
                if event.key == pygame.K_LEFT and head == left:
                    FPS = FPS*1.1
                if event.key == pygame.K_LEFT and head == right:
                    FPS = FPS * 1.1
                if event.key == pygame.K_LEFT and head == up:
                    FPS = FPS * 1.1
                if event.key == pygame.K_LEFT and head == down:
                    FPS = FPS * 1.1
                if event.key == pygame.K_LEFT and head == right:
                    FPS = FPS * 0.8
                if event.key == pygame.K_LEFT and head == left:
                    FPS = FPS * 0.8
                if event.key == pygame.K_LEFT and head == down:
                    FPS = FPS * 0.8
                if event.key == pygame.K_LEFT and head == down:
                    FPS = FPS * 0.8
        # if snake.bottom > height or snake.top < 0 or snake.left < 0 or snake.right > width:
        #     return
        if snake.colliderect(apple):

            add_parts_of_snake(snake, snake_tail, head)
            apple = make_new_apple()
            score += 10
        if len(snake_tail) != 0 and snake.collidelist(snake_tail) != -1:
            return

        if snake.bottom > height:
            snake = pygame.Rect(snake.left, 0, size, size)
        if snake.bottom < 0:
            snake = pygame.Rect(snake.left,height, size, size)
        if snake.left < 0:
            snake = pygame.Rect(width, snake.top,size, size)
        if snake.left > width:
            snake = pygame.Rect(0, snake.top, size, size)








        sc.fill((0,120,0))
        draw_snake(snake,snake_tail,head)
        showsroce = fontscore.render('applescore ' + str(score), 1, (red))
        sc.blit(showsroce, (0,0))

        sc.blit(appple, (apple))

        clock.tick(FPS)
        pygame.display.update()
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.load('shrek.mp3')
pygame.mixer.music.play(-1)


main(FPS)
