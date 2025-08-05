import pygame
import random
import time
pygame.init()

pygame.display.set_caption("Recycling game")
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])

def changebg(img):
    bg = pygame.image.load(img)
    bg = pygame.transform.scale(bg,(screen_width,screen_height))
    screen.blit(bg,(0,0))

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('bin.png')
        self.image=pygame.transform.scale(self.image,(40,60))
        self.rect=self.image.get_rect()

class Recyclable(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image=pygame.image.load(img)
        self.image=pygame.transform.scale(img,(30,30))
        self.rect=self.image.get_rect()

class NonRecyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("plastic.png")
        self.image=pygame.transform.scale(self.image,(40,40))
        self.rect=self.image.get_rect()

item_list = pygame.sprite.Group() #recyclable
plastic_list = pygame.sprite.Group() #nonrecyclable
allsprites = pygame.sprite.Group()


bin=Bin()
allsprites.add(bin)

#diff images that can spawn
images = ["item1.png", "item2.png", 'item3.png']

for i in range (50):
    item=Recyclable(random.choice(images))
    item.rect.x=random.randrage(screen_width)
    item.rect.y=random.randrage(screen_height)

    item_list.add(item)
    allsprites.add(item)

for i in range (20):
    plastic=NonRecyclable()
    plastic.rect.x=random.randrange(screen_width)
    plastic.rect.y=random.randrange(screen_height)

    plastic_list.add(plastic)
    allsprites.add(plastic)

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

play = True
score = 0
clock = pygame.time.Clock()
start_time = time.time()
