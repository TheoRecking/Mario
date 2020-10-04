import pygame


    
def terrain(screen,cubeliste,cubecadliste,pimpliste,indecubeliste,escliste,numero,gumbaliste):
    
            if numero == 1:
                    ID=pygame.image.load("asset/level_1-1/lvl1.png").convert_alpha()
            else:
                    ID=pygame.image.load("asset/level_1-1/lvltest.png").convert_alpha()

            screen.blit(ID, (0,0))

          

            """ premier affichage du terrain:"""


             
            for x in  range (0,205):     #test a chaque pixel de l'ID map la couleur de celui ci et tente de savoir si elle correspond a un cube         
                for y in range (0,16):

                        color = screen.get_at((x,y))
                        if color == pygame.Color(0,74,127,255): #lorsqu'une couleur est detectee:
                                cbon = False
                                for cube in cubeliste: #on test chaque cube
                                        if cube.statut == "non" and cbon == False: #si le cube n'est pas place:
                                                cube.x = x*43
                                                cube.y = y*43
                                                cube.ysaut=cube.y
                                                cube.ybase=cube.y
                                                cube.statut = "oui"
                                                cube.collider.move_ip(cube.x,cube.y)
                                                cbon = True

                        elif color == pygame.Color(255,255,0,255): #lorsqu'une couleur est detectee:
                                cbon = False
                                for cube in cubecadliste: #on test chaque cube
                                        if cube.statut == "non" and cbon == False: #si le cube n'est pas place:
                                                cube.x = x*43
                                                cube.y = y*43
                                                cube.statut = "oui"
                                                cube.collider.move_ip(cube.x,cube.y)
                                                cbon = True


                        elif color == pygame.Color(181,230,29,255): #lorsqu'une couleur est detectee:
                                cbon = False
                                for pimp in pimpliste: #on test chaque pimp
                                        if pimp.statut == "non" and cbon == False and pimp.taille == 1: #si le cube n'est pas place:
                                                pimp.x = x*43
                                                pimp.y = y*43
                                                pimp.statut = "oui"
                                                pimp.collider.move_ip(pimp.x,pimp.y)
                                                cbon = True

                        elif color == pygame.Color(0,255,0,255): #lorsqu'une couleur est detectee:
                                cbon = False
                                for pimp in pimpliste: #on test chaque pimp
                                        if pimp.statut == "non" and cbon == False and pimp.taille == 2: #si le cube n'est pas place:
                                                pimp.x = x*43
                                                pimp.y = y*43                                              
                                                pimp.statut = "oui"
                                                pimp.collider.move_ip(pimp.x,pimp.y)
                                                cbon = True

                        elif color == pygame.Color(34,177,76,255): #lorsqu'une couleur est detectee:
                                cbon = False
                                for pimp in pimpliste: #on test chaque pimp
                                        if pimp.statut == "non" and cbon == False and pimp.taille == 3: #si le tuyeau n'est pas place:
                                                pimp.x = x*43
                                                pimp.y = y*43                                              
                                                pimp.statut = "oui"
                                                pimp.collider.move_ip(pimp.x,pimp.y)
                                                cbon = True


                        elif color == pygame.Color(127,51,0,255): #lorsqu'une couleur est detectee:
                                cbon = False
                                for cube in indecubeliste: #on test chaque cube
                                        if cube.statut == "non" and cbon == False: #si le cube n'est pas place:
                                                cube.x = x*43
                                                cube.y = y*43                                              
                                                cube.statut = "oui"
                                                cube.collider.move_ip(cube.x,cube.y)
                                                cbon = True

                        elif color == pygame.Color(237,28,36,255): #lorsqu'une couleur est detectee:
                                cbon = False
                                for esc in escliste: #on test chaque escalier
                                        if esc.statut == "non" and cbon == False and esc.taille == 1: #si l'escalier n'est pas place:
                                                esc.x = x*43
                                                esc.y = y*43
                                                esc.statut = "oui"
                                                esc.collider.move_ip(esc.x,esc.y)
                                                cbon = True

                        elif color == pygame.Color(255,127,39,255): #lorsqu'une couleur est detectee:
                                cbon = False
                                for esc in escliste: #on test chaque escalier
                                        if esc.statut == "non" and cbon == False and esc.taille == 2: #si l'escalier n'est pas place:
                                                esc.x = x*43
                                                esc.y = y*43                                            
                                                esc.statut = "oui"
                                                esc.collider.move_ip(esc.x,esc.y)
                                                cbon = True

                        elif color == pygame.Color(255,200,0,255): #lorsqu'une couleur est detectee:
                                cbon = False
                                for esc in escliste: #on test chaque escalier
                                        if esc.statut == "non" and cbon == False and esc.taille == 3: #si l'escalier n'est pas place:
                                                esc.x = x*43
                                                esc.y = y*43                                             
                                                esc.statut = "oui"
                                                esc.collider.move_ip(esc.x,esc.y)
                                                cbon = True

                        elif color == pygame.Color(239,228,176,255): #lorsqu'une couleur est detectee:
                                cbon = False
                                for esc in escliste: #on test chaque escalier
                                        if esc.statut == "non" and cbon == False and esc.taille == 4: #si l'escalier n'est pas place:
                                                esc.x = x*43
                                                esc.y = y*43                                           
                                                esc.statut = "oui"
                                                esc.collider.move_ip(esc.x,esc.y)
                                                cbon = True



                        elif color == pygame.Color(232,169,18,255): #lorsqu'une couleur est detectee:
                                cbon = False
                                for gumba in gumbaliste: #on test chaque escalier
                                        if gumba.statut == "non" and cbon == False: #si l'escalier n'est pas place:
                                                gumba.x = x*43
                                                gumba.y = y*43                                           
                                                gumba.statut = "oui"
                                                for collider in gumba.colliderliste:
                                                        collider.move_ip(gumba.x,gumba.y)
                                                cbon = True
                                           
                                           
                               
  

                        


                               

                                                        
                                

                        
