import pygame, sys, random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
    # create x and y position

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (126,166,114), fruit_rect)



pygame.init()
cell_size = 40
cell_number = 20

screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
# used to set fps
clock = pygame.time.Clock()

fruit = FRUIT()

test_surface = pygame.Surface((100,200))
test_surface.fill((0,0,255))
test_rect = test_surface.get_rect(center = (200,250))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175,250,70))
    fruit.draw_fruit()
    pygame.display.update()
    
    # pygame.draw.rect(screen, pygame.Color('red'), test_rect)
    # test_rect.right += 1
    screen.blit(test_surface,test_rect)
    # set fps to 60 fps
    clock.tick(60)