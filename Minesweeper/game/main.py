import pygame
import random

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 770
SCREEN_HEIGHT = 881

class Field(pygame.sprite.Sprite):
    def __init__(self):
        super(Field, self).__init__()
        self.surf = pygame.image.load("field.jpg").convert()
        self.surf_click = pygame.image.load("field_click.jpg").convert()
        self.surf_mine = pygame.image.load("mine.jpg").convert()
        self.position_x = counter_x
        self.position_y = counter_y
        self.mine = is_mine


pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Minesweeper')

counter_x = 33
counter_y = 149
field_list = []
# number of mines: 40
# a list containing the fields where there is a mine
mine_list = []
for number in range(40):
    add = random.randint(1,257)
    while add in mine_list:
        add = random.randint(1,257)
    mine_list.append(add)

for number in range(1,257):
    if number in mine_list:
        is_mine = 1
    else:
        is_mine = 0
    field_list.append(Field())
    if number % 16 == 0:
        counter_y += 44
        counter_x -= 660
    else:
        counter_x += 44


# Run until the user asks to quit
running = True
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    # Draw the frame
    frame = pygame.image.load("frame.jpg").convert()
    screen.blit(frame, (0,0))

    for item in field_list:
        if item.mine == 1:
            screen.blit(item.surf_mine, (item.position_x,item.position_y))
        else:
            screen.blit(item.surf, (item.position_x,item.position_y))

    pygame.display.flip()

pygame.quit()