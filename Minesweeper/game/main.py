import pygame
import random

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
)

SCREEN_WIDTH = 770
SCREEN_HEIGHT = 881

pygame.init()

font = pygame.font.SysFont("Arial", 20)

LEFT = 1
RIGHT = 3

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Minesweeper')

class Restart_button(pygame.sprite.Sprite):
    def __init__(self):
        super(Restart_button, self).__init__()
        self.surf = pygame.image.load("restart.jpg").convert()
        self.surf_click = pygame.image.load("restart_click.jpg").convert()
        self.surf_defeat = pygame.image.load("restart_defeat.jpg").convert()
        self.surf_defeat_click = pygame.image.load("restart_defeat_click.jpg").convert()
        self.surf_victory = pygame.image.load("restart_victory.jpg").convert()
        self.surf_victory_click = pygame.image.load("restart_victory_click.jpg").convert()
        self.button_rect = pygame.Rect(349, 38, 71, 72)
        self.held = 0

    def show(self):
        if defeat == 0 and victory == 0 and self.held == 0:
            screen.blit(self.surf, (349, 38))
        elif defeat == 1 and self.held == 0:
            screen.blit(self.surf_defeat, (349, 38))
        elif victory == 1 and self.held == 0:
            screen.blit(self.surf_victory, (349, 38))
        elif defeat == 0 and victory == 0 and self.held == 1:
            screen.blit(self.surf_click, (349, 38))
        elif defeat == 1 and self.held == 1:
            screen.blit(self.surf_defeat_click, (349, 38))
        elif victory == 1 and self.held == 1:
            screen.blit(self.surf_victory_click, (349, 38))

    def hold(self, event):
        if self.button_rect.collidepoint(event.pos):
            self.held = 1
        else:
            self.held = 0
    
    def click(self, event):
        self.held = 0
        if self.button_rect.collidepoint(event.pos):
            pass


class Field(pygame.sprite.Sprite):
    def __init__(self):
        super(Field, self).__init__()
        self.surf = pygame.image.load("field.jpg").convert()
        self.surf_click = pygame.image.load("field_click.jpg").convert()
        self.surf_mine = pygame.image.load("mine.JPG").convert()
        self.surf_mine_explode = pygame.image.load("mine_explode.jpg").convert()
        self.surf_flag = pygame.image.load("flag.jpg").convert()
        self.surf_flag_wrong = pygame.image.load("flag_wrong.jpg").convert()
        self.surf_grid = pygame.image.load("grid.jpg").convert()
        self.surf_held = pygame.image.load("field_click.jpg").convert()
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
        self.flagged = 0
        self.clicked = 0
        self.held = 0
        self.number_of_mines = 0
        self.index_num = index_number
        self.range = []
        self.held_in_range = 0
        self.flags_in_range = 0



    def get_range(self):
        if self.index_num == top_left:
            self.range = [field_list[field_list.index(self) + 1], field_list[field_list.index(self) + 16], field_list[field_list.index(self) + 17]]
        elif self.index_num in top_row:
            self.range = [field_list[field_list.index(self) - 1], field_list[field_list.index(self) + 1], field_list[field_list.index(self) + 15], field_list[field_list.index(self) + 16], field_list[field_list.index(self) + 17]]
        elif self.index_num == top_right:
            self.range = [field_list[field_list.index(self) - 1], field_list[field_list.index(self) + 15], field_list[field_list.index(self) + 16]]
        elif self.index_num == bottom_left:
            self.range = [field_list[field_list.index(self) - 16], field_list[field_list.index(self) - 15], field_list[field_list.index(self) + 1]]
        elif self.index_num in bottom_row:
            self.range = [field_list[field_list.index(self) - 1], field_list[field_list.index(self) + 1], field_list[field_list.index(self) - 17], field_list[field_list.index(self) - 16], field_list[field_list.index(self) - 15]]
        elif self.index_num == bottom_right:
            self.range = [field_list[field_list.index(self) - 1], field_list[field_list.index(self) - 17], field_list[field_list.index(self) - 16]]
        elif self.index_num in left_column:
            self.range = [field_list[field_list.index(self) - 16], field_list[field_list.index(self) - 15], field_list[field_list.index(self) + 1], field_list[field_list.index(self) + 16], field_list[field_list.index(self) + 17]]
        elif self.index_num in right_column:
            self.range = [field_list[field_list.index(self) - 17], field_list[field_list.index(self) - 16], field_list[field_list.index(self) - 1], field_list[field_list.index(self) + 15], field_list[field_list.index(self) + 16]]
        else:
            self.range = [field_list[field_list.index(self) - 17], field_list[field_list.index(self) - 16], field_list[field_list.index(self) - 15], field_list[field_list.index(self) - 1], field_list[field_list.index(self) + 1], field_list[field_list.index(self) + 15], field_list[field_list.index(self) + 16], field_list[field_list.index(self) + 17]]

    def scan(self):
        number = 0
        for item in self.range:
            if item.mine == 1:
                number += 1
        self.number_of_mines = number

    
    def show(self):
        if self.flagged == 1 and self.mine == 0 and defeat == 1:
            screen.blit(self.surf_flag_wrong, (self.position_x, self.position_y))
        elif self.flagged == 1:
            screen.blit(self.surf_flag, (self.position_x, self.position_y))
        elif self.held == 1 and self.clicked == 0:
            screen.blit(self.surf_held, (self.position_x, self.position_y))
        elif self.clicked == 1 and self.mine == 1:
            screen.blit(self.surf_mine_explode, (self.position_x, self.position_y))
        elif self.clicked == 0 and self.mine == 1 and defeat == 1:
            screen.blit(self.surf_mine, (self.position_x, self.position_y))
        elif self.clicked == 1 and self.mine == 0:
            if self.number_of_mines == 0:
                screen.blit(self.surf_grid, (self.position_x, self.position_y))
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

    def hold(self, event):
        self.held_in_range = 0
        for item in self.range:
                if item.clicked == 1 and item.button_rect.collidepoint(event.pos):
                    self.held_in_range = 1
                    
        if self.button_rect.collidepoint(event.pos) and self.flagged == 0 and self.clicked == 0:
            self.held = 1
        elif self.button_rect.collidepoint(event.pos) and self.flagged == 0 and self.clicked == 1:
            for item in self.range:
                item.held = 1
        elif self.held_in_range == 0:
            self.held = 0


    def click(self, event):
        global defeat
        self.held = 0
        self.flags_in_range = 0
        for item in self.range:
            if item.flagged == 1:
                self.flags_in_range += 1

        if self.button_rect.collidepoint(event.pos) and self.flagged == 0 and self.clicked == 0:
            self.clicked = 1
            if self.mine == 1:
                defeat = 1
        elif self.button_rect.collidepoint(event.pos) and self.flagged == 0 and self.clicked == 1 and self.flags_in_range == self.number_of_mines:
            for item in self.range:
                if item.flagged == 0:
                    item.clicked = 1
                    if item.mine == 1:
                        defeat = 1
        

    def right_click(self, event):
        if self.button_rect.collidepoint(event.pos) and self.flagged == 0 and self.clicked == 0:
            self.flagged = 1
        elif self.button_rect.collidepoint(event.pos) and self.flagged == 1 and self.clicked == 0:
            self.flagged = 0



    
    def autoreveal(self):
        if self.clicked == 1 and self.number_of_mines == 0 and self.mine == 0:
            for item in self.range:
                item.clicked = 1


field_list = []
# number of mines: 40
# a list containing the fields where there is a mine
mine_list = []
victory = 0
defeat = 0
counter_x = 33
counter_y = 149
index_number = 0

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
    index_number += 1
    if number % 16 == 0:
        counter_y += 44
        counter_x -= 660
    else:
        counter_x += 44

top_left = 0
top_row = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
top_right = 15
bottom_left = 240
bottom_row = [241,242,243,244,245,246,247,248,249,250,251,252,253,254]
bottom_right = 255
left_column = [16,32,48,64,80,96,112,128,144,160,176,192,208,224]
right_column = [31,47,63,79,95,111,127,143,159,175,191,207,223,239]


res = Restart_button()


for item in field_list:
    item.get_range()

for item in field_list:
    item.scan()

lmb = 0
rmb = 0


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
        elif event.type == MOUSEBUTTONDOWN and event.button == LEFT:
                lmb = 1
        elif event.type == MOUSEBUTTONUP and event.button == LEFT:
            for item in field_list:
                item.click(event)
            res.click(event)
            lmb = 0
        elif defeat == 0:
            if event.type == MOUSEBUTTONDOWN and event.button == RIGHT and rmb == 0:
                rmb = 1
                for item in field_list:
                    item.right_click(event)
            elif event.type == MOUSEBUTTONUP and event.button == RIGHT:
                rmb = 0

    # Draw the frame
    frame = pygame.image.load("frame3.jpg").convert()
    screen.blit(frame, (0,0))


    if lmb == 1:
        if defeat == 0:
            for item in field_list:
                item.hold(event)
        res.hold(event)
        



    for item in field_list:
        item.autoreveal()

    for item in field_list:
        item.show()
    
    res.show()

    pygame.display.flip()

pygame.quit()