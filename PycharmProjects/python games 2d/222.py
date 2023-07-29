import pygame
pygame.init()
FPS = (60)
SCREEN = (1000, 1000)
SC = pygame.display.set_mode(SCREEN, pygame.RESIZABLE)
pygame.display.set_caption('vroom vroom')
Clock = pygame.time.Clock()
Car_surf_main = pygame.image.load('pixil-frame-0 (1).png').convert_alpha()
Car_surf_2 = pygame.image.load('pixil-frame-0.png').convert_alpha()
back = pygame.image.load('road_0.png').convert_alpha()
ca_rect = Car_surf_main
car_rect = Car_surf_main.get_rect(center=(250, 250))

ca_rect_2 = Car_surf_2
car_rect_2 = Car_surf_2.get_rect(center=(250, 250))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()



    if event.type == pygame.KEYDOWN:
        if event.type == pygame.K_UP:
            ca_rect_2 = Car_surf_2
        if event.type == pygame.K_DOWN:
            ca_rect_2 = pygame.transform.rotate(Car_surf_2, 180)
        if event.type == pygame.K_RIGHT:
            ca_rect_2 = pygame.transform.rotate(Car_surf_2, -90)
        if event.type == pygame.K_LEFT:
            ca_rect_2 = pygame.transform.rotate(Car_surf_2, 90)

    if event.type == pygame.KEYDOWN:
        if event.type == pygame.K_w:
            ca_rect = Car_surf_main
        if event.type == pygame.K_s:
            ca_rect = pygame.transform.rotate(Car_surf_main, 180)
        if event.type == pygame.K_d:
            ca_rect = pygame.transform.rotate(Car_surf_main, -90)
        if event.type == pygame.K_a:
            ca_rect = pygame.transform.rotate(Car_surf_main, 90)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ca_rect_2.y > 0:
        ca_rect_2.y -= 5
    if keys[pygame.K_DOWN] and ca_rect_2.bottom < SCREEN[0]:
        ca_rect_2.y += 3
    if keys[pygame.K_RIGHT] and ca_rect_2.x > 0:
        ca_rect_2.x += 5
    if keys[pygame.K_LEFT] and ca_rect_2.right > SCREEN[1]:
        ca_rect_2.x -= 5
    if keys[pygame.K_w] and ca_rect.y > 0:
        ca_rect.y -= 1
    if keys[pygame.K_d] and ca_rect.right < SCREEN[0]:
        ca_rect.x += 1
    if keys[pygame.K_a] and ca_rect.x > 0:
        ca_rect.x -= 1
    if keys[pygame.K_s] and ca_rect.bottom < SCREEN[1]:
        ca_rect.y += 1


    SC.fill((0, 245, 0))
    SC.blit(back, (0, 0))
    SC.blit(ca_rect_2, car_rect_2)
    SC.blit(ca_rect , car_rect)
    Clock.tick(FPS)

