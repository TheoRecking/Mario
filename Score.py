import pygame
from pygame.locals import *
import ActorClass
from ActorClass import*
import MarioClass
from MarioClass import*


class Score:

        def __init__(self,screen):

                self.screen = screen #la fenetre

                self.c=0 #compteur du score 
                self.p=0 #compteur des pieces
                self.x=50 #position x
                self.y=45 #position y
                self.j=0  #compteur du temps de l'affichage de la piece
                self.h=0  #compteur du "clignotement" de la piece
                
                self.piece1 = pygame.image.load("asset/gui/piece1.png").convert_alpha() #image 1 de la piece
                self.piece2 = pygame.image.load("asset/gui/piece2.png").convert_alpha() #image 2 de la piece

                #image des numeros
                self.zero = pygame.image.load("asset/gui/num0.png").convert_alpha()
                self.une = pygame.image.load("asset/gui/num1.png").convert_alpha()
                self.deux = pygame.image.load("asset/gui/num2.png").convert_alpha()
                self.trois = pygame.image.load("asset/gui/num3.png").convert_alpha()
                self.quatre = pygame.image.load("asset/gui/num4.png").convert_alpha()
                self.cinq = pygame.image.load("asset/gui/num5.png").convert_alpha()
                self.six = pygame.image.load("asset/gui/num6.png").convert_alpha()
                self.sept = pygame.image.load("asset/gui/num7.png").convert_alpha()
                self.huit = pygame.image.load("asset/gui/num8.png").convert_alpha()
                self.neuf = pygame.image.load("asset/gui/num9.png").convert_alpha()


        def affichage(self):
        

                self.dixmille=(self.c//10000)+10      #dizaine de millier
                self.mille=((self.c%10000)//1000)+10  #millier
                self.cent= ((self.c%1000)//100)+10    #centaine
                self.dix=((self.c%100)//10)+10        #dizaine
                self.un=(self.c%10)+10                #unitee






                #Dizaine de millier
                if self.dixmille==10:
                        self.screen.blit(self.zero,(self.x,self.y))
                elif self.dixmille==11:
                        self.screen.blit(self.une,(self.x,self.y))
                elif self.dixmille==12:
                        self.screen.blit(self.deux,(self.x,self.y))
                elif self.dixmille==13:
                        self.screen.blit(self.trois,(self.x,self.y))
                elif self.dixmille==14:
                        self.screen.blit(self.quatre,(self.x,self.y))
                elif self.dixmille==15:
                        self.screen.blit(self.cinq,(self.x,self.y))
                elif self.dixmille==16:
                        self.screen.blit(self.six,(self.x,self.y))
                elif self.dixmille==17:
                        self.screen.blit(self.sept,(self.x,self.y))
                elif self.dixmille==18:
                        self.screen.blit(self.huit,(self.x,self.y))
                elif self.dixmille==19:
                        self.screen.blit(self.neuf,(self.x,self.y))
                        
                #Millier
               
                if self.mille==10:
                        self.screen.blit(self.zero,(self.x+25,self.y))
                elif self.mille==11:
                        self.screen.blit(self.une,(self.x+25,self.y))
                elif self.mille==12:
                        self.screen.blit(self.deux,(self.x+25,self.y))
                elif self.mille==13:
                        self.screen.blit(self.trois,(self.x+25,self.y))
                elif self.mille==14:
                        self.screen.blit(self.quatre,(self.x+25,self.y))
                elif self.mille==15:
                        self.screen.blit(self.cinq,(self.x+25,self.y))
                elif self.mille==16:
                        self.screen.blit(self.six,(self.x+25,self.y))
                elif self.mille==17:
                        self.screen.blit(self.sept,(self.x+25,self.y))
                elif self.mille==18:
                        self.screen.blit(self.huit,(self.x+25,self.y))
                elif self.mille==19:
                        self.screen.blit(self.neuf,(self.x+25,self.y))

                #Centaine
                
                if self.cent==10:
                        self.screen.blit(self.zero,(self.x+50,self.y))
                elif self.cent==11:
                        self.screen.blit(self.une,(self.x+50,self.y))
                elif self.cent==12:
                        self.screen.blit(self.deux,(self.x+50,self.y))
                elif self.cent==13:
                        self.screen.blit(self.trois,(self.x+50,self.y))
                elif self.cent==14:
                        self.screen.blit(self.quatre,(self.x+50,self.y))
                elif self.cent==15:
                        self.screen.blit(self.cinq,(self.x+50,self.y))
                elif self.cent==16:
                        self.screen.blit(self.six,(self.x+50,self.y))
                elif self.cent==17:
                        self.screen.blit(self.sept,(self.x+50,self.y))
                elif self.cent==18:
                        self.screen.blit(self.huit,(self.x+50,self.y))
                elif self.cent==19:
                        self.screen.blit(self.neuf,(self.x+50,self.y))
                
                
                


                #Dizaine
                if self.dix==10:
                        self.screen.blit(self.zero,(self.x+75,self.y))
                elif self.dix==11:
                        self.screen.blit(self.une,(self.x+75,self.y))
                elif self.dix==12:
                        self.screen.blit(self.deux,(self.x+75,self.y))
                elif self.dix==13:
                        self.screen.blit(self.trois,(self.x+75,self.y))
                elif self.dix==14:
                        self.screen.blit(self.quatre,(self.x+75,self.y))
                elif self.dix==15:
                        self.screen.blit(self.cinq,(self.x+75,self.y))
                elif self.dix==16:
                        self.screen.blit(self.six,(self.x+75,self.y))
                elif self.dix==17:
                        self.screen.blit(self.sept,(self.x+75,self.y))
                elif self.dix==18:
                        self.screen.blit(self.huit,(self.x+75,self.y))
                elif self.dix==19:
                        self.screen.blit(self.neuf,(self.x+75,self.y))


                #Unitee
                if self.un==10:
                        self.screen.blit(self.zero,(self.x+100,self.y))
                elif self.un==11:
                        self.screen.blit(self.une,(self.x+100,self.y))
                elif self.un==12:
                        self.screen.blit(self.deux,(self.x+100,self.y))
                elif self.un==13:
                        self.screen.blit(self.trois,(self.x+100,self.y))
                elif self.un==14:
                        self.screen.blit(self.quatre,(self.x+100,self.y))
                elif self.un==15:
                        self.screen.blit(self.cinq,(self.x+100,self.y))
                elif self.un==16:
                        self.screen.blit(self.six,(self.x+100,self.y))
                elif self.un==17:
                        self.screen.blit(self.sept,(self.x+100,self.y))
                elif self.un==18:
                        self.screen.blit(self.huit,(self.x+100,self.y))
                elif self.un==19:
                        self.screen.blit(self.neuf,(self.x+100,self.y))


                #piece

                self.dix=((self.p%100)//10)+10  #dizaine
                self.un=(self.p%10)+10          #dizaine

                self.j+=1
                if self.j>20:
                        self.j = 0
                        self.h+=1
                if self.h%2 == 0:
                        self.screen.blit(self.piece1,(self.x+275,self.y-40))
                if self.h%2 ==1:
                        self.screen.blit(self.piece2,(self.x+275,self.y-40))


                #Dizaine
                if self.dix==10:
                        self.screen.blit(self.zero,(self.x+275,self.y))
                elif self.dix==11:
                        self.screen.blit(self.une,(self.x+275,self.y))
                elif self.dix==12:
                        self.screen.blit(self.deux,(self.x+275,self.y))
                elif self.dix==13:
                        self.screen.blit(self.trois,(self.x+275,self.y))
                elif self.dix==14:
                        self.screen.blit(self.quatre,(self.x+275,self.y))
                elif self.dix==15:
                        self.screen.blit(self.cinq,(self.x+275,self.y))
                elif self.dix==16:
                        self.screen.blit(self.six,(self.x+275,self.y))
                elif self.dix==17:
                        self.screen.blit(self.sept,(self.x+275,self.y))
                elif self.dix==18:
                        self.screen.blit(self.huit,(self.x+275,self.y))
                elif self.dix==19:
                        self.screen.blit(self.neuf,(self.x+275,self.y))


                #Unitee
                if self.un==10:
                        self.screen.blit(self.zero,(self.x+300,self.y))
                elif self.un==11:
                        self.screen.blit(self.une,(self.x+300,self.y))
                elif self.un==12:
                        self.screen.blit(self.deux,(self.x+300,self.y))
                elif self.un==13:
                        self.screen.blit(self.trois,(self.x+300,self.y))
                elif self.un==14:
                        self.screen.blit(self.quatre,(self.x+300,self.y))
                elif self.un==15:
                        self.screen.blit(self.cinq,(self.x+300,self.y))
                elif self.un==16:
                        self.screen.blit(self.six,(self.x+300,self.y))
                elif self.un==17:
                        self.screen.blit(self.sept,(self.x+300,self.y))
                elif self.un==18:
                        self.screen.blit(self.huit,(self.x+300,self.y))
                elif self.un==19:
                        self.screen.blit(self.neuf,(self.x+300,self.y))

          
                







        
                        

                
