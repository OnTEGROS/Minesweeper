import pygame
import random

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
)

SCREEN_WIDTH = 770
SCREEN_HEIGHT = 881

pygame.init()

font = pygame.font.SysFont("Arial", 20)

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Minesweeper')

victory = 0
defeat = 0

class Field(pygame.sprite.Sprite):
    def __init__(self):
        super(Field, self).__init__()
        self.surf = pygame.image.load("field.jpg").convert()
        self.surf_click = pygame.image.load("field_click.jpg").convert()
        self.surf_mine = pygame.image.load("mine.JPG").convert()
        self.surf_mine_explode = pygame.image.load("mine_explode.jpg").convert()
        self.flag = pygame.image.load("flag.jpg").convert()
        self.flag_wrong = pygame.image.load("flag_wrong.jpg").convert()
        self.grid = pygame.image.load("grid.jpg").convert()
        self.one = pygame.image.load("one.jpg").convert()
        self.two = pygame.image.load("two.jpg").convert()
        self.three = pygame.image.load("three.jpg").convert()
        self.four = pygame.image.load("four.jpg").convert()
        self.five = pygame.image.load("five.jpg").convert()
        self.six = pygame.image.load("six.jpg").convert()
        self.seven = pygame.image.load("seven.jpg").convert()
        self.eight = pygame.image.load("eight.jpg").convert()
        self.position_x = counter_x
        self.position_y = counter_y
        self.button_rect = pygame.Rect(self.position_x, self.position_y, 44, 44)
        self.mine = is_mine
        self.clicked = 0
        self.number_of_mines = 0
        self.index_num = 0

    def index_number(self):
        self.index_num = str(field_list.index(self))

    def scan(self):
        number = 0
        try:
            if field_list[field_list.index(self) - 17].mine == 1:
                number += 1
        except IndexError:
            pass
        try:
            if field_list[field_list.index(self) - 16].mine == 1:
                number += 1
        except IndexError:
            pass
        try:
            if field_list[field_list.index(self) - 15].mine == 1:
                number += 1
        except IndexError:
            pass
        try:
            if field_list[field_list.index(self) - 1].mine == 1:
                number += 1
        except IndexError:
            pass
        try:
            if field_list[field_list.index(self) + 1].mine == 1:
                number += 1
        except IndexError:
            pass
        try:
            if field_list[field_list.index(self) + 15].mine == 1:
                number += 1
        except IndexError:
            pass
        try:
            if field_list[field_list.index(self) + 16].mine == 1:
                number += 1
        except IndexError:
            pass
        try:
            if field_list[field_list.index(self) + 17].mine == 1:
                number += 1
        except IndexError:
            pass

        self.number_of_mines = number

    
    def show(self):
        if self.clicked == 1 and self.mine == 1:
            screen.blit(self.surf_mine_explode, (self.position_x, self.position_y))
        elif self.clicked == 0 and self.mine == 1 and defeat == 1:
            screen.blit(self.surf_mine, (self.position_x, self.position_y))
        elif self.clicked == 1 and self.mine == 0:
            if self.number_of_mines == 0:
                screen.blit(self.grid, (self.position_x, self.position_y))
            elif self.number_of_mines == 1:
                screen.blit(self.one, (self.position_x, self.position_y))
            elif self.number_of_mines == 2:
                screen.blit(self.two, (self.position_x, self.position_y))
            elif self.number_of_mines == 3:
                screen.blit(self.three, (self.position_x, self.position_y))
            elif self.number_of_mines == 4:
                screen.blit(self.four, (self.position_x, self.position_y))
            elif self.number_of_mines == 5:
                screen.blit(self.five, (self.position_x, self.position_y))
            elif self.number_of_mines == 6:
                screen.blit(self.six, (self.position_x, self.position_y))
            elif self.number_of_mines == 7:
                screen.blit(self.seven, (self.position_x, self.position_y))
            elif self.number_of_mines == 8:
                screen.blit(self.eight, (self.position_x, self.position_y))
        else:
            screen.blit(self.surf, (self.position_x, self.position_y))
            #screen.blit(font.render(self.index_num, 1, pygame.Color("Red")), (self.position_x+11, self.position_y+11))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.button_rect.collidepoint(x, y):
                    self.clicked = 1
                    if self.mine == 1:
                        global defeat
                        defeat = 1





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

for item in field_list:
    item.index_number()


for item in field_list:
    item.scan()


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

    if defeat == 0:
        for item in field_list:
            item.click(event)

    for item in field_list:
        item.show()

    pygame.display.flip()

pygame.quit()