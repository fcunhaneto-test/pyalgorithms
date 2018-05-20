import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# try to reduce cpu use
pygame.mixer.quit()

# Define windows size
WINDOW_X = 1024
WINDOW_Y = 768

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

RADIUS = 20

screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y), 0, 32)
pygame.display.set_caption("Draw Tree")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

tree_height = 1
leaf_num = 2**tree_height
x_center = int(leaf_num / 2)
division = 2*x_center + 1
division_space = int(WINDOW_X / division)
division_space_center = int(division_space / 2)
loop1 = tree_height - 1
loop2_fact = 2

root_center = (x_center * division_space) + division_space_center
nodes = [(root_center, RADIUS)]

y_space = 100
y = y_space

if tree_height > 1:
    n1_center = int(x_center/2) * division_space + division_space_center
    n2_center = (3 * int(x_center/2)) * division_space + division_space_center
    nodes.append((n1_center, y))
    nodes.append((n2_center, y))


if tree_height > 2:
    for n in range(1, loop1):
        print(n)
        y += y_space
        space_div = 2**n
        space = space = int(x_center / space_div)
        sum_space = int(space / 2)
        loop2 = loop2_fact**(1+n)
        for m in range(0, loop2):
            x = sum_space * division_space + division_space_center
            nodes.append((x, y))
            sum_space += space

    leaf_nodes = []
    y += y_space
    for i in range(1, leaf_num+1):
        x = i * division_space
        nodes.append((x, y))

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        screen.fill(WHITE)

        for point in nodes:
            x, y = point
            pygame.draw.circle(screen, RED, (x, y), RADIUS, 2)

        # Limit to 60 frames per second
        clock.tick(30)

        pygame.display.update()
