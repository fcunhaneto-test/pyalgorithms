import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# try to reduce cpu use
pygame.mixer.quit()

# Define windows size
WINDOW_X = 1800
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

# tree height
tree_height = 5
# num of leaf is tree is complete
leaf_num = 2**tree_height

# x axi center
x_center = int(leaf_num / 2)

# number o x axi max division
division = 2*x_center + 1
# number of pixel of x axi division
division_space = int(WINDOW_X / division)

# center of divison space
division_space_center = int(division_space / 2)

# last number in first loop
loop1 = tree_height - 1

# factor to calculate last number inb second loop
loop2_fact = 2

x = 0
y = 0

# pixel height between parent and child node
y_space = 100

# root x value
root_center = (x_center * division_space) + division_space_center

y += y_space
node1_center = int(x_center/2) * division_space + division_space_center
node2_center = (3 * int(x_center/2)) * division_space + division_space_center


nodes = []
for n in range(1, loop1):
    y += y_space

    # total number of division
    space_div = 2**n
    # pixel space between divisions
    space = int(x_center / space_div)
    # factor used to sum pixel spaces between division
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
    leaf_nodes.append((x, y))

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        screen.fill(WHITE)

        pygame.draw.circle(screen, RED, (root_center, RADIUS), RADIUS, 2)

        pygame.draw.circle(screen, RED, (node1_center, 100), RADIUS, 2)
        pygame.draw.circle(screen, RED, (node2_center, 100), RADIUS, 2)

        for xy in nodes:
            pygame.draw.circle(screen, RED, xy, RADIUS, 2)

        for xy in leaf_nodes:
            pygame.draw.circle(screen, RED, xy, RADIUS, 2)

        # Limit to 60 frames per second
        clock.tick(30)

        pygame.display.update()
