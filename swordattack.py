import pygame

from common import Vector2
import settings
import math
#import player
import keyboard_input
import player

#16.30 aloitettu
class Slash(pygame.sprite.Sprite):
    

    #self,playerpostition(vector2)
    def __init__(self,playerpos: Vector2, *groups) -> None:

        super().__init__(groups)

        #IMPORTANT HAVE TO BE TELEGRAPH
        self.newimage = pygame.image.load('assets/art/slash.png')
        #self.image = pygame.transform.rotate(self.image, int(0))
        self.image = None

        #self.player_rect = player().rect()
        #print(self.player_rect.center)
        self.playerxy = playerpos
        self.angle = 0
        
        
        #self.rect = self.image.get_rect()

        #self.rect.center = playerpos+Vector2(64,0)
        
        self.__x = playerpos.x# - self.__width/2
        self.__y = playerpos.y# - self.__height/2
        #self.rect.centerx + 64

        #self.spriteposition_x = playerpos.x - self.rect.centerx
        #self.spriteposition_y = playerpos.y - self.rect.centery

        #self.mousepos = playerpos

        #startpos_x = self.mousepos.x - self.rect.centerx
        #startpos_y = self.mousepos.y - self.rect.centery

        #self.angle = math.atan2(startpos_y, startpos_x)
   # def position(self,pos: Vector2)->None:
    #    self.rect.center = pos+Vector2(64,0)

    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.playerxy.x, mouse_y - self.playerxy.y
        self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.newimage, int(self.angle))
        print(self.angle)
        self.rect = self.image.get_rect(center=self.playerxy)#self.rect = self.image.get_rect(center=self.playerxy+Vector2(64,0))
        #self.image = self.newimage

    def update(self) -> None:
        #mouse_rel_to_player = keyboard_input.get_mouse_position_relative(self.player.rect)
        #self.rect.center = self.playerxy#+Vector2()
        #self.newimage = pygame.transform.rotate(self.image, int(self.angle))
        #self.rect = self.newimage.get_rect(center=self.playerxy)
        self.rotate()
    
        #
    #    pass

#draw triangle start  shit
"""""
    def createAttackArea() -> None:
        x1 = self.angle.x
        y1 = self.angle.y

        x2 = random.randint(-250, wn_width + 250)
        y2 = random.randint(-250, wn_height + 250)

        x3 = random.randint(-250, wn_width + 250)
    y3 = random.randint(-250, wn_height + 250)
"""