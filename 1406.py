import pygame
import os

from clickable_classes import ADVENTURE_FONT_NON_ITALIC, ADVENTURE_FONT

#settings
pygame.init()
pygame.font.init()
pygame.mixer.init(frequency=8000)

WIDTH, HEIGHT = 950,600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Private Eye")

from clickable_classes import NEXT_BUTTON, redraw_window, fade_in_and_out, change_cursor, Text, Text_non_italic, Clickable, FadeIn, AudioClue, CollectableClue, DraggableClue, ZoomableClue

FPS = 120
WHITE = (255, 255, 255)
BLACK = (0,0,0)
TRANSPARENT = (0,0,0,0)
ADVENTURE_FONT = pygame.font.SysFont('arial', 20, italic=True)
ADVENTURE_FONT_NON_ITALIC = pygame.font.SysFont('arial', 20, italic=False)

# LOAD ALL IMAGES AND SOUNDS
# Menu files
MENU_SCREEN = pygame.transform.scale(pygame.image.load((os.path.join("art", "other",'menu_screen.png'))), (WIDTH, HEIGHT))
pygame.mixer.music.load((os.path.join("sounds", 'menu_music.mp3')))

# ROOM 1
# Room 1 files
ROOM_1_BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room1", "room1.png")), (WIDTH, HEIGHT)
)
ROOM_1_PHONE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room1", "room1_phone.png")), (100, 80)
)
ROOM_1_TISSUES = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room1", "room1_tissues.png")), (75, 90)
)
ROOM_1_KEY = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room1", "room1_key.png")), (40, 15)
)
ROOM_1_MOTHER = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room1", "room1_mother.png")), (220, 290)
)
ROOM_1_FOLDER = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room1", "room1_folder.png")), (120, 100)
)
# Room 1 sounds
ROOM_1_MOTHER_SPEAK = pygame.mixer.Sound(os.path.join("sounds", "room1_woman.mp3"))
ROOM_1_MAN = pygame.mixer.Sound(os.path.join("sounds", "room1_man.mp3"))
ROOM_1_PHONE_SOUND = pygame.mixer.Sound(os.path.join("sounds", "phone-ringing.mp3"))
ROOM_1_PHONE_PICKUP = pygame.mixer.Sound(os.path.join("sounds", "phone_pick_up.mp3"))
ROOM_1_DOOR_KNOCK = pygame.mixer.Sound(os.path.join("sounds", "door_knock.mp3"))
ROOM_1_CRYING = pygame.mixer.Sound(os.path.join("sounds", "room1_crying.mp3"))

# Room 2 images
ROOM_2_BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room2", "room2.png")), (WIDTH, HEIGHT)
).convert_alpha()
ROOM_2_NOTE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room2", "room2_note.png")), (18, 15)
).convert_alpha()
ROOM_2_NOTE_ZOOM = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room2", "room2_note_zoom.png")), (600, 550)
).convert_alpha()
ROOM_2_TWINKLE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room2", "room2_twinkle.png")), (15, 25)
).convert_alpha()
ROOM_2_KEY = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room2", "room2_key.png")), (20, 25)
).convert_alpha()
ROOM_2_DIARY = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room2", "room2_diary.png")), (70, 50)
).convert_alpha()
ROOM_2_CANDLE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room2", "room2_candle.png")), (30, 80)
).convert_alpha()

# for middle of rooms 2&3
# ROOM_23_BACKGROUND = pygame.transform.scale(
#     pygame.image.load(os.path.join("art", "room2", "ROOM_23_BACKGROUND.jpeg")),
#     (WIDTH, HEIGHT),
# ).convert_alpha()

# Room 3 images
ROOM_3_BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room3", "room3.png")), (WIDTH, HEIGHT)
)
ROOM_3_DIARY = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room3", "room2_diary_zoom.png")), (700, 550)
).convert_alpha()
ROOM_3_PEOPLE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room3", "room3_people.png")), (370, 240)
)
ROOM_3_CANDLE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room3", "room3_candle.png")), (140, 160)
)
ROOM_3_CARD = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room3", "room3_card.png")), (50, 40)
)
ROOM_3_FILE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room3", "room3_file.png")), (80, 80)
)
# ROOM_3_KEY = pygame.transform.scale(pygame.image.load(os.path.join("art", "room3", 'room3_key.png')), (40, 30))
ROOM_3_PHOTO = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room3", "room3_photo.png")), (100, 100)
)
ROOM_3_PHOTO_FLIP = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room3", "room3_photo_flip.png")), (60, 60)
)
# Room 3 sounds
ROOM_3_DAD = pygame.mixer.Sound(os.path.join("sounds", "ROOM_3_DAD.mp3"))
ROOM_3_MUM = pygame.mixer.Sound(os.path.join("sounds", "ROOM_3_mum.mp3"))
ROOM_3_DAUGHTER = pygame.mixer.Sound(os.path.join("sounds", "ROOM_3_DAUGHTER.mp3"))

# Room 4 images
ROOM_4_BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room4", "room4.png")), (WIDTH, HEIGHT)
)
ROOM_4_DRUNK = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room4", "room4_drunk.png")), (350, 350)
)
ROOM_4_WATER = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room4", "room4_water.png")), (50, 42)
)
ROOM_4_BOTTLE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room4", "room4_bottle.png")), (80, 50)
)
ROOM_4_FULL_BOTTLE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room4", "room4_full_bottle.png")), (65, 75)
)
ROOM_4_BAG = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room4", "room4_bag.png")), (100, 150)
)
ROOM_4_OPEN_BAG = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room4", "room4_open_bag.png")), (100, 150)
)
# ROOM_4_SHINE = pygame.transform.scale(pygame.image.load(os.path.join("art", "room4", 'room4_shine.png')), (35, 35))
ROOM_4_NECKLACE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room4", "room4_necklace.png")), (120, 110)
)
# Room 4 sounds
ROOM_4_DRUNK_TALK = pygame.mixer.Sound(os.path.join("sounds", "room4_drunk.mp3"))
ROOM_4_DRUNK_TALK2 = pygame.mixer.Sound(os.path.join("sounds", "room4_drunk2.mp3"))
ROOM_4_WATER_RUN = pygame.mixer.Sound(os.path.join("sounds",'room4_water.mp3'))

# Room 5 images
ROOM_5_BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room5", "room5.png")), (WIDTH, HEIGHT)
)
ROOM_5_MAN = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room5", "room5_man.png")), (270, 450)
)
ROOM_5_ROCK = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room5", "room5_rock.png")), (40, 35)
)
ROOM_5_LOCK = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room5", "room5_lock.png")), (20, 30)
)
ROOM_5_KEYHOLE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room5", "room5_keyhole.png")), (10, 10)
)
ROOM_5_PLANT = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room5", "room5_plant.png")), (220, 220)
)
ROOM_5_NOTE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room5", "room5_note.png")), (300, 450)
)
ROOM_5_KEY = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room5", "room5_key.png")), (50, 30)
)
# Room 5 sounds
ROOM_5_CAR = pygame.mixer.Sound(os.path.join("sounds", "room5_car.mp3"))
ROOM_5_CAR2 = pygame.mixer.Sound(os.path.join("sounds", "room5_car2.mp3"))
ROOM_5_MAN_SPEAK = pygame.mixer.Sound(os.path.join("sounds", "room5_man.mp3"))
ROOM_5_SMASH = pygame.mixer.Sound(os.path.join("sounds", "room5_smash.mp3"))

# Room 6 images
ROOM_6_BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room6", "room6.png")), (WIDTH, HEIGHT)
)
ROOM_6_DRINK = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room6", "room6_drink.png")), (30, 30)
)
ROOM_6_VIP = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room6", "room6_vip.png")), (70, 50)
)
ROOM_6_VIP_GONE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room6", "room6_vip_gone.png")), (70, 50)
)
ROOM_6_ROPE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room6", "room6_rope.png")), (380, 250)
)
ROOM_6_VIP_MAN = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room6", "room6_vip_man.png")), (80, 250)
)
ROOM_6_VIP_MAN_END = pygame.transform.scale(pygame.image.load(os.path.join("art", "room6", 'room6_vip_man_end.png')), (80, 250))
ROOM_6_GANG = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room6", "room6_thugs.png")), (350, 270)
)
ROOM_6_BOUNCER = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room6", "room6_bouncer.png")),
    (250, HEIGHT - 20),
)
ROOM_6_BOUNCER_VIP = pygame.transform.scale(pygame.image.load(os.path.join("art", "room6", 'room6_bouncer_vip.png')), (250, HEIGHT-20))
ROOM_6_BAT = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room6", "room6_bat.png")), (65, 120)
)
ROOM_6_BAT_TURN = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room6", "room6_bat_turn.png")), (65, 120)
)
ROOM_6_WINDOW = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room6", "room6_window.png")), (120, 45)
)
ROOM_6_WINDOW_BROKEN = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room6", "room6_window_broken.png")),
    (120, 45),
)
# Room 6 sounds
ROOM_6_VIP_MAN_SPEAK = pygame.mixer.Sound(
    os.path.join("sounds", "room6_vip_man_speak.mp3")
)
ROOM_6_GANG_SPEAK = pygame.mixer.Sound(os.path.join("sounds", "room6_gang_speak.mp3"))
ROOM_6_WINDOW_SMASH = pygame.mixer.Sound(os.path.join("sounds", "room6_window.mp3"))
ROOM_6_MUSIC = pygame.mixer.Sound(os.path.join("sounds",'room6_music.mp3'))

# Room 7 images
ROOM_7_BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room7", "office7.png")), (WIDTH, HEIGHT)
)
ROOM_7_NECKLACE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room7", "necklacesmall7.png")), (75, 60)
)
ROOM_7_NECKLACE_ZOOM = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room7", "necklacezoom7.png")), (450, 450)
)
ROOM_7_POSTER = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room7", "postersmall7.png")), (180, 65)
)
ROOM_7_POSTER_ZOOM = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room7", "posterzoom7.png")), (350, 450)
)
ROOM_7_PHOTO = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room7", "picsmall7.png")), (100, 80)
)
ROOM_7_PHOTO_ZOOM = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room7", "piczoom7.png")), (650, 400)
)
ROOM_7_FOLDER = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room7", "foldersmall7.png")), (100, 60)
)
ROOM_7_FOLDER_ZOOM = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room7", "folderzoom7.png")), (550, 450)
)
ROOM_7_DIARY = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room7", "diarysmall7.png")), (100, 60)
)
ROOM_7_DIARY_ZOOM = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room7", "diaryzoom7.png")), (550, 400)
)
ROOM_7_FILE_ZOOM = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room7", "room3_file.png")), (500, 500)
)
GUESS_BOX = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "other", "text_box.png")), (270, 150)
)

# You lose images
YOU_LOSE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "badend", "you_lose.png")), (WIDTH, HEIGHT)
)
TRY_AGAIN = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "badend", "tryagain.png")), (800, 200)
)

# Room 8 images

ROOM_8_BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room8", "room8.png")), (WIDTH, HEIGHT)
)
ROOM_8_PLANK1 = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room8", "plank18.png")), (200, 140)
)
ROOM_8_PLANK2 = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room8", "plank28.png")), (200, 130)
)
ROOM_8_PLANK3 = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room8", "plank38.png")), (210, 80)
)
ROOM_8_STICK1 = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room8", "stick18.png")), (150, 95)
)
ROOM_8_STICK2 = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room8", "stick28.png")), (100, 80)
)
ROOM_8_STICK3 = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room8", "stick38.png")), (150, 30)
)
ROOM_8_KEY = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room8", "key8.png")), (30, 15)
)
ROOM_8_TREE = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room8", "tree8.png")), (10, 20)
)
ROOM_8_GRASS1 = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room8", "grass18.png")), (100, 100)
)
ROOM_8_GRASS2 = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room8", "grass28.png")), (100, 100)
)
ROOM_8_LOCK = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room8", "lock8.png")), (15, 25)
)
ROOM_8_MOTHER = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room8", "mother8.png")), (250, 550)
)
ROOM_8_MOTHER_HIT = pygame.transform.scale(pygame.image.load(os.path.join("art", "room8","mother_hit8.png")), (353, 563))
ROOM_8_GIRL = pygame.transform.scale(
    pygame.image.load(os.path.join("art", "room8", "daughter8.png")), (200, 400)
)
# Room 8 sounds

ROOM_8_KEY_LOCK = pygame.mixer.Sound(os.path.join("sounds", "room8_key_lock.mp3"))
ROOM_8_GIRL_SPEAK = pygame.mixer.Sound(os.path.join("sounds", "room8_girl.mp3"))
ROOM_8_MOTHER_SPEAK = pygame.mixer.Sound(os.path.join("sounds", "room8_mother.mp3"))
ROOM_8_PLANK_HIT_SOUND = pygame.mixer.Sound(os.path.join("sounds","room8_hit.mp3"))

# Ending images
END = pygame.transform.scale(pygame.image.load(os.path.join("art", 'other', 'good.png')), (WIDTH, HEIGHT))

# ROOM CLASSES
class MenuScreen():
    def __init__(self):
        self.image = MENU_SCREEN
        self.text = Text("", "bottom")
        self.has_collectable = False
        self.end_items= []
        self.next_room = False
        
    def start_screen(self):

        WIN.blit(self.image, (0,0))
        
        pygame.mixer.music.load(os.path.join("sounds","menu_music.mp3"))
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(loops=-1)
        
        if pygame.mouse.get_pressed()[0]:
            self.next_room = True
          
        pygame.display.update()    
     
class Room1():
    def __init__(self):        
        self.image = ROOM_1_BACKGROUND
        self.drawer = pygame.draw.rect(WIN, TRANSPARENT, (320,570,50,50))
        self.folder = CollectableClue(self, 246, 409, ROOM_1_FOLDER, 15, HEIGHT - 100)
        self.mother = FadeIn(self, 105, 132, ROOM_1_MOTHER)
        self.phone = Clickable(self, 650, 310, ROOM_1_PHONE)
        self.phone_call = AudioClue(self, self.phone, ROOM_1_PHONE_PICKUP, 1000, False, ROOM_1_MAN, ROOM_1_DOOR_KNOCK, self.mother.fade_in, fourth_sound=ROOM_1_CRYING)
        self.tissues = Clickable(self, 361, 317, ROOM_1_TISSUES)
        self.mother_speech = AudioClue(self, self.tissues, ROOM_1_MOTHER_SPEAK, 100, False)
        self.key = DraggableClue(self, ROOM_1_KEY, 380, 385, True, area=self.drawer)
        self.text = Text("She seems too upset to speak.                                                                 Maybe I should give her some tissues and she'll be able to tell us about the case?", "top")
        self.start_items = [self.key, self.phone, self.tissues, self.folder]
        self.end_items = [self.key, self.phone, self.mother, self.tissues, self.folder, self.folder.next_room_button]
        self.current_items = [self.key, self.phone, self.mother, self.tissues]
        self.all_items = list(set(self.end_items + self.start_items + self.current_items))
        self.has_collectable = True
        self.next_room = False

    def play_room(self):

        WIN.blit(self.image, (0, 0))
        self.phone.draw()
        
        # cursor becomes hand when hovering over Clickable
        pos = pygame.mouse.get_pos()                    
        change_cursor(self.all_items, pos)
          
        # so that we can't click the tissues before the phone is answered
        if self.phone.clicked == True:
            self.tissues.draw()
        else:
            WIN.blit(self.tissues.image, (361, 317))

        # phone rings, click & answer, man speaks and woman appears
        ROOM_1_PHONE_SOUND.play()        
        if self.phone.clicked == True:
            ROOM_1_PHONE_SOUND.stop()
            
            self.phone_call.play_sound((650, 310))
            self.phone_call.sound = ""
 
            if self.mother.show_fader == True:
                WIN.blit(self.mother.image, (self.mother.rect.topleft))
                # redraw so it appears in front of self.mother
                self.tissues.draw()
                self.text.blit_text()
                
        # give tissues to mother, mother speaks 
        if self.tissues.clicked == True:
            self.phone_call.fourth_sound.stop()
            self.tissues.rect.topleft = (214, 262) #this moves it to her hands
            self.mother_speech.play_sound((214, 262))
            self.mother_speech.sound = ""
        
        # key is revealed, can be moved
        if self.phone.clicked == True and self.tissues.clicked == True:
            self.text = Text("Oh good, that seems to have helped her.                                                   Ah! There's the key to the drawer! Let's get that casefile.", "top")
            self.key.draw()
            if isinstance(self.key, DraggableClue):
                self.key.click_and_drag()
        
        # reveal the folder once key reaches drawer
        if self.key.rect.colliderect(self.drawer):
            self.folder.self_vis = True
            self.key.rect.topleft = (190, 410)
            self.key = Clickable(self, 190, 410, ROOM_1_KEY)
        
        if not isinstance(self.key, DraggableClue):
            self.folder.draw()
            self.folder.self_vis = True
        
        # collect the folder and put in inventory before going to next room
        if self.folder.clicked == True:
            self.folder.next_room_button.self_vis = True
            self.folder.collect()
            self.folder.rect.x = self.folder.next_x
            self.folder.rect.y = self.folder.next_y
            self.text = Text("Time to go and see what clues we can find in her daughter's bedroom...", "top")
    
        if self.folder.next_room_button.clicked == True:
            self.mother.self_vis = True
            self.next_room = True
                   
        pygame.display.update()  
        

class Room2():
    def __init__(self):
        self.image = ROOM_2_BACKGROUND
        self.note_zoom = ROOM_2_NOTE_ZOOM
        self.diary = Clickable(self, 38, 365, ROOM_2_DIARY)
        self.diary2 = CollectableClue(self, 40, 355, ROOM_2_DIARY, 15, HEIGHT - 100)
        self.twinkle = DraggableClue(self, ROOM_2_TWINKLE, 640, 552, True, area=self.diary)
        self.candle = ZoomableClue(self, 656, 243, ROOM_2_CANDLE, self.note_zoom, 150, 20)
        self.key = ROOM_2_KEY
        self.note = DraggableClue(self, ROOM_2_NOTE, 900, 490, True, area=self.candle)
        self.text = Text("Okay, where to look first? Hmm, those posters seems quite interesting. Oh! I've heard of magic ink before! You hold the note over heat and the ink becomes visible!", "top")
        self.start_items = [self.candle, self.diary, self.note]
        self.end_items = [self.candle, self.note, self.diary, self.diary2.next_room_button, self.twinkle]
        self.all_items = list(set(self.end_items + self.start_items))
        self.has_collectable = True
        self.next_room = False
    
    def play_room(self):
        WIN.blit(self.image, (0,0))

        # cursor becomes hand when hovering over Clickable
        pos = pygame.mouse.get_pos()                    
        change_cursor(self.all_items, pos)
        
        self.twinkle.draw()
        self.candle.draw()
        self.note.draw()
        self.note.click_and_drag()
        self.diary.draw()
        
        clicked_yet = [item for item in self.end_items if item.clicked == True]
        
        if len(clicked_yet) != 4:
            self.text.blit_text()
        
        # take the note to candle, show the note on screen
        if self.note.area.rect.collidepoint(pos) and self.note.clicked == True:
            WIN.blit(self.note_zoom, (150,0))
            self.text.remove_text()
            
        # click the twinkle, turns into a key    
        if self.twinkle.clicked == True:
            self.twinkle.image = self.key
            self.twinkle.click_and_drag()
            self.text = Text("Aha, that looks like a diary key! Let's grab it and see what we can find out.", "top")
        
        # take the key to the diary, put both in inventory
        if self.diary.clicked == True:
            self.diary.self_vis = False
            self.diary.image = ""
            self.diary2.collect()
            self.diary2.draw()
            self.diary2.self_vis = True
            self.diary2.rect.x = self.diary2.next_x
            self.diary2.rect.y = self.diary2.next_y
            self.twinkle.draw()
            self.twinkle.rect.topleft = (50, 510)
            self.diary2.next_room_button.self_vis = True
         
        if self.diary2.next_room_button.clicked == True:
            self.next_room = True
    
        pygame.display.update()

class Room23():
    def __init__(self):
        self.image = ROOM_2_BACKGROUND
        self.diary = Clickable(self, 120, 10, ROOM_3_DIARY)
        self.small_diary = Clickable(self, 15, HEIGHT - 100, ROOM_2_DIARY)
        self.key = Clickable(self, 50, 525, ROOM_2_KEY)
        self.text = Text("", "bottom")
        self.start_items = [self.diary]
        self.end_items = [self.diary,self.small_diary, self.key]
        self.all_items = list(set(self.end_items + self.start_items))
        self.has_collectable = True
        self.next_room = False
        
    def play_room(self):
        WIN.blit(self.image, (0,0))

        self.small_diary.image = pygame.transform.scale(ROOM_2_DIARY, (80,60))
        self.small_diary.draw()
        self.key.draw()
        self.diary.draw()
        
        ROOM_23_FONT = pygame.font.SysFont('arial', 20)
        display_text = ROOM_23_FONT.render("Got a clue!", 1, WHITE)
        WIN.blit(display_text, (10, 570))
        
        # cursor becomes hand when hovering over Clickable
        pos = pygame.mouse.get_pos()                    
        change_cursor(self.all_items, pos)
        
        if pygame.mouse.get_pressed()[0] and self.diary.rect.collidepoint(pos):
            self.next_room = True
           
        pygame.display.update()    

class Room3():
    def __init__(self):
        self.image = ROOM_3_BACKGROUND
        self.candle = Clickable(self, 590, 350, ROOM_3_CANDLE)
        self.photo = CollectableClue(self, 70, 140, ROOM_3_PHOTO, 700, 250)
        self.file = CollectableClue(self, 815, 280, ROOM_3_FILE, 15, HEIGHT - 100)
        self.people = Clickable(self, 570, 146, ROOM_3_PEOPLE)
        self.peoplespeak = AudioClue(self, self.people, ROOM_3_DAD, 1500, False, ROOM_3_MUM)
        self.daughterspeak = AudioClue(self, self.people, ROOM_3_DAUGHTER, 300, False)
        self.drawer = pygame.draw.rect(WIN, TRANSPARENT, (90,250,80,80))
        self.card = DraggableClue(self, ROOM_3_CARD, 630, 415, True, area=self.drawer)
        self.text = Text("It seems from what she wrote in her diary her friend might know something... Let's see if she'll help.", "top")
        self.text_non_italic = Text_non_italic("", "bottom")
        self.start_items = [self.candle, self.people]
        self.end_items = [self.candle, self.people, self.photo, self.card, self.file, self.file.next_room_button]
        self.all_items = list(set(self.end_items + self.start_items))
        self.has_collectable = True
        self.next_room = False
        
    def play_room(self):
        WIN.blit(self.image, (0,0))
        pos = pygame.mouse.get_pos()
        self.candle.draw()
        self.photo.draw()
        self.file.draw()
        self.people.draw()
        self.text.blit_text()
        self.text_non_italic.blit_text_non_italic()
        
        # cursor becomes hand when hovering over Clickable
        pos = pygame.mouse.get_pos()                    
        change_cursor(self.all_items, pos)
        
        # click the family, dad and mum speak
        if self.people.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.peoplespeak.play_sound((self.peoplespeak.item.rect.topleft))
            self.peoplespeak.sound = ""
            
        if self.peoplespeak.sound == "":
            self.text = Text("Hmm, well they won't be much help. What did the daughter shove in the drawer just before I came in? It's locked, maybe the key card is around here...", "top")


        # click the candle, it moves to the side
        if self.candle.clicked == True and self.peoplespeak.sound == "":
            self.candle.rect.topleft = (520,350)
            self.card.draw()
            self.card.click_and_drag()
            
        # take the card to the drawers, the photo appears
        if self.card.rect.colliderect(self.drawer):
            self.card.image = ""
            self.card.self_vis = False
            self.photo.self_vis = True
        
        # switch the photo image round so it fits in daughter's hands    
        if self.photo.clicked == True:
            self.photo.draw()
            self.photo.image = ROOM_3_PHOTO_FLIP
            self.photo.rect.x = self.photo.next_x
            self.photo.rect.y = self.photo.next_y
        
        # click the photo, goes to girl who speaks
        if self.photo.rect.topleft == (self.photo.next_x, self.photo.next_y):
            self.text = Text("", "top")
            self.text_non_italic = Text_non_italic('"So are you sure you don\'t know anything at all?"                                "Then who\'s this boy with you in the photo?"                                        "And what\'s that file your father has?"', "bottom")
            self.daughterspeak.play_sound(self.daughterspeak.item.rect.topleft)
            self.daughterspeak.sound = ""
            self.file.self_vis = True
            self.file.collect()
            self.file.next_room_button.self_vis = True
            
        # grab the file
        if self.file.clicked == True:
            self.file.rect.x = self.file.next_x
            self.file.rect.y = self.file.next_y
            #self.file.draw()
        
        if self.file.rect.topleft == (self.file.next_x, self.file.next_y):
            self.file.collect()
            self.text = Text("It looks like the father collected information on this boy, Tom, he must have been concerned too! Let's see if we can find that boy at that alleyway Emma mentioned.", "top")
            self.text_non_italic.remove_text_non_italic()

        if self.file.next_room_button.clicked == True:
            self.next_room = True
    
        pygame.display.update()
     

class Room4():
    def __init__(self):
        self.image = ROOM_4_BACKGROUND   
        self.drunk = Clickable(self, 250, 225, ROOM_4_DRUNK)
        self.drunk_talk = AudioClue(self, self.drunk, ROOM_4_DRUNK_TALK, 500, False)
        self.drunk_head = pygame.draw.rect(WIN, TRANSPARENT, (300,250,50,50))
        self.drunk_talk2 = AudioClue(self, self.drunk, ROOM_4_DRUNK_TALK2, 500, False)
        self.water = Clickable(self, 898, 415, ROOM_4_WATER)
        self.water_run = AudioClue(self, self.drunk, ROOM_4_WATER_RUN, 150, False)
        self.bottle = DraggableClue(self, ROOM_4_BOTTLE, 70, 480, True, area=self.water)
        self.full_bottle = ROOM_4_FULL_BOTTLE
        self.bag = Clickable(self, 543, 170, ROOM_4_BAG)
        self.open_bag = ROOM_4_OPEN_BAG
        # self.shine = ROOM_4_SHINE
        self.necklace = CollectableClue(self, 600, 355, ROOM_4_NECKLACE, 15, HEIGHT - 105)
        self.text = Text("Well, Tom doesn't seem to be anywhere around here.                                I wonder if this man has seen him...", "top")
        self.start_items = [self.drunk, self.bottle, self.bag]
        self.end_items = [self.drunk, self.bottle, self.bag, self.necklace, self.necklace.next_room_button]
        self.all_items = list(set(self.end_items + self.start_items))
        self.has_collectable = True
        self.next_room= False
        
    def play_room(self):
        WIN.blit(self.image, (0,0))
        
        self.bag.draw()
        self.drunk.draw()
        self.bottle.draw()
        self.text.blit_text()
        self.bottle.click_and_drag()
        
        # cursor becomes hand when hovering over Clickable
        pos = pygame.mouse.get_pos()                    
        change_cursor(self.all_items, pos)
        
        # click the drunk who talks
        if self.drunk.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.text.remove_text()
            self.drunk_talk.play_sound(self.drunk_talk.item.rect.topleft)
            self.drunk_talk.sound = ""
        
        if self.drunk_talk.sound == "":
            self.bottle.click_and_drag()
        
        # take the bottle to the water and fill it, water run sound
        if self.bottle.rect.colliderect(self.water):
            self.bottle.rect.topleft = (908, 452)
            self.water.draw()
            self.bottle.draw()
            self.bottle.image = self.full_bottle
            self.water_run.play_sound((250, 225))
            
        if self.bottle.image == self.full_bottle and not self.bottle.rect.colliderect(self.water):
            self.water_run.sound.stop()
        
        # give to drunk who then talks
        if self.bottle.rect.colliderect(self.drunk_head) and self.bottle.image == self.full_bottle:
            self.bottle.rect.topleft = (280, 450)
            self.drunk_talk2.play_sound(self.drunk_talk2.item.rect.topleft)
            self.drunk_talk2.sound = ""
        
        # open the bag, necklace fall on floor, collect it
        if self.bag.clicked == True and self.bottle.image == self.full_bottle and self.drunk_talk2.sound == "":
            self.bag.image = self.open_bag  
        
        if self.bag.image == self.open_bag and self.drunk_talk2.sound == "":
            self.necklace.self_vis = True
            self.necklace.draw()
            self.text = Text("This looks like a lady's necklace, could it be the one Tom gave to Sara? And on the back there's an address. Why would he try to get rid of it, maybe they had a fight?", "top")
            
        if self.necklace.clicked == True and self.drunk_talk2.sound == "":
            self.necklace.collect()
            self.necklace.next_room_button.self_vis= True
            self.necklace.rect.x = self.necklace.next_x
            self.necklace.rect.y = self.necklace.next_y
            self.text = Text("Let's go check out that address and see if he will be there.", "top")
            
        if self.necklace.next_room_button.clicked == True:
            self.next_room = True    
        
        pygame.display.update()

class Room5():
    def __init__(self):
        self.image = ROOM_5_BACKGROUND 
        self.man = FadeIn(self, 15, 170, ROOM_5_MAN)
        self.man_speak = AudioClue(self, self.man, ROOM_5_MAN_SPEAK, 500, False)
        self.plant = Clickable(self, 660, 290, ROOM_5_PLANT)
        self.lock= Clickable(self, 244, 200, ROOM_5_LOCK)
        self.rock = DraggableClue(self, ROOM_5_ROCK, 640, 455, True, area=self.lock)
        self.rock_end = Clickable(self, 640, 455, ROOM_5_ROCK)
        self.keyhole = Clickable(self, 585, 200, ROOM_5_KEYHOLE)
        self.key = DraggableClue(self, ROOM_5_KEY, 700, 460, True, area= self.keyhole)
        self.key_end = Clickable(self, 720, 465, ROOM_5_KEY)
        self.car = AudioClue(self, self.keyhole, ROOM_5_CAR2, 0, True, ROOM_5_CAR, func=self.man.fade_in)
        self.smash = AudioClue(self, self.lock, ROOM_5_SMASH, 50, True)
        self.poster = CollectableClue(self, 350, 5, ROOM_5_NOTE, 25, HEIGHT - 115, size=(55, 80))
        self.lock_space = pygame.draw.rect(WIN, TRANSPARENT, (238,200,30,30))
        self.text = Text("Looks like there's no one home. Nothing wrong with having a little look around though. Might be worth trying to get some clues.", "top")
        self.text_italic = Text_non_italic("", "bottom")
        self.start_items = [self.key, self.plant, self.lock, self.rock, self.keyhole]
        self.end_items = [self.plant, self.rock_end, self.keyhole, self.key_end, self.poster, self.poster.next_room_button]
        self.current_items = [self.plant, self.rock, self.keyhole, self.key, self.lock]
        self.all_items = list(set(self.end_items + self.start_items + self.current_items))
        self.has_collectable = True
        self.next_room= False

    def play_room(self):
        WIN.blit(self.image, (0,0))
        
        self.plant.draw()
        self.keyhole.draw()
        self.lock.draw()
        self.rock.draw()
        self.text.blit_text()
        self.text_italic.blit_text_non_italic()
        
        # cursor becomes hand when hovering over Clickable
        pos = pygame.mouse.get_pos()                    
        change_cursor(self.all_items, pos)
        
        # move plant, collect key, take to door, man arrives
        if self.plant.clicked == True:
            self.text.remove_text()
            self.plant.rect.topleft = (750, 290)
            self.key.draw()
            if isinstance(self.key, DraggableClue):
                self.key.click_and_drag()
        
        # father arrives home as you try to enter
        if self.key.rect.colliderect(self.keyhole):
            self.key = Clickable(self, 720, 465, ROOM_5_KEY)
            self.car.play_sound((585, 200))
            self.car.sound = ""
            self.man_speak.play_sound(self.man.rect.topleft)
            self.man_speak.sound = ""
            pygame.time.delay(6000)
            self.man.image == ""
            self.man.self_vis = False
            self.man.fade_out()
        
        if self.man_speak.sound == "":
            self.text = Text("Looks like I'll need some way of breaking in to the garage! That lock doesn't look sturdy, with a little force it should open.", "top")
            if isinstance(self.rock, DraggableClue):
                self.rock.click_and_drag()
        
        # grab rock, smash lock
        if self.rock.rect.colliderect(self.lock):
            self.rock = Clickable(self, 640, 455, ROOM_5_ROCK)
            self.rock.rect.topleft = (640, 455)
            self.smash.play_sound((244, 200))
            self.smash.sound = ""
            self.lock.image = ""
            self.text.remove_text()
        
        # collect the poster clue
        if self.lock.image == "":    
            self.poster.draw()
            if self.lock_space.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                self.poster.self_vis = True
        
        if self.poster.self_vis == True:
            self.text.remove_text()
            self.text_italic = Text_non_italic('"Hmm, poster advertising a club... And today the members are meeting up. Guess I am gonna go clubbing tonight..."', "bottom")
        
        if self.poster.clicked == True:
            self.poster.collect()
            self.rock.rect.topleft = (640, 455)
            self.poster.next_room_button.self_vis = True
            self.poster.rect.x = self.poster.next_x
            self.poster.rect.y = self.poster.next_y
            
        if self.poster.next_room_button.clicked == True:
            self.next_room = True
        
        pygame.display.update()

class Room6():
    def __init__(self):
        self.image = ROOM_6_BACKGROUND  
        self.vip_man = Clickable(self, 400, 60,  ROOM_6_VIP_MAN)
        self.bouncer = Clickable(self, 700, 20, ROOM_6_BOUNCER)
        self.bouncer_vip = FadeIn(self, 700, 20, ROOM_6_BOUNCER_VIP)
        self.drink = DraggableClue(self, ROOM_6_DRINK, 75, 210, True, area=self.vip_man)
        self.vip = DraggableClue(self, ROOM_6_VIP, 310, 50, True, area=self.bouncer)
        self.rope = Clickable(self, 525, 165, ROOM_6_ROPE)
        self.gang = Clickable(self, 545, 100, ROOM_6_GANG)
        self.window = Clickable(self, 570, 15, ROOM_6_WINDOW)
        self.window_smash = AudioClue(self, self.drink, ROOM_5_SMASH, 100, True)
        self.bat_click = Clickable(self, 470, 230, ROOM_6_BAT)
        self.bat = DraggableClue(self, ROOM_6_BAT, 470, 230, True, area=self.window)
        self.bat_end = Clickable(self, 470, 230, ROOM_6_BAT)
        self.vip_man_speak = AudioClue(self, self.vip_man, ROOM_6_VIP_MAN_SPEAK, 0, True)
        self.gang_speak = AudioClue(self, self.gang, ROOM_6_GANG_SPEAK, 0, True)
        self.text = Text("Those guys look like his friends I saw in the photo in the file her friend's dad had. But they're in the VIP area, how do I get in?", "bottom")
        self.next_room_button = Clickable(self, WIDTH - 200, HEIGHT - 150, NEXT_BUTTON)
        self.start_items =[self.vip_man, self.gang, self.rope, self.bouncer, self.drink, self.window, self.bat]
        self.end_items =[self.vip_man, self.window, self.gang, self.bat_end, self.next_room_button]
        self.current_items = [self.vip_man, self.window, self.bat, self.gang, self.rope]
        self.all_items = list(set(self.end_items + self.start_items + self.current_items + [self.vip]))
        self.has_collectable = False
        self.next_room = False
        
    def play_room(self):
        WIN.blit(self.image, (0,0))
        WIN.blit(ROOM_6_GANG, (545, 100))

        self.window.draw()
        self.vip_man.draw()
        self.rope.draw()
        self.bouncer.draw()
        self.bat_click.draw()
        self.drink.draw()
        self.text.blit_text()
        
        # cursor becomes hand when hovering over Clickable
        pos = pygame.mouse.get_pos()                    
        change_cursor(self.all_items, pos)
        
        # speak to man to get vip ticket
        if self.vip_man.clicked == True: 
            self.vip_man_speak.play_sound((400, 60))
            self.vip_man_speak.sound = ""
            self.text.text = "OK, looks like I'll have to buy this guy a drink if I want to get into the VIP area."
            if isinstance(self.drink, DraggableClue):
                self.drink.click_and_drag()
        
        # give man drink
        if self.drink.rect.colliderect(self.vip_man):
            self.vip_man.image = ROOM_6_VIP_MAN_END
            self.drink.rect.topleft = (430, 130)
            self.vip_man.draw()
            self.drink.image == ""
            self.drink = Clickable(self, 430, 130, ROOM_6_DRINK)
            
        if self.drink.rect.topleft == (430, 130):    
            self.vip.draw()
            self.vip.click_and_drag()
            
        # give vip ticket to bouncer who disappears
        if self.vip.rect.colliderect(self.bouncer):
            self.bouncer.image = ""
            self.bouncer.self_vis = False
            self.bouncer_vip.draw()
            self.vip.rect.topleft = (790, 190)
            self.vip.image = ""
        
        if self.vip.image == "":
            self.bouncer_vip.fade_out()
            self.bouncer_vip.image = ""
            self.bouncer_vip.self_vis = False
            self.text.remove_text()
            self.bat.draw()
            self.bat_click.image = ""
            
        if self.bat.clicked == True:
            self.bat.image = ROOM_6_BAT_TURN
            if isinstance(self.bat, DraggableClue):
                self.bat.click_and_drag()

        # remove rope and speak to Tom's gang
        if self.rope.clicked == True and self.bouncer.image == "":
            self.rope.image = ""
            self.text.text = "Excuse me, I'm looking for this guy, Tom. Have you seen him?"
            
        if self.gang.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] and self.bouncer_vip.image == "" and self.rope.image == "":
            self.gang_speak.play_sound((545, 100))
            self.gang_speak.sound = ""
            
        if self.gang_speak.sound == "" and isinstance(self.bat, DraggableClue):
            self.text.remove_text()
            self.bat.click_and_drag()

        #smash the window and leave
        if self.bat.clicked == True and self.vip.image == "":
            self.text.text = "Uh-oh, looks like I better get out of here!"
            self.bat.image = ROOM_6_BAT_TURN
        
        if self.bat.rect.colliderect(self.window) and pygame.mouse.get_pressed()[0]:
            self.window.image = ROOM_6_WINDOW_BROKEN
            self.bat.image = ROOM_6_BAT
            self.window_smash.play_sound((430, 130))
            self.bat = Clickable(self, 470, 230, ROOM_6_BAT)
            self.bat_end.draw()
            self.window_smash.sound == ""
            
        if self.window.image == ROOM_6_WINDOW_BROKEN:
            self.text.text = "Uh-oh, looks like I better get out of here!"
            self.next_room_button.draw()
            self.vip_man.image = ROOM_6_VIP_MAN_END
            
        if self.next_room_button.clicked == True:
            self.next_room = True
               
        pygame.display.update()
       
class Room7():
    def __init__(self):
        self.image = ROOM_7_BACKGROUND
        self.necklace = Clickable(self, 590, 380, ROOM_7_NECKLACE)
        self.necklace_zoom = CollectableClue(self, 280, 25, ROOM_7_NECKLACE_ZOOM, 0, 0)
        self.photo = Clickable(self, 550, 290, ROOM_7_PHOTO)
        self.photo_zoom = CollectableClue(self, 145, 30, ROOM_7_PHOTO_ZOOM, 0, 0)
        self.folder = Clickable(self, 270, 440, ROOM_7_FOLDER)
        self.folder_zoom = CollectableClue(self, 190, 30, ROOM_7_FOLDER_ZOOM, 0, 0)
        self.diary = Clickable(self, 380, 420, ROOM_7_DIARY)
        self.diary_zoom = CollectableClue(self, 180, 30, ROOM_7_DIARY_ZOOM, 0, 0)
        self.poster = Clickable(self, 420, 370, ROOM_7_POSTER)
        self.poster_zoom = CollectableClue(self, 290, 30, ROOM_7_POSTER_ZOOM, 0, 0)
        self.file = Clickable(self, 190, 355, ROOM_3_FILE)
        self.file_zoom = CollectableClue(self, 260, 10, ROOM_7_FILE_ZOOM, 0, 0)
        self.necklace_text = Text("Tom gave her a necklace with his address on it, who knows why he'd want her to go there, seems like he had a rough family dynamic.", "bottom")
        self.file_text = Text("Her friend's father was gathering information on Tom which is a bit much, but seems like he didn't actually find a lot to be worried about, he's just a kid.", "bottom")
        self.photo_text = Text("So, we know she was friends with Tom, who these parents all thought was trouble.", "bottom")
        self.poster_text = Text("We didn't find him at the club with his gang, but it seems he ran with a rough crowd, I wouldn't trust them, or anyone they hung around with.", "bottom")
        self.diary_text = Text("We know from her diary her mother was overprotective of her and would do anything to keep her away from Tom.", "bottom")
        self.final_text = Text("Now that I'm looking at all of this, I think it's pretty obvious who knows where she is!", "bottom")
        self.text = Text("", "bottom")
        self.guess1 = Clickable(self, 160, 30, GUESS_BOX)
        self.guess2 = Clickable(self, 500, 30, GUESS_BOX)
        self.guess3 = Clickable(self, 160, 165, GUESS_BOX)
        self.guess4 = Clickable(self, 500, 165, GUESS_BOX)
        self.guesses = [self.guess1, self.guess2, self.guess3, self.guess4]
        self.start_items = [self.necklace, self.photo, self.folder, self.file, self.diary, self.poster]
        self.end_items = [self.necklace, self.photo, self.folder, self.file, self.diary, self.poster]
        self.all_items = list(set(self.end_items + self.start_items))
        self.has_collectable = False
        self.next_room = False
        self.lose_screen = False
        
    def play_room(self):
        WIN.blit(self.image, (0,0))
        
        self.poster.draw()
        self.necklace.draw()
        self.photo.draw()
        self.diary.draw()
        self.file.draw()
        WIN.blit(self.folder.image, (270, 440))
        
        pos = pygame.mouse.get_pos()                    
        # allows changing the cursor only for images before the final guesses
        zoom_images = [self.file_zoom, self.necklace_zoom, self.poster_zoom, self.photo_zoom, self.diary_zoom]
        zoomed = [item for item in zoom_images if item.image != ""]
        # cursor becomes hand when hovering over Clickables
        if len(zoomed) or (self.folder.clicked == False and not len(zoomed)):
            change_cursor(self.all_items, pos)
        
        def click_item(item, item_zoom, item_text):
            if item.clicked == True:
                item_text.blit_text()
                item_zoom.draw()
                item_zoom.self_vis = True
                if pygame.mouse.get_pressed()[0] and not item.rect.collidepoint(pos):
                    item_zoom.self_vis = False
                    item_zoom.image = ""
                    item_text.remove_text()
                    
        click_item(self.file, self.file_zoom, self.file_text)    
        click_item(self.necklace, self.necklace_zoom, self.necklace_text)
        click_item(self.poster, self.poster_zoom, self.poster_text)
        click_item(self.diary, self.diary_zoom, self.diary_text)
        click_item(self.photo, self.photo_zoom, self.photo_text)        
        
        # which clues have been clicked and which haven't, enter final stage
        clues = [self.necklace, self.photo, self.file, self.diary, self.poster]
        clicked_items = [item for item in clues if item.clicked == True]
        final = len(clicked_items) == 5
        
        # pick who you think it is
        if final:
            if self.folder.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                self.folder.clicked = True
                
            if self.folder.clicked == True:    
                self.folder.draw()
                self.final_text.blit_text()
                self.folder_zoom.draw()
                self.folder_zoom.self_vis = True
                self.file_zoom.image = ""
                self.necklace_zoom.image = ""
                self.poster_zoom.image = ""
                self.photo_zoom.image = ""
                self.diary_zoom.image = ""
                self.guess1.draw()
                self.guess2.draw()
                self.guess3.draw()
                self.guess4.draw()
                self.guess1.draw()
                guess1 = ADVENTURE_FONT.render(
                            "The Boy", 1, BLACK)
                WIN.blit(guess1, (250, 90))
                guess2 = ADVENTURE_FONT.render(
                            "The Boy's Friends", 1, BLACK)
                WIN.blit(guess2, (550, 90))
                guess3 = ADVENTURE_FONT.render(
                            "The Girl's Mother", 1, BLACK)
                WIN.blit(guess3, (200, 230))
                guess4 = ADVENTURE_FONT.render(
                            "The Friend's Parents", 1, BLACK)
                WIN.blit(guess4, (540, 230))
                change_cursor(self.guesses, pos)
                
                # you lose screen
                if pygame.mouse.get_pressed()[0] and (self.guess1.rect.collidepoint(pos) or self.guess2.rect.collidepoint(pos) or self.guess4.rect.collidepoint(pos)):
                    self.state = 'you_lose'
                    self.lose_screen = True
                
                # continue to last room to finish the game
                if self.guess3.clicked == True:
                    self.next_room = True
                
        pygame.display.update()

class YouLose():
    def __init__(self):
        self.image = YOU_LOSE
        self.image_space = self.image.get_rect()
        self.try_again = Clickable(self, 80, 370, TRY_AGAIN)
        self.text = Text("", "bottom")
        self.start_items = []
        self.end_items = []
        self.all_items = list(set(self.end_items + self.start_items))
        self.has_collectable = False
        self.back_room = False
        
    def play_room(self):
        WIN.blit(self.image, (0,0)) 

        self.try_again.draw()
        
        # hand cursor if you hover over button
        if self.try_again.rect.collidepoint(pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
        if pygame.mouse.get_pressed()[0] and self.try_again.rect.collidepoint(pos):
            self.back_room = True
        
        pygame.display.update()

class Room8:
    def __init__(self):
        self.image = ROOM_8_BACKGROUND
        self.plank1 = Clickable(self, 365, 285, ROOM_8_PLANK1)
        self.plank2 = Clickable(self, 360, 290, ROOM_8_PLANK2)
        self.plank3 = Clickable(self, 360, 177, ROOM_8_PLANK3)
        self.stick1 = DraggableClue(self, ROOM_8_STICK1, 380, 503, True, area=self.plank1)
        self.stick2 = DraggableClue(self, ROOM_8_STICK2, 797, 490, True, area=self.plank2)
        self.stick3 = DraggableClue(self, ROOM_8_STICK3, 586, 560, True, area=self.plank3)
        self.lock = Clickable(self, 386, 268, ROOM_8_LOCK)
        self.key = DraggableClue(self, ROOM_8_KEY, 261, 189, True, area=self.lock)
        self.tree = Clickable(self, 242, 183, ROOM_8_TREE)
        self.grass1 = Clickable(self, 630, 530, ROOM_8_GRASS1)
        self.grass2 = Clickable(self, 380, 540, ROOM_8_GRASS2)
        self.plank_hit = DraggableClue(self, ROOM_8_PLANK2, 506, 482, True)
        self.girl_items = [self.tree, self.grass1, self.grass2, self.plank_hit]
        self.girl = FadeIn(self, 560, 300, ROOM_8_GIRL , self.girl_items)
        self.girl_click = Clickable(self, 560, 300, ROOM_8_GIRL)
        self.mother_items = [self.plank_hit, self.girl_click, self.grass1, self.grass2, self.tree]
        self.mother_hit_items = [self.girl_click, self.grass1, self.grass2, self.tree]
        self.mother = FadeIn(self, 133, 199, ROOM_8_MOTHER, self.mother_items, self.mother_hit_items)
        self.plank_hit = DraggableClue(self, ROOM_8_PLANK2, 506, 482, True, area=self.mother)
        self.lock_sound = AudioClue(self, self.lock, ROOM_8_KEY_LOCK, 500, False, func=self.girl.fade_in)
        self.girl_speak = AudioClue(self, self.girl, ROOM_8_GIRL_SPEAK, 3000, False, func=self.mother.fade_in, func_pause=True)
        self.mother_speak = AudioClue(self, self.mother, ROOM_8_MOTHER_SPEAK, 500, False)
        self.plank_hit_mother = AudioClue(self, self.girl, ROOM_8_PLANK_HIT_SOUND, 500, False, func=self.mother.fade_out)
        self.text = Text("Just like in the notes, Sara's mother owns this land, and someone seems to be inside that shed!", "top")
        self.start_items = [self.plank1,self.plank2,self.plank3,self.stick1,self.stick2,self.stick3,self.lock,self.grass1, self.grass2]
        self.end_items = [self.girl, self.plank_hit]
        self.current_items = [self.girl, self.tree, self.key]
        self.all_items = list(set(self.end_items + self.start_items + self.current_items))
        self.end_screen = False
        self.has_collectable = False

    def play_room(self):
        WIN.blit(self.image, (0, 0))
        WIN.blit(self.tree.image, (242, 183))

        self.lock.draw()
        self.plank1.draw()
        self.plank2.draw()
        self.plank3.draw()
        self.grass1.draw()
        self.grass2.draw()
        self.stick1.draw()
        self.stick1.click_and_drag()
        self.stick2.draw()
        self.stick3.draw()
        
        pos = pygame.mouse.get_pos()
        change_cursor(self.all_items, pos)

        self.text.blit_text()

        # stick 1 logic
        if self.stick1.area.rect.collidepoint(pos) and self.stick1.clicked == True:
            if (self.stick1.rect.colliderect(self.plank2) and pygame.mouse.get_pressed()[0]):
                self.plank2.image = ""
                self.plank2.self_vis = False
                
        if self.plank2.image == "" and self.plank2.self_vis == False:
            self.text.remove_text()

        # when plank 2 gone stick 1 dissapears
        if self.plank2.image == "" and self.plank2.self_vis == False:
            self.stick1.image = ""
            self.stick1.self_vis = False

        # when plank 2 dissapears stick 3 appears
        if self.plank2.image == "" and self.plank2.self_vis == False:
            self.stick3.click_and_drag()
        else:
            WIN.blit(self.stick3.image, (586, 560))

        # stick 3 logic
        if self.stick3.area.rect.collidepoint(pos) and self.stick3.clicked == True:
            if (
                self.stick3.rect.colliderect(self.plank3)
                and pygame.mouse.get_pressed()[0]
            ):
                self.plank3.image = ""
                self.plank3.self_vis = False

        # when plank 3 gone stick 3 dissapears
        if self.plank3.image == "" and self.plank3.self_vis == False:
            self.stick3.image = ""
            self.stick3.self_vis = False

        # if plank 3 gone stick 2 movable
        if self.plank3.image == "" and self.plank3.self_vis == False:
            self.stick2.click_and_drag()
        else:
            WIN.blit(self.stick2.image, (797, 490))

        # stick 2 logic
        if self.stick2.area.rect.collidepoint(pos) and self.stick2.clicked == True:
            if (
                self.stick2.rect.colliderect(self.plank1)
                and pygame.mouse.get_pressed()[0]
            ):
                self.plank1.image = ""
                self.plank1.self_vis = False

        # when plank 1 gone stick 2 dissapears
        if self.plank1.image == "" and self.plank1.self_vis == False:
            self.stick2.image = ""
            self.stick2.self_vis = False

        if self.plank1.image == "" and self.plank1.self_vis == False:
            self.plank_hit.draw()
            if self.mother.show_fader == True:
                self.plank_hit.draw()
                self.plank_hit.click_and_drag()

        # key appears from hole in tree
        if (self.stick2.image == "" and self.stick2.self_vis == False):
            self.tree.draw()
            if self.tree.clicked == True:
                self.key.draw()  # key is draw when the tree is clicked before the planks are gone
                self.key.click_and_drag()
         
        # key drags to lock, girl appears    
        if self.key.rect.colliderect(self.lock) and pygame.mouse.get_pressed()[0]:
            self.lock.image = ""
            self.lock.self_vis = False
            self.lock_sound.play_sound((386, 268))
            self.lock_sound == ""
            self.lock.rect.topleft = (0,0)
        
        # girl speaks
        if self.girl.show_fader == True:
            self.key.image = ""
            WIN.blit(self.girl.image, (560, 300))
            self.girl.draw()
            self.girl_speak.play_sound((560, 300))
            self.girl_speak.sound = ""
        
        # mother appears and speaks
        if self.mother.show_fader == True:
            WIN.blit(self.mother.image, (133, 199))
            self.mother_speak.play_sound((133, 199))
            self.mother_speak.sound = ""

        if self.plank_hit.rect.colliderect(self.mother) and pygame.mouse.get_pressed()[0] and self.mother.show_fader == True:
            self.plank_hit.image = ""
            self.plank_hit.self_vis = False
            self.mother.image = ROOM_8_MOTHER_HIT
            self.mother.rect.topleft = (132, 185)
            self.plank_hit_mother.play_sound((560, 300))
            self.plank_hit_mother.sound = ""
            # trying to find a way to keep text on screen longer
            self.text.text = "WOOHOOOO!"
            pygame.time.delay(3000)
            self.end_screen = True            
            
        if self.end_screen == True:
            self.plank_hit.image = ""
            self.plank_hit.self_vis = False
            self.girl.self_vis = True
        
        pygame.display.update()


class End():
    def __init__(self):
        self.has_collectable = False
        self.image = END
        self.start_items = []
        self.end_items = []
        self.all_items = []
        
    def play_room(self):
        WIN.blit(self.image, (0,0))
        
        pygame.display.update()


# initialise the classes
menu = MenuScreen()
room1 = Room1()
room2 = Room2()
room23 = Room23()
room3 = Room3()
room4 = Room4()
room5 = Room5()
room6 = Room6()
room7 = Room7()
you_lose = YouLose()
room8 = Room8()
end = End()


# decided which room to play and how to move between rooms
class GameState():
    
    def __init__(self):
        self.state = 'room5'
        
    def menu(self):
        menu.start_screen()
        
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        
        if menu.next_room == True:
            fade_in_and_out(WIDTH, HEIGHT, 'room1', self, menu, room1)
            self.state = 'room1'
        
    def room1(self):
        room1.play_room()
        
        if room1.next_room == True:
            fade_in_and_out(WIDTH, HEIGHT, 'room2', self, room1, room2)
            self.state = 'room2'
            
    def room2(self):
        room2.play_room()
        
        if room2.next_room == True:
            self.state = 'room23'
            
    def room23(self):
        room23.play_room()
        
        if room23.next_room == True:
            fade_in_and_out(WIDTH, HEIGHT, 'room3', self, room23, room3)
            self.state = 'room3'
            
            
    def room3(self):
        room3.play_room()
        
        if room3.next_room == True:
            fade_in_and_out(WIDTH, HEIGHT, 'room4', self, room3, room4)
            self.state = 'room4'
          
    def room4(self):
        room4.play_room()
        
        if room4.next_room == True:
            fade_in_and_out(WIDTH, HEIGHT, 'room5', self, room4, room5)
            self.state = 'room5'
    
    def room5(self):
        room5.play_room()
        
        if room5.next_room == True:
            fade_in_and_out(WIDTH, HEIGHT, 'room6', self, room5, room6)
            self.state = 'room6'
    
    def room6(self): 
        room6.play_room()
        
        if room6.next_room == True:
            fade_in_and_out(WIDTH, HEIGHT, 'room7', self, room6, room7)
            self.state = 'room7'
   
    def room7(self):   
        room7.play_room() 
        you_lose.back_room = False
        
        if room7.next_room == True:
            fade_in_and_out(WIDTH, HEIGHT, 'room8', self, room7, room8)
            self.state = 'room8'
            
        if room7.lose_screen == True:
            fade_in_and_out(WIDTH, HEIGHT, 'you_lose', self, room7, you_lose)
            self.state = 'you_lose'
            
    def you_lose(self):
        you_lose.play_room() 
        room7.lose_screen = False
        
        if you_lose.back_room == True:
            fade_in_and_out(WIDTH, HEIGHT, 'room7', self, you_lose, room7)
            self.state = 'room7'
            
    def room8(self):
        room8.play_room()
        
        if room8.end_screen == True:
            fade_in_and_out(WIDTH, HEIGHT, 'room8', self, room8, end)
            self.state = 'end'

    def end(self):
        end.play_room()
            
    # decides which room to show         
    def state_manager(self):
        if self.state == 'menu':
            self.menu()
        if self.state == 'room1':
            self.room1()
        if self.state == 'room2':
            self.room2()
        if self.state == 'room23':
            self.room23()     
        if self.state == 'room3':
            self.room3() 
        if self.state == 'room4':
            self.room4()
        if self.state == 'room5':
            self.room5()
        if self.state == 'room6':
            self.room6()
        if self.state == 'room7':
            self.room7()
        if self.state == 'you_lose':
            self.you_lose()
        if self.state == 'room8':
            self.room8()
        if self.state == 'end':
            self.end()

# run the whole game loop below
game_state = GameState()  
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)

    pos = pygame.mouse.get_pos()
    
    # only used during development, remove after
    if pygame.mouse.get_pressed()[0]:
        print(pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False      
            
    game_state.state_manager()
      
pygame.quit()
