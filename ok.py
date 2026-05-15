import pygame
pygame.init()

newscreen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("okay")

circlecolor = (255, 0, 0)
circleradius = 40

circle_x = 150
circle_y = 150
vel = 5  

clock = pygame.time.Clock()

loop = True
while loop:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    kyes = pygame.key.get_pressed()

    
    if kyes[pygame.K_a]: # Left
        circle_x -= vel

    if kyes[pygame.K_d]: # Right
        circle_x += vel

    if kyes[pygame.K_w]: # Up
        circle_y -= vel

    if kyes[pygame.K_s]: # Down
        circle_y += vel

    newscreen.fill((99, 5, 9))  

    pygame.draw.circle(newscreen, circlecolor, (circle_x, circle_y), circleradius)

    pygame.display.update()

pygame.quit()
