import pygame
pygame.init()
FPS = 60
SCREEN = (1080, 1000)
sc = pygame.display.set_mode(SCREEN, pygame.RESIZABLE)
pygame.display.set_caption('RACE')
clock = pygame.time.Clock()

car_surf_main = pygame.image.load('pixil-frame-0.png').convert_alpha()

car_surf_2 = pygame.image.load('pixil-frame-0 (1).png').convert_alpha()

back = pygame.image.load('road_0.png').convert_alpha()

car_surf = car_surf_main
car_rect = car_surf_main.get_rect(center=(250,250))

car_surf2 = car_surf_2
car_rect2 = car_surf_2.get_rect(center=(-250,250))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                car_surf = pygame.transform.rotate(car_surf_main, -90)
            if event.key == pygame.K_LEFT:
                car_surf = pygame.transform.rotate(car_surf_main, 90)
            if event.key == pygame.K_UP:
                car_surf = car_surf_main
            if event.key == pygame.K_DOWN:
                car_surf = pygame.transform.rotate(car_surf_main, 180)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                car_surf2 = pygame.transform.rotate(car_surf_2, -90)
            if event.key == pygame.K_a:
                car_surf2 = pygame.transform.rotate(car_surf_2, 90)
            if event.key == pygame.K_w:
                car_surf2 = car_surf_2
            if event.key == pygame.K_s:
                car_surf2 = pygame.transform.rotate(car_surf_2, 180)
            





    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and car_rect.y > 0:
        car_rect.y -= 1
    if keys[pygame.K_RIGHT] and car_rect.right < SCREEN[0]:
        car_rect.x += 1
    if keys[pygame.K_LEFT] and car_rect.x > 0:
        car_rect.x -= 1
    if keys[pygame.K_DOWN] and car_rect.bottom < SCREEN[1]:
        car_rect.y += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and car_rect2.y > 0:
        car_rect2.y -= 1
    if keys[pygame.K_d] and car_rect2.right < SCREEN[0]:
        car_rect2.x += 1
    if keys[pygame.K_a] and car_rect2.x > 0:
        car_rect2.x -= 1
    if keys[pygame.K_s] and car_rect2.bottom < SCREEN[1]:
        car_rect2.y += 1



    sc.fill((0, 255, 0))
    sc.blit(back, (0, 0))
    sc.blit(car_surf, car_rect)
    sc.blit(car_surf2, car_rect2)
    pygame.display.update()
    clock.tick(FPS)

