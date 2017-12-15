import pygame #Used kids can code base template to get
import random
import os
import time

iwanttodie = False
difficulty = 5
img_dir = os.path.join(os.path.dirname(__file__), "img")
level = 1
lvl = 1
dimw = 1280
dimh = 720
fps = 30
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

game_folder = os.path.dirname(__file__)
game_folder = os.path.join(game_folder, "img")
img = img_dir





class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.center = (dimw / 2, dimh / 2)
    def update(self):
        global level
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
        if keystate[pygame.K_e]:
            level = level+1
        self.rect.y += self.speedy
        if self.rect.left > dimw:
            self.rect.left = 0
        if self.rect.right < 0:
            self.rect.right = 1280
        if level==1:
            self.image.fill(blue)
        if level==2:
            self.image.fill(black)
        if level==3:
            self.image.fill(red)
        if level==4:
            self.image.fill(green)
        if level==5:
            self.image.fill(yellow)



class Greenaway(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_dir, "GROOOOOOOOOOOOOOOOOOOOOENEWEG.png"))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(5,1280),0)
    def update(self):
        global level
        global lvl
        global difficulty
        difficulty = int(5 + 2 * level)
        if level==1:
            self.rect.y += 10
        if level>=2:
            self.rect.y += 15
        if self.rect.y > 720:
            lvl+=1
            if lvl>=10*level:
                level += 1
                lvl = 0
                difficulty = int(5 + 2*level)
            self.rect.center = (random.randint(5,1280),0)



player = Player()
players = pygame.sprite.Group()
players.add(player)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((dimw , dimh))
pygame.display.set_caption("Stealy the thingy")
clock = pygame.time.Clock()

iwanttodie = pygame.sprite.spritecollide(Player, Greenaway, False)
if iwanttodie:
    pygame.quit()

for i in range(difficulty):
    Groenwegguard_sprites = pygame.sprite.Group()
    g = Greenaway()
    players.add(g)
    Groenwegguard_sprites.add(g)
    Groenwegguard_sprites.update()


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