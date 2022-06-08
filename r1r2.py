import pygame
import os

# settings
pygame.init()
pygame.font.init()
pygame.mixer.init(frequency=8000)

WIDTH, HEIGHT = 950, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Private Eye")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TRANSPARENT = (0, 0, 0, 0)

ADVENTURE_FONT = pygame.font.SysFont("comicsans", 20)

from clickable_classes import *

# Room 1 files
STUDY_ROOM = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room1", "office1.png")), (WIDTH, HEIGHT)
)
NEXT_BUTTON = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "other", "next_button.png")), (70, 70)
).convert_alpha()
PHONE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room1", "phone1.png")), (130, 135)
)
TISSUES = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room1", "tissues1.png")), (75, 90)
)
KEY = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room1", "key1.png")), (40, 15)
)
MOTHER = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room1", "mother1.png")), (250, 320)
)
FOLDER = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room1", "folder1.png")), (120, 100)
)
DRAWER_SHAPE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room6", "glass6.png")), (220, 100)
)

# # Room 1 sounds
WOMAN = pygame.mixer.Sound(os.path.join("sounds&music", "room1", "room_1_woman.mp3"))
LITTLE = pygame.mixer.Sound(
    os.path.join("sounds&music", "room1", "little_girl_voice.mp3")
)
MAN = pygame.mixer.Sound(os.path.join("sounds&music", "room1", "room_1_man.mp3"))
PHONE_SOUND = pygame.mixer.Sound(
    os.path.join("sounds&music", "room1", "phone_ringing.mp3")
)
PHONE_PICKUP = pygame.mixer.Sound(
    os.path.join("sounds&music", "room1", "phone_pick_up.mp3")
)
DOOR_KNOCK = pygame.mixer.Sound(os.path.join("sounds&music", "room1", "door_knock.mp3"))

# Room 2 images
ROOM_2_BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room2", "bedroom.png")), (WIDTH, HEIGHT)
).convert_alpha()
ROOM_2_NOTE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room2", "paper2.png")), (18, 15)
).convert_alpha()
ROOM_2_NOTE_ZOOM = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room2", "paperburned2.png")), (600, 550)
).convert_alpha()
ROOM_2_TWINKLE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room2", "spark2.png")), (15, 25)
).convert_alpha()
ROOM_2_KEY = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room2", "key2.png")), (20, 20)
).convert_alpha()
ROOM_2_DIARY = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room2", "diary2.png")), (100, 70)
).convert_alpha()
ROOM_2_DIARY_ZOOM = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room2", "diaryopen2.png")), (700, 550)
).convert_alpha()
ROOM_2_CANDLE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room2", "candle2.png")), (30, 80)
).convert_alpha()

# Room 3 images

# Room 3 sounds


# to help fade between scenes, used by rooms and items, change to what's visible at beginning
def redraw_window(room, items):
    WIN.blit(room.image, (0, 0))
    for item in items:
        if item.self_vis == True:
            WIN.blit(item.image, (item.rect.topleft))


# fade between scenes
def fade_in_and_out(width, height, state, room, current_room, next_room):

    fade = pygame.Surface((width, height))
    fade.fill((0, 0, 0))

    for alpha in range(255):
        fade.set_alpha(alpha)
        redraw_window(current_room, current_room.items)
        WIN.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(1)

    # change to next room
    room.state = state

    for alpha in range(255):
        fade.set_alpha(255 - alpha)
        redraw_window(next_room, next_room.items)
        WIN.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(1)


# initialise the rooms
class MenuScreen:
    def __init__(self):
        # self.start_button = Clickable(self, 100, 100, START_BUTTON)
        self.start = False
        # self.items = [self.start_button]
        # self.image = KITCHEN

    def start_screen(self):
        # menu_screen = pygame.Surface((WIDTH, HEIGHT))
        # menu_screen.fill((0,0,0))
        WIN.blit(self.image, (0, 0))
        self.start_button.draw()

        pos = pygame.mouse.get_pos()

        if self.start_button.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.start = True

        pygame.display.update()


class Room1:
    def __init__(self):
        self.image = STUDY_ROOM
        self.cooldown = 5000
        self.last = pygame.time.get_ticks()
        self.next_room = False
        self.drawer = pygame.draw.rect(WIN, TRANSPARENT, (300, 530, 50, 50))
        self.collect_folder = CollectableClue(self, 246, 409, FOLDER, 20, HEIGHT - 75)
        self.text = Text(
            "She's too upset to speak. Maybe give her the tissues and she'll explain?"
        )
        self.mother = FadeIn(self, 105, 120, MOTHER)
        self.phone = Clickable(self, 620, 290, PHONE)
        self.phone_call = AudioClue(
            self, self.phone, PHONE_PICKUP, 1500, MAN, DOOR_KNOCK, self.mother.fade_in
        )
        self.click_tissues = Clickable(self, 361, 317, TISSUES)
        self.mother_speech = AudioClue(self, self.click_tissues, WOMAN, 100)
        self.drag_key = DraggableClue(self, KEY, 380, 385, True, area=self.drawer)
        self.items = [
            self.drag_key,
            self.phone,
            self.mother,
            self.click_tissues,
            self.collect_folder,
        ]

    def play_room(self):

        WIN.blit(self.image, (0, 0))
        self.phone.draw()
        self.drag_key.draw()
        self.collect_folder.draw()
        self.collect_folder.collect()

        # so that we can't click the tissues before the phone is answered
        if self.phone.clicked == True:
            self.click_tissues.draw()
        else:
            WIN.blit(self.click_tissues.image, (361, 317))

        # phone rings, click & answer, man speaks and woman appears
        PHONE_SOUND.play()
        if self.phone.clicked == True:
            PHONE_SOUND.stop()

            self.phone_call.play_sound((620, 290))
            self.phone_call.sound = ""

            if self.mother.show_fader == True:
                WIN.blit(self.mother.image, (self.mother.rect.topleft))
                # redraw so it appears in front of self.mother
                self.click_tissues.draw()
                self.text.draw_text()

        # give tissues to mother, mother speaks
        if self.click_tissues.clicked == True:
            self.click_tissues.rect.topleft = (214, 262)  # this moves it to her hands
            self.mother_speech.play_sound((214, 262))
            self.mother_speech.sound = ""

        # key is revealed, can be moved
        if self.phone.clicked == True and self.click_tissues.clicked == True:
            self.text = Text("Ah, there's the key to the drawer! Let's get that folder")
            self.drag_key.click_and_drag()

        # reveal the folder once key reaches drawer
        if self.drag_key.rect.colliderect(self.drawer):
            self.collect_folder.self_vis = True

        # collect the folder and put in inventory before going to next room
        if self.collect_folder.clicked == True:
            self.collect_folder.rect.x = self.collect_folder.next_x
            self.collect_folder.rect.y = self.collect_folder.next_y
            self.text.text = "On to the next room!"
            self.drag_key.rect.topleft = (190, 410)

        if self.collect_folder.next_room_button.clicked == True:
            self.next_room = True

        pygame.display.update()


# self, 246, 409, FOLDER, 20, HEIGHT - 75
class Room2:
    def __init__(self):
        self.image = ROOM_2_BACKGROUND
        self.open_diary = ROOM_2_DIARY_ZOOM
        self.note_zoom = ROOM_2_NOTE_ZOOM
        self.twinkle = ROOM_2_TWINKLE
        self.text = Text("Probably should check her diary for clues...")
        self.diary = ZoomableClue(self, 40, 360, ROOM_2_DIARY, self.open_diary, 120, 30)
        self.candle = ZoomableClue(
            self, 656, 243, ROOM_2_CANDLE, self.note_zoom, 150, 20
        )
        self.key = CollectableClue(self, 640, 552, ROOM_2_TWINKLE, 20, HEIGHT - 75)
        self.note = DraggableClue(self, ROOM_2_NOTE, 900, 490, True, area=self.candle)
        self.next_room = False
        self.items = [
            self.candle,
            self.diary,
            self.open_diary,
            self.note,
            self.note_zoom,
            self.twinkle,
            self.key,
        ]

    def play_room(self):
        WIN.blit(self.image, (0, 0))
        pos = pygame.mouse.get_pos()

        clicked_items = [
            item
            for item in self.items
            if item is not self
            and isinstance(item, DraggableClue)
            and item.clicked == True
        ]

        self.key.draw()
        self.diary.draw()
        self.candle.draw()
        self.note.draw()
        self.text.draw_text()

        if self.diary.clicked == True:
            # self.diary.zoom()
            self.diary.clue_zoom = True
            if pygame.mouse.get_pressed()[0] and not self.diary.clue_space.collidepoint(
                pos
            ):
                self.diary.toggle_image = ""

        """    
        # twinkle turns into key, drag key to diary, open diary shown, click off to not show
        if self.key.clicked == True:
            self.key.image = ROOM_2_KEY
            self.key.draw()
            self.key.click_and_drag()

            if self.key.is_zoom == True:
                self.diary.zoom()
                self.diary.clue_zoom = True
                if pygame.mouse.get_pressed()[0] and not self.diary.clue_space.collidepoint(pos) and len(clicked_items) == 0:  
                    self.diary.toggle_image = ""
        """
        # drag ball to candle, show note, click off to not show
        if self.candle.clicked == True:
            if self.note.is_zoom == True:
                self.cande.zoom()
                self.candle.clue_zoom = True
                if (
                    pygame.mouse.get_pressed()[0]
                    and not self.candle.clue_space.collidepoint(pos)
                    and len(clicked_items) == 0
                ):
                    self.candle.toggle_image = ""

        if pygame.mouse.get_pressed()[0] and not self.candle.clue_space.collidepoint(
            pos
        ):
            self.candle.toggle_image = ""

        if self.note.clicked == True:
            self.note.click_and_drag()

        pygame.display.update()


# for checking where images go
class Test:
    def __init__(self):
        self.image = ROOM_2_BACKGROUND

    def play_room(self):

        WIN.blit(self.image, (0, 0))

        pygame.display.update()


menu = MenuScreen()
room1 = Room1()
room2 = Room2()
test = Test()


class GameState:
    def __init__(self):
        self.state = "room2"  # or menu

    def menu(self):

        menu.start_screen()

        if menu.start == True:
            fade_in_and_out(WIDTH, HEIGHT, "room1", self, menu, room1)
            self.state = "room1"

    def room1(self):

        room1.play_room()

        if room1.next_room == True:
            fade_in_and_out(WIDTH, HEIGHT, "room2", self, room1, room2)
            self.state = "room2"

    def room2(self):

        room2.play_room()

        if room2.next_room == True:
            fade_in_and_out(WIDTH, HEIGHT, "room3", self, room2, room2)
            self.state = "room3"

    def test(self):

        test.play_room()

        pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            print(pos)

    # decides which room to show
    def state_manager(self):
        if self.state == "menu":
            self.menu()
        if self.state == "room1":
            self.room1()
        if self.state == "room2":
            self.room2()
        if self.state == "test":
            self.test()
        # etc for all rooms


# run the whole game
game_state = GameState()

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)

    pos = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        pass
        print(pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    game_state.state_manager()

pygame.quit()
