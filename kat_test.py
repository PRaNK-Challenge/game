import pygame
import os

# settings
pygame.init()
pygame.font.init()
pygame.mixer.init(frequency=8000)

WIDTH, HEIGHT = 950, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ROOM 8")

FPS = 144

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TRANSPARENT = (0, 0, 0, 0)

ADVENTURE_FONT = pygame.font.SysFont("comicsans", 20)
NEXT_BUTTON = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "other", "next_button.png")), (200, 150)
).convert_alpha()
TEXT_BOX = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "other", "text_box.png")), (800, 140)
)

# from clickable_classes import *

ROOM_8_BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room8_temp", "forest.png")), (WIDTH, HEIGHT)
)
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


def draw_window(plank1):
    WIN.fill(WHITE)
    WIN.blit(ROOM_8_PLANK1, (plank1.x, plank1.y))
    # WIN.blit(ROOM_8_PLANK2, (plank2.x, plank2.y))
    pygame.display.update()


# # main function
# def main():
#     plank1 = pygame.Rect(100, 300, 200, 150)
#     plank2 = pygame.Rect(400, 300, 200, 150)

#     plank1_dragging = False

#     clock = pygame.time.Clock()
#     run = True
#     while run:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False

#         draw_window(plank1, plank2)

#     # mouse_click = pygame.mouse.get_pressed
#     # pos = pygame.mouse.get_pos()

#     # if mouse_click()[0]:
#     #     pass
#     #     print(pos)

#     pygame.quit()


import pygame

# --- constants --- (UPPER_CASE names)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FPS = 144

# --- main ---

# - init -

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# - objects -

plank1 = pygame.Rect(100, 300, 200, 150)
draw_window(plank1)
plank1_dragging = False

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if plank1.collidepoint(event.pos):
                    plank1_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = plank1.x - mouse_x
                    offset_y = plank1.y - mouse_y
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                plank1_dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if plank1_dragging:
                mouse_x, mouse_y = event.pos
                plank1.x = mouse_x + offset_x
                plank1.y = mouse_y + offset_y

    # draw_window(plank1)


#     # - draws (without updates) -

#     screen.fill(WHITE)
#     pygame.draw.rect(screen, BLUE, plank1)
#     pygame.display.flip()

# - end -

pygame.quit()
