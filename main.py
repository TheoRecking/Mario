import pygame
import MarioClass
import TerrainClass
import CubeClass
import physique
import Timer
import cursorclass
import ActorClass
import Score
import flagClass

from flagClass import *
from ActorClass import  *
from physique import *
from CubeClass import *
from pygame import *
from MarioClass import *
from TerrainClass import *
from Timer import *
from cursorclass import *
from Score import*

pygame.init()





def level1(fenetre,vie):

        clock=pygame.time.Clock()

        """//////////////////////////
        ////  LES VARIABLES \\\\
        \\\\\\\\\\\\\\\\\\\\\\\\\\\""""
       
        music = pygame.mixer.music.load("asset/sound/mainmusic.mp3")
        mortmusic = pygame.mixer.Sound ("asset/sound/smb_mariodie.wav")
        gameovermusic = pygame.mixer.Sound ("asset/sound/smb_gameover.wav")
        winmusic = pygame.mixer.Sound ("asset/sound/smb_stage_clear.wav")

        """Le score"""
        score=Score(fenetre)
         
        

        gumba1 =Gumba(0,0,fenetre)
        gumba2 =Gumba(0,0,fenetre)
        gumba3 =Gumba(0,0,fenetre)
        gumba4 =Gumba(0,0,fenetre)
        gumba5 =Gumba(0,0,fenetre)
        gumba6 =Gumba(0,0,fenetre)
        gumba7 =Gumba(0,0,fenetre)
        gumba8 =Gumba(0,0,fenetre)
        gumba9 =Gumba(0,0,fenetre)
        gumba10 =Gumba(0,0,fenetre)
        gumba11 =Gumba(0,0,fenetre)
        gumba12 =Gumba(0,0,fenetre)
        gumba13 =Gumba(0,0,fenetre)
        gumba14 =Gumba(0,0,fenetre)
        gumba15 =Gumba(0,0,fenetre)
        gumba16 =Gumba(0,0,fenetre)

        gumbaliste = [gumba1,gumba2,gumba3,gumba4,gumba5,gumba6,gumba7,gumba8,gumba9,gumba10,gumba11,gumba12,gumba13,gumba14,gumba15,gumba16]
        
        mario = Mario(vie,1,fenetre)
        mario_w = pygame.image.load("asset/gui/mario_w.png")
        world = pygame.image.load("asset/gui/world.png")
        version = pygame.image.load("asset/gui/version.png")
        
        lifex3 = pygame.image.load("asset/gui/menu/lifex3.png")
        lifex2 = pygame.image.load("asset/gui/menu/lifex2.png")
        lifex1 = pygame.image.load("asset/gui/menu/lifex1.png")
        lifex0 = pygame.image.load("asset/gui/menu/lifex0.png")
        youwin = pygame.image.load("asset/gui/menu/youwin.png") 
        gameover = pygame.image.load("asset/gui/menu/gameover.png")
        

        """cube normal:"""
        cube1 = Block(fenetre)
        cube2 = Block(fenetre)
        cube3 = Block(fenetre)
        cube4 = Block(fenetre)
        cube5 = Block(fenetre)
        cube6 = Block(fenetre)
        cube7 = Block(fenetre)
        cube8 = Block(fenetre)
        cube9 = Block(fenetre)
        cube10 = Block(fenetre)
        cube11 = Block(fenetre)
        cube12 = Block(fenetre)
        cube13 = Block(fenetre)
        cube14 = Block(fenetre)
        cube15 = Block(fenetre)
        cube16 = Block(fenetre)
        cube17 = Block(fenetre)
        cube18 = Block(fenetre)
        cube19 = Block(fenetre)
        cube20 = Block(fenetre)
        cube21 = Block(fenetre) 
        cube22 = Block(fenetre)
        cube23 = Block(fenetre)
        cube24 = Block(fenetre)
        cube25 = Block(fenetre)
        cube26 = Block(fenetre)
        cube27 = Block(fenetre)
        cube28 = Block(fenetre)
        cube29 = Block(fenetre)
        cube30 = Block(fenetre)
        cube31 = Block(fenetre)
        cube32 = Block(fenetre)
        cube33 = Block(fenetre)
        


        """cube cadeau"""

        cubecad1 = Block(fenetre,'cadeau',score)
        cubecad2 = Block(fenetre,'cadeau',score,'champignon')
        cubecad3 = Block(fenetre,'cadeau',score)
        cubecad4 = Block(fenetre,'cadeau',score)
        cubecad5 = Block(fenetre,'cadeau',score)
        cubecad6 = Block(fenetre,'cadeau',score)
        cubecad7 = Block(fenetre,'cadeau',score)
        cubecad8 = Block(fenetre,'cadeau',score)
        cubecad9 = Block(fenetre,'cadeau',score)

        """cube indestructible"""

        indecube1 =  Block(fenetre,'indestructible')
        indecube2 = Block(fenetre,'indestructible')
        indecube3 = Block(fenetre,'indestructible')

        """pimp"""

        pimp1 = Pimp(fenetre,1)
        pimp2 = Pimp(fenetre,1)
        pimp3 = Pimp(fenetre,1)
        pimp4 = Pimp(fenetre,2)
        pimp5 = Pimp(fenetre,3)
        pimp6 = Pimp(fenetre,3)

        """trou"""

        sol1 = Sol (fenetre, 1)
        sol2 = Sol (fenetre, 2)
        sol3 = Sol (fenetre, 3)
        sol4 = Sol (fenetre, 4)

        """escalier"""
        esc1=Esc(fenetre,1)
        esc2=Esc(fenetre,1)
        esc3=Esc(fenetre,1)
        esc4=Esc(fenetre,1)
        esc5=Esc(fenetre,1)
        esc6=Esc(fenetre,1)
        esc7=Esc(fenetre,2)
        esc8=Esc(fenetre,2)
        esc9=Esc(fenetre,2)
        esc10=Esc(fenetre,2)
        esc11=Esc(fenetre,2)
        esc12=Esc(fenetre,2)
        esc13=Esc(fenetre,3)
        esc14=Esc(fenetre,3)
        esc15=Esc(fenetre,3)
        esc16=Esc(fenetre,3)
        esc17=Esc(fenetre,3)
        esc18=Esc(fenetre,3)
        esc19=Esc(fenetre,4)
        esc20=Esc(fenetre,4)
        esc21=Esc(fenetre,4)
        esc22=Esc(fenetre,4)
        esc23=Esc(fenetre,4)
        esc24=Esc(fenetre,4)
        esc25=Esc(fenetre,4)
        esc26=Esc(fenetre,4)
        esc27=Esc(fenetre,4)
        esc28=Esc(fenetre,4)
        esc29=Esc(fenetre,4)
        esc30=Esc(fenetre,4)
        esc31=Esc(fenetre,4)




        """ Le fond"""

        fond = Fond(fenetre)

        """Le timer"""
        timer=Timer(fenetre)

        """le drapeau"""
        flag = Flag(1,fenetre)

        """les listes de collisions et d'objets:"""

        escalier = [esc1,esc2,esc3,esc4,esc5,esc6,esc7,esc8,esc9,esc10,esc11,esc12,esc13,esc14,esc15,esc16,esc17,esc18,esc19,esc20,esc21,esc22,esc23,esc24,esc25,esc26,esc27,esc28,esc29,esc30,esc31]
        escaliercollider=[esc1.collider,esc2.collider,esc3.collider,esc4.collider,esc5.collider,esc6.collider,esc7.collider,esc8.collider,esc9.collider,esc10.collider,esc11.collider,esc12.collider,esc13.collider,esc14.collider,esc15.collider,esc16.collider,esc17.collider,esc18.collider,esc19.collider,esc20.collider,esc21.collider,esc22.collider,esc23.collider,esc24.collider,esc25.collider,esc26.collider,esc27.collider,esc28.collider,esc29.collider,esc30.collider,esc31.collider]


        indecube = [indecube1,indecube2,indecube3]
        indecubecollider = [indecube1.collider,indecube2.collider,indecube3.collider]

        pimp = [pimp1,pimp2,pimp3,pimp4,pimp5,pimp6] 
        pimpcollider = [pimp1.collider,pimp2.collider,pimp3.collider,pimp4.collider,pimp5.collider,pimp6.collider]

        trou = [fond,sol1,sol2,sol3,sol4]
        troucollider =[sol1.collider,sol2.collider,sol3.collider,sol4.collider]
        
        cube=[cube1,cube2,cube3,cube4,cube5,cube6,cube7,cube8,cube9,cube10,cube11,cube12,cube13,cube14,cube15,cube16,cube17,cube18,cube19,cube20,cube21,cube22,cube23,cube24,cube25,cube26,cube27,cube28,cube29,cube30,cube31,cube32,cube33]
        cubecollider = [cube1.collider,cube2.collider,cube3.collider,cube4.collider,cube5.collider,cube6.collider,cube7.collider,cube8.collider,cube9.collider,cube10.collider,cube11.collider,cube12.collider,cube13.collider,cube14.collider,cube15.collider,cube16.collider,cube17.collider,cube18.collider,cube19.collider,cube20.collider,cube21.collider,cube22.collider,cube23.collider,cube24.collider,cube25.collider,cube26.collider,cube27.collider,cube28.collider,cube29.collider,cube30.collider,cube31.collider,cube32.collider,cube33.collider]


        cubecad=[cubecad1,cubecad2,cubecad3,cubecad4,cubecad5,cubecad6,cubecad7,cubecad8,cubecad9]
        cubecadcollider=[cubecad1.collider,cubecad2.collider,cubecad3.collider,cubecad4.collider,cubecad5.collider,cubecad6.collider,cubecad7.collider,cubecad8.collider,cubecad9.collider]

        cubetotal = cube + cubecad + pimp + indecube + escalier + [flag]
        terrain(fenetre,cube,cubecad,pimp,indecube,escalier,1,gumbaliste)
        pygame.display.update()

        
        back = pygame.Rect(0,0,1,640)
        scrollback = [back]
        
        static = indecubecollider+pimpcollider+cubecollider+cubecadcollider+escaliercollider+troucollider + scrollback
        static2 = indecubecollider+pimpcollider+cubecollider+cubecadcollider+escaliercollider+troucollider #la liste des statics
        movible = [mario]
        
        actualiser =  trou


        """//////////////////////////
        ////  LE PROGRAMME  \\\\
        \\\\\\\\\\\\\\\\\\\\\\\\\\\""""

        i=0
        n=0
        time=pygame.image.load("asset/gui/Timer.png").convert_alpha()
        quitter = False
        inlevel = True
        compteurmort = 0

        pygame.mixer.music.play()

        #if vie == 4:
                #mario.state = "dead"
        
        
        while not quitter == True: # toutes les image, l'ordi recalcule:
                
                if inlevel == True:
                    
                        if mario.state == "alive" and mario.fin == False:

                                mario.saut(static) #on test si le joueur saute  
                                mario.control() #on active le control de mario
                        
                                if mario.vitesse!=0:    
                                        n+=1
                                        if n == 4:
                                                i+=1
                                                n=0
                                if mario.vitesse == 0:
                                        i=0
                                        n=0
                                
                                scrollingbis(cubetotal,mario,mario.vitesse,trou) # on actualise le scrolling du terrain
                                mario.statut(gumbaliste) #on test si mario meurt
                                
                                for gumba in gumbaliste: #on active tout les goombas
                                        gumba.Ia(static2, mario,score)
                                        gumba.affichage()

                                for cube in cubecad: #on active les champignons qui sont sortis des cubes cadeaux
                                        cube.cadeauIa(static,mario)

                                   
                                physique(movible,static) #on active la physique
                                mario.affichage(i) #on affiche mario
                                timer.affichage() #on affiche le timer
                                fenetre.blit(time,(730,20))
                                score.affichage() #le score
                                fenetre.blit(mario_w,(30,10))
                                fenetre.blit(world,(500,10))
                                compteurmort = 0 #le compteur mort de mario = 0 car mario n'est pas mort
                               

                        if mario.state == "dead": #si mario meurt, on joue la musique de fin selon le nombre de vie restant a Mario
                                pygame.mixer.music.stop()
                                if compteurmort == 0 and mario.vie != 0:
                                        mortmusic.play()
                                if compteurmort == 0 and mario.vie == 0:
                                        gameovermusic.play()
                                
                                        
                                compteurmort +=1 #le compteur de mort de mario s'active
 
                                if vie == 4: #on affiche differents messages selon les vie restantes a Mario
                                        fenetre.blit(lifex3,(0,0))

                                if vie == 3:
                                        fenetre.blit(lifex2,(0,0))
                                
                                if vie == 2:
                                        fenetre.blit(lifex1,(0,0))
                                        
                                if vie == 1:
                                        fenetre.blit(lifex0,(0,0))
                                        
                                if vie == 0:
                                        fenetre.blit(gameover,(0,0))

                                
                                if compteurmort == 100 and vie != 0: #quend le compteur mort est finis, si il reste des vies
                                        level1(fenetre,vie-1) #on relance le level, une vie en moins
                                        inlevel = False #puis on quitte la fonction
                                        quitter = True
                                        
                                        
                                if compteurmort == 100 and vie == 0: #si il n'y a plus de vie, on quitte la fonction
                                    
                                        inlevel = False
                                        quitter = True

                        if mario.fin == True: #si mario est arrivé a la fin

                                if compteurmort == 0:
                                        winmusic.play() #on joue le compteur de la victoire
                                        fenetre.blit(youwin,(0,0))
                                        timer.affichage() #on affiche le temps pour faire le niveau
                                pygame.mixer.music.stop()
                                compteurmort +=1
                                fenetre.blit(time,(730,20))
                                score.affichage()
                                fenetre.blit(mario_w,(30,10))
                                fenetre.blit(world,(500,10))
                               
                                if compteurmort == 300: #si le compteur de temps est arrivé a 300, on revient au menu
                        
                                        inlevel = False
                                        quitter = True

                                
                
                clock.tick(60) #attendre 1/60 secondes    
                pygame.event.pump()#l'image se rafraiche toutes les /60 de secondes
                pygame.display.flip() #on actualise l'écran
                pygame.display.update() #on actualise l'écran

        
      
       
