import pygame
from pygame import *

class Cursor:
    
    def __init__ (self,x,y,image): 

       
        self.image = image #image du curseur
        self.x = x #coordonée x
        self.ybase = y #coordonée y représentant la coordonée de la position initiale
        self.y = y #coordonné y du curseur
        self.position = 1 # position du curseur

    def curseur(self, ecart_y, nombredechoix): #methode du menu

        clock=pygame.time.Clock()  #horloge
        if self.position == 1: #si la position du curseur est a nouveau 1
            self.y =self.ybase #on repositione l'image au bonne endroit
        if pygame.key.get_pressed()[K_DOWN] == True: #si on appuie sur bas
            self.y += ecart_y # on descend de x pixel vers le bas
            self.position +=1 #on augmente de 1 la position
            if self.position == nombredechoix + 1: #si on dépasse le nombre de choix
                self.y = self.ybase #on réinitialise y une premiere fois pour éviter les bugs
                self.position =1 #la postion revient a 1
            clock.tick(6) #on attend un peu pour laisser le temps a l'utilisateur de retirer son doigt

        if pygame.key.get_pressed()[K_UP] == True: #si l'utilisateur appuie sur haut
            self.y -= ecart_y #on augmente la position du curseur sur l'axe y
            self.position -=1 #on enlève 1 a sa position dans le tableau
            if self.position == 0: #si il arrive a 0 alors il va a la fin du tableau
                self.y += (nombredechoix)*ecart_y
                self.position = nombredechoix
            clock.tick(6)#on attend un peu pour laisser le temps a l'utilisateur de retirer son doigt
            
    def affichage(self,fenetre): #affichage

          fenetre.blit(self.image,(self.x,self.y))
    
