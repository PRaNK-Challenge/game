import pygame
import os

pygame.init()
pygame.font.init()
pygame.mixer.init(frequency=8000)
pygame.display.set_caption("Private Eye")

WIDTH, HEIGHT = 950,600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0,0,0)
TRANSPARENT = (0,0,0,0)
ADVENTURE_FONT = pygame.font.SysFont('arial', 20)
NEXT_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("art", "other",'next_button.png')), (180,120)).convert_alpha()
TEXT_BOX = pygame.transform.scale(pygame.image.load(os.path.join("art", "other",'text_box.png')), (600, 130))

# HELPER FUNCTIONS
# to help fade between scenes, used by rooms and items, change to what's visible at beginning
def redraw_window(room, items, next_room="", show_got_clue=""):
    WIN.blit(room.image, (0,0))
    for item in items:
        if item.self_vis == True:
            WIN.blit(item.image, (item.rect.topleft))     
    # don't want this to run if it's a fadein... something similar for got a clue
    if next_room == "next_room":
        room.text.blit_text()      
    
    if show_got_clue == True:
        if room.has_collectable == True:
            clue_text = ADVENTURE_FONT.render(
                        "Got a clue!", 1, WHITE)
            WIN.blit(clue_text, (10, 570))
        
# fade between scenes (technically fade out and in but w/e)
def fade_in_and_out(width, height, state, room, current_room, next_room): 
    
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))

    for alpha in range(255):
        fade.set_alpha(alpha)
        redraw_window(current_room, current_room.end_items, "next_room", show_got_clue = True)
        WIN.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(1)
        
    # change to next room    
    room.state = state
                
    for alpha in range (255):
        fade.set_alpha(255-alpha)
        redraw_window(next_room, next_room.start_items, show_got_clue = False)
        WIN.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(1)

# change the look of the cursor when hovering over an item that could be clicked
def change_cursor(items, pos):
            hover_items = [item for item in items if item.rect.collidepoint(pos) and item.self_vis == True]
            if len(hover_items):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
 
# CLASSES               
# for putting text on screen
class Text():
    def __init__(self, text, blit_position):
        self.text = text
        self.self_vis = False
        self.blit_position = blit_position
        self.position = (180, 495) if self.blit_position == "bottom" else (180, 25)
        self.place_text = (155, 470) if self.blit_position == "bottom" else (155, 0)
        
    # for text over multiple lines    
    def blit_text(self):
        if self.text == "":
            pass
        else:
            WIN.blit(TEXT_BOX, self.place_text)
            words = [word.split(' ') for word in self.text.splitlines()]  # 2D array where each row is a list of words.
            space = ADVENTURE_FONT.size(' ')[0]  # The width of a space.
            max_width = 730
            x, y = self.position
            for line in words:
                for word in line:
                    word_surface = ADVENTURE_FONT.render(word, 1, BLACK)
                    word_width, word_height = word_surface.get_size()
                    if x + word_width >= max_width:
                        x = self.position[0]  # Reset the x.
                        y += word_height  # Start on new row.
                    WIN.blit(word_surface, (x, y))
                    x += word_width + space
                x = self.position[0]  # Reset the x.
                y += word_height  # Start on new row.
           
    def remove_text(self):
        self.text = "" 
 
       
# Parent class for drawing images on screen and checking if they've been clicked
class Clickable():
    def __init__(self, room, x, y, image=""):
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x
        self.y= y
        self.rect.topleft = (x, y)
        self.clicked = False
        self.room = room
        self.self_vis = True
    
    def draw(self):
        if self.image == "":
            pass
        else:
            pos = pygame.mouse.get_pos()
            if self.self_vis == True:
                WIN.blit(self.image, (self.rect.x, self.rect.y))
                if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:# and len(clicked_items) == 0:
                    self.clicked=True


# item that fades into the room
class FadeIn(Clickable):
    def __init__(self, room, x, y, image, extra_current_items=[], extra_current_items2=[]):
        super().__init__(room, x, y, image)
        self.show_fader = False
        self.self_vis = False
        self.extra_current_items = extra_current_items
        self.extra_current_items2 = extra_current_items2
        
    def fade_in(self):
        
        current_items = self.extra_current_items if len(self.extra_current_items) else self.room.current_items
        
        if self.image != "":
            for alpha in range(256):
                self.image.set_alpha(alpha)
                redraw_window(self.room, current_items)
                WIN.blit(self.image, (self.rect.topleft))
                pygame.display.update()   
            if alpha == 255:
                self.show_fader = True

    def fade_out(self):
        
        current_items = self.extra_current_items2 if len(self.extra_current_items2) else self.extra_current_items if len(self.extra_current_items) else self.room.current_items
        
        if self.image != "":
            for alpha in range(256):
                self.image.set_alpha(256-alpha)
                redraw_window(self.room, current_items)
                WIN.blit(self.image, (self.rect.topleft))
                pygame.display.update()        


# Audio clue that can trigger a function if needed
class AudioClue():
    def __init__(self, room, item, sound, pause, repeat, second_sound="", third_sound="", func="", fourth_sound="", func_pause=""):
        self.room = room
        self.item = item
        self.sound = sound
        self.repeat = repeat
        self.second_sound = second_sound
        self.third_sound = third_sound
        self.pause = pause
        self.func = func
        self.func_pause = func_pause
        self.arrived = False
        self.third_sound = third_sound
        self.fourth_sound = fourth_sound
        self.sound_length = int(self.sound.get_length())
        if self.second_sound != "":
            self.second_sound_length = int(self.second_sound.get_length())
        if self.third_sound != "":
            self.third_sound_length = int(self.third_sound.get_length())
        if self.fourth_sound != "":
            self.fourth_sound_length = int(self.third_sound.get_length())    
        
    def carry_out_func(self):
        # if you need to carry out a function once the sound stops
        if self.func == "":
            pass
        else:
            if self.func_pause == True:
                pygame.time.delay(self.pause)
                self.func()
            else:
                self.func()

    def play_sound(self, topleft):        
        # this will stop the sound playing more than once

        if self.sound != "":
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if self.item.rect.collidepoint(topleft) and pygame.mouse.get_pressed()[0] and self.item.rect.topleft == topleft:           
                if self.second_sound == "":
                    pygame.time.delay(self.pause)
                    self.sound.play()
                    self.carry_out_func()
                else:
                    self.sound.play()
                    pygame.time.delay(self.pause + 2000)
                    self.second_sound.play()
                    pygame.time.delay(self.second_sound_length + 3000)
                    if self.repeat == True:
                        self.carry_out_func()
                        
                    if self.third_sound == "":
                        pass
                    else:
                        pygame.time.delay(self.second_sound_length + 13500)
                        self.third_sound.play()
                        pygame.time.delay(self.third_sound_length + 3000)
                        self.carry_out_func()
                        if self.fourth_sound != "":
                            self.fourth_sound.play()
   
         
# A clickable item that can be collected, final clue before next room
class CollectableClue(Clickable):
    def __init__(self, room, x, y, image, next_x, next_y, size= ""):
        super().__init__(room, x, y, image)
        self.next_room_button = Clickable(room, WIDTH - 200, HEIGHT - 150, NEXT_BUTTON)  
        self.next_room_button.self_vis = False
        self.next_x = next_x
        self.next_y = next_y
        self.room = room
        self.self_vis = False
        self.text = "Got a clue!"
        self.size = size
        
    def collect(self):
        pos = pygame.mouse.get_pos()
        
        #control item locations, put into inventory
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:# and len(clicked_items) == 0:
            self.clicked=True
        
        if self.clicked == True:
            if self.size == "":
                self.image = pygame.transform.scale(self.image, (80,60)) #will need to be general?
            else:
                self.image = pygame.transform.scale(self.image, self.size)
            self.next_room_button.draw()
            display_text = ADVENTURE_FONT.render(
                    self.text, 1, WHITE)
            WIN.blit(display_text, (10, 570))
      

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
        
        clicked_items = [item for item in self.room.end_items if item is not self and isinstance(item, DraggableClue) and item.clicked == True]
        
        if self.image != "":
            if self.clicked == True and len(clicked_items) == 0:
                self.rect.x = pos[0] - self.rect.width/2
                self.rect.y = pos[1] - self.rect.height/2
            
            if self.clicked == True and len(clicked_items) == 1:
                self.rect.x = pos[0] - self.rect.width/2
                self.rect.y = pos[1] - self.rect.height/2
            
            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False
                
            vis = False
            
            if isinstance(self.area, pygame.Rect):
                if self.area.collidepoint(pos):
                        self.clicked = True
                        vis= not vis
                if vis == True and self.second_image!="":
                    WIN.blit(self.second_image, (150, 20))
            else:
                if self.area.rect.collidepoint(pos) and self.clicked ==True:
                    self.clicked = True
                    vis= not vis
                              
                
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
                    
