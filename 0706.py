import pygame

#settings
pygame.init()
pygame.font.init()
pygame.mixer.init(frequency=8000)

WIDTH, HEIGHT = 950,600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

from clickable_classes import *

pygame.display.set_caption("Private Eye")

FPS = 144

WHITE = (255, 255, 255)
BLACK = (0,0,0)
TRANSPARENT = (0,0,0,0)
ADVENTURE_FONT = pygame.font.SysFont('arial', 20)

# Files for all rooms
ADVENTURE_FONT = pygame.font.SysFont('arial', 20)
NEXT_BUTTON = pygame.transform.scale(pygame.image.load('next_button.png'), (200,150)).convert_alpha()
TEXT_BOX = pygame.transform.scale(pygame.image.load('text_box.png'), (800, 140))

# Menu files
MENU_SCREEN = pygame.transform.scale(pygame.image.load('menu_screen.png'), (WIDTH, HEIGHT))
pygame.mixer.music.load('menu_music.mp3')

# Room 1 files
STUDY_ROOM = pygame.transform.scale(pygame.image.load('room1.png'), (WIDTH, HEIGHT))
PHONE = pygame.transform.scale(pygame.image.load('room1_phone.png'), (120,110))
TISSUES = pygame.transform.scale(pygame.image.load('room1_tissues.png'), (75,90))
KEY = pygame.transform.scale(pygame.image.load('room1_key.png'), (40,15))
MOTHER = pygame.transform.scale(pygame.image.load('room1_mother.png'), (220,290))
FOLDER = pygame.transform.scale(pygame.image.load('room1_folder.png'), (120, 100))
DRAWER_SHAPE = pygame.transform.scale(pygame.image.load('room1_drawer.png'), (220,100))
# Room 1 sounds
WOMAN = pygame.mixer.Sound('room1_woman.mp3')
MAN = pygame.mixer.Sound('room1_man.mp3')
PHONE_SOUND = pygame.mixer.Sound('phone-ringing.mp3')
PHONE_PICKUP = pygame.mixer.Sound('phone_pick_up.mp3')
DOOR_KNOCK = pygame.mixer.Sound('door_knock.mp3')
CRYING = pygame.mixer.Sound('room1_crying.mp3')

# Room 2 images
ROOM_2_BACKGROUND = pygame.transform.scale(pygame.image.load('room2.png'), (WIDTH, HEIGHT)).convert_alpha()
ROOM_2_NOTE = pygame.transform.scale(pygame.image.load('room2_note.png'), (18, 15)).convert_alpha()
ROOM_2_NOTE_ZOOM = pygame.transform.scale(pygame.image.load('room2_note_zoom.png'), (600, 550)).convert_alpha()
ROOM_2_TWINKLE = pygame.transform.scale(pygame.image.load('room2_twinkle.png'), (15, 25)).convert_alpha()
ROOM_2_KEY = pygame.transform.scale(pygame.image.load('room2_key.png'), (20, 25)).convert_alpha()
ROOM_2_DIARY = pygame.transform.scale(pygame.image.load('room2_diary.png'), (100, 70)).convert_alpha()
ROOM_2_CANDLE = pygame.transform.scale(pygame.image.load('room2_candle.png'), (30,80)).convert_alpha()

#for middle of rooms 2&3
ROOM_23_BACKGROUND = pygame.transform.scale(pygame.image.load('ROOM_23_BACKGROUND.jpg'), (WIDTH, HEIGHT)).convert_alpha()

# Room 3 images
ROOM_3_BACKGROUND = pygame.transform.scale(pygame.image.load('room3.png'), (WIDTH, HEIGHT))
ROOM_3_DIARY = pygame.transform.scale(pygame.image.load('room2_diary_zoom.png'), (700, 550)).convert_alpha()
ROOM_3_PEOPLE = pygame.transform.scale(pygame.image.load('room3_people.png'), (380, 285))
ROOM_3_CANDLE = pygame.transform.scale(pygame.image.load('room3_candle.png'), (120, 140))
ROOM_3_CARD = pygame.transform.scale(pygame.image.load('room3_card.png'), (50, 40))
ROOM_3_FILE = pygame.transform.scale(pygame.image.load('room3_file.png'), (100, 100))
ROOM_3_KEY = pygame.transform.scale(pygame.image.load('room3_key.png'), (40, 30))
ROOM_3_PHOTO = pygame.transform.scale(pygame.image.load('room3_photo.png'), (100, 100))
ROOM_3_PHOTO_FLIP = pygame.transform.scale(pygame.image.load('room3_photo_flip.png'), (80, 80))
# Room 3 sounds
ROOM_3_DAD = pygame.mixer.Sound('ROOM_3_DAD.mp3')
ROOM_3_MUM = pygame.mixer.Sound('ROOM_3_mum.mp3')
ROOM_3_DAUGHTER = pygame.mixer.Sound('ROOM_3_DAUGHTER.mp3')

# Room 4 images
ROOM_4_BACKGROUND = pygame.transform.scale(pygame.image.load('room4.png'), (WIDTH, HEIGHT))
ROOM_4_DRUNK = pygame.transform.scale(pygame.image.load('room4_drunk.png'), (350, 350))
ROOM_4_WATER = pygame.transform.scale(pygame.image.load('room4_water.png'), (50, 42))
ROOM_4_BOTTLE = pygame.transform.scale(pygame.image.load('room4_bottle.png'), (80, 50))
ROOM_4_FULL_BOTTLE = pygame.transform.scale(pygame.image.load('room4_full_bottle.png'), (65, 75))
ROOM_4_BAG = pygame.transform.scale(pygame.image.load('room4_bag.png'), (100, 150))
ROOM_4_OPEN_BAG = pygame.transform.scale(pygame.image.load('room4_open_bag.png'), (100, 150))
ROOM_4_SHINE = pygame.transform.scale(pygame.image.load('room4_shine.png'), (35, 35))
ROOM_4_NECKLACE = pygame.transform.scale(pygame.image.load('room4_necklace.png'), (120, 110)) 
# Room 4 sounds
ROOM_4_DRUNK_TALK = pygame.mixer.Sound('room4_drunk.mp3')
ROOM_4_DRUNK_TALK2 = pygame.mixer.Sound('room4_drunk2.mp3')

# Room 5 images
ROOM_5_BACKGROUND = pygame.transform.scale(pygame.image.load('room5.png'), (WIDTH, HEIGHT))
ROOM_5_MAN = pygame.transform.scale(pygame.image.load('room5_man.png'), (270, 450))
ROOM_5_ROCK = pygame.transform.scale(pygame.image.load('room5_rock.png'), (40, 35)) 
ROOM_5_LOCK = pygame.transform.scale(pygame.image.load('room5_lock.png'), (20, 30))
ROOM_5_KEYHOLE = pygame.transform.scale(pygame.image.load('room5_keyhole.png'), (10, 10))
ROOM_5_PLANT = pygame.transform.scale(pygame.image.load('room5_plant.png'), (220, 220))
ROOM_5_NOTE = pygame.transform.scale(pygame.image.load('room5_note.png'), (300, 450))
ROOM_5_KEY = pygame.transform.scale(pygame.image.load('room5_key.png'), (50, 30))
# Room 5 sounds
ROOM_5_CAR = pygame.mixer.Sound('room5_car.mp3')    
ROOM_5_CAR2 = pygame.mixer.Sound('room5_car2.mp3')    
ROOM_5_MAN_SPEAK = pygame.mixer.Sound('room5_man.mp3')  
ROOM_5_SMASH = pygame.mixer.Sound('room5_smash.mp3')

# Room 6 images
ROOM_6_BACKGROUND = pygame.transform.scale(pygame.image.load('room6.png'), (WIDTH, HEIGHT))
ROOM_6_DRINK = pygame.transform.scale(pygame.image.load('room6_drink.png'), (30, 30))
ROOM_6_VIP = pygame.transform.scale(pygame.image.load('room6_vip.png'), (70, 50))
ROOM_6_VIP_GONE = pygame.transform.scale(pygame.image.load('room6_vip_gone.png'), (70, 50))
ROOM_6_ROPE = pygame.transform.scale(pygame.image.load('room6_rope.png'), (380, 250))
ROOM_6_VIP_MAN = pygame.transform.scale(pygame.image.load('room6_vip_man.png'), (80, 250))
ROOM_6_THUGS = pygame.transform.scale(pygame.image.load('room6_thugs.png'), (350, 270))
ROOM_6_BOUNCER = pygame.transform.scale(pygame.image.load('room6_bouncer.png'), (250, HEIGHT-20))
ROOM_6_BAT = pygame.transform.scale(pygame.image.load('room6_bat.png'), (65, 120))
ROOM_6_BAT_TURN = pygame.transform.scale(pygame.image.load('room6_bat_turn.png'), (65, 120))
ROOM_6_WINDOW = pygame.transform.scale(pygame.image.load('room6_window.png'), (120, 45))
ROOM_6_WINDOW_BROKEN = pygame.transform.scale(pygame.image.load('room6_window_broken.png'), (120, 45))        
# Room 6 sounds
ROOM_6_VIP_MAN_SPEAK = pygame.mixer.Sound('room6_vip_man_speak.mp3')
ROOM_6_THUG_SPEAK = pygame.mixer.Sound('room6_thugs_speak.mp3')
ROOM_6_WINDOW_SMASH = pygame.mixer.Sound('room6_window.mp3')

# Room 7 images
ROOM_7_BACKGROUND = pygame.transform.scale(pygame.image.load('office7.png'), (WIDTH, HEIGHT))
ROOM_7_NECKLACE = pygame.transform.scale(pygame.image.load('necklacesmall7.png'), (75, 60))
ROOM_7_NECKLACE_ZOOM = pygame.transform.scale(pygame.image.load('necklacezoom7.png'), (450, 450))
ROOM_7_POSTER = pygame.transform.scale(pygame.image.load('postersmall7.png'), (180, 65))
ROOM_7_POSTER_ZOOM = pygame.transform.scale(pygame.image.load('posterzoom7.png'), (350, 450))
ROOM_7_PHOTO = pygame.transform.scale(pygame.image.load('picsmall7.png'), (100, 80))
ROOM_7_PHOTO_ZOOM = pygame.transform.scale(pygame.image.load('piczoom7.png'), (650, 400))
ROOM_7_FOLDER = pygame.transform.scale(pygame.image.load('foldersmall7.png'), (100, 60))
ROOM_7_FOLDER_ZOOM = pygame.transform.scale(pygame.image.load('folderzoom7.png'), (550, 450))
ROOM_7_DIARY = pygame.transform.scale(pygame.image.load('diarysmall7.png'), (100, 60))
ROOM_7_DIARY_ZOOM = pygame.transform.scale(pygame.image.load('diaryzoom7.png'), (550, 400))
ROOM_7_FILE_ZOOM = pygame.transform.scale(pygame.image.load('room3_file.png'), (500, 500))
GUESS_BOX = pygame.transform.scale(pygame.image.load('text_box.png'), (270, 150))

# You lose images
YOU_LOSE = pygame.transform.scale(pygame.image.load('you_lose.png'), (WIDTH, HEIGHT))
TRY_AGAIN = pygame.transform.scale(pygame.image.load('tryagain.png'), (800, 200))

# Room 8 images
ROOM_8_BACKGROUND = pygame.transform.scale(pygame.image.load('room8.png'), (WIDTH, HEIGHT))
ROOM_8_PLANK1 = pygame.transform.scale(pygame.image.load('plank18.png'), (250, 170))
ROOM_8_PLANK2 = pygame.transform.scale(pygame.image.load('plank28.png'), (250, 140))
ROOM_8_PLANK3 = pygame.transform.scale(pygame.image.load('plank38.png'), (250, 140))
ROOM_8_STICK1 = pygame.transform.scale(pygame.image.load('stick18.png'), (150, 95))
ROOM_8_STICK2 = pygame.transform.scale(pygame.image.load('stick28.png'), (150, 150))
ROOM_8_STICK3 = pygame.transform.scale(pygame.image.load('stick38.png'), (250, 100))
ROOM_8_KEY = pygame.transform.scale(pygame.image.load('key8.png'), (100, 50))
ROOM_8_TREE = pygame.transform.scale(pygame.image.load('tree8.png'), (30, 50))
ROOM_8_GRASS = pygame.transform.scale(pygame.image.load('grass8.png'), (80, 25))
ROOM_8_LOCK = pygame.transform.scale(pygame.image.load('lock8.png'), (25, 25))
# Room 8 sounds

# Ending images
END = pygame.transform.scale(pygame.image.load('good.png'), (WIDTH, HEIGHT))

# to help fade between scenes, used by rooms and items, change to what's visible at beginning
def redraw_window(room, items):
    WIN.blit(room.image, (0,0))
    for item in items:
        if item.self_vis == True:
            WIN.blit(item.image, (item.rect.topleft))     
            
# fade between scenes - CAN I REMOVE THIS
def fade_in_and_out(width, height, state, room, current_room, next_room): 
    
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    
    for alpha in range(255):
        fade.set_alpha(alpha)
        redraw_window(current_room, current_room.end_items)
        WIN.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(1)
        
    # change to next room    
    room.state = state
                
    for alpha in range (255): 
        fade.set_alpha(255-alpha)
        redraw_window(next_room, next_room.start_items)
        WIN.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(1)

# initialise the rooms
class MenuScreen():
    def __init__(self):
        self.image = MENU_SCREEN
        self.next_room = False
        self.end_items= []
        
    def start_screen(self):

        WIN.blit(self.image, (0,0))
        
        pygame.mixer.music.load("menu_music.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(loops=-1)
        
        if pygame.mouse.get_pressed()[0]:
            self.next_room = True
          
        pygame.display.update()    
     
class Room1():
    def __init__(self):        
        self.image = STUDY_ROOM
        self.cooldown = 5000
        self.last = pygame.time.get_ticks()
        self.next_room = False
        self.drawer = pygame.draw.rect(WIN, TRANSPARENT, (320,570,50,50))
        self.collect_folder = CollectableClue(self, 246, 409, FOLDER, 15, HEIGHT - 100)
        self.text = Text("She seems too upset to speak.                                                      Maybe I should give her some tissues and she'll be able to tell us about the case?", "top")
        self.mother = FadeIn(self, 105, 132, MOTHER)
        self.phone = Clickable(self, 620, 290, PHONE)
        self.phone_call = AudioClue(self, self.phone, PHONE_PICKUP, 1000, False, MAN, DOOR_KNOCK, self.mother.fade_in, fourth_sound=CRYING)
        self.click_tissues = Clickable(self, 361, 317, TISSUES)
        self.mother_speech = AudioClue(self, self.click_tissues, WOMAN, 100, False)
        self.drag_key = DraggableClue(self, KEY, 380, 385, True, area=self.drawer)
        self.start_items = [self.drag_key, self.phone, self.click_tissues, self.collect_folder]
        self.end_items = [self.drag_key, self.phone, self.mother, self.click_tissues]
        self.current_items = [self.drag_key, self.phone, self.mother, self.click_tissues]

    def play_room(self):

        WIN.blit(self.image, (0, 0))
        self.phone.draw()
        
        items = self.start_items + self.end_items
        clicked_items = list(set([item for item in items if item is not self and isinstance(item, DraggableClue) and item.clicked == True]))
        
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
                self.text.blit_text()
                
        # give tissues to mother, mother speaks 
        if self.click_tissues.clicked == True:
            self.phone_call.fourth_sound.stop()
            self.click_tissues.rect.topleft = (214, 262) #this moves it to her hands
            self.mother_speech.play_sound((214, 262))
            self.mother_speech.sound = ""
        
        # key is revealed, can be moved
        if self.phone.clicked == True and self.click_tissues.clicked == True:
            self.text = Text("Oh good, that seems to have helped her.                                                                                                                          Ah! There's the key to the drawer! Let's get that casefile.", "top")
            self.drag_key.draw()
            if isinstance(self.drag_key, DraggableClue):
                self.drag_key.click_and_drag()
        
        # reveal the folder once key reaches drawer
        if self.drag_key.rect.colliderect(self.drawer):
            self.collect_folder.self_vis = True
            self.drag_key.rect.topleft = (190, 410)
            self.drag_key = Clickable(self, 190, 410, KEY)
        
        if not isinstance(self.drag_key, DraggableClue):
            self.collect_folder.draw()
            self.collect_folder.self_vis = True
        
        # collect the folder and put in inventory before going to next room
        if self.collect_folder.clicked == True:
            self.collect_folder.collect()
            self.collect_folder.rect.x = self.collect_folder.next_x
            self.collect_folder.rect.y = self.collect_folder.next_y
            self.text.text = "Time to go and see what clues we can find in her daughter's bedroom..."
    
        if self.collect_folder.next_room_button.clicked == True:
            self.next_room = True
                   
        pygame.display.update()  
        

class Room2():
    def __init__(self):
        self.image = ROOM_2_BACKGROUND
        self.note_zoom = ROOM_2_NOTE_ZOOM
        self.diary = CollectableClue(self, 40, 355, ROOM_2_DIARY, 15, HEIGHT - 100)
        self.twinkle = DraggableClue(self, ROOM_2_TWINKLE, 640, 552, True, area=self.diary)
        self.text = Text("Okay, where to look first? Hmm, those posters seems quite interesting. Oh! I've heard of magic ink before! You hold the note over heat and the ink becomes visible!", "top")
        self.candle = ZoomableClue(self, 656, 243, ROOM_2_CANDLE, self.note_zoom, 150, 20)
        self.key = ROOM_2_KEY
        self.note = DraggableClue(self, ROOM_2_NOTE, 900, 490, True, area=self.candle)
        self.next_room = False
        self.start_items = [self.candle, self.diary, self.note, self.twinkle]
        self.end_items = [self.candle, self.note, self.twinkle]
    
    def play_room(self):
        WIN.blit(self.image, (0,0))

        pos = pygame.mouse.get_pos()
        
        clicked_items = [item for item in self.end_items if item is not self and isinstance(item, DraggableClue) and item.clicked == True]
        
        self.twinkle.draw()
        self.candle.draw()
        self.note.draw()
        self.note.click_and_drag()
        self.diary.self_vis = True
        self.diary.draw()
        self.diary.collect()
        
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
            self.diary.rect.x = self.diary.next_x
            self.diary.rect.y = self.diary.next_y
            self.twinkle.draw()
            self.twinkle.rect.topleft = (50, 525)
         
        if self.diary.next_room_button.clicked == True:
            self.next_room = True
    
        pygame.display.update()

class Room23():
    def __init__(self):
        self.image = ROOM_23_BACKGROUND
        self.diary = Clickable(self, 120, 10, ROOM_3_DIARY)
        self.next_room = False
        self.start_items = [self.diary]
        self.end_items = [self.diary]
        
    def play_room(self):
        WIN.blit(self.image, (0,0))
        pos = pygame.mouse.get_pos()
        
        self.diary.draw()
        
        if pygame.mouse.get_pressed()[0] and self.diary.rect.collidepoint(pos):
            self.next_room = True
           
        pygame.display.update()    

class Room3():
    def __init__(self):
        self.image = ROOM_3_BACKGROUND
        self.candle = Clickable(self, 590, 350, ROOM_3_CANDLE)
        self.photo = CollectableClue(self, 70, 140, ROOM_3_PHOTO, 700, 250)
        self.file = CollectableClue(self, 850, 280, ROOM_3_FILE, 15, HEIGHT - 100)
        self.people = Clickable(self, 570, 107, ROOM_3_PEOPLE)
        self.peoplespeak = AudioClue(self, self.people, ROOM_3_DAD, 1500, False, ROOM_3_MUM)
        self.daughterspeak = AudioClue(self, self.people, ROOM_3_DAUGHTER, 300, False)
        self.drawer = pygame.draw.rect(WIN, TRANSPARENT, (90,250,80,80))
        self.card = DraggableClue(self, ROOM_3_CARD, 600, 400, True, area=self.drawer)
        self.start_items = [self.candle, self.people]
        self.end_items = [self.candle, self.people, self.photo, self.card]
        self.multiline_text = Text("It seems from what she wrote in her diary her friend might know something... Let's see if she'll help.", "top")
        self.next_room = False
        
    def play_room(self):
        WIN.blit(self.image, (0,0))
        pos = pygame.mouse.get_pos()
        self.candle.draw()
        self.photo.draw()
        self.file.draw()
        self.people.draw()
        self.multiline_text.blit_text()
        
        # click the family, dad and mum speak
        if self.people.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.peoplespeak.play_sound((self.peoplespeak.item.rect.topleft))
            self.peoplespeak.sound = ""
            
        if self.peoplespeak.sound == "":
            self.multiline_text = Text("Hmm, well they won't be much help. What did the daughter shove in the drawer just before I came in? It's locked, maybe the key card is around here...", "top")
         
        # click the candle, it moves to the side - SORT OUT?
        if self.candle.clicked == True and self.peoplespeak.sound == "":
            self.candle.rect.topleft = (520,350)
            self.card.draw()
            self.card.click_and_drag()
            
        # take the card to the drawers, the photo appears
        if self.card.rect.colliderect(self.drawer): 
            self.card.rect.topleft = (520, 350)
            self.photo.self_vis = True
        
        # switch the photo image round so it fits in daughter's hands    
        if self.photo.clicked == True:
            self.photo.draw()
            self.photo.image = ROOM_3_PHOTO_FLIP
            self.photo.rect.x = self.photo.next_x
            self.photo.rect.y = self.photo.next_y
        
        # click the photo, goes to girl who speaks
        if self.photo.rect.topleft == (self.photo.next_x, self.photo.next_y):
            self.multiline_text = Text("So are you sure you don't know anything at all?                                 Then who's this boy with you in the photo?                                     And what's that file your father has?", "bottom")
            self.daughterspeak.play_sound(self.daughterspeak.item.rect.topleft)
            self.daughterspeak.sound = ""
            self.file.self_vis = True
            self.file.collect()
            
        # grab the file
        if self.file.clicked == True:
            self.file.draw()
            self.file.rect.x = self.file.next_x
            self.file.rect.y = self.file.next_y
        
        if self.file.rect.topleft == (self.file.next_x, self.file.next_y):
            self.file.collect()
            self.multiline_text = Text("It looks like the father collected information on this boy, Tom, he must have been concerned too! Let's see if we can find that boy at that alleyway Emma mentioned.", "top")
        
        if self.file.next_room_button.clicked == True:
            self.next_room = True
        
        pygame.display.update()
     

class Room4():
    def __init__(self):
        self.image = ROOM_4_BACKGROUND   
        self.drunk = Clickable(self, 250, 225, ROOM_4_DRUNK)
        self.drunk_talk = AudioClue(self, self.drunk, ROOM_4_DRUNK_TALK, 1500, False)
        self.drunk_head = pygame.draw.rect(WIN, TRANSPARENT, (300,250,50,50))
        self.drunk_talk2 = AudioClue(self, self.drunk, ROOM_4_DRUNK_TALK2, 500, False)
        self.water = Clickable(self, 898, 415, ROOM_4_WATER)
        self.bottle = DraggableClue(self, ROOM_4_BOTTLE, 70, 480, True, area=self.water)
        self.full_bottle = ROOM_4_FULL_BOTTLE
        self.bag = Clickable(self, 543, 170, ROOM_4_BAG)
        self.open_bag = ROOM_4_OPEN_BAG
        self.shine = ROOM_4_SHINE
        self.necklace = CollectableClue(self, 600, 355, ROOM_4_NECKLACE, 15, HEIGHT - 105)
        self.multiline_text = Text("Well, Tom doesn't seem to be anywhere around here.                                   I wonder if this man has seen him...", "top")
        self.next_room = False
        self.start_items = [self.drunk, self.bottle, self.bag]
        self.end_items = [self.drunk, self.bottle, self.bag]
        
    def play_room(self):
        WIN.blit(self.image, (0,0))
        
        self.bag.draw()
        self.bottle.click_and_drag()
        self.drunk.draw()
        self.bottle.draw()
        self.multiline_text.blit_text()
        
        # click the drunk who talks
        if self.drunk.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.multiline_text.remove_text()
            self.drunk_talk.play_sound(self.drunk_talk.item.rect.topleft)
            self.drunk_talk.sound = ""
        
        # take the bottle to the water and fill it
        if self.bottle.rect.colliderect(self.water):
            self.water.draw()
            self.bottle.draw()
            self.bottle.image = self.full_bottle
        
        # give to drunk who then talks
        if self.bottle.rect.colliderect(self.drunk_head) and self.bottle.image == self.full_bottle:
            self.bottle.rect.topleft = (280, 450)
            self.drunk_talk2.play_sound(self.drunk_talk2.item.rect.topleft)
            self.drunk_talk2.sound = ""
        
        # open the bag, necklace fall on floor, collect it
        if self.bag.clicked == True and self.bottle.image == self.full_bottle:
            self.bag.image = self.open_bag  
        
        if self.bag.image == self.open_bag:
            self.necklace.self_vis = True
            self.necklace.draw()
            self.multiline_text = Text("This looks like a lady's necklace, could it be that's the one Tom gave to Sara? And on the back there's an address. Why would he try to get rid of it, maybe they had a fight?", "top")
            
        if self.necklace.clicked == True:
            self.necklace.collect()
            self.necklace.rect.x = self.necklace.next_x
            self.necklace.rect.y = self.necklace.next_y
            self.multiline_text = Text("Let's go check out that address and see if he will be there.", "top")
            
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
        self.keyhole = Clickable(self, 585, 200, ROOM_5_KEYHOLE)
        self.key = DraggableClue(self, ROOM_5_KEY, 730, 475, True, area= self.keyhole)
        self.car = AudioClue(self, self.keyhole, ROOM_5_CAR2, 0, True, ROOM_5_CAR, func=self.man.fade_in)
        self.smash = AudioClue(self, self.lock, ROOM_5_SMASH, 50, True)
        self.poster = CollectableClue(self, 350, 5, ROOM_5_NOTE, 25, HEIGHT - 115, size=(55, 80))
        self.lock_space = pygame.draw.rect(WIN, TRANSPARENT, (238,200,30,30))
        self.next_room = False
        self.multiline_text = Text("Looks like there's no one home. Nothing wrong with having a little look around though. Might be worth trying to get some clues.", "top")
        self.start_items = [self.key, self.plant, self.lock, self.rock, self.keyhole]
        self.end_items = [self.plant, self.rock, self.keyhole, self.key]
        self.current_items = [self.plant, self.rock, self.keyhole, self.key, self.lock]

    def play_room(self):
        WIN.blit(self.image, (0,0))
        
        self.plant.draw()
        self.keyhole.draw()
        self.lock.draw()
        self.rock.draw()
        self.multiline_text.blit_text()
        
        # move plant, collect key, take to door, man arrives
        if self.plant.clicked == True:
            self.multiline_text.remove_text()
            self.plant.rect.topleft = (750, 290)
            self.key.draw()
            if isinstance(self.key, DraggableClue):
                self.key.click_and_drag()
        
        # father arrives home as you try to enter
        if self.key.rect.colliderect(self.keyhole):
            self.key = Clickable(self, 730, 475, ROOM_5_KEY)
            self.key.rect.topleft=(730, 475)
            self.car.play_sound((585, 200))
            self.car.sound = ""
            self.man_speak.play_sound(self.man.rect.topleft)
            self.man_speak.sound = ""
            pygame.time.delay(5000)
            self.man.image == ""
            self.man.self_vis = False
            self.man.fade_out()
        
        if self.man_speak.sound == "":
            self.multiline_text = Text("Looks like I'll need some way of breaking in to the garage! That lock doesn't look sturdy, with a little force it should open.", "top")
            if isinstance(self.rock, DraggableClue):
                self.rock.click_and_drag()
        
        # grab rock, smash lock
        if self.rock.rect.colliderect(self.lock):
            self.rock = Clickable(self, 640, 455, ROOM_5_ROCK)
            self.smash.play_sound((244, 200))
            self.smash.sound = ""
            self.lock.image = ""
            self.multiline_text.remove_text()
        
        # collect the poster clue
        pos = pygame.mouse.get_pos()
        if self.lock.image == "":    
            self.poster.draw()
            if self.lock_space.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                self.poster.self_vis = True
        
        if self.poster.self_vis == True:
            self.multiline_text = Text("Poster about a club... And today the members are meeting up. Guess I am gonna go clubbing tonight...", "top")
        
        if self.poster.clicked == True:
            self.poster.collect()
            self.poster.rect.x = self.poster.next_x
            self.poster.rect.y = self.poster.next_y
            
        if self.poster.next_room_button.clicked == True:
            self.next_room = True
        
        pygame.display.update()

class Room6():
    def __init__(self):
        self.image = ROOM_6_BACKGROUND  
        self.vip_man = Clickable(self, 400, 60,  ROOM_6_VIP_MAN)
        self.bouncer = FadeIn(self, 700, 20, ROOM_6_BOUNCER)
        self.drink = DraggableClue(self, ROOM_6_DRINK, 75, 210, True, area=self.vip_man)
        self.vip = DraggableClue(self, ROOM_6_VIP, 310, 50, True, area=self.bouncer)
        self.rope = Clickable(self, 525, 165, ROOM_6_ROPE)
        self.thugs = Clickable(self, 545, 100, ROOM_6_THUGS)
        self.window = Clickable(self, 570, 15, ROOM_6_WINDOW)
        self.window_smash = AudioClue(self, self.drink, ROOM_5_SMASH, 100, True)
        self.bat = DraggableClue(self, ROOM_6_BAT, 470, 230, True, area=self.window)
        self.text = Text("Those guys in the VIP section must be the club members. But how do I get in with this bouncer keeping an eye?", "top")
        self.vip_man_speak = AudioClue(self, self.vip_man, ROOM_6_VIP_MAN_SPEAK, 0, True)
        self.thug_speak = AudioClue(self, self.thugs, ROOM_6_THUG_SPEAK, 0, True)
        self.next_room_button = Clickable(self, WIDTH - 200, HEIGHT - 150, NEXT_BUTTON)
        self.next_room = False
        self.start_items =[self.vip_man, self.thugs, self.rope, self.bouncer, self.drink, self.window, self.bat]
        self.end_items =[self.vip_man, self.window, self.thugs, self.bat, self.vip]
        self.current_items = [self.vip_man, self.window, self.bat, self.thugs, self.rope, self.vip, self.drink]
        
    def play_room(self):
        WIN.blit(self.image, (0,0))
        WIN.blit(ROOM_6_THUGS, (545, 100))
        
        self.window.draw()
        self.vip_man.draw()
        self.rope.draw()
        self.bouncer.draw()
        self.bat.draw()
        self.drink.draw()
        self.text.blit_text()
        self.drink.click_and_drag()            
        
        clicked_items = list(set([item for item in self.current_items if item is not self and isinstance(item, DraggableClue) and item.clicked == True]))
        # speak to man to get vip ticket
        if self.vip_man.clicked == True:
            self.vip_man_speak.play_sound((400, 60))
            self.vip_man_speak.sound = ""
            self.text.text = "Ok, guess I will be spending some money tonight..."
            
        # give man drink    
        if self.drink.rect.colliderect(self.vip_man):
            WIN.blit(ROOM_6_DRINK, (430, 130))
            self.drink.rect.topleft = (430, 130)
            self.vip.draw()
            self.vip.click_and_drag()
            
        # give vip ticket to bouncer who disappears
        if self.vip.rect.colliderect(self.bouncer):
            self.vip.draw()
            self.vip.image == ROOM_6_VIP_GONE
            self.vip.rect.topleft = (725,35)
            self.bouncer.fade_out()
            self.bouncer.self_vis = False
            self.bouncer.image = ""
            self.drink.image = ""
            
        if self.bouncer.image == "" and self.bouncer.self_vis == False:
            self.text.remove_text()
            self.vip.self_vis = False
            self.thugs.draw()
            self.rope.draw()
            self.bat.draw()
        
        # remove rope and speak to Tom's gang
        if self.rope.clicked == True and self.vip.rect.topleft == (725,35):
            self.rope.image = ""
            self.text.text = "Excuse me, I'm looking for a guy named Tom. Have you seen him?"
            
        if self.thugs.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] and self.vip.rect.topleft == (725,35):
            self.thug_speak.play_sound((545, 100))
            self.thug_speak.sound = ""
            
        if self.thug_speak.sound == "" and isinstance(self.bat, DraggableClue):
            self.text.remove_text()
            self.bat.click_and_drag()

        #smash the window and leave
        if self.bat.clicked == True:
            self.text.text = "Uh-oh, looks like I better get out of here and fast!"
            self.bat.image = ROOM_6_BAT_TURN
        
        if self.bat.rect.colliderect(self.window) and pygame.mouse.get_pressed()[0]:
            self.window.image = ROOM_6_WINDOW_BROKEN
            self.bat.image = ROOM_6_BAT
            self.window_smash.play_sound((430, 130))
            self.bat.rect.topleft = (650, 180)
            self.bat = Clickable(self, 650, 180, ROOM_6_BAT)
            self.window_smash.sound == ""
            
        if self.window.image == ROOM_6_WINDOW_BROKEN:
            self.text.text = "Uh-oh, looks like I better get out of here and fast!"
            self.next_room_button.draw()
            
        if self.next_room_button.clicked == True:
            self.next_room = True
               
        pygame.display.update()
       
class Room7():
    def __init__(self):
        self.image = ROOM_7_BACKGROUND
        self.necklace_text = Text("Tom gave her a necklace with his address on it, who knows why he'd want her to go there, seems like he had a rough family dynamic.", "bottom")
        self.file_text = Text("Her friend's father was gathering information on Tom which is a bit much, but seems like he didn't actually find a lot to be worried about, he's just a kid.", "bottom")
        self.photo_text = Text("So, we know she was friends with Tom, but all the parents thought he was trouble.", "bottom")
        self.poster_text = Text("We didn't find him at the club with his gang, which could be a good sign. But it seems he ran with a rough crowd, I wouldn't trust them.", "bottom")
        self.diary_text = Text("We know from her diary her mother was overprotective of her and would do anything to keep her away from Tom.", "bottom")
        self.final_text = Text("Now that I'm looking at all of this, I think it's pretty obvious who knows where she is!", "bottom")
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
        self.guess1 = Clickable(self, 160, 30, GUESS_BOX)
        self.guess2 = Clickable(self, 500, 30, GUESS_BOX)
        self.guess3 = Clickable(self, 160, 165, GUESS_BOX)
        self.guess4 = Clickable(self, 500, 165, GUESS_BOX)
        self.start_items = [self.necklace, self.photo, self.folder, self.file, self.diary, self.poster]
        self.end_items = [self.necklace, self.photo, self.folder, self.file, self.diary, self.poster]
        self.next_room = False
        self.lose_screen = False
        
    def play_room(self):
        WIN.blit(self.image, (0,0))
        
        self.poster.draw()
        self.necklace.draw()
        self.photo.draw()
        self.folder.draw()
        self.diary.draw()
        self.file.draw()
        
        pos = pygame.mouse.get_pos()
        
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
            if self.folder.clicked == True:
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
        self.back_room = False
        self.try_again = Clickable(self, 80, 370, TRY_AGAIN)
        self.start_items = []
        self.end_items = []
        
    def play_room(self):
        WIN.blit(self.image, (0,0)) 

        self.try_again.draw()
        
        if pygame.mouse.get_pressed()[0] and self.try_again.rect.collidepoint(pos):
            self.back_room = True
        
        pygame.display.update()


class Room8():
    def __init__(self):
        self.image = ROOM_8_BACKGROUND  
        self.plank1 = Clickable(self, 335, 265, ROOM_8_PLANK1)
        self.plank2 = Clickable(self, 340, 280, ROOM_8_PLANK2)
        self.plank3 = Clickable(self, 335, 120, ROOM_8_PLANK3)
        self.stick1 = Clickable(self, 330, 510, ROOM_8_STICK1)
        self.stick2 = Clickable(self, 800, 430, ROOM_8_STICK2)
        self.stick3 = Clickable(self, 560, 480, ROOM_8_STICK3)
        self.lock = Clickable(self, 380, 272, ROOM_8_LOCK)
        self.key = DraggableClue(self, ROOM_8_KEY, 270, 190, True, area=self.lock)
        self.tree = Clickable(self, 230, 175, ROOM_8_TREE)
        self.grass1 = Clickable(self, 380, 540, ROOM_8_GRASS)
        self.grass2 = Clickable(self, 630, 530, ROOM_8_GRASS)
        self.grass3 = Clickable(self, 835, 500, ROOM_8_GRASS)
        self.girl = FadeIn(self, 700, 20, ROOM_6_BOUNCER)
        #self.girl_talk - AudioClue() e.g. AudioClue(self, self.drink, ROOM_5_SMASH, 100, True) - copy people_speak from room3 if you want two people to speak after each other
        self.text = Text("", "bottom")
        self.start_items = []
        self.end_items = []
        self.current_items = []
        self.next_room = []
        self.next_room = False
        
    def play_room(self):
        WIN.blit(self.image, (0,0))
        
        self.lock.draw()
        self.plank1.draw()
        self.plank2.draw()
        self.plank3.draw()
        self.tree.draw()
        self.stick1.draw()
        self.stick2.draw()
        self.stick3.draw()
        self.grass1.draw()
        self.grass2.draw()
        self.grass3.draw()
        #self.girl.draw() after she's faded in
        
        self.text.blit_text()
        # self.text.text = "whatever"
        
        if self.key.rect.colliderect(self.lock) and pygame.mouse.get_pressed()[0]:
            self.lock.image = ""
            self.lock.self_vis = False
            self.key.image = ""
            self.key.self_vis = False
          
        if self.tree.clicked == True: # logic so they can't click if the planks' images aren't ""
            self.key.draw()
            self.key.click_and_drag()    
        # if key and lock self_vis = False and images = "":
        # girl fades in
        
        #once the game is complete, should be a button (can be next button) which if clicked self.next_room = True
        
        pygame.display.update()

class End():
    def __init__(self):
        self.image = END
        self.start_items = []
        self.end_items = []
        
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
        self.state = 'room8'
        
    def menu(self):
        
        menu.start_screen()
        
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
            fade_in_and_out(WIDTH, HEIGHT, 'room3', self, room2, room23)
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
            self.state = 'end'
            
        if room7.lose_screen == True:
            fade_in_and_out(WIDTH, HEIGHT, 'you_lose', self, room7, you_lose)
            self.state = 'you_lose'
            
    def you_lose(self):
        
        you_lose.play_room()
        
        room7.lose_screen = False
        
        if you_lose.back_room == True:
            fade_in_and_out(WIDTH, HEIGHT, 'room2', self, you_lose, room7)
            self.state = 'room7'
            
    def room8(self):
        
        room8.play_room()
        
        if room8.next_room == True:
            fade_in_and_out(WIDTH, HEIGHT, 'room2', self, room8, end)
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
    
    if pygame.mouse.get_pressed()[0]:
        print(pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False      
            
    game_state.state_manager()
      
pygame.quit()

