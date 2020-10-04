import pygame
import MarioClass
import TerrainClass
import CubeClass
import physique
import Timer
import cursorclass
import main

from main import *
from physique import *
from CubeClass import *
from pygame import *
from MarioClass import *
from TerrainClass import *
from Timer import *
from cursorclass import *

pygame.init()
clock=pygame.time.Clock()
fenetre = pygame.display.set_mode((860, 640))




"""//////////////////////////
  ////  LE PROGRAMME  \\\\
\\\\\\\\\\\\\\\\\\\\\\\\\\\""""


#les menus
menu = pygame.image.load("asset/gui/menu/menuprint.png")
menu2 = pygame.image.load("asset/gui/menu/menuprint2.png")
#le curseur
cursor1 = pygame.image.load("asset/gui/mushroomcursor.png").convert_alpha()

#les "objets" curseurs
curseur1 = Cursor( 250,385,cursor1)
curseur2 = Cursor( 250,385,cursor1)

#element du meby
time=pygame.image.load("asset/gui/Timer.png").convert_alpha()

inmenu = True #on est dans le menu
sousmenu = False #on est pas dans le sous-menu
inlevel = False #on est pas dans level
intest = False #on n'est pas dans le leveltest (marche plus)
quitter = False #on quite pas
        

while quitter == False: # toutes les image, l'ordi recalcule:

        """MENU"""       
                 
        if inlevel == True: #si on a lancer le level1
                level1(fenetre,4) #on lance la fonction level1(voir fichier main)
                inlevel = False #quand la fonction est terminée, on est plus dans level
                inmenu = True #on repasse dans le menu
                
        if inmenu == True:
                
                                      
                fenetre.blit(menu,(0,0)) #afficher le menu
                curseur1.affichage(fenetre) #afficher le curseur
                curseur1.curseur(40,3) #activer le menu
                if pygame.key.get_pressed()[K_RETURN] == True and curseur1.position == 1: #si on selection le choix 1
                        inmenu = False  
                        inlevel = True #on passe dans level1

                if pygame.key.get_pressed()[K_RETURN] == True and curseur1.position == 3: #si on effectue le choix 3
                        sousmenu = True  #on passe dans le sous menu
                        inmenu = False
                        curseur1.position =1 #on repasse le curseur en position 1 pour que le menu soit remis a zero si on revient dessus"
                        enable2 = False  # cette boolean sert a Ã©vitÃ© que le choix numero 1 du sous menu sois activÃ© directement (car entrÃ© est appuyÃ©)
                        clock.tick(7)


                """Sous MENU"""


        if sousmenu == True:    

                fenetre.blit(menu2,(0,0))       #afficher le sous menu
                curseur2.affichage(fenetre)     #afficher le curseur
                curseur2.curseur(40,3)  #activer le curseur
                if pygame.key.get_pressed()[K_RETURN] == True and curseur2.position == 1 and sousmenu == True and enable2 == True: #choix 1 
                        sousmenu = False
                        intest = True   #on passe dans testlevel. On doit charger le terrain (level1 par defaut)
                        
                if pygame.key.get_pressed()[K_RETURN] == True and curseur2.position == 2: # si on fait le choix 2, on quitte
                        quitter = True
                if pygame.key.get_pressed()[K_RETURN] == True and curseur2.position == 3:       #si on fait le choix 3, on revient sur le menu
                        sousmenu = False
                        inmenu = True
                        curseur2.position =1
                        clock.tick(7)
                enable2 = True #on effectue tout un tour de boucle avant d'activer enable pour laisser le temps a l'utilisateur de relever le doigt

        clock.tick(60) #attendre 1/60 secondes    
        pygame.event.pump()#l'image se rafraiche toutes les /60 de secondes
        pygame.display.update()

                



