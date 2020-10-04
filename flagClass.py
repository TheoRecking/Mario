import pygame
from pygame import *

class Flag: #le petit drapeau

    def __init__(self,level,fenetre):

        if level == 1: #si il s'agit du niveau 1
 
            self.x = 8229 #on positionne le drapeau aux bonnes coordonées
            self.y = 140

            self.flag = pygame.image.load("asset/decor/flag/flag.png").convert_alpha()
            self.collider = self.flag.get_rect()
            self.collider.move_ip(8229,140) #on creer un collider qui définis si mario est arrivé au drapeau ou non
            
            self.flagcollider = pygame.Rect(8279,0,100,640)
            self.colliderliste = [self.collider]
            self.colliderliste2 = [self.flagcollider]
            self.screen = fenetre


    def collisionperso(self,mario):

        if mario.colliderdroite.collidelist(self.colliderliste2) != -1: #si mario est arrivé au drapeau, alors active mario.fin : le niveau est terminé
            mario.fin = True
            mario.vitesse = 0

    def scrolling(self,mario,vitesse):# scrolling du drapeaue
                if pygame.key.get_pressed()[pygame.K_RIGHT] ==True  and mario.collider.collidelist(mario.scrolling) != -1:
                    self.x-=mario.vitesse
                    self.collider.move_ip(-mario.vitesse,0)
                    self.flagcollider.move_ip(-mario.vitesse,0)
    def affichage(self): #affichage du drapeau
        self.screen.blit(self.flag,self.collider)        

    
            

        
