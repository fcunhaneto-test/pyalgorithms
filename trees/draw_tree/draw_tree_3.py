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

tree_height = 3
leaf_num = 2**tree_height
x_center = int(leaf_num / 2)
division = 2*x_center + 1
division_space = int(WINDOW_X / division)
division_space_center = int(division_space / 2)
loop1 = tree_height - 1
loop2_fact = 2

nodes = []
line = []
lines = []

root_center = (x_center * division_space) + division_space_center
nodes.append((root_center, RADIUS))

y_space = 100
y = y_space

if tree_height > 1:
    n1_center = int(x_center/2) * division_space + division_space_center
    n2_center = (3 * int(x_center/2)) * division_space + division_space_center
    nodes.append((n1_center, y))
    nodes.append((n2_center, y))
    lines.append([(root_center, RADIUS), (n1_center, y_space)])
    lines.append([(root_center, RADIUS), (n2_center, y_space)])


if tree_height > 2:
    for expo in range(1, loop1):
        y += y_space
        space_div = 2**expo
        space = space = int(x_center / space_div)
        sum_space = int(space / 2)
        loop2 = loop2_fact**(1+expo)
        for m in range(0, loop2):
            x = sum_space * division_space + division_space_center
            nodes.append((x, y))
            sum_space += space

    leaf_nodes = []
    y += y_space
    for i in range(1, leaf_num+1):
        x = i * division_space
        nodes.append((x, y))

ini_ini = 1
ini_end = 3
expo = 2
print(nodes)
while ini_end < leaf_num:
    points_ini = nodes[ini_ini:ini_end]

    end_ini = ini_end + 1
    end_end = int(2**(expo+1)) - 1
    points_end = nodes[end_ini:end_end]

    ini = end_ini - 1
    for p in points_ini:
        print('point ini:', p)
        print('ini:', ini)

        for x in range(0, 2):
            print('ini+x:', ini+x)
            lines.append([p, nodes[ini+x]])

        ini += 2

    ini_ini = end_ini - 1
    ini_end = end_end

    end_ini = end_ini + 1
    expo += 1
    end_end = 2**expo - 1

print(lines)



while True:
    for event in pygame.event.get():
        # event = pygame.event.wait()
        if event.type == QUIT:
            pygame.quit()
            exit()

        screen.fill(WHITE)

        for point in nodes:
            x, y = point
            pygame.draw.circle(screen, RED, (x, y), RADIUS, 2)

        for line in lines:
            x, y = line[0]
            r, s = line[1]

            pygame.draw.line(screen, BLACK, [x, y], [r, s], 1)

        # Limit to 60 frames per second
        clock.tick(30)

        pygame.display.update()
