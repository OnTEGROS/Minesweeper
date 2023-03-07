import pygame
import random
from datetime import datetime
from pygame import mixer

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
mixer.init

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
            mixer.music.load("sound4.mp3")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            global defeat
            global victory
            global score_recorded
            global click_count
            global current_time
            global timer_seconds
            global timer_ones
            global timer_tens
            global timer_hundreds
            global defeat_sound_played
            global defeat_animation_frame
            global death_variant
            global victory_sound_played
            for item in field_list:
                item.flagged = 0
                item.clicked = 0
            defeat = 0
            victory = 0
            death_variant = random.randint(1,6)
            defeat_sound_played = 0
            defeat_animation_frame = 0
            score_recorded = 0
            click_count = 0
            current_time = 0
            timer_seconds = 0
            timer_ones = 0
            timer_tens = 0
            timer_hundreds = 0
            victory_sound_played = 0



            for item in field_list:
                item.mine = 0
            for number in range(40):
                random_field = random.choice(field_list)
                while random_field.mine == 1:
                    random_field = random.choice(field_list)
                random_field.mine = 1

            for item in field_list:
                item.get_range()
                item.scan()
            


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
        self.mine = 0
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
        global click_count
        self.held = 0
        self.flags_in_range = 0
        for item in self.range:
            if item.flagged == 1:
                self.flags_in_range += 1

        if self.button_rect.collidepoint(event.pos) and self.flagged == 0 and self.clicked == 0:
            self.clicked = 1
            if self.mine == 0:
                mixer.music.load("sound2.mp3")
                mixer.music.set_volume(1)
                mixer.music.play()
            if self.mine == 1 and click_count == 0:
                mixer.music.load("sound2.mp3")
                mixer.music.set_volume(1)
                mixer.music.play()
                mine_placed = 0
                while mine_placed == 0:
                    place = random.choice(field_list)
                    if place.mine == 0 and place.index_num != self.index_num:
                        place.mine = 1
                        mine_placed = 1
                self.mine = 0
                for item in field_list:
                    item.scan()
            elif self.mine == 1:
                defeat = 1
            click_count += 1
        elif self.button_rect.collidepoint(event.pos) and self.flagged == 0 and self.clicked == 1:
            sound_play_clearance = 1
            if self.flags_in_range == self.number_of_mines:
                sound_play_clearance = 0
                for item in self.range:
                    if item.flagged == 0 and item.clicked == 0:
                        item.clicked = 1
                        sound_play_clearance = 2
                        if item.mine == 1:
                            defeat = 1
                            sound_play_clearance = 0
            if sound_play_clearance == 2:
                mixer.music.load("sound2.mp3")
                mixer.music.set_volume(1)
                mixer.music.play()
            elif sound_play_clearance == 1:
                mixer.music.load("sound2a.mp3")
                mixer.music.set_volume(1)
                mixer.music.play()
            click_count += 1
        

    def right_click(self, event):
        global click_count
        if self.button_rect.collidepoint(event.pos) and self.flagged == 0 and self.clicked == 0:
            mixer.music.load("sound6.mp3")
            mixer.music.set_volume(0.6)
            mixer.music.play()
            self.flagged = 1
            click_count += 1
        elif self.button_rect.collidepoint(event.pos) and self.flagged == 1 and self.clicked == 0:
            mixer.music.load("sound7.mp3")
            mixer.music.set_volume(0.6)
            mixer.music.play()
            self.flagged = 0
            click_count += 1



    
    def autoreveal(self):
        if self.clicked == 1 and self.number_of_mines == 0 and self.mine == 0:
            for item in self.range:
                if item.flagged == 0:
                    item.clicked = 1

# 40 mines
field_list = []
victory = 0
defeat = 0
click_count = 0
score_recorded = 0
current_time = 0
frame_play_time = 0
requirement = 1000
timer_seconds = 0
timer_ones = 0
timer_tens = 0
timer_hundreds = 0
defeat_sound_played = 0
defeat_animation_frame = 0
victory_sound_played = 0
death_variant = random.randint(1,6)
counter_x = 33
counter_y = 149
index_number = 0

for number in range(1,257):
    field_list.append(Field())
    index_number += 1
    if number % 16 == 0:
        counter_y += 44
        counter_x -= 660
    else:
        counter_x += 44

for number in range(40):
    random_field = random.choice(field_list)
    while random_field.mine == 1:
        random_field = random.choice(field_list)
    random_field.mine = 1



top_left = 0
top_row = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
top_right = 15
bottom_left = 240
bottom_row = [241,242,243,244,245,246,247,248,249,250,251,252,253,254]
bottom_right = 255
left_column = [16,32,48,64,80,96,112,128,144,160,176,192,208,224]
right_column = [31,47,63,79,95,111,127,143,159,175,191,207,223,239]
display_numbers = ["timer_zero.JPG", "timer_one.jpg", "timer_two.jpg", "timer_three.jpg", "timer_four.jpg", "timer_five.jpg", "timer_six.jpg", "timer_seven.jpg", "timer_eight.jpg", "timer_nine.jpg", ]


res = Restart_button()


for item in field_list:
    item.get_range()

for item in field_list:
    item.scan()

lmb = 0
rmb = 0


def defeat_explode():
    mixer.music.load("explosion.mp3")
    mixer.music.set_volume(0.9)
    mixer.music.play()

animation_list = []
for number in range(7,42):
    ani_str = ("explosion_animation\explosion_"+str(number)+".PNG")
    ani_add = pygame.image.load(ani_str).convert()
    ani_add.set_colorkey(pygame.Color(255, 255, 255))
    animation_list.append(ani_add)

def defeat_vine():
    mixer.music.load("vine_boom.mp3")
    mixer.music.set_volume(0.55)
    mixer.music.play()

animation_vine = pygame.image.load("skull.PNG").convert()
animation_vine.set_colorkey(pygame.Color(255, 255, 255))

def defeat_spunchbop():
    mixer.music.load("spunchbop.mp3")
    mixer.music.set_volume(1)
    mixer.music.play()

animation_spunchbop = pygame.image.load("stare.jpg").convert()

def defeat_shock():
    mixer.music.load("cave.mp3")
    mixer.music.set_volume(1)
    mixer.music.play()

animation_shock = pygame.image.load("shock.PNG").convert()
animation_shock.set_colorkey((0, 255, 1))

def defeat_trollge_sad():
    mixer.music.load("trollge_sad2.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()

animation_trollge_sad = pygame.image.load("trollge_sad.jpg").convert()

def defeat_trollge_sus():
    mixer.music.load("trollge_sus.mp3")
    mixer.music.set_volume(0.4)
    mixer.music.play()

animation_trollge_sus = pygame.image.load("trollge_sus.jpg").convert()


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
            if defeat == 0 and victory == 0:
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

    # the timer
    current_time = pygame.time.get_ticks()
    if current_time >= requirement:  
        requirement += 1000
        if click_count > 0 and victory == 0 and defeat == 0:
            timer_seconds += 1
            if timer_seconds <= 999:
                timer_ones += 1
                if timer_ones == 10:
                    timer_tens += 1
                    timer_ones = 0
                if timer_tens == 10:
                    timer_hundreds += 1
                    timer_tens = 0
        mines_remaining_test = 0
        for item in field_list:
            if item.mine == 1:
                mines_remaining_test += 1

    timer_first = pygame.image.load(display_numbers[timer_hundreds]).convert()
    timer_second = pygame.image.load(display_numbers[timer_tens]).convert()
    timer_third = pygame.image.load(display_numbers[timer_ones]).convert()

    # mine counter
    remaning_mines = 0
    for item in field_list:
        if item.mine == 1:
            remaning_mines += 1
    mines_tens = 4
    mines_ones = 0
    if defeat == 0:
        for item in field_list:
            if item.flagged == 1:
                remaning_mines -= 1
                if remaning_mines >= 0:
                    mines_ones -= 1
                    if mines_ones == -1:
                        mines_tens -= 1
                        mines_ones = 9
    else:
        for item in field_list:
            if item.flagged == 1 and item.mine == 1:
                remaning_mines -= 1
                if remaning_mines >= 0:
                    mines_ones -= 1
                    if mines_ones == -1:
                        mines_tens -= 1
                        mines_ones = 9

    mines_first = pygame.image.load("timer_zero.JPG").convert()
    mines_second = pygame.image.load(display_numbers[mines_tens]).convert()
    mines_third = pygame.image.load(display_numbers[mines_ones]).convert()

    

    # checking for victory
    unclicked_list = []
    for item in field_list:
        if item.mine == 0 and item.clicked == 0:
            unclicked_list.append(item)
    if unclicked_list == []:
        victory = 1
        if victory_sound_played == 0:
            mixer.music.load("sound9.mp3")
            mixer.music.set_volume(0.25)
            mixer.music.play()
            victory_sound_played = 1
        for item in field_list:
            if item.mine == 1:
                item.flagged = 1
        if score_recorded == 0:
            score_recorded = 1
            now = datetime.now()
            dt_string = now.strftime("%d. %m. %Y %H:%M:%S")
            clicks_record = str(click_count)
            time_record = str(timer_seconds)
            with open("scores.txt", "a") as scores:
                scores.write(dt_string)
                scores.write(", finished in ")
                scores.write(clicks_record)
                scores.write(" clicks")
                scores.write(" and ")
                scores.write(time_record)
                scores.write(" seconds")
                scores.write("\n")


    # Draw the frame
    frame = pygame.image.load("frame.jpg").convert()
    screen.blit(frame, (0,0))


    if lmb == 1:
        if defeat == 0 and victory == 0:
            for item in field_list:
                item.hold(event)
        res.hold(event)
        



    for item in field_list:
        item.autoreveal()

    for item in field_list:
        item.show()
    
    res.show()

    screen.blit(timer_first, (44,41))
    screen.blit(timer_second, (80,41))
    screen.blit(timer_third, (116,41))
    screen.blit(mines_first, (619,41))
    screen.blit(mines_second, (655,41))
    screen.blit(mines_third, (691,41))


    if defeat == 1 and defeat_sound_played == 0 and death_variant == 1:
        defeat_explode()
        defeat_sound_played = 1

    if defeat == 1 and defeat_animation_frame <= 34 and death_variant == 1:
        position_x_explosion = 0
        position_y_explosion = 0
        while position_x_explosion == 0 and position_y_explosion == 0:
            for item in field_list:
                if item.mine == 1 and item.clicked == 1:
                    position_x_explosion = item.position_x
                    position_y_explosion = item.position_y
        screen.blit(animation_list[defeat_animation_frame], (position_x_explosion-300, position_y_explosion-160))
        if current_time - frame_play_time > 17:
            frame_play_time = pygame.time.get_ticks()
            defeat_animation_frame += 1


    if defeat == 1 and defeat_sound_played == 0 and death_variant == 2:
        defeat_vine()
        defeat_sound_played = 1

    if defeat == 1 and defeat_animation_frame <= 34 and death_variant == 2:
        position_x_explosion = 0
        position_y_explosion = 0
        while position_x_explosion == 0 and position_y_explosion == 0:
            for item in field_list:
                if item.mine == 1 and item.clicked == 1:
                    position_x_explosion = item.position_x
                    position_y_explosion = item.position_y
        animation_vine.set_alpha(230-8*defeat_animation_frame)
        vine_resized = pygame.transform.scale(animation_vine, (150+10*defeat_animation_frame,150+10*defeat_animation_frame))
        screen.blit(vine_resized, (position_x_explosion+22-75-5*defeat_animation_frame, position_y_explosion+22-75-5*defeat_animation_frame))
        defeat_animation_frame += 1


    if defeat == 1 and defeat_sound_played == 0 and death_variant == 3:
        defeat_spunchbop()
        defeat_sound_played = 1

    if defeat == 1 and defeat_animation_frame <= 88 and death_variant == 3:
        position_x_explosion = 0
        position_y_explosion = 0
        while position_x_explosion == 0 and position_y_explosion == 0:
            for item in field_list:
                if item.mine == 1 and item.clicked == 1:
                    position_x_explosion = item.position_x
                    position_y_explosion = item.position_y
        animation_spunchbop.set_alpha(220-1.5*defeat_animation_frame)
        spunchbop_resized = pygame.transform.scale(animation_spunchbop, (44+defeat_animation_frame,44+defeat_animation_frame))
        screen.blit(spunchbop_resized, (position_x_explosion-0.5*defeat_animation_frame, position_y_explosion-0.5*defeat_animation_frame))
        defeat_animation_frame += 1
    elif defeat == 1 and defeat_animation_frame > 88 and defeat_animation_frame < 108 and death_variant == 3:
        animation_spunchbop.set_alpha(88-9*(defeat_animation_frame - 88))
        spunchbop_resized = pygame.transform.scale(animation_spunchbop, (132, 132))
        screen.blit(spunchbop_resized, (position_x_explosion-44, position_y_explosion-44))
        defeat_animation_frame += 1


    if defeat == 1 and defeat_sound_played == 0 and death_variant == 4:
        defeat_shock()
        defeat_sound_played = 1

    if defeat == 1 and defeat_animation_frame <= 135 and death_variant == 4:
        position_x_explosion = 0
        position_y_explosion = 0
        while position_x_explosion == 0 and position_y_explosion == 0:
            for item in field_list:
                if item.mine == 1 and item.clicked == 1:
                    position_x_explosion = item.position_x
                    position_y_explosion = item.position_y
        animation_shock.set_alpha(220-2*defeat_animation_frame)
        shock_resized = pygame.transform.scale(animation_shock, (150+4*defeat_animation_frame,150+4*defeat_animation_frame))
        screen.blit(shock_resized, (position_x_explosion+22-75-2*defeat_animation_frame, position_y_explosion+22-75-2*defeat_animation_frame))
        defeat_animation_frame += 1


    if defeat == 1 and defeat_sound_played == 0 and death_variant == 5:
        defeat_trollge_sad()
        defeat_sound_played = 1

    if defeat == 1 and defeat_animation_frame <= 90 and death_variant == 5:
        position_x_explosion = 0
        position_y_explosion = 0
        while position_x_explosion == 0 and position_y_explosion == 0:
            for item in field_list:
                if item.mine == 1 and item.clicked == 1:
                    position_x_explosion = item.position_x
                    position_y_explosion = item.position_y
        animation_trollge_sad.set_alpha(200-2.5*defeat_animation_frame)
        trollge_sad_resized = pygame.transform.scale(animation_trollge_sad, (60+2*defeat_animation_frame,60+2*defeat_animation_frame))
        screen.blit(trollge_sad_resized, (position_x_explosion+22-30-defeat_animation_frame, position_y_explosion+22-30-defeat_animation_frame))
        defeat_animation_frame += 1

    if defeat == 1 and defeat_sound_played == 0 and death_variant == 6:
        defeat_trollge_sus()
        defeat_sound_played = 1

    if defeat == 1 and defeat_animation_frame <= 200 and death_variant == 6:
        position_x_explosion = 0
        position_y_explosion = 0
        while position_x_explosion == 0 and position_y_explosion == 0:
            for item in field_list:
                if item.mine == 1 and item.clicked == 1:
                    position_x_explosion = item.position_x
                    position_y_explosion = item.position_y
        animation_trollge_sus.set_alpha(200-2*defeat_animation_frame)
        trollge_sus_resized = pygame.transform.scale(animation_trollge_sus, (60+2*defeat_animation_frame,60+2*defeat_animation_frame))
        screen.blit(trollge_sus_resized, (position_x_explosion+22-30-1*defeat_animation_frame, position_y_explosion+22-30-1*defeat_animation_frame))
        defeat_animation_frame += 1
    

    

    pygame.display.flip()

mixer.quit()
pygame.quit()