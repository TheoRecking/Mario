import pygame
import ActorClass
from ActorClass import *

class Coins: #Classe Piece
    def __init__(self,x,y,screen):

        self.x = x #coordonée x
        self.y = y #coordonée  y
        self.screen = screen # ecran

        #image des pieces

        self.coin1 = pygame.image.load("asset/decor/piece/coin1.png").convert_alpha()
        self.coin2 = pygame.image.load("asset/decor/piece/coin2.png").convert_alpha()
        self.coin3 = pygame.image.load("asset/decor/piece/coin3.png").convert_alpha()
        self.coin4 = pygame.image.load("asset/decor/piece/coin4.png").convert_alpha()
        self.coinscore = pygame.image.load("asset/decor/piece/coinscore.png").convert_alpha()

        
        self.i = 0 #compteur
        
        self.activer = False#permet de savoir si le cadeau qui contient la piece a été activé ou non
        
    def affichage(self):  #methode affichage
        if self.activer == True: #si la piece est activer
            if self.i <40: #tant que le compteur <40 on affiche la piece qui monte...
                self.i+=1
                self.y-=2.5

                if self.i%4 == 0:
                    self.screen.blit(self.coin1,(self.x,self.y))
                if self.i%4 == 1:
                    self.screen.blit(self.coin2,(self.x,self.y))
                if self.i%4 == 2:
                    self.screen.blit(self.coin3,(self.x,self.y))
                if self.i%4 == 3:
                    self.screen.blit(self.coin4,(self.x,self.y))

                self.screen.blit(self.coinscore,(self.x + 50,self.y-50)) # et le score que l'on décale un peu

                    
                        

class Particules: #classe particule, qui calcule la poussiere quand un bloc est cassé
    def __init__(self,block,x,y,xdif,ydif,dire,screen):
        self.block = block # le bloc qui est cassé
        self.dire = dire #la direction de la particule(droite ou gauche)
        self.screen = screen  # l'écran
        self.particule =  pygame.image.load("asset/decor/cube/particule.png").convert_alpha() #l'image de la particule

        self.x1 = self.block.x #coordoné x
        self.y1 = self.block.y #coordoné y 
        self.xdif = xdif #cette variable sert a savoir de quel coté du cube droite/gauche est la particule
        self.ydif = ydif #cette variable sert a savoir de quel coté du cube haut/droit est la particule

        self.monte = True #cette variable sert a savoir si la particule monte ou descend

    def affichage(self): #affichage de la particule
        if self.block.casse == False: # si le bloc n'est pas cassé
            self.x1 = self.block.x + self.xdif # alors la particule se recalque sur les cordonnés du bloc en se décalant du bon nombre de pixel pour allé dans le coin qui lui est assigné
            self.y1 = self.block.y - self.ydif
            self.y1b = self.y1 - 40 #on réinitialise y1b qui est la hauteur a partir de laquelle la particule va redescendre, pour s'assurer qu'il est toujours bien défini.
            
            
        if self.block.casse == True: #si le cube est cassé
            self.screen.blit(self.particule,(self.x1,self.y1)) #on affiche la particule
            if self.dire == 'L': # si il est dirigé vers la gauche, on le bouge a gauche
                self.x1-=0.5     
            if self.dire == 'D': # si il est dirigé vers la droite, on le bouge a droite
                self.x1+=0.5
                
            if self.y1 == self.y1b: #quand la coordonée y arrive a sa hauteur max
                self.monte = False #la particule cesse de monter
            if self.monte == True: #si elle monte, on diminue la coordonée y
                self.y1-=4 
            if self.monte == False: #sinon, on l'augmente
                self.y1+=4

    def scrolling(self,mario): #scrolling de la particule
                if pygame.key.get_pressed()[pygame.K_RIGHT] ==True  and mario.collider.collidelist(mario.scrolling) != -1:
                    self.x1-=mario.vitesse
               
                  

class Block:

    def __init__(self,screen,types = 'normal', score = '',cadeau ='piece'):

        #sons:
        self.sonblock = pygame.mixer.Sound ("asset/sound/smb_breakblock.wav")
        self.sonpiece = pygame.mixer.Sound ("asset/sound/smb_coin.wav")
        self.sonchamp = pygame.mixer.Sound ("asset/sound/smb_powerup_appears.wav")

        

        if types == 'normal': #si c'est un cube normal
            self.cube = pygame.image.load("asset/decor/cube/block3.png").convert_alpha() #image du cube normal
        elif types == 'cadeau': #si c'est un cube cadeau
            self.cube = pygame.image.load("asset/decor/cube/bloc2.png").convert_alpha() #image du cube cadeau 1
            self.cube2 = pygame.image.load("asset/decor/cube/bloc2_2.png").convert_alpha() #image du cube cadeau 2
        elif types =='indestructible': #si c'est un cube indestructible
            self.cube = pygame.image.load("asset/decor/cube/block.png").convert_alpha() #image du cube indestructible
        self.i=0 #timer pour 'laffichage du cube cadeau
        self.n=0 #timer bis pour 'laffichage du cube cadeau
        self.types = types   #le type
        self.screen = screen #la fenetre
        self.x = 0 # la position x
        self.y = 0 #la positioin y
        self.ysaut=self.y
        self.statut = "non" #le cube n'est pas affiche
        self.collider = self.cube.get_rect()
        self.collision = [self.collider]
        self.collider.move_ip(self.x,self.y) #on deplace les collider sur l'image
        self.ybase = self.y #la montee du cube
        self.cadeau = cadeau #le cadeau du cube
        self.piece = Coins(0,0,self.screen) #la piece dans le cadeau
        self.champignon = Champignons(0,0,self.screen) #le champignon dans le cadeau

    

        self.casse = False #le cube n'est pas casse
        self.particule = Particules(self,self.x,self.y,0,0,'L',screen) #les particules
        self.particule2 = Particules(self,self.x,self.y-40,0,40,'L',screen)
        self.particule3 = Particules(self,self.x+40,self.y,40,0,'D',screen)
        self.particule4 = Particules(self,self.x+40,self.y-40,40,40,'D',screen)
        self.particuleliste = [self.particule , self.particule2 , self.particule3 , self.particule4]
        self.score = score


    def affichage(self):

        self.n+=1 #le timer pour l'affichage
        if self.n == 20:
                        self.i+=1
                        self.n=0
                        
        if self.casse == False: #si le cube n'est pas casse
            self.screen.blit(self.cube,self.collider) #on affiche le cube
            if self.types == 'cadeau': #si c'est un cube cadeau
                    if self.i%2==0:  #celon le timer on affiche soit la version brillante, soit sombre du cube cadeau
                      self.screen.blit(self.cube,self.collider)
                    else:
                      self.screen.blit(self.cube2,self.collider)
        for particule in self.particuleliste:
             particule.affichage() #on regarde si on doit afficher particule

        if self.champignon.ia == False: #si le champignon du cube n'est pas actif, on lui demande de suivre le cube 
            if self.champignon.x != self.x and self.champignon.y != self.y:
                self.champignon.x = self.x
                self.champignon.y = self.y-44

            if self.champignon.x != self.x : 
                    self.champignon.x += self.x-self.champignon.x

        if self.champignon.ia == True: #si le champignon est actif
            self.champignon.affichage() #on l'affiche

        if self.piece.activer == False: #si la piece n'est pas active
                self.piece.x = self.x # on lui demande de suivre le cube
                self.piece.y = self.y-44 

        if self.piece.activer == True: #sinon on l'affiche
                self.piece.x += (-self.piece.x + self.x)
                self.piece.affichage()
                

            


    def scrolling(self,mario,vitesse):

                        
                if pygame.key.get_pressed()[pygame.K_RIGHT] ==True  and mario.collider.collidelist(mario.scrolling) != -1: #on active le scrolling de l'objet si mario est arrivé a la bordure droite de sa zone d'action
                    self.x-=mario.vitesse
                    self.collider.move_ip(-mario.vitesse,0)

                    for particule in self.particuleliste: #de meme on active le scrolling pour la particule
                        particule.scrolling(mario)
                 
                    
                
                    
                    
    def cadeauIa(self,static,mario): #cette methode a pour but de calculer le comportement du cadeau champignon si il est activé
            if self.champignon.ia == True:
                self.champignon.Ia(static,mario)
                self.champignon.collisionperso(mario,self.score)
        
    def collisionperso(self,perso): # cette methode calcule le comportement du cube si il rentre en collision avec le perso
        
        if self.types == 'normal': #si le cube est normal
            if perso.taille == 1: #et mario petit, le cube remonte
                if perso.colliderdessus.collidelist(self.collision) != -1:
                    if self.y==self.ysaut:
                        self.ysaut=self.y-20
                        self.ybase=self.y

                if self.y >self.ysaut and self.y <= self.ybase:
                    self.y-=2
                    self.collider.move_ip(0,-2)

                if self.y <= self.ysaut and self.y <= self.ybase:
                    self.ysaut = self.ybase
                    self.collider.move_ip(0,2)
                    self.y+=2
                if self.y>self.ybase and self.y-self.ybase <= 2:
                    
                    self.collider.move_ip(0,self.ybase-self.y)
                    self.y=self.ybase

            if perso.taille == 2: #si mario est grand
                if perso.colliderdessus.collidelist(self.collision) != -1: #le cube se casse
                    self.casse = True
                    self.sonblock.play()
                    self.collider.move_ip(0,1000)

        if self.types == 'cadeau': #si le cube est de type cadeau
            if perso.colliderdessus.collidelist(self.collision) != -1:
                if self.cadeau == "champignon": #et qu'il a un champignon
                    if self.champignon.ia == False: #si le cadeau n'a pas été pris
                            for collider in self.champignon.colliderliste: #on remonte le champignon
                                collider.move_ip(self.x,self.y-44)
                            self.champignon.ia = True #et on l'active 
                            self.sonchamp.play()#on joue le son du cadeau
                            self.types = 'indestructible' #le bloc n'a plus de cadeau, il devient de type 'indestructible'
                            self.cube = pygame.image.load("asset/decor/cube/block.png").convert_alpha() #on remplace donc l'image du cube cadeau par celui de cube indestructible
                            
                if self.cadeau == "piece":
                    if self.piece.activer == False: #si il n'a pas encore donné sa piece:
                        self.piece.activer = True
                        self.score.c += 200 #on rajoute 200 au score
                        self.score.p +=1 #on rajoute 1 au compteur de piece
                        self.sonpiece.play() #on joue le son du cadeau
                        self.types = 'indestructible' #le bloc n'a plus de cadeau, il devient de type 'indestructible'
                        self.cube = pygame.image.load("asset/decor/cube/block.png").convert_alpha()   #on remplace donc l'image du cube cadeau par celui de cube indestructible
 
class Pimp:
    """class tuyau"""
    
    def __init__(self,screen,taille = 1):

        #on regarde de quel taille est le tuyau
        if taille == 1: 
            self.pimp = pygame.image.load("asset/decor/pimp/pimp1.png").convert_alpha()
        elif taille == 2:
            self.pimp = pygame.image.load("asset/decor/pimp/pimp2.png").convert_alpha()
        elif taille == 3:
            self.pimp = pygame.image.load("asset/decor/pimp/pimp3.png").convert_alpha()

        self.screen = screen  
        self.x = 0 #il n'est pas encore placé, on l'initialise donc a 0,0 avec comme attribut statut = "non"
        self.y = 0
        self.statut = "non" 
        self.taille = taille
            
        self.collider = self.pimp.get_rect() #boite de collision du tuyeau
        self.collider.move_ip(self.x,self.y)


    def affichage(self):
        self.screen.blit(self.pimp,self.collider)   

    def scrolling(self,mario,vitesse): #scrolling du tuyau si mario arrive au bord de l'ecran
                if pygame.key.get_pressed()[pygame.K_RIGHT] ==True  and mario.collider.collidelist(mario.scrolling) != -1:
                    self.x-=mario.vitesse
                    self.collider.move_ip(-mario.vitesse,0)

    def collisionperso(self,mario): #n'a aucun but, cette fonction n'éxiste que pour pouvoir etre dans la meme liste que bloc, retourne donc la boolean True
                return True
        
                    
                                                  


class Esc:

        """class escalier"""

        def __init__(self,screen,taille = 1):
 
            if taille == 1: #on regarde de quel taille est l'escalier
                self.esc = pygame.image.load("asset/decor/cube/esc1.png").convert_alpha()
            elif taille == 2:
                self.esc = pygame.image.load("asset/decor/cube/esc2.png").convert_alpha()
            elif taille == 3:
                self.esc = pygame.image.load("asset/decor/cube/esc3.png").convert_alpha()
            else:
                self.esc = pygame.image.load("asset/decor/cube/esc4.png").convert_alpha()

            self.screen = screen
            self.x = 0 #il n'est pas encore placé, on l'initialise donc a 0,0 avec comme attribut statut = "non"
            self.y = 0
            self.statut = "non"
            self.taille = taille

            self.collider = self.esc.get_rect()
            self.collider.move_ip(self.x,self.y)


        def affichage(self):
            self.screen.blit(self.esc,self.collider)   

        def scrolling(self,mario,vitesse): #scrolling de l'escalier si mario arrive au bord de l'ecran
                    if pygame.key.get_pressed()[pygame.K_RIGHT] ==True  and mario.collider.collidelist(mario.scrolling) != -1:
                        self.x-=mario.vitesse
                        self.collider.move_ip(-mario.vitesse,0)
    
        def collisionperso(self,mario): #n'a aucun but, cette fonction n'éxiste que pour pouvoir etre dans la meme liste que bloc, retourne donc la boolean True
                return True


                    
    
def scrollingbis(liste,mario,vitesse,sol,level =1): #cette fonction gère le scrolling, l'affichage et la collision avec le personnage de la pluspart des éléments du jeu
    if level == 1: #si on est dans le level 1
        for terrain in sol: #on affiche le sol
            terrain.affichage()
            terrain.scrolling(mario,vitesse)

        for cube in liste: #pour tout les éléments contenu dans la lite 'liste'
            if cube.x<=860 and cube.x>=-300: #si il est dans les alentour de l'écran
                cube.affichage() #on l'affiche
                cube.collisionperso(mario) #et on calcule la collision avec le perso et le scrolling
                cube.scrolling(mario,vitesse)
            elif cube.x>840: #si il n'est jammais passé dans l'écran
                cube.scrolling(mario,vitesse) #on calcule le scrolling
               
