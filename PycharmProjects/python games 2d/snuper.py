import pygame, sys, random

width = 640
height = 400
FPS = 20

pygame.init()
sc = pygame.display.set_mode((width, height))
pygame.display.set_caption('SHREKOOD')
clock = pygame.time.Clock()


def finish():
    pygame.quit()
    sys.exit()

def main():
    x,y = -1,-1
    pygame.mouse.set_visible(0)


    bg = pygame.image.load('9d42e2c5f0c6e98f77661b40d67c48fe.jpg')
    bg = pygame.transform.scale(bg, (width, height))
    target = pygame.image.load('download.jpg')

    targetPosition = target.get_rect()
    targetPosition.bottom = random.randint(32, 365)
    targetPosition.left = random.randint(0,592)
    shotsound = pygame.mixer.Sound('sniper/weapons/ak47.wav')
    score = 0
    R = random.randint(1,255)
    G = random.randint(1, 255)
    B = random.randint(1,255)
    ColorGenerator = R, G, B
    fontscore = pygame.font.Font('sniper/scootchover-sans.ttf', 24)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish()
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    shot = pygame.Rect(x, y, 1,1)
                    if shot.colliderect(targetPosition):
                        score += 10
                        targetPosition.bottom = random.randint(56, 365)
                        targetPosition.left = random.randint(0, 592)
                    shotsound.play()
        showScore = fontscore.render('score ' + str(score), 1, (255, 0, 255))
        sc.blit(bg, (0, 0))


        sc.blit(target, targetPosition)
        sc.blit(showScore, (0,0))
        pygame.draw.line(sc, ColorGenerator, (x - 15,y), (x + 15, y))
        pygame.draw.line(sc, ColorGenerator, (x,y - 15), (x,y + 15))
        clock.tick(FPS)
        pygame.display.update()
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.load('shrek.mp3')
pygame.mixer.music.play(-1)
main()