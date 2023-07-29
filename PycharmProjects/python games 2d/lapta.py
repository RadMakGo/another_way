import pygame,sys, random

pygame.init()

size_w = 90
size_h = 30


width = 400
height = 600
FPS = 20

sc = pygame.display.set_mode((width, height))
sc = pygame.display.set_mode((width, height ))
clock = pygame.time.Clock()
pygame.display.set_caption('lapto')
bg = pygame.image.load('field.jpg')
bg = pygame.transform.scale(bg,(400, 600))
scoreenemy = 0
scorehero = 0

def finish():
    pygame.quit()
    sys.exit(0)


def main():
    global scoreheroв, scoreenemy
    sneg = pygame.image.load('pixil-frame-0 (1).png').convert_alpha()
    sneg_rect = sneg.get_rect(center=(width / 2, height - 61.5))
    blue = pygame.image.load('pixil-frame-0.png').convert_alpha()
    blue = pygame.transform.rotate(blue, 180)
    blue_rect = blue.get_rect(center=(width / 2, 63.5))

    enemy = pygame.Rect(width / 2 - 45, 40, size_w, size_h)
    hero = pygame.Rect(width / 2 - 45, height - 40 - 30, size_w, size_h )
    ball = pygame.Rect(width / 2 - 10, height / 2 - 10,  20, 20)
    x_ball_speed = 0
    y_ball_speed = 0
    while not x_ball_speed:
        x_ball_speed = random.randint(-10, 10)
    while not y_ball_speed:
        y_ball_speed = random.randint(-10, 10)

    Fontscore = pygame.font.Font('sniper/scootchover-sans.ttf', 24)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            hero.move_ip(-15, 0)
            sneg_rect.x -= 15
        elif keys[pygame.K_RIGHT]:
            hero.move_ip(15,0)
            sneg_rect.x += 15
        if keys[pygame.K_a]:
            enemy.move_ip(-15, 0)
            blue_rect.x -= 15
        elif keys[pygame.K_d]:
            enemy.move_ip(15,0)
            blue_rect.x += 15
        ball.move_ip(x_ball_speed, y_ball_speed)

        if ball.colliderect(hero):
            y_ball_speed = -10

        if ball.colliderect(enemy):
            y_ball_speed = 10
        if ball.x > width - 20:
            x_ball_speed = random.randint(-10, -1)
        if ball.x < 0:
            x_ball_speed = random.randint(1, 10)

        if ball.y > height:
            pygame.time.delay(1000)
            scoreenemy += 1
            main()
        if ball.y < -20:
            scorehero += 1
            pygame.time.delay(1000)
            main()


        sc.blit(bg, (0, 0))
        showScore = Fontscore.render('score ' + str(scoreenemy), 1, (255, 0, 255))
        showScore2 = Fontscore.render('score ' + str(scorehero), 1, (200, 0, 255))
        sc.blit(showScore, (0, 0))
        sc.blit(showScore2, (0, 550))
        pygame.draw.rect(sc, (48, 208, 242), enemy)
        pygame.draw.rect(sc, (242, 148, 165), hero)
        sc.blit(blue, blue_rect)
        sc.blit(sneg, sneg_rect)
        pygame.draw.ellipse(sc, (43, 166, 255), ball)
        pygame.display.update()
        clock.tick(FPS)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.load('AllStar.mp3')
pygame.mixer.music.play(-1)
main()