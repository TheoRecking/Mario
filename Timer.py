import pygame
from pygame.locals import*




class Timer :

        def __init__(self,fenetre):

                self.n=300    #Temps total du timer
                self.i=0      #Initialisation du timer

                
                #Images des numeros
                self.zero = pygame.image.load("asset/gui/num0.png").convert_alpha()
                self. un = pygame.image.load("asset/gui/num1.png").convert_alpha()
                self.deux = pygame.image.load("asset/gui/num2.png").convert_alpha()
                self.trois = pygame.image.load("asset/gui/num3.png").convert_alpha()
                self.quatre = pygame.image.load("asset/gui/num4.png").convert_alpha()
                self.cinq = pygame.image.load("asset/gui/num5.png").convert_alpha()
                self.six = pygame.image.load("asset/gui/num6.png").convert_alpha()
                self.sept = pygame.image.load("asset/gui/num7.png").convert_alpha()
                self.huit = pygame.image.load("asset/gui/num8.png").convert_alpha()
                self.neuf = pygame.image.load("asset/gui/num9.png").convert_alpha()

                self.fenetre=fenetre #la fenetre
                self.x=750           #position x
                self.y=45            #position y



        def affichage(self,fin = False):

                self.i+=1 #le compteur augmente de 1
                if 300-self.i//60 != self.n and fin == False:  # Si [ 300 - le laps de temps deja parcouru ]  est different de la valeur actuelle du timer
                        self.n=300-self.i//60 # alors le timer prend la valeur  [ 300-temps deja passee]




                if self.n>=0: # Si le timer n'est pas arrive a zero, on calcule :

                        cent=self.n//100        #les centaines
                        dix=(self.n%100)//10    #les dizaines
                        un=self.n%10            #les unitees




               #Centaine
                        if cent ==3:
                                self.fenetre.blit(self.trois,(self.x,self.y))
                        elif cent==2:
                                self.fenetre.blit(self.deux,(self.x,self.y))
                        elif cent==1:
                                self.fenetre.blit(self.un,(self.x,self.y))


                #Dizaine
                        if dix==0:
                               self.fenetre.blit(self.zero,(self.x+25,self.y))
                        elif dix==1:
                               self.fenetre.blit(self.un,(self.x+25,self.y))
                        elif dix==2:
                               self.fenetre.blit(self.deux,(self.x+25,self.y))
                        elif dix==3:
                               self.fenetre.blit(self.trois,(self.x+25,self.y))
                        elif dix==4:
                               self.fenetre.blit(self.quatre,(self.x+25,self.y))
                        elif dix==5:
                               self.fenetre.blit(self.cinq,(self.x+25,self.y))
                        elif dix==6:
                               self.fenetre.blit(self.six,(self.x+25,self.y))
                        elif dix==7:
                               self.fenetre.blit(self.sept,(self.x+25,self.y))
                        elif dix==8:
                               self.fenetre.blit(self.huit,(self.x+25,self.y))
                        elif dix==9:
                               self.fenetre.blit(self.neuf,(self.x+25,self.y))


                #Unitee
                        if un==0:
                               self.fenetre.blit(self.zero,(self.x+50,self.y))
                        elif un==1:
                               self.fenetre.blit(self.un,(self.x+50,self.y))
                        elif un==2:
                               self.fenetre.blit(self.deux,(self.x+50,self.y))
                        elif un==3:
                               self.fenetre.blit(self.trois,(self.x+50,self.y))
                        elif un==4:
                               self.fenetre.blit(self.quatre,(self.x+50,self.y))
                        elif un==5:
                               self.fenetre.blit(self.cinq,(self.x+50,self.y))
                        elif un==6:
                               self.fenetre.blit(self.six,(self.x+50,self.y))
                        elif un==7:
                               self.fenetre.blit(self.sept,(self.x+50,self.y))
                        elif un==8:
                               self.fenetre.blit(self.huit,(self.x+50,self.y))
                        elif un==9:
                               self.fenetre.blit(self.neuf,(self.x+50,self.y))










