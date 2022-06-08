import pygame
import os

WIDTH, HEIGHT = 950, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ROOM 8")

FPS = 144

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TRANSPARENT = (0, 0, 0, 0)

# ADVENTURE_FONT = pygame.font.SysFont('comicsans', 20)
# NEXT_BUTTON = pygame.transform.scale(pygame.image.load('next_button.png'), (200,150)).convert_alpha()
# TEXT_BOX = pygame.transform.scale(pygame.image.load('text_box.png'), (800, 140))

# # from clickable_classes import *

# ROOM_8_BACKGROUND = pygame.transform.scale(pygame.image.load('forest.png'), (WIDTH, HEIGHT))
ROOM_8_PLANK1 = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room8_temp", "plank18.png")), (200, 150)
)
ROOM_8_PLANK2 = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room8_temp", "plank28.png")), (200, 150)
)
# ROOM_8_PLANK3 = pygame.transform.scale(pygame.image.load("plank38.png"), (120, 100))
# ROOM_8_STICK1 = pygame.transform.scale(pygame.image.load("stick18.png"), (120, 100))
# ROOM_8_STICK2 = pygame.transform.scale(pygame.image.load("stick28.png"), (120, 100))
# ROOM_8_STICK3 = pygame.transform.scale(pygame.image.load("stick38.png"), (120, 100))
# ROOM_8_TREE = pygame.transform.scale(pygame.image.load("tree8.png"), (120, 100))
# ROOM_8_LOCK = pygame.transform.scale(pygame.image.load("lock8.png"), (120, 100))
# ROOM_8_KEY = pygame.transform.scale(pygame.image.load("key8.png"), (120, 100))
# ROOM_8_GRASS = pygame.transform.scale(pygame.image.load("grass8.png"), (120, 100))


def draw_window(plank1, plank2):
    WIN.fill(WHITE)
    WIN.blit(ROOM_8_PLANK1, (plank1.x, plank1.y))
    WIN.blit(ROOM_8_PLANK2, (plank2.x, plank2.y))
    pygame.display.update()


# main function
def main():
    plank1 = pygame.Rect(100, 300, 200, 150)
    plank2 = pygame.Rect(400, 300, 200, 150)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(plank1, plank2)

    mouse_click = pygame.mouse.get_pressed
    pos = pygame.mouse.get_pos()

    if mouse_click()[0]:
        pass
        print(pos)

    pygame.quit()


# to make sure it runs from this directory
if __name__ == "__main__":
    main()
