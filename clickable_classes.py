import pygame

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
NEXT_BUTTON = pygame.transform.scale(pygame.image.load('next_button.png'), (70,70)).convert_alpha()

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
        redraw_window(current_room, current_room.items)
        WIN.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(1)
        
    # change to next room    
    room.state = state
                
    for alpha in range (255): 
        fade.set_alpha(255-alpha)
        redraw_window(next_room, next_room.items)
        WIN.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(1)

# for putting text on screen
class Text():
    def __init__(self, text):
        self.text = text
        self.self_vis = False
        
    def draw_text(self):
        display_text = ADVENTURE_FONT.render(
                self.text, 1, WHITE)
        WIN.blit(display_text, (WIDTH/2 - 200, HEIGHT - 100))
        pygame.display.update()
        
    def remove_text(self):
        self.text = ""
        
        
# Parent class for drawing images on screen and checking if they've been clicked
class Clickable():
    def __init__(self, room, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x
        self.y= y
        self.rect.topleft = (x, y)
        self.clicked = False
        self.room = room
        self.self_vis = True
    
    def draw(self):
        if self.self_vis == True:
            WIN.blit(self.image, (self.rect.x, self.rect.y))       
            pos = pygame.mouse.get_pos()
            
            clicked_items = [item for item in self.room.items if item is not self and isinstance(item, DraggableClue) and item.clicked == True]

            if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] and len(clicked_items) == 0:
                self.clicked=True

# item that fades into the room
class FadeIn(Clickable):
    def __init__(self, room, x, y, image):
        super().__init__(room, x, y, image)
        self.show_fader = False
        
    def fade_in(self):
        for alpha in range(256):
            self.image.set_alpha(alpha)
            redraw_window(self.room, self.room.items)
            WIN.blit(self.image, (self.rect.topleft))
            pygame.display.update()
        if alpha == 255:
            self.show_fader = True


class AudioClue():
    def __init__(self, room, item, sound, pause, second_sound="", third_sound="", func=""):
        self.room = room
        self.item = item
        self.sound = sound
        self.second_sound = second_sound
        self.third_sound = third_sound
        self.pause = pause
        self.func = func
        self.arrived = False
        self.third_sound = third_sound
        self.sound_length = int(self.sound.get_length())
        if self.second_sound != "":
            self.second_sound_length = int(self.second_sound.get_length())
        if self.third_sound != "":
            self.third_sound_length = int(self.third_sound.get_length())
     
    def carry_out_func(self):
        # if you need to carry out a function once the sound stops
        if self.func == "":
            pass
        else:
            self.func()
        
    def play_sound(self, topleft):        
        # this will stop the sound playing more than once
        if self.sound != "":

            if self.item.rect.collidepoint(topleft) and pygame.mouse.get_pressed()[0] and self.item.rect.topleft == topleft:           
                if self.second_sound == "":
                    pygame.time.delay(self.pause)
                    self.sound.play()
                    self.carry_out_func()
                
                else:
                    self.sound.play()
                    pygame.time.delay(self.pause)
                    self.second_sound.play()
                    pygame.time.delay(self.second_sound_length + 3000)
                    #pass a function that can be called once the sound has finished
                    if self.third_sound == "":
                        pass
                    else:
                        # make more generic, or a variable
                        pygame.time.delay(self.second_sound_length + 9500)
                        self.third_sound.play()
                        pygame.time.delay(self.third_sound_length + 3000)
                        self.carry_out_func()
                    
                 
# Child class, a clickable item that can be collected, final clue before next room
class CollectableClue(Clickable):
    def __init__(self, room, x, y, image, next_x, next_y):
        super().__init__(room, x, y, image)
        self.next_room_button = Clickable(room, WIDTH - 100, HEIGHT - 100, NEXT_BUTTON)  
        self.next_x = next_x
        self.next_y = next_y
        self.room = room
        self.self_vis = False
        
    def collect(self):
        pos = pygame.mouse.get_pos()
        #this will give us which draggables are being clicked so other items don't react when dragged over!
        clicked_items = [item for item in self.room.items if item is not self and isinstance(item, DraggableClue) and item.clicked == True]

        #control item locations, put into inventory
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] and len(clicked_items) == 0:
            self.clicked=True
        
        if self.clicked == True and len(clicked_items) == 0:
            self.image = pygame.transform.scale(self.image, (80,60)) #will need to be general?
            self.next_room_button.draw()        
      

class DraggableClue(Clickable):
    def __init__(self, room, image, x, y, self_vis, area="", second_image="", func=""):
        super().__init__(room, x, y, image)
        self.area = area
        self.second_image = second_image
        self.room = room
        self.arrived = False
        self.func = func
        self.self_vis = self_vis
        self.is_zoom = False
        self.move_back = False
        
    def click_and_drag(self):

        pos = pygame.mouse.get_pos()
    
        clicked_items = [item for item in self.room.items if item is not self and isinstance(item, DraggableClue) and item.clicked == True]
        
        if self.clicked == True and len(clicked_items) == 0:
            self.rect.x = pos[0] - self.rect.width/2
            self.rect.y = pos[1] - self.rect.height/2

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False        
            
        if self.rect.colliderect(self.area.rect):
            self.is_zoom = True
            if self.func == "":
                pass
            else:
                self.func()    
                
class ZoomableClue(Clickable):
    def __init__(self, room, x, y, image, toggle_image, second_x, second_y):
        super().__init__(room, x, y, image)
        self.toggle_image = toggle_image
        self.clue_zoom = False
        self.clue_space = self.toggle_image.get_rect()
        self.second_x = second_x
        self.second_y = second_y
    
    def zoom(self):   
        if self.toggle_image == "":
            pass
        
        else:
        
            pos = pygame.mouse.get_pos()

            if self.self_vis == True:
                WIN.blit(self.image, (self.rect.x, self.rect.y))
                #to make the clue bigger then disappear    
                if pygame.mouse.get_pressed()[0] and not self.clue_space.collidepoint(pos):
                    self.clue_zoom = False
                
                if self.clue_zoom == True:
                    WIN.blit(self.toggle_image, (self.second_x, self.second_y))
                    #self.self_vis == False