# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 15:40:49 2022

@author: nmcdermott1
"""

import pygame
#from ClickableClasses import Clickable, ClickableClue, CollectableClue 

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Adventure Game!")

FPS = 60

WHITE = (255, 255, 255)
TRANSPARENT = (0,0,0,0)

ADVENTURE_FONT = pygame.font.SysFont('arial', 40)

KITCHEN = pygame.transform.scale(pygame.image.load('kitchen.png'), (WIDTH, HEIGHT))
STUDY_ROOM = pygame.transform.scale(pygame.image.load('study_room.png'), (WIDTH, HEIGHT))
CANDLE = pygame.transform.scale(pygame.image.load('candle.png'), (55,60)).convert_alpha()
BOOK = pygame.transform.scale(pygame.image.load('book.png'), (55,60)).convert_alpha()
OPEN_BOOK = pygame.transform.scale(pygame.image.load('open_book.png'), (600,500)).convert_alpha()
KETTLE = pygame.transform.scale(pygame.image.load('kettle.png'), (55,60)).convert_alpha()
PAN = pygame.transform.scale(pygame.image.load('pan.png'), (55,60)).convert_alpha()
NEXT_BUTTON = pygame.transform.scale(pygame.image.load('next_button.png'), (70,70)).convert_alpha()


# Parent class for drawing images on screen
class Clickable():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.self_vis = True #this is its own image

# should accept the next room?            
class NextButton(Clickable):
    def _init__(self, x, y, image):
        super ().__init__(x, y, image)
        self.clicked = False
        
    def draw(self):
        WIN.blit(NEXT_BUTTON, (self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.clicked = True
        

#click_next_button = NextButton(WIDTH - 100, HEIGHT - 100, NEXT_BUTTON)  
# Child class, a clickable item that provides a clue
class ClickableClue(Clickable):
    def __init__(self, x, y, image, toggle_image):
        super().__init__(x, y, image) #might need to add size change
        self.toggle_image = toggle_image
        self.clue_vis = False
    
    def draw(self):
        #get mouse position
        pos = pygame.mouse.get_pos()
        
        #control its visibility
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.clicked = True
            self.clue_vis = True
        
        #the book is still visible when the room changes...

        if self.self_vis == True:
            WIN.blit(self.image, (self.rect.x, self.rect.y))
                
        if self.clue_vis == True:
            WIN.blit(self.toggle_image, (150, 10))
            self.self_vis == False
           
            
# Child class, a clickable item that can be collected    
class CollectableClue(Clickable):
    def __init__(self, x, y, image, clue):
        super().__init__(x, y, image)
        self.clue = clue
        self.next_button = NextButton(WIDTH - 100, HEIGHT - 100, NEXT_BUTTON)
        self.next_room_button = NextButton(WIDTH - 100, HEIGHT - 100, NEXT_BUTTON)  
        
    def draw(self):
        #get mouse position
        pos = pygame.mouse.get_pos()
        
        # the clue must be clicked first before the collectable clue can be collected
        if self.clue.clicked == True:
        
            #control item locations, put into inventory
            if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                self.clicked = True
        
        #control item locations, put into inventory
        if self.clicked == False:
            WIN.blit(self.image, (self.rect.x, self.rect.y))
        else:
            WIN.blit(self.image, (50, HEIGHT - 100))
            self.next_button.draw()
            #click_next_button.move_room()
            if self.next_room_button.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                self.next_room_button.clicked = True
            



class Room():
    def __init__(self, image, x1, y1, clue, x2, y2, clue_note, clickable):
        self.current_room = False
        self.image = image   
        self.click_clue = ClickableClue(x1, y1, clue, clue_note)
        self.collect_clue = CollectableClue(x2, y2, clickable, self.click_clue)
        self.next_room = False
        
    def draw_room(self):

        if self.current_room == True:
            WIN.blit(self.image, (0, 0))
            self.collect_clue.draw()
            self.click_clue.draw()
        
            #print(self.collect_clue.next_room_button.clicked)
            if self.collect_clue.next_room_button.clicked == True:
                self.next_room = True
        
            pygame.display.update()
        
        
room1 = Room(STUDY_ROOM, 450, 240, BOOK, 600, 250, OPEN_BOOK, CANDLE)
room2 = Room(KITCHEN, 200, 200, CANDLE, 400, 100, BOOK, OPEN_BOOK)


"""
class Scene():
    def __init__(self):
        self.scenes = []
    def input(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass
    
class SceneManager():
    def __init__(self):
        pass
        
#e.g. scenemanager.push(room1)

"""



def draw_window(room):
    
    current = 1
    if current == 1:
        room.draw_room()
        room.current_room = True
        if room.collect_clue.next_room_button.clicked == True:
            room.current_room = False
            room.draw_room()

    pos = pygame.mouse.get_pos()

    #candle shows over book
    if pygame.mouse.get_pressed()[0]:
        if room.click_clue.rect.collidepoint(pos):
            room.click_clue.clue_vis = True
        if not room.click_clue.rect.collidepoint(pos):
            room.click_clue.clue_vis = False
 
            
    pygame.display.update()
    
    

def main():
    
    clock = pygame.time.Clock()
    
    #create new scene manager here
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        current_room = 1
    
        #base this ona Boolean
        if current_room == 1:
            draw_window(room1)
            #print(room1.collect_clue.next_room_button.clicked)
            if room1.collect_clue.next_room_button.clicked == True:
                print("")
    

        #draw_window()            
                               
    pygame.quit()          
    

    
if __name__ == "__main__":
    main()

#this script relies on some aspects from ClickableClasses!
