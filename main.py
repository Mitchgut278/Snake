import pygame, sys


pygame.init()
screen = pygame.display.set_mode((400,500))
# used to set fps
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200))
test_surface.fill((0,0,255))

x_pos = 200
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    screen.fill((175,250,70))
    x_pos += 1
    screen.blit(test_surface,(x_pos, 250))
    # set fps to 60 fps
    clock.tick(60)