import pygame
class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/attack_1.png'))
        self.sprites.append(pygame.image.load('sprites/attack_2.png'))
        self.sprites.append(pygame.image.load('sprites/attack_3.png'))
        self.sprites.append(pygame.image.load('sprites/attack_4.png'))
        self.sprites.append(pygame.image.load('sprites/attack_5.png'))
        self.sprites.append(pygame.image.load('sprites/attack_6.png'))
        self.sprites.append(pygame.image.load('sprites/attack_7.png'))
        self.sprites.append(pygame.image.load('sprites/attack_8.png'))
        self.sprites.append(pygame.image.load('sprites/attack_9.png'))
        self.sprites.append(pygame.image.load('sprites/attack_10.png'))
       
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image,(128*3,64*3))

        self.rect = self.image.get_rect()
    
        self.rect.topleft = 100, 100
        self.animar = False

    def atacar(self):
        self.animar=True

    def update(self):
        if self.animar==True:
            self.atual = self.atual + 0.02
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image,(128*3,64*3))



           

todas_sprites = pygame.sprite.Group()
sapo = Sapo()
todas_sprites.add(sapo)