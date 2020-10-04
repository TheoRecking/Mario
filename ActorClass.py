# -*- coding: cp1252 -*-
import pygame

class Actor:

    def __init__ (self,x,y,screen):

        self.screen = screen #l'ecran
        self.x = x #x
        self.y = y #y
        self.right = True #il est tourné vers la droite
        self.statut = "non" #sert pour savoir si il a été placé ou non (TerrainClass)
        
        self.actor=pygame.image.load("asset/ennemies/goombas.png").convert_alpha() #image de l'acteur
        self.scoremort = pygame.image.load("asset/decor/piece/coinscore.png").convert_alpha() #image (200 pts)
        self.scoremort2 = pygame.image.load("asset/decor/piece/coinscore2.png").convert_alpha() #image (1000 pts)

        
        self.screen.blit(self.actor,(self.x,self.y)) #affiche l'acteur

        self.collider = self.actor.get_rect()                           #on definis toutes les boites de collisions qui composent l'objet
        self.colliderdessous = pygame.Rect(self.x+7,self.y+42,22,1)       #celle du dessous
        self.colliderdessus =  pygame.Rect(self.x-3,self.y-1,50,1)          #celle du dessus
        self.colliderdroite = pygame.Rect(self.x+41,self.y+5,4,35)      #celle de droite
        self.collidergauche = pygame.Rect(self.x-3,self.y+5,4,35)            #celle de gauche
        self.colliderpoint = pygame.Rect(self.x+50,self.y-30,1,1)        #collider du score
        

        self.colliderliste = [self.collider,self.colliderdessous,self.colliderdessus,self.colliderdroite,self.collidergauche,self.colliderpoint] #liste de tous les colliders
        
        
        self.collider.move_ip(self.x,self.y) #on deplace le collider a la bonne coordonée
        self.state='alive' #il est vivant


    def Ia (self,static,mario): #IA

        if pygame.key.get_pressed()[pygame.K_RIGHT] ==True  and mario.collider.collidelist(mario.scrolling) != -1: #Scrolling
            self.x-=mario.vitesse
            for collider in self.colliderliste :
                collider.move_ip(-mario.vitesse,0)

        if self.state == 'alive':   #Physique
            if self.colliderdessous.collidelist(static) == -1:
                for collider in self.colliderliste:
                    self.y+=8
                    collider.move_ip(0,8)

            if self.colliderdessous.collidelist(static) != -1: #Physique(2)
                while self.colliderdessous.collidelist(static) != -1:
                    for collider in self.colliderliste:
                        self.y-=1
                        collider.move_ip(0,-1)
                for collider in self.colliderliste:
                        self.y +=3
                        collider.move_ip(0,3) 

            if self.colliderdroite.collidelist(static) != -1: #si il touche un mur il change de direction
                self.right = False
               
            elif self.collidergauche.collidelist(static) != -1:
                self.right = True
    

            if mario.x-self.x < 870 and mario.x-self.x >-1500:    #si le goumba est assez proche de mario , il se déplace (2 pixel par rafraichissement)
                if self.right == True:  
                    self.x += 2
                    for collider in self.colliderliste:
                        collider.move_ip (2,0)
                if self.right == False:
                    self.x -=2
                    for collider in self.colliderliste:
                        collider.move_ip (-2,0)

    def affichage(self):
                
        self.screen.blit(self.actor, self.collider )


class Gumba(Actor): #la classe Gumba qui hérite de Actor

    def __init__(self,x,y,screen):

        Actor.__init__(self,x,y,screen) #on initialise les arguments d'Actor
        self.right = False #les gumbas sont tournés vers la gauche
        self.actor2=pygame.image.load("asset/ennemies/goombas2.png").convert_alpha()
        self.mort=[self.colliderdessus] #le collider qui permet de savoir si le gumba meurt ou pas
        self.colliderdessus.move_ip(0,-5) #on le remonte pour eviter les bugs de collisions
        self.i = 0 #compteur partie 1
        self.n = 0 #compteur partie 2
        self.dead=pygame.image.load("asset/ennemies/goombas_dead.png").convert_alpha() #image du gumba mort
        self.timermort = 0 #timeur du gumba mort
        self.son = pygame.mixer.Sound ("asset/sound/smb_kick.wav") #son du gumba quand il meurt

    def Ia(self,static,mario,score):
        Actor.Ia(self,static,mario) #on appel Ia de Actor(class)
        
        if  mario.collider.collidelist(self.mort)!=-1 and mario.state == 'alive' and mario.comptup1 == 0 or mario.collider.collidelist(self.mort)!=-1 and mario.state == 'alive' and mario.comptup1 == 21:
            #si mario est grand ou petit et qu'il touche la tete du gumba:
            
            self.state='dead'#le gumba meurt
            self.son.play() #on joue le son du gumba qui meurt
            
            score.c += 200 #on augmente le score de 200
            mario.justkill = True #mario vient juste de tuer un gumba
            self.colliderdroite.move_ip(0,1000) #on elimine les colliders pour qu'ils ne gènent pas
            self.collidergauche.move_ip(0,1000)
            self.colliderdessus.move_ip(0,1000)

        if self.state =='dead':
            self.timermort+=1   #si il est mort, on lance le timer mort

    def affichage(self):
        if self.state == 'alive': #si il est en vie
            self.n += 1 #le premier timer se lance
            if self.n > 8: #si le premier timer est superieur a 8
                self.i+=1 #le deuxieme timer s'augmente
                self.n = 0 #le premier revient a 0
            
            if self.i % 2 == 0: #si le reste du timer 2 /2 = 0
                self.screen.blit(self.actor, self.collider ) #on affiche une premiere image
            if self.i % 2 == 1: #sinon
                self.screen.blit(self.actor2, self.collider ) #on affiche une autre

        elif self.timermort <= 100: #si le timermort est pas encore a 100
            self.screen.blit(self.dead,self.collider) # on affiche le gumba mort
            if self.timermort <= 50:
                self.screen.blit(self.scoremort,self.colliderpoint) #si le timermort n'est pas arrivé a 50 on affiche le score

class Champignons (Actor): #la classe Champignon qui hérite de Actor

    def __init__(self,x,y,screen):
        Actor.__init__(self,x,y,screen)     #on initialise les arguments d'Actor                     
        self.actor=pygame.image.load("asset/ennemies/shroom.png").convert_alpha()   #on appel l'image champignon
        self.mort=[self.colliderdessous,self.colliderdessus,self.colliderdroite,self.collidergauche] #les colliders entraint un champignon pris
        self.ia = False #de base le champignon est dans un cube, donc son Ia est desactivée
        self.timermort = 0 #le timermort
        self.son = pygame.mixer.Sound ("asset/sound/smb_powerup.wav") #le son

    def collisionperso(self,mario,score): #collision avec le perso
        if mario.collider.collidelist(self.mort)!=-1 and mario.state=='alive':
            self.son.play()
            self.state='dead' #le champignon meurt
            score.c += 1000 #on augmente le score
            for collider in self.mort:
                collider.move_ip(0,1000) #on bouge le collider pour qu'il ne gene plus
                
            if mario.taille == 1: #si mario est petit, il devient grand, on ajuste donc les colliders
                mario.colliderdessus.move_ip(0,-20) 
                mario.collider.move_ip(0,20)
                mario.colliderdessous.move_ip(0,20)
                mario.colliderdroite.move_ip(0,10)
                mario.collidergauche.move_ip(0,10)
                mario.collidergoumba.move_ip(0,10)
            mario.taille=2
            mario.y=mario.y-20 #mario grandit de 20 pixel vers le haut

    def affichage(self): #affichage
        if self.state=='alive':
            self.screen.blit(self.actor,self.collider)

        if self.state=='dead':
            if self.timermort <= 50:
                self.screen.blit(self.scoremort2,self.colliderpoint)
                self.timermort+=1
                
    def scrolling(self,mario,vitesse): #scrolling
        if pygame.key.get_pressed()[pygame.K_RIGHT] ==True  and mario.collider.collidelist(mario.scrolling) != -1:
                    self.x-=mario.vitesse
                    for collider in self.colliderliste:
                        collider.move_ip(-mario.vitesse,0)


            
        
            
