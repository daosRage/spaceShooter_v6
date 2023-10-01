from data import *

class Sprite(pygame.Rect):
    def __init__(self, x, y, width, height, hp= None, image= None, speed= None):
        super().__init__(x, y, width, height)
        self.HP = hp
        self.IMAGE = image
        self.SPEED = speed


class Hero(Sprite):
    def __init__(self, x, y, width, height, hp= 3, image= None, speed= 5):
        super().__init__(x, y, width, height, hp, image, speed)
        self.MOVE = {"LEFT": False, "RIGHT": False}
    
    def move(self, window):
        if self.MOVE["LEFT"] == True:
            self.x -= self.SPEED
        if self.MOVE["RIGHT"] == True:
            self.x += self.SPEED
        pygame.draw.rect(window, (120,120,120),self) 
