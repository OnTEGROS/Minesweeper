import pygame

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
        self.rect = self.surf.get_rect()


pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Minesweeper')

field = Field()

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

    screen.blit(field.surf, (33,149))

    pygame.display.flip()

pygame.quit()