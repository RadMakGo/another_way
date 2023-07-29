import pygame
pygame.init()
width = 2500
height = 1400

sc = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
FPS = 60



square = pygame.Rect(width / 2, height / 2, 30, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
            square.y -= 1
    if keys[pygame.K_d]:
            square.x += 1
    if keys[pygame.K_a]:
            square.x -= 1
    if keys[pygame.K_s]:
            square.y += 1
    if keys[pygame.K_e]:
        exit()

     # sc.fill((0,0,0))
    pygame.draw.circle(sc, (255, 0, 0),(500, 500), 20)
    pygame.draw.circle(sc, (255,0, 0),(60, 60), 20)
    pygame.draw.rect(sc, (100,255,0), square)
    clock.tick(FPS)
    pygame.display.update()

