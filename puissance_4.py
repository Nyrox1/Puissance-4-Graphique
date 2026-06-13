from graphics_nsi import*


Tableau=[0,0,0,0,0,0,0]

case = [ [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]




#Le damier du jeu
def grille():
    for j in range(0,6):
        j=j*100+50
        for i in range(0,7):
            attendre(50)
            i=i*100+50
            P=Point(i,j)
            draw_fill_rectangle(P,75,75,blue)
    return


def grilleRouge():
    for j in range(0,6):
        j=j*100+50
        for i in range(0,7):
            attendre(50)
            i=i*100+50
            P=Point(i,j)
            draw_fill_rectangle(P,75,75,red)
    return


def grilleJaune():
    for j in range(0,6):
        j=j*100+50
        for i in range(0,7):
            attendre(50)
            i=i*100+50
            P=Point(i,j)
            draw_fill_rectangle(P,75,75,yellow)
    return


def dessineJeton(P,couleur):
    #Premiere colonne
    if P.x<100:
        P=Point(50,550-100*Tableau[0])
        draw_fill_circle(P,30,couleur)
        if couleur==red:
            if Tableau[0]==0:
                case[5][0]+=1
            elif Tableau[0]==1:
                case[4][0]+=1
            elif Tableau[0]==2:
                case[3][0]+=1
            elif Tableau[0]==3:
                case[2][0]+=1
            elif Tableau[0]==4:
                case[1][0]+=1
            else:
                case[0][0]+=1
        else:
            if Tableau[0]==0:
                case[5][0]+=50
            elif Tableau[0]==1:
                case[4][0]+=50
            elif Tableau[0]==2:
                case[3][0]+=50
            elif Tableau[0]==3:
                case[2][0]+=50
            elif Tableau[0]==4:
                case[1][0]+=50
            else:
                case[0][0]+=50
        Tableau[0]+=1
    #Deuxieme colonne
    elif P.x<200:
        P=Point(150,550-100*Tableau[1])
        draw_fill_circle(P,30,couleur)
        if couleur==red:
            if Tableau[1]==0:
                case[5][1]+=1
            elif Tableau[1]==1:
                case[4][1]+=1
            elif Tableau[1]==2:
                case[3][1]+=1
            elif Tableau[1]==3:
                case[2][1]+=1
            elif Tableau[1]==4:
                case[1][1]+=1
            else:
                case[0][1]+=1
        else:
            if Tableau[1]==0:
                case[5][1]+=50
            elif Tableau[1]==1:
                case[4][1]+=50
            elif Tableau[1]==2:
                case[3][1]+=50
            elif Tableau[1]==3:
                case[2][1]+=50
            elif Tableau[1]==4:
                case[1][1]+=50
            else:
                case[0][1]+=50
        Tableau[1]+=1
    #toisieme colonne
    elif P.x<300:
        Q=Point(250,550-100*Tableau[2])
        draw_fill_circle(Q,30,couleur)
        if couleur==red:
            if Tableau[2]==0:
                case[5][2]+=1
            elif Tableau[2]==1:
                case[4][2]+=1
            elif Tableau[2]==2:
                case[3][2]+=1
            elif Tableau[2]==3:
                case[2][2]+=1
            elif Tableau[2]==4:
                case[1][2]+=1
            else:
                case[0][2]+=1
        else:
            if Tableau[2]==0:
                case[5][2]+=50
            elif Tableau[2]==1:
                case[4][2]+=50
            elif Tableau[2]==2:
                case[3][2]+=50
            elif Tableau[2]==3:
                case[2][2]+=50
            elif Tableau[2]==4:
                case[1][2]+=50
            else:
                case[0][2]+=50
        Tableau[2]+=1
    #quatrieme colonne
    elif P.x<400:
        P=Point(350,550-100*Tableau[3])
        draw_fill_circle(P,30,couleur)
        if couleur==red:
            if Tableau[3]==0:
                case[5][3]+=1
            elif Tableau[3]==1:
                case[4][3]+=1
            elif Tableau[3]==2:
                case[3][3]+=1
            elif Tableau[3]==3:
                case[2][3]+=1
            elif Tableau[3]==4:
                case[1][3]+=1
            else:
                case[0][3]+=1
        else:
            if Tableau[3]==0:
                case[5][3]+=50
            elif Tableau[3]==1:
                case[4][3]+=50
            elif Tableau[3]==2:
                case[3][3]+=50
            elif Tableau[3]==3:
                case[2][3]+=50
            elif Tableau[3]==4:
                case[1][3]+=50
            else:
                case[0][3]+=50
        Tableau[3]+=1
    #cinquieme colonne
    elif P.x<500:
        P=Point(450,550-100*Tableau[4])
        draw_fill_circle(P,30,couleur)
        if couleur==red:
            if Tableau[4]==0:
                case[5][4]+=1
            elif Tableau[4]==1:
                case[4][4]+=1
            elif Tableau[4]==2:
                case[3][4]+=1
            elif Tableau[4]==3:
                case[2][4]+=1
            elif Tableau[4]==4:
                case[1][4]+=1
            else:
                case[0][4]+=1
        else:
            if Tableau[4]==0:
                case[5][4]+=50
            elif Tableau[4]==1:
                case[4][4]+=50
            elif Tableau[4]==2:
                case[3][4]+=50
            elif Tableau[4]==3:
                case[2][4]+=50
            elif Tableau[4]==4:
                case[1][4]+=50
            else:
                case[0][4]+=50
        Tableau[4]+=1
    #sixieme colonne
    elif P.x<600:
        P=Point(550,550-100*Tableau[5])
        draw_fill_circle(P,30,couleur)
        if couleur==red:
            if Tableau[5]==0:
                case[5][5]+=1
            elif Tableau[5]==1:
                case[4][5]+=1
            elif Tableau[5]==2:
                case[3][5]+=1
            elif Tableau[5]==3:
                case[2][5]+=1
            elif Tableau[5]==4:
                case[1][5]+=1
            else:
                case[0][5]+=1
        else:
            if Tableau[5]==0:
                case[5][5]+=50
            elif Tableau[5]==1:
                case[4][5]+=50
            elif Tableau[5]==2:
                case[3][5]+=50
            elif Tableau[5]==3:
                case[2][5]+=50
            elif Tableau[5]==4:
                case[1][5]+=50
            else:
                case[0][5]+=50
        Tableau[5]+=1
    #septieme colonne
    else:
        P=Point(650,550-100*Tableau[6])
        draw_fill_circle(P,30,couleur)
        if couleur==red:
            if Tableau[6]==0:
                case[5][6]+=1
            elif Tableau[6]==1:
                case[4][6]+=1
            elif Tableau[6]==2:
                case[3][6]+=1
            elif Tableau[6]==3:
                case[2][6]+=1
            elif Tableau[6]==4:
                case[1][6]+=1
            else:
                case[0][6]+=1
        else:
            if Tableau[6]==0:
                case[5][6]+=50
            elif Tableau[6]==1:
                case[4][6]+=50
            elif Tableau[6]==2:
                case[3][6]+=50
            elif Tableau[6]==3:
                case[2][6]+=50
            elif Tableau[6]==4:
                case[1][6]+=50
            else:
                case[0][6]+=50
        Tableau[6]+=1
    return


def victoire():
    Victoire=0
    #Horrizontal rouge
    if case[5][0]+case[5][1]+case[5][2]+case[5][3]==4:
        Victoire=1
    elif case[5][1]+case[5][2]+case[5][3]+case[5][4]==4:
        Victoire=1
    elif case[5][2]+case[5][3]+case[5][4]+case[5][5]==4:
        Victoire=1
    elif case[5][3]+case[5][4]+case[5][5]+case[5][6]==4:
        Victoire=1
    elif case[4][0]+case[4][1]+case[4][2]+case[4][3]==4:
        Victoire=1
    elif case[4][1]+case[4][2]+case[4][3]+case[4][4]==4:
        Victoire=1
    elif case[4][2]+case[4][3]+case[4][4]+case[4][5]==4:
        Victoire=1
    elif case[4][3]+case[4][4]+case[4][5]+case[4][6]==4:
        Victoire=1
    elif case[3][0]+case[3][1]+case[3][2]+case[3][3]==4:
        Victoire=1
    elif case[3][1]+case[3][2]+case[3][3]+case[3][4]==4:
        Victoire=1
    elif case[3][2]+case[3][3]+case[3][4]+case[3][5]==4:
        Victoire=1
    elif case[3][3]+case[3][4]+case[3][5]+case[3][6]==4:
        Victoire=1
    elif case[2][0]+case[2][1]+case[2][2]+case[2][3]==4:
        Victoire=1
    elif case[2][1]+case[2][2]+case[2][3]+case[2][4]==4:
        Victoire=1
    elif case[2][2]+case[2][3]+case[2][4]+case[2][5]==4:
        Victoire=1
    elif case[2][3]+case[2][4]+case[2][5]+case[2][6]==4:
        Victoire=1
    elif case[1][0]+case[1][1]+case[1][2]+case[1][3]==4:
        Victoire=1
    elif case[1][1]+case[1][2]+case[1][3]+case[1][4]==4:
        Victoire=1
    elif case[1][2]+case[1][3]+case[1][4]+case[1][5]==4:
        Victoire=1
    elif case[1][3]+case[1][4]+case[1][5]+case[1][6]==4:
        Victoire=1
    elif case[0][0]+case[0][1]+case[0][2]+case[0][3]==4:
        Victoire=1
    elif case[0][1]+case[0][2]+case[0][3]+case[0][4]==4:
        Victoire=1
    elif case[0][2]+case[0][3]+case[0][4]+case[0][5]==4:
        Victoire=1
    elif case[0][3]+case[0][4]+case[0][5]+case[0][6]==4:
        Victoire=1
    #Vertical Rouge
    elif case[5][0]+case[4][0]+case[3][0]+case[2][0]==4:
        Victoire=1
    elif case[4][0]+case[3][0]+case[2][0]+case[1][0]==4:
        Victoire=1
    elif case[3][0]+case[2][0]+case[1][0]+case[0][0]==4:
        Victoire=1
    elif case[5][1]+case[4][1]+case[3][1]+case[2][1]==4:
        Victoire=1
    elif case[4][1]+case[3][1]+case[2][1]+case[1][1]==4:
        Victoire=1
    elif case[3][1]+case[2][1]+case[1][1]+case[0][1]==4:
        Victoire=1
    elif case[5][2]+case[4][2]+case[3][2]+case[2][2]==4:
        Victoire=1
    elif case[4][2]+case[3][2]+case[2][2]+case[1][2]==4:
        Victoire=1
    elif case[3][2]+case[2][2]+case[1][2]+case[0][2]==4:
        Victoire=1
    elif case[5][3]+case[4][3]+case[3][3]+case[2][3]==4:
        Victoire=1
    elif case[4][3]+case[3][3]+case[2][3]+case[1][3]==4:
        Victoire=1
    elif case[3][3]+case[2][3]+case[1][3]+case[0][3]==4:
        Victoire=1
    elif case[5][4]+case[4][4]+case[3][4]+case[2][4]==4:
        Victoire=1
    elif case[4][4]+case[3][4]+case[2][4]+case[1][4]==4:
        Victoire=1
    elif case[3][4]+case[2][4]+case[1][4]+case[0][4]==4:
        Victoire=1
    elif case[5][5]+case[4][5]+case[3][5]+case[2][5]==4:
        Victoire=1
    elif case[4][5]+case[3][5]+case[2][5]+case[1][5]==4:
        Victoire=1
    elif case[3][5]+case[2][5]+case[1][5]+case[0][5]==4:
        Victoire=1
    elif case[5][6]+case[4][6]+case[3][6]+case[2][6]==4:
        Victoire=1
    elif case[4][6]+case[3][6]+case[2][6]+case[1][6]==4:
        Victoire=1
    elif case[3][6]+case[2][6]+case[1][6]+case[0][6]==4:
        Victoire=1
    #Diagonale vers la droite Rouge
    elif case[5][0]+case[4][1]+case[3][2]+case[2][3]==4:
        Victoire=1
    elif case[5][1]+case[4][2]+case[3][3]+case[2][4]==4:
        Victoire=1
    elif case[5][2]+case[4][3]+case[3][4]+case[2][5]==4:
        Victoire=1
    elif case[5][3]+case[4][4]+case[3][5]+case[2][6]==4:
        Victoire=1
    elif case[4][0]+case[3][1]+case[2][2]+case[1][3]==4:
        Victoire=1
    elif case[4][1]+case[3][2]+case[2][3]+case[1][4]==4:
        Victoire=1
    elif case[4][2]+case[3][3]+case[2][4]+case[1][5]==4:
        Victoire=1
    elif case[4][3]+case[3][4]+case[2][5]+case[1][6]==4:
        Victoire=1
    elif case[3][0]+case[2][1]+case[1][2]+case[0][3]==4:
        Victoire=1
    elif case[3][1]+case[2][2]+case[1][3]+case[0][4]==4:
        Victoire=1
    elif case[3][2]+case[2][3]+case[1][4]+case[0][5]==4:
        Victoire=1
    elif case[3][3]+case[2][4]+case[1][5]+case[0][6]==4:
        Victoire=1
    #Diagonale vers la gauche Rouge
    elif case[5][6]+case[4][5]+case[3][4]+case[2][3]==4:
        Victoire=1
    elif case[5][5]+case[4][4]+case[3][3]+case[2][2]==4:
        Victoire=1
    elif case[5][4]+case[4][3]+case[3][2]+case[2][1]==4:
        Victoire=1
    elif case[5][3]+case[4][2]+case[3][1]+case[2][0]==4:
        Victoire=1
    elif case[4][6]+case[3][5]+case[2][4]+case[1][3]==4:
        Victoire=1
    elif case[4][5]+case[3][4]+case[2][3]+case[1][2]==4:
        Victoire=1
    elif case[4][4]+case[3][3]+case[2][2]+case[1][1]==4:
        Victoire=1
    elif case[4][3]+case[3][2]+case[2][1]+case[1][0]==4:
        Victoire=1
    elif case[3][6]+case[2][5]+case[1][4]+case[0][3]==4:
        Victoire=1
    elif case[3][5]+case[2][4]+case[1][3]+case[0][2]==4:
        Victoire=1
    elif case[3][4]+case[2][3]+case[1][2]+case[0][1]==4:
        Victoire=1
    elif case[3][3]+case[2][2]+case[1][1]+case[0][0]==4:
        Victoire=1
    #Si un puissance 4 rouge
    if Victoire==1:
        return Victoire
    #Horrizontal Jaune
    if case[5][0]+case[5][1]+case[5][2]+case[5][3]==200:
        Victoire=2
    elif case[5][1]+case[5][2]+case[5][3]+case[5][4]==200:
        Victoire=2
    elif case[5][2]+case[5][3]+case[5][4]+case[5][5]==200:
        Victoire=2
    elif case[5][3]+case[5][4]+case[5][5]+case[5][6]==200:
        Victoire=2
    elif case[4][0]+case[4][1]+case[4][2]+case[4][3]==200:
        Victoire=2
    elif case[4][1]+case[4][2]+case[4][3]+case[4][4]==200:
        Victoire=2
    elif case[4][2]+case[4][3]+case[4][4]+case[4][5]==200:
        Victoire=2
    elif case[4][3]+case[4][4]+case[4][5]+case[4][6]==200:
        Victoire=2
    elif case[3][0]+case[3][1]+case[3][2]+case[3][3]==200:
        Victoire=2
    elif case[3][1]+case[3][2]+case[3][3]+case[3][4]==200:
        Victoire=2
    elif case[3][2]+case[3][3]+case[3][4]+case[3][5]==200:
        Victoire=2
    elif case[3][3]+case[3][4]+case[3][5]+case[3][6]==200:
        Victoire=2
    elif case[2][0]+case[2][1]+case[2][2]+case[2][3]==200:
        Victoire=2
    elif case[2][1]+case[2][2]+case[2][3]+case[2][4]==200:
        Victoire=2
    elif case[2][2]+case[2][3]+case[2][4]+case[2][5]==200:
        Victoire=2
    elif case[2][3]+case[2][4]+case[2][5]+case[2][6]==200:
        Victoire=2
    elif case[1][0]+case[1][1]+case[1][2]+case[1][3]==200:
        Victoire=2
    elif case[1][1]+case[1][2]+case[1][3]+case[1][4]==200:
        Victoire=2
    elif case[1][2]+case[1][3]+case[1][4]+case[1][5]==200:
        Victoire=2
    elif case[1][3]+case[1][4]+case[1][5]+case[1][6]==200:
        Victoire=2
    elif case[0][0]+case[0][1]+case[0][2]+case[0][3]==200:
        Victoire=2
    elif case[0][1]+case[0][2]+case[0][3]+case[0][4]==200:
        Victoire=2
    elif case[0][2]+case[0][3]+case[0][4]+case[0][5]==200:
        Victoire=2
    elif case[0][3]+case[0][4]+case[0][5]+case[0][6]==200:
        Victoire=2
    #Vertical Jaune
    elif case[5][0]+case[4][0]+case[3][0]+case[2][0]==200:
        Victoire=2
    elif case[4][0]+case[3][0]+case[2][0]+case[1][0]==200:
        Victoire=2
    elif case[3][0]+case[2][0]+case[1][0]+case[0][0]==200:
        Victoire=2
    elif case[5][1]+case[4][1]+case[3][1]+case[2][1]==200:
        Victoire=2
    elif case[4][1]+case[3][1]+case[2][1]+case[1][1]==200:
        Victoire=2
    elif case[3][1]+case[2][1]+case[1][1]+case[0][1]==200:
        Victoire=2
    elif case[5][2]+case[4][2]+case[3][2]+case[2][2]==200:
        Victoire=2
    elif case[4][2]+case[3][2]+case[2][2]+case[1][2]==200:
        Victoire=2
    elif case[3][2]+case[2][2]+case[1][2]+case[0][2]==200:
        Victoire=2
    elif case[5][3]+case[4][3]+case[3][3]+case[2][3]==200:
        Victoire=2
    elif case[4][3]+case[3][3]+case[2][3]+case[1][3]==200:
        Victoire=2
    elif case[3][3]+case[2][3]+case[1][3]+case[0][3]==200:
        Victoire=2
    elif case[5][4]+case[4][4]+case[3][4]+case[2][4]==200:
        Victoire=2
    elif case[4][4]+case[3][4]+case[2][4]+case[1][4]==200:
        Victoire=2
    elif case[3][4]+case[2][4]+case[1][4]+case[0][4]==200:
        Victoire=2
    elif case[5][5]+case[4][5]+case[3][5]+case[2][5]==200:
        Victoire=2
    elif case[4][5]+case[3][5]+case[2][5]+case[1][5]==200:
        Victoire=2
    elif case[3][5]+case[2][5]+case[1][5]+case[0][5]==200:
        Victoire=2
    elif case[5][6]+case[4][6]+case[3][6]+case[2][6]==200:
        Victoire=2
    elif case[4][6]+case[3][6]+case[2][6]+case[1][6]==200:
        Victoire=2
    elif case[3][6]+case[2][6]+case[1][6]+case[0][6]==200:
        Victoire=2
    #Diagonale vers la droite Jaune
    elif case[5][0]+case[4][1]+case[3][2]+case[2][3]==200:
        Victoire=2
    elif case[5][1]+case[4][2]+case[3][3]+case[2][4]==200:
        Victoire=2
    elif case[5][2]+case[4][3]+case[3][4]+case[2][5]==200:
        Victoire=2
    elif case[5][3]+case[4][4]+case[3][5]+case[2][6]==200:
        Victoire=2
    elif case[4][0]+case[3][1]+case[2][2]+case[1][3]==200:
        Victoire=2
    elif case[4][1]+case[3][2]+case[2][3]+case[1][4]==200:
        Victoire=2
    elif case[4][2]+case[3][3]+case[2][4]+case[1][5]==200:
        Victoire=2
    elif case[4][3]+case[3][4]+case[2][5]+case[1][6]==200:
        Victoire=2
    elif case[3][0]+case[2][1]+case[1][2]+case[0][3]==200:
        Victoire=2
    elif case[3][1]+case[2][2]+case[1][3]+case[0][4]==200:
        Victoire=2
    elif case[3][2]+case[2][3]+case[1][4]+case[0][5]==200:
        Victoire=2
    elif case[3][3]+case[2][4]+case[1][5]+case[0][6]==200:
        Victoire=2
    #Diagonale vers la gauche Jaune
    elif case[5][6]+case[4][5]+case[3][4]+case[2][3]==200:
        Victoire=2
    elif case[5][5]+case[4][4]+case[3][3]+case[2][2]==200:
        Victoire=2
    elif case[5][4]+case[4][3]+case[3][2]+case[2][1]==200:
        Victoire=2
    elif case[5][3]+case[4][2]+case[3][1]+case[2][0]==200:
        Victoire=2
    elif case[4][6]+case[3][5]+case[2][4]+case[1][3]==200:
        Victoire=2
    elif case[4][5]+case[3][4]+case[2][3]+case[1][2]==200:
        Victoire=2
    elif case[4][4]+case[3][3]+case[2][2]+case[1][1]==200:
        Victoire=2
    elif case[4][3]+case[3][2]+case[2][1]+case[1][0]==200:
        Victoire=2
    elif case[3][6]+case[2][5]+case[1][4]+case[0][3]==200:
        Victoire=2
    elif case[3][5]+case[2][4]+case[1][3]+case[0][2]==200:
        Victoire=2
    elif case[3][4]+case[2][3]+case[1][2]+case[0][1]==200:
        Victoire=2
    elif case[3][3]+case[2][2]+case[1][1]+case[0][0]==200:
        Victoire=2
    return Victoire



#Le tour de chaque joueur
def Tour():
    egalite=0
    gagnant=0
    while egalite<=20:
        #Tour du joueur rouge
        P=wait_clic()
        dessineJeton(P,red)
        test=victoire()
        #Si un puissance 4 rouge
        if test==1:
            gagnant="rouge"
            return gagnant
        #Tour du joueur jaune
        P=wait_clic()
        dessineJeton(P,yellow)
        test=victoire()
        #Si un puissance 4 jaune
        if test==2:
            gagnant="jaune"
            return gagnant
        egalite+=1
    gagnant="aucun"
    return gagnant




def main():
    init_graphic(700,600,"exercices")
    grille()
    gagnant=Tour()
    if gagnant=="rouge":
        grilleRouge()
    elif gagnant=="jaune":
        grilleJaune()
    else:
        grille()
    wait_escape()
    if gagnant=="rouge":
        reponse=input("Bravo ! Le joueur rouge a gagné !")
    elif gagnant=="jaune":
        reponse=input("Bravo ! Le joueur jaune a gagné !")
    else:
        reponse=input("La partie est terminé, c'est une égalité.")
    return


main()


