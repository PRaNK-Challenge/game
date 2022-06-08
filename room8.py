import pygame

#settings
pygame.init()
pygame.font.init()
pygame.mixer.init(frequency=8000)

WIDTH, HEIGHT = 950,600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Private Eye")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0,0,0)
TRANSPARENT = (0,0,0,0)


ADVENTURE_FONT = pygame.font.SysFont('comicsans', 20)
NEXT_BUTTON = pygame.transform.scale(pygame.image.load('next_button.png'), (200,150)).convert_alpha()
TEXT_BOX = pygame.transform.scale(pygame.image.load('text_box.png'), (800, 140))

from clickable_classes import *

# Room 8 images
ROOM_8_BACKGROUND = pygame.transform.scale(pygame.image.load('forest.png'), (WIDTH, HEIGHT))
ROOM_8_Plank1 = pygame.transform.scale(pygame.image.load('plank18.png'), (120, 100))

# to help fade between scenes, used by rooms and items, change to what's visible at beginning
def redraw_window(room, items):
    WIN.blit(room.image, (0,0))
    for item in items:
        if item.self_vis == True:
            WIN.blit(item.image, (item.rect.topleft))     
            
# fade between scenes
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

class Room8():
    def __init__(self):
        self.image = ROOM_8_BACKGROUND
        self.next_room = False
        self.Plank1 = Clickable(self, 550, 340, ROOM_8_Plank1)
        self.text = Text("Hello.")
        #self.photo = Clickable()
        self.start_items = []
        self.end_items = []
        self.next_room = False
        
    def play_room(self):
        WIN.blit(self.image, (0,0))
        
        self.plank1.draw()
        
        if self.plank1.clicked == True:
            self.text.blit_text()
            
        #if x.clicked == True:
         #   self.text = Text("new writing")
        
        pygame.display.update()



# class Room8():
#     def __init__(self):
#         self.image = ROOM_8_BACKGROUND   
        
#     def play_room(self):
#         pass

# room8 = Room8()

# class GameState():
    
#     def __init__(self):
#         self.state = 'room8'
   
#     def room8(self):
        
#         room8.play_room()
        
#         if room8.next_room == True:
#             fade_in_and_out(WIDTH, HEIGHT, 'room2', self, room8, room8)
#             self.state = 'room8'
    
#     def room8(self):
#         pass
            
            
        
#     # decides which room to show         
#     def state_manager(self):
#         if self.state == 'menu':
#             self.menu()
#         if self.state == 'room1':
#             self.room1()
#         if self.state == 'room2':
#             self.room2()
#         if self.state == 'room23':
#             self.room23()     
#         if self.state == 'room3':
#             self.room3() 
#         if self.state == 'room4':
#             self.room4()
#         if self.state == 'room5':
#             self.room5()
#         if self.state == 'room7':
#             self.room7()
#         if self.state == 'room8':
#             self.room8()
#             #etc for all rooms    



# #run the whole game
# game_state = GameState()  

# clock = pygame.time.Clock()
# run = True
# while run:
#     clock.tick(FPS)

#     pos = pygame.mouse.get_pos()
    
#     if pygame.mouse.get_pressed()[0]:
#         pass
#         print(pos)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False      
            
#     game_state.state_manager()
      
# pygame.quit()

