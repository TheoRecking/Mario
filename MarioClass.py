import pygame

class Mario:
    """class definissant Mario caracterise par:
              -sa vie
              -sa vitesse
              -sa direction
              -sa taille
              -son etat"""

    def __init__(self,vie,acceleration,screen,numero = 1):

        self.screen = screen #l'ecran

        self.vie = vie #le nombre de vie
        self.acceleration = acceleration #l'acceleration de mario
        self.vitesse = 0 
        self.right = True
        self.state = 'alive' #mario est en vie
        self.fin = False

        self.comptup1 = 0 #compteur pour la taille 1
        self.comptup2 = 0 #compteur pour la taille 2
        
        self.taille = 1 #mario a 2 taille, petit et normal, 1 = petit, 2 = normal

        self.x = 100
        self.y = 508
        if numero == 2:
            self.x = 300
        

        #les images de mario
        self.mario1=pygame.image.load("asset/mario/petit/mario_right_step1.png").convert_alpha()
        self.mario2=pygame.image.load("asset/mario/petit/mario_right_step2.png").convert_alpha()
        self.mario3=pygame.image.load("asset/mario/petit/mario_right_step3.png").convert_alpha()
        self.marioidle1=pygame.image.load("asset/mario/petit/mario.png").convert_alpha()

        self.marioidleG=pygame.image.load("asset/mario/grand/Super Mario.png").convert_alpha()
        self.mario1G=pygame.image.load("asset/mario/grand/Super Mario - Walk1.png").convert_alpha()
        self.mario2G=pygame.image.load("asset/mario/grand/Super Mario - Walk2.png").convert_alpha()
        self.mario3G=pygame.image.load("asset/mario/grand/Super Mario - Walk3.png").convert_alpha()

        self.mario1L=pygame.image.load("asset/mario/petit/mario_left_step1.png").convert_alpha()
        self.mario2L=pygame.image.load("asset/mario/petit/mario_left_step2.png").convert_alpha()
        self.mario3L=pygame.image.load("asset/mario/petit/mario_left_step3.png").convert_alpha()
        
        self.marioidle2=pygame.image.load("asset/mario/petit/mario_left.png").convert_alpha()
        self.marioidleLG=pygame.image.load("asset/mario/grand/Super MarioL.png").convert_alpha()
        
        self.mario1LG=pygame.image.load("asset/mario/grand/Super Mario - Walk1L.png").convert_alpha()
        self.mario2LG=pygame.image.load("asset/mario/grand/Super Mario - Walk2L.png").convert_alpha()
        self.mario3LG=pygame.image.load("asset/mario/grand/Super Mario - Walk3L.png").convert_alpha()
    
        self.mariojump1=pygame.image.load("asset/mario/petit/mario_right_jump.png").convert_alpha()
        self.mariojump2=pygame.image.load("asset/mario/petit/mario_left_jump.png").convert_alpha()

        self.mariojump1G=pygame.image.load("asset/mario/grand/Super Mario - Jump.png").convert_alpha() 
        self.mariojump2G=pygame.image.load("asset/mario/grand/Super Mario - JumpL.png").convert_alpha()

        self.jumpsound = pygame.mixer.Sound ("asset/sound/smb_jumpsmall.wav")
        self.jumpsound2 = pygame.mixer.Sound ("asset/sound/smb_jump-super.wav")
        self.retreci = pygame.mixer.Sound ("asset/sound/smb_pipe.wav")

        self.screen.blit(self.marioidle1,(self.x,self.y)) #affiche mario
        self.collider = self.marioidle1.get_rect()                           #on definis toutes les boites de collisions qui composent l'objet
        self.colliderdessous = pygame.Rect(self.x+7,self.y+42,22,1)       #celle du dessous
        self.colliderdessus =  pygame.Rect(self.x+7,self.y,22,1)          #celle du dessus
        self.colliderdroite = pygame.Rect(self.x+44,self.y+5,4,35)      #celle de droite
        self.collidergauche = pygame.Rect(self.x-3,self.y+5,4,35)       #celle de gauche
        self.collidergoumba = pygame.Rect(self.x,self.y+42,40,1)  
        self.colliderliste = [self.collider,self.colliderdessous,self.colliderdessus,self.colliderdroite,self.collidergauche,self.collidergoumba] # la liste de tout les colliders
        self.mort=[self.colliderdroite,self.collidergauche]    
    
        self.collider.move_ip(self.x,self.y) #la bloc de collision bouge vers Mario


        self.colliderscrolling = pygame.Rect(430,0,430,640) #deffinition de l'espace dans lequel mario ne peux pas aller
        self.scrollingx = 430
        self.scrolling = [self.colliderscrolling]


        
        self.v_x = 0 #la vitesse sur l'axe x
        self.v_y= 0 #la vitesse sur l'axe y
        self.v_saut = 0 #la vitesse du saut
        self.v_gravitation = 0 #la force de la gravitation
        self.jump = False #mario est t'il en train de sauter
        self.i = 0 #compteur1
        self.n = 0  #compteur2

        self.collidertrou = pygame.Rect(0,640,860,10) #si mario touche ce collider il est hor sde l'écran il meurt
        self.mortliste = [self.collidertrou]

        self.back = pygame.Rect(0,0,1,640)
        self.scrollback = [self.back] #collider qui empeche d'aller en arriere
        self.justkill = False
        





    def affichage(self,i):

        if self.taille == 1 and self.comptup1 > 0: #si la taille = 1 mais le compteur de taille superieur a 0 alors, mario est en train de rapetissir
            self.comptup2 +=1 #on lance donc le compteur pour la taille
            if self.comptup2 == 3:
                self.comptup1 -= 1
                self.comptup2 =0
                
        if self.taille == 2 and self.comptup1 < 21: #pareil si la taille = 2
            self.comptup2 +=1
            if self.comptup2 == 3:
                self.comptup1 += 1
                self.comptup2 =0
                
            
        if self.jump == True:       # si mario saute alors le sprite de mouvement est composé d'une seule image
            i = -1
        if self.vitesse > 0 and i >=0:  #si la vitesse de mario est > 0 donc il est tourné vers la droite.
            if i%3==0: #pour avoir un sprite en mouvement on se sert du reste de la division d'un compteur par 3. ce reste prend donc les valeurs 1, 2, ou 3
                if self.comptup1%2 == 0: # meme technique pour savoir si on doit afficher un mario grand ou petit
                    self.screen.blit(self.mario1,self.colliderdessus)
                else:
                    self.screen.blit(self.mario1G,self.colliderdessus) 
            elif i%3==1:
                if self.comptup1%2 == 0:
                    self.screen.blit(self.mario2,self.colliderdessus)
                else:
                    self.screen.blit(self.mario2G,self.colliderdessus)
            elif i%3==2:
                if self.comptup1%2 == 0:
                    self.screen.blit(self.mario3,self.colliderdessus)
                else:
                    self.screen.blit(self.mario3G,self.colliderdessus)

        if self.vitesse < 0 and i >=0:  #idem
            if i%3==0:
                if self.comptup1%2 == 0:
                    self.screen.blit(self.mario1L,self.colliderdessus)
                else:
                    self.screen.blit(self.mario1LG,self.colliderdessus)
            elif i%3==1:
                if self.comptup1%2 == 0:
                    self.screen.blit(self.mario2L,self.colliderdessus)
                else:
                    self.screen.blit(self.mario2LG,self.colliderdessus)
            elif i%3==2:
                if self.comptup1%2 == 0:
                    self.screen.blit(self.mario3L,self.colliderdessus)
                else:
                    self.screen.blit(self.mario3LG,self.colliderdessus)



        if self.vitesse == 0 and i >=0 and self.comptup1%2 == 0: #idem
            if self.right == True:
                self.screen.blit(self.marioidle1,self.colliderdessus)
            else:
                self.screen.blit(self.marioidle2,self.colliderdessus)


        if self.vitesse == 0 and i >=0 and self.comptup1%2 == 1:#idem
            if self.right == True:
                self.screen.blit(self.marioidleG,self.colliderdessus)
            else:
                self.screen.blit(self.marioidleLG,self.colliderdessus)

        if i == -1: #idem
            if self.right == True:
                if self.comptup1%2 == 0:
                    self.screen.blit(self.mariojump1,self.colliderdessus)
                else:
                    self.screen.blit(self.mariojump1G,self.colliderdessus)
            else:
                if self.comptup1%2 == 0:
                    self.screen.blit(self.mariojump2,self.colliderdessus)
                else:
                    self.screen.blit(self.mariojump2G,self.colliderdessus)

        if self.collider.collidelist(self.mortliste) != -1:
            self.state = "dead"
            
    


    def control(self, escalade = False):    #le control du personnage
    
        if self.jump == False or escalade == True:
            
            if self.collider.collidelist(self.scrolling) == -1 and pygame.key.get_pressed()[pygame.K_RIGHT] ==True: #si mario peut se deplacer vers la droite

                if self.vitesse <=6:    #si sa vitesse est inferieur a 5 (a regler)
                     self.vitesse+=self.acceleration # il accelere
                for collider in self.colliderliste:
                        collider.move_ip(self.vitesse,0) # il se deplace
          
            elif pygame.key.get_pressed() [pygame.K_LEFT]==True and self.collider.collidelist(self.scrollback) == -1: #si mario peut se deplacer vers la gauche (collider a definir pour qu'il ne sorte pas de l'ecran)

                if self.vitesse >0 : #si sa vitesse etait positive (mouvement vers la droite) elle redevient egale a 0
                    self.vitesse =0
                if self.vitesse >=-6: #il accelere tant que sa vitesse est superieur a -5
                    self.vitesse-=self.acceleration
                for collider in self.colliderliste:
                    collider.move_ip(self.vitesse,0)

            elif pygame.key.get_pressed() [pygame.K_LEFT]== False and pygame.key.get_pressed()[pygame.K_RIGHT] == False: #si aucunes touche n'est appuyee, sa vitesse redevient nul

                self.vitesse = 0
    
            elif self.collider.collidelist(self.scrolling) != -1 and self.vitesse == 0 and pygame.key.get_pressed()[pygame.K_RIGHT] ==True: #si il demmare colle a l'extremite de la zone dans laquelle il peut se deplacer, sa vitesse est directement egale a 5 (pour eviter les bugs)

                 self.vitesse = 6

            if self.vitesse > 0:
                self.right = True
            if self.vitesse <0:
                self.right = False
    


    def controlsaut(self,direction = ""):

    

        if direction == "gauche":

                 if pygame.key.get_pressed()[pygame.K_RIGHT] ==True: 
                        return True

        if direction == "droit":
                 if pygame.key.get_pressed() [pygame.K_LEFT]==True:
                        return True



    def surlesol(self,static): #return true si mario est sur le sol
                 if self.colliderdessous.collidelist(static) == -1: 
                    return False
                 else:
                     return True


    def saut(self,static):
        
        if self.justkill == True: #si mario vient de tuer un goomba
                self.jump = True #on active le saut
                self.v_gravitation = 0.97 #la force de la gravitation
                
                if self.vitesse>0: #selon la direction de mario, on initialise  la variable v_x qui sera la vitesse de maio sur l'axe x et v_saut qui seras la poussé que recevera Mario a chaque frame (d'abord vers le haut puis vers le bas)
                    self.v_x = self.vitesse-5
                    self.v_saut = (-self.vitesse-2)*2.2
                if self.vitesse<0:
                    self.v_saut = (self.vitesse-2)*2.2
                    self.v_x = self.vitesse+5
                if self.vitesse == 0:
                    self.v_saut = -8.5*2.3
                    self.v_x = 0

                self.v_y = self.v_saut
                self.i = 0
                self.n = 0
                    

        if self.jump == False and pygame.key.get_pressed() [pygame.K_q]==True and self.colliderdessous.collidelist(static)!=-1: #si on appuie sur la touche saut, alors on initialise le saut avec les memes variables que précédement
                    if self.taille == 1: #on joue le son du saut
                        self.jumpsound.play()
                    if self.taille == 2:
                        self.jumpsound2.play()

                    self.v_gravitation = 0.97 #la force de la gravitation
                    self.jump = True 

                    if self.vitesse>0:
                        self.v_x = self.vitesse-2
                        self.v_saut = (-self.vitesse-2)*2.9
                    if self.vitesse<0:
                        self.v_saut = (self.vitesse-2)*2.9
                        self.v_x = self.vitesse+2
                    if self.vitesse == 0:
                        self.v_saut = -8.5*3
                        self.v_x = 0

                    self.v_y = self.v_saut
                    self.i = 0 #compteur1
                    self.n = 0 #compteur2
        
        if self.jump == True and self.i<=1: #mario se souleve legerement (1 frame, c'est pour éviter tout contact de mario avec le sol, au début réel du saut)
                for collider in self.colliderliste:
                    collider.move_ip(0,self.v_y)
                self.v_y+=self.v_gravitation
                if self.collider.collidelist(self.scrolling) != -1:
                    self.v_x = 0
                self.i+=1



        if self.jump == True and self.surlesol(static) == False and self.i >1 and self.i < 18: #premiere étape du saut

                if self.v_x >=0 or self.v_x<0 and self.collider.collidelist(self.scrollback) == -1:
                    for collider in self.colliderliste: # on bouge mario de facon a effectuer le saut
                            collider.move_ip(self.v_x,self.v_y)   #on bouge mario 
                self.v_y+= self.v_gravitation   #on augmente v_y de facon a ce que mario est de plus en plus tendance a descendre
                if self.colliderdessus.collidelist(static) != -1 :# si on a une collision avec le haut de mario on descend
                        self.v_y=0.1       
                if self.v_x == 0 and self.collider.collidelist(self.scrolling) == -1: #si le saut etais surplace: on autorise le deplacement celon les touches de l'utilisateur                                                            
                             if pygame.key.get_pressed() [pygame.K_RIGHT]==True:
                                 self.v_x = 4
                             if pygame.key.get_pressed() [pygame.K_LEFT]==True:
                                 self.v_x = -4
                             self.control()

                if self.colliderdessus.collidelist(static) == -1: #si on a aucune collision vers le haut   
                    if self.colliderdroite.collidelist(static) != -1 and self.v_x > 0 or self.collidergauche.collidelist(static) != -1 and self.v_x < 0: #mais une collision vers la droite
                        if self.n<17: #mario escalade le mur pendant 17 frames
                            for collider in self.colliderliste: 
                                 collider.move_ip(0,-2)
                            self.control(True)
                            self.n+=1                       

                if self.collider.collidelist(self.scrolling) != -1 and self.v_x>0:
                             self.v_x = 0
                if self.n == 0 or self.n>15:        
                    self.i +=1


        if self.jump == True and self.surlesol(static) == False and self.i <80 and self.i >= 18: # tant que le joueur ne touche pas le sol:
                if self.v_x >=0 or self.v_x<0 and self.collider.collidelist(self.scrollback) == -1:
                    for collider in self.colliderliste: #on bouge mario
                                 collider.move_ip(self.v_x,self.v_y) 
                if self.controlsaut("droit")== True and self.v_x>0: #si on appuie sur la touche inverse a la direction, mario se stop
                             self.v_x = 1
                if self.controlsaut("gauche")== True and self.v_x<0:
                             self.v_x = -1
                self.v_y+= self.v_gravitation
                if self.colliderdessus.collidelist(static) != -1: # si on detecte une collision sur le dessus de la tete de mario on arrete de monter
                             self.v_y=0.1
                if self.collider.collidelist(self.scrolling) != -1 and self.v_x>0: #si le saut rentre dans la zone de scrolling, il s'arrete d'avancer
                             self.v_x = 0
                if self.v_x == 0 and self.collider.collidelist(self.scrolling) == -1:#si le saut etais surplace: on autorise le deplacement celon les touches de l'utilisateur                                           
                             if pygame.key.get_pressed() [pygame.K_RIGHT]==True:
                                 self.v_x = 4
                             if pygame.key.get_pressed() [pygame.K_LEFT]==True:
                                 self.v_x = -4
                self.i +=1
                

        if self.i >=80 or self.surlesol(static)==True: #si mario touche le sol, ou le 80 frames se sont deja écoulés, on arrete le saut

            self.jump = False
            

    def statut(self,ennemis): 
        for ennemi in ennemis: #si parmis tout les ennemis, mario en touche 1 par le collidergoomba, il meurt ou retrécis selon sa taille
            if ennemi.colliderdroite.collidelist(self.mort)!=-1 and ennemi.statut != 'alive' and self.comptup1 == 0 or ennemi.collidergauche.collidelist(self.mort)!=-1 and ennemi.statut != 'alive' and self.comptup1 == 0:
                self.state='dead'
            elif ennemi.collidergauche.collidelist(self.mort)!=-1 and ennemi.statut != 'alive' and self.comptup1 == 21 or ennemi.colliderdroite.collidelist(self.mort)!=-1 and ennemi.statut != 'alive' and self.comptup1 == 21 :
                self.taille = 1
                self.comptup1 -=1

                self.colliderdessus.move_ip(0,20) 
                self.collider.move_ip(0,-20)
                self.colliderdessous.move_ip(0,-20)
                self.colliderdroite.move_ip(0,-10)
                self.collidergauche.move_ip(0,-10)
                self.collidergoumba.move_ip(0,-10)
                self.retreci.play()
                
        self.justkill = False #mario meurt, il ne vient donc pas de tuer un goomba

       
class Sol:
    "classe du sol, tres sommaire qui permet son affichage"

    def __init__(self,screen,classe):
        
        self.screen = screen
        if classe == 1:
            self.sol = pygame.image.load("asset/sol/sol1.png").convert_alpha()
            self.x=0
            self.y=554
        elif classe == 2:
            self.sol = pygame.image.load("asset/sol/sol2.png").convert_alpha()
            self.x=2969
            self.y=554
        elif classe == 3:
            self.sol = pygame.image.load("asset/sol/sol3.png").convert_alpha()
            self.x=3702
            self.y=554
            
        elif classe == 4:
            self.sol = pygame.image.load("asset/sol/sol4.png").convert_alpha()
            self.x = 6579
            self.y=554
        
        self.collider = self.sol.get_rect()
        self.collider.move_ip(self.x,self.y)
        
    def affichage(self):

        self.screen.blit(self.sol,self.collider)

    def scrolling(self,mario,vitesse):
        if pygame.key.get_pressed()[pygame.K_RIGHT] ==True  and mario.collider.collidelist(mario.scrolling) != -1 and mario.fin == False:
                self.x-=mario.vitesse
                self.collider.move_ip(-mario.vitesse,0)
    def collisionperso(self,mario):
        return True



class Fond:
    """defilement du fond du jeu"""

    def __init__(self,screen):
        
        self.screen = screen
        self.x=0
        self.fond = pygame.image.load("asset/level_1-1/fond.png").convert_alpha()
        self.collider = self.fond.get_rect()
        
    def affichage(self):

        self.screen.blit(self.fond,self.collider)

    def scrolling(self,mario,vitesse):
        if pygame.key.get_pressed()[pygame.K_RIGHT] ==True  and mario.collider.collidelist(mario.scrolling) != -1 and mario.fin == False:
                self.x-=mario.vitesse
                self.collider.move_ip(-mario.vitesse,0)
    def collisionperso(self,mario):
        return True


        




        

