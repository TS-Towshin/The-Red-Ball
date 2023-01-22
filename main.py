import pygame
import random

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("The Red Ball")
value = 10
font = pygame.font.Font(None, 20)
running = True
x = 30
y = 65
r_x = random.randint(60, screen.get_width()-40)
r_y = random.randint(65, screen.get_height()-40)
points = 0
speed = 0.05
while running:
    width = screen.get_width()-40
    height = screen.get_height()-40
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            size = event.size
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_d] and x < width:
        x += speed
    if keys[pygame.K_a] and x > 30:
        x -= speed
    if keys[pygame.K_w] and y > 35:
        y -= speed
    if keys[pygame.K_s] and y < height:
        y += speed
    if x >= r_x and y >= r_y and x <= r_x+25 and y <= r_y+25:
        points += 1
        if points <= 5:
            speed *= 1.25
        elif points > 5 and points <= 10:
            speed *= 1.2
        elif points > 10 and points <= 15:
            speed *= 1.15
        else:
            speed *= 1.1
        r_x = random.randint(60, screen.get_width() - 40)
        r_y = random.randint(65, screen.get_height() - 40)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 255), (r_x, r_y, 25, 25))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 20)
    coordinates = font.render(f"Coordinates: {int(x)}, {int(y)}", True, (255, 255, 255))
    point_render = font.render(f"Points: {points}", True, (255, 255, 255))
    speed_render = font.render(f"speed: {speed}", True, (255, 255, 255))
    screen.blit(coordinates, (0, 0))
    screen.blit(point_render, (0, 15))
    screen.blit(speed_render, (0, 30))
    pygame.display.update()
pygame.quit()
