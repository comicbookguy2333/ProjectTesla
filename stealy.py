import pygame #Used kids can code base template to get
import random
import time

dimw = 1280
dimh = 720
fps = 30

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.center = (dimw / 2, dimh / 2)
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_d]:
            self.speedx = 5
        self.rect.x += self.speedx
        if keystate[pygame.K_s]:
            self.speedy = 5
        if keystate[pygame.K_w]:
            self.speedy = -5
        self.rect.y += self.speedy
        if self.rect.left > dimw:
            self.rect.right = 0


class Greenaway(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = (100,100)


player = Player()
players = pygame.sprite.Group()
players.add(player)
Groenwegguard_sprites = pygame.sprite.Group()
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((dimw , dimh))
pygame.display.set_caption("Stealy the thingy")
clock = pygame.time.Clock()
Groenwegguard_sprites.update()

for i in range(1):
    g = Greenaway()
    players.add(g)
    Groenwegguard_sprites.add(g)

running = True
while running:
    clock.tick(fps)
    players.update()
    screen.fill(white)
    players.draw(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame. quit