import pygame
pygame.init()
width = 1000
height = 800

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
            square.y -= 10
    if keys[pygame.K_d]:
            square.x += 10
    if keys[pygame.K_a]:
            square.x -= 10
    if keys[pygame.K_s]:
            square.y += 10
      # sc.fill((0,0,0))
    # pygame.draw.rect(sc, (68, 0, 235), (40,40, 150, 170), 10 )
    # pygame.draw.circle(sc, (255,0,255),(0,0), 40)
    pygame.draw.rect(sc, (100,128,0), square)
    clock.tick(FPS)
    pygame.display.update()


