import pygame

def physique(movible, static):

    """definis la physique entre une liste d'element movible(ils doivent avoir une vitesse) et un liste d'element static"""


    for objet in movible: #tout les objets movibles
        if objet.colliderdessous.collidelist(static) == -1: #tombent si il ne sont pas sur des static
            for collider in objet.colliderliste:
                collider.move_ip(0,8)

        if objet.colliderdessous.collidelist(static) != -1: #si ils rentrent dans un static 
            while objet.colliderdessous.collidelist(static) != -1: #alors ils remontent tant qu'ils sont dedans

                for collider in objet.colliderliste:
                    collider.move_ip(0,-1)

            for collider in objet.colliderliste:
                    collider.move_ip(0,3)  



        

        
        if objet.colliderdroite.collidelist(static) != -1: #si ils touchent un objet a droite

           
            while objet.colliderdroite.collidelist(static) != -1: #ils ne peuvent pas rentrer dedans
                

                for collider in objet.colliderliste:
                    collider.move_ip(-1,0)

            for collider in objet.colliderliste:
                    collider.move_ip(-3,0)



        if objet.collidergauche.collidelist(static) != -1:   # pareil par la gauche
            while objet.collidergauche.collidelist(static) != -1:

                for collider in objet.colliderliste:
                    collider.move_ip(1,0)

            for collider in objet.colliderliste:
                    collider.move_ip(3,0)

                    
    
        if objet.colliderdessus.collidelist(static) != -1: #et pour le dessus
            while objet.colliderdessus.collidelist(static) != -1:

                for collider in objet.colliderliste:
                    collider.move_ip(0,1)

            for collider in objet.colliderliste:
                    collider.move_ip(0,3)           
                                   
