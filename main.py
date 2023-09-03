import copy
import random
import time

import pygame
from google_trans_new import google_translator
from DicoUtile import ListeMot

Translator = google_translator()

ListeToutMot = copy.deepcopy(ListeMot)

random.shuffle(ListeMot)
ListeMot = ListeMot[:11]
ListeMotCopy = copy.deepcopy(ListeMot)


pygame.init()
size = 1920,1080
screen = pygame.display.set_mode(size,True)
screen.blit(pygame.image.load("image/mathemo.png"), (0, 0))

PlayButton = pygame.image.load("image/play-button.png")
PlayButtonBig = pygame.transform.scale(PlayButton,(PlayButton.get_width()+10,PlayButton.get_height()+10))
PlayButtonNormal =  pygame.image.load("image/play-button.png")
TrueIcone = pygame.image.load("image/TrueIcone.png")
FalseIcone = pygame.image.load("image/wrongIcone.png")
RelaunchIcone = pygame.image.load("image/relaunch.png")
TimerIcone = pygame.image.load("image/timer.png")
TimerIconeNormal = pygame.image.load("image/timer.png")
TopBanner = pygame.transform.scale(pygame.image.load("image/mathemoo.png") ,(1920,151))
Exit = pygame.image.load("image/exit.png")

Exit = pygame.transform.scale(Exit,(70,70))
TrueIcone = pygame.transform.scale(TrueIcone,(70,70))
FalseIcone = pygame.transform.scale(FalseIcone,(70,70))
RelaunchIcone = pygame.transform.scale(RelaunchIcone,(80,80))
TimerIcone = pygame.transform.scale(TimerIcone,(PlayButtonNormal.get_width(),PlayButtonNormal.get_width()))
TimerIconeNormal = pygame.transform.scale(TimerIconeNormal,(PlayButtonNormal.get_width(),PlayButtonNormal.get_width()))
TimerIconeBig = pygame.transform.scale(TimerIcone,(TimerIcone.get_width()+10,TimerIcone.get_height()+10))

font = pygame.font.Font("Fichier utiles/fonts/BebasKai.ttf",72)

def afficher_texte(screen,font,texte,x,y,color=(255,255,255)):
    TexteAffiche = font.render(texte,True, color)
    screen.blit(TexteAffiche, (x-TexteAffiche.get_width()//2,y))

def GenererMot(Game):
    if Game["ListeMot"] == []:
        Game["ListeMot"] = copy.deepcopy(Game["ListeMotCopy"])
        random.shuffle(Game["ListeMot"])
        Game["ListeMotTraduit"] = [mot["motTraduit"] for mot in Game["ListeMot"]]

    Game["mot"] = (Game["ListeMot"].pop(0))["mot"]
    Game["motTraduit"] = (Game["ListeMotTraduit"].pop(0))

def AjouterCompteurDict(Game,mot):
    try:
        Game["DictionnaireCompteur"][mot]+=1
        if Game["DictionnaireCompteur"][mot] == 10:
            Game["ListeMotappris"].append(mot)
    except:
        Game["DictionnaireCompteur"][mot] = 1

def reinitialise():
    global ListeMot
    global ListeMotCopy
    ListeMot = copy.deepcopy(ListeToutMot)
    random.shuffle(ListeMot)
    ListeMot = ListeMot[:11]
    ListeMotCopy = copy.deepcopy(ListeMot)
    global Game
    global Temps
    global GameTemps
    Game = {"Ecran affiché": False,
            "etat": "CheckList",
            "textePlayer": "",
            "wrongAnswer": "Pas trouvée",
            "mot": "",
            "motTraduit": "",
            "motAncien": "",
            "motTraduitAncien": "",
            "ListeMot": ListeMot,
            "ListeMotCopy": ListeMotCopy,
            "ListeMotappris": [],
            "DictionnaireCompteur": {}
            }
    Game["ListeMotTraduit"] = [mot["motTraduit"] for mot in Game["ListeMot"]]
    Temps = [4, 0, 1]
    GameTemps = {"ListeMotTotale": [],
                 "ListeMotCorrecte": [],
                 "ListeMotTotaleNonTraduit": [],
                 "ValeurAffichageReponse" : 0}

def reinitialiserListeMot(Game,Time=False):
    global ListeMot
    global ListeMotCopy
    ListeMot = copy.deepcopy(ListeToutMot)
    random.shuffle(ListeMot)
    if Time==False:
        ListeMot = ListeMot[:11]
    ListeMotCopy = copy.deepcopy(ListeMot)
    Game["ListeMot"] = ListeMot
    Game["ListeMotCopy"] = ListeMotCopy
    Game["ListeMotTraduit"] = [mot["motTraduit"] for mot in Game["ListeMot"]]

    GenererMot(Game)


BoxPlay = [pygame.Color('white'),pygame.Rect(screen.get_width()//2 - 300//2, screen.get_height()//2 - 150, 300, 300)]
BoxTime = [pygame.Color('white'),pygame.Rect(screen.get_width()//2 - 300//2, screen.get_height()//2 +200, 300, 300)]
BoxWrite = [pygame.Color('white'),pygame.Rect(screen.get_width()//2 - 1600//2, 250, 1600, 100)]

BoxLeft = [pygame.Color('white'),pygame.Rect(10, 495, 100, 100)]
BoxRight = [pygame.Color('white'),pygame.Rect(1800, 495, 100, 100)]

BoxRelaunch = [pygame.Color('white'),pygame.Rect(10, 50, 100, 100)]

BoxExit = [pygame.Color('white'),pygame.Rect(1800, 50, 100, 100)]



Game = {"Ecran affiché" : False,
        "etat" : "menue",
        "textePlayer":"",
        "wrongAnswer" : "Pas trouvée",
        "mot":"",
        "motTraduit":"",
        "motAncien" : "",
        "motTraduitAncien" : "",
        "ListeMot" : ListeMot,
        "ListeMotCopy" : ListeMotCopy,
        "ListeMotappris" : [],
        "DictionnaireCompteur" : {}
        }
#Temps = [temps avant le début de la partie, temps ou le compteur a commencer (qu'il faut soustraire a time.time() ), compteur affiché]
Temps = [4,0,1]
GameTemps = {"ListeMotTotale" : [],
             "ListeMotCorrecte" : [],
             "ListeMotTotaleNonTraduit" : [],
             "ValeurAffichageReponse" : 0}

Game["ListeMotTraduit"] = [mot["motTraduit"] for mot in Game["ListeMot"]]

GenererMot(Game)

running = True
Background = pygame.transform.scale(pygame.image.load("image/mathemo.png"),(1920,1080))

while running:

    pygame.display.flip()


    if Game["Ecran affiché"] == False:

        Game["Ecran affiché"] = True
        screen.blit(Background, (0, 0))

        if Game["etat"] == "menue":
            afficher_texte(screen,font,"Bienvenue au English Vocabulary game !",screen.get_width()//2,50)
            afficher_texte(screen,font,"Clickez sur le bouton pour commencer",screen.get_width()//2,150)
            pygame.draw.rect(screen, BoxPlay[0] , BoxPlay[1], 10)
            pygame.draw.rect(screen, BoxTime[0] , BoxTime[1], 10)
            screen.blit(PlayButton,(screen.get_width()//2 - PlayButton.get_width()//2, screen.get_height()//2 - PlayButton.get_height()//2))
            screen.blit(TimerIcone,(screen.get_width()//2 - TimerIcone.get_width()//2, screen.get_height()//2 - TimerIcone.get_height()//2 +350))

        if Game["etat"] == "Playing":
            afficher_texte(screen,font,"Mot à traduire : " + Game["mot"],screen.get_width()//2,50)
            afficher_texte(screen,font,"(Appuyez sur entrée pour valider votre réponse)",screen.get_width()//2,150)
            pygame.draw.rect(screen, BoxWrite[0] , BoxWrite[1], 10)
            pygame.draw.rect(screen, BoxRight[0] , BoxRight[1], 10)
            afficher_texte(screen, font, Game["textePlayer"], screen.get_width() // 2,255)
            afficher_texte(screen, font,"->", 1850,500)

            if  Game["wrongAnswer"] == "Faux":
                afficher_texte(screen, font, "Faux !", screen.get_width() // 2, 400,color=(255, 0, 0))
                afficher_texte(screen, font, Game["motAncien"] + " en anglais se dit", screen.get_width() // 2, 500,color=(255, 0, 0))
                afficher_texte(screen, font,Game["motTraduitAncien"], screen.get_width() // 2, 600,color=(19, 13, 132))
            elif Game["wrongAnswer"] == "Vrai":
                afficher_texte(screen, font, "Vrai !", screen.get_width() // 2, 400,color=(60, 133, 40))

            afficher_texte(screen, font, "Nombre de mots appris : " + str(len(Game["ListeMotappris"])) + "/"+str(len(Game["ListeMotCopy"])), screen.get_width() // 2, 800, color=(60, 133, 40))
            afficher_texte(screen, font, "(Un mot est considéré comme appris au bout de 10 réussites)", screen.get_width() // 2, 900)

        if Game["etat"] == "CheckList":

            afficher_texte(screen,font,"Mot",screen.get_width()//2-600,50)
            afficher_texte(screen,font,"Traduction",screen.get_width()//2,50)
            afficher_texte(screen,font,"Appris",screen.get_width()//2+600,50)
            for i in range(len(ListeMotCopy)) :
                mot = ListeMotCopy[i]
                afficher_texte(screen, font, mot["mot"], screen.get_width() // 2 - 600, 150+80*i,color=(8, 113, 208))
                afficher_texte(screen, font, mot["motTraduit"], screen.get_width() // 2, 150+80*i,color=(255, 0, 0))
                if mot["motTraduit"] in Game["ListeMotappris"]:
                    screen.blit(TrueIcone,(screen.get_width() //2 + 600 - TrueIcone.get_width()//2, 150 + 80 * i))
                else:
                    screen.blit(FalseIcone,(screen.get_width() //2 + 600 - FalseIcone.get_width()//2, 150 + 80 * i))

            pygame.draw.rect(screen, BoxLeft[0] , BoxLeft[1], 10)
            afficher_texte(screen, font,"<-", 60,500)
            pygame.draw.rect(screen, BoxRelaunch[0] ,BoxRelaunch[1], 10)
            screen.blit(RelaunchIcone,(22,60))

            pygame.draw.rect(screen, BoxExit[0] ,BoxExit[1], 10)
            screen.blit(Exit,(1812,60))

        if Game["etat"] == "PlayingTimeLoading":
            Game["Ecran affiché"] = False
            Temps[2] = int(Temps[0] - (time.time()-Temps[1]))
            afficher_texte(screen,font,str(Temps[2]),screen.get_width()//2,screen.get_height()//2-100)
            if Temps[2] == 0:
                Game["etat"] = "TimePlaying"
                Temps = [4, 0, 1]
                Temps[1] = time.time()
                #Temps = [ne sert a rien ici, temps début, temps écoulé depuis le début (atteindra 1 minute) ]

        if Game["etat"] == "TimePlaying":
            pygame.draw.rect(screen, BoxWrite[0] , BoxWrite[1], 10)
            afficher_texte(screen,font,"Mot à traduire : " + Game["mot"],screen.get_width()//2,500)
            afficher_texte(screen, font, Game["textePlayer"], screen.get_width() // 2,255)

        if Game["etat"] == "resultat":
            print(GameTemps)
            pygame.draw.rect(screen, BoxRelaunch[0] ,BoxRelaunch[1], 10)
            screen.blit(RelaunchIcone,(22,60))
            afficher_texte(screen,font,"Résultat :",screen.get_width()//2,50)
            afficher_texte(screen, font, "mots traduits corrects : " + str(len(GameTemps['ListeMotCorrecte'])), screen.get_width() // 2, 150)
            afficher_texte(screen, font, "Totale des mots : " + str(len(GameTemps['ListeMotTotale'])), screen.get_width() // 2, 250)
            Pourcentage = (len(GameTemps['ListeMotCorrecte']) *100)//len(GameTemps['ListeMotTotale'])
            afficher_texte(screen, font, "Pourcentage correct : " + str(Pourcentage) +"%", screen.get_width() // 2, 350)
            pygame.draw.rect(screen, BoxExit[0] ,BoxExit[1], 10)
            screen.blit(Exit,(1812,60))

            for i in range(GameTemps["ValeurAffichageReponse"],GameTemps["ValeurAffichageReponse"]+9):
                if i < len(GameTemps["ListeMotTotale"]):
                    if GameTemps["ListeMotTotale"][i] in GameTemps["ListeMotCorrecte"]:
                        color = (8, 113, 208)
                    else:
                        color = (255, 0, 0)

                    afficher_texte(screen, font, GameTemps["ListeMotTotaleNonTraduit"][i] + " --> " + GameTemps["ListeMotTotale"][i],screen.get_width() // 2, 440+(i-GameTemps["ValeurAffichageReponse"])*70,color=color)


    if Game["etat"] == "TimePlaying":
        screen.blit(TopBanner,(0,0))
        Temps[2] = int((time.time() - Temps[1]))
        afficher_texte(screen, font, str(60-Temps[2]), screen.get_width() // 2, 50)
        if Temps[2]>=60:

            Game["Ecran affiché"] = False
            Game["etat"] = "resultat"
            pygame.mixer.music.load("Sounds/resultat.mp3")
            pygame.mixer.music.play(1)


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.MOUSEMOTION:

            Game["Ecran affiché"] = False

            if Game["etat"] == "menue":
                if BoxPlay[1].collidepoint(event.pos):
                    PlayButton = PlayButtonBig
                    BoxPlay[0] = pygame.Color("gray")
                else:
                    PlayButton = PlayButtonNormal
                    BoxPlay[0] = pygame.Color("white")

                if BoxTime[1].collidepoint(event.pos):
                    TimerIcone = TimerIconeBig
                    BoxTime[0] = pygame.Color("gray")
                else:
                    TimerIcone = TimerIconeNormal
                    BoxTime[0] = pygame.Color("white")

            if Game["etat"] == "Playing":
                if BoxRight[1].collidepoint(event.pos):
                    BoxRight = [pygame.Color('gray'), pygame.Rect(1800-5, 495-5, 110, 110)]
                else:
                    BoxRight = [pygame.Color('white'), pygame.Rect(1800, 495, 100, 100)]

            if Game["etat"] == "CheckList":
                if BoxLeft[1].collidepoint(event.pos):
                    BoxLeft = [pygame.Color('gray'), pygame.Rect(10-5, 495-5, 110, 110)]
                else:
                    BoxLeft = [pygame.Color('white'), pygame.Rect(10, 495, 100, 100)]

            if Game["etat"] == "CheckList" or Game["etat"] == "resultat":
                if BoxRelaunch[1].collidepoint(event.pos):
                    BoxRelaunch = [pygame.Color('gray'), pygame.Rect(10-5, 50-5, 110, 110)]
                else:
                    BoxRelaunch = [pygame.Color('white'), pygame.Rect(10, 50, 100, 100)]

                if BoxExit[1].collidepoint(event.pos):
                    BoxExit = [pygame.Color('gray'),pygame.Rect(1800-5, 50-5, 110, 110)]
                else:
                    BoxExit = [pygame.Color('white'),pygame.Rect(1800, 50, 100, 100)]

        if event.type == pygame.MOUSEBUTTONDOWN:
            Game["Ecran affiché"] = False

            if Game["etat"] == "menue":
                if BoxPlay[1].collidepoint(event.pos):
                    Game["etat"] = "Playing"

                if BoxTime[1].collidepoint(event.pos):
                    Game["etat"] = "PlayingTimeLoading"
                    Temps[1] = time.time()
                    reinitialiserListeMot(Game,True)

            if Game["etat"] == "Playing":
                if BoxRight[1].collidepoint(event.pos):
                    Game["etat"] = "CheckList"

            if Game["etat"] == "CheckList":
                if BoxLeft[1].collidepoint(event.pos):
                    Game["etat"] = "Playing"

                if BoxRelaunch[1].collidepoint(event.pos):
                    reinitialise()
                    reinitialiserListeMot(Game, False)

            if Game["etat"] == "resultat":
                if BoxRelaunch[1].collidepoint(event.pos):
                    reinitialise()

                    Game["etat"] = "PlayingTimeLoading"
                    Temps[1] = time.time()

                    reinitialiserListeMot(Game,True)

            if Game["etat"] == "CheckList" or Game["etat"] == "resultat":

                if BoxExit[1].collidepoint(event.pos):
                    reinitialise()
                    Game["etat"] = "menue"
                    reinitialiserListeMot(Game,False)

                if event.button == 5 : #Scroll
                    GameTemps["ValeurAffichageReponse"]+=1
                    if GameTemps["ValeurAffichageReponse"]+9 > len(GameTemps["ListeMotTotale"]):
                        GameTemps["ValeurAffichageReponse"] -= 1

                if event.button == 4 : #Scroll
                    GameTemps["ValeurAffichageReponse"]-=1
                    if 0 > GameTemps["ValeurAffichageReponse"]:
                        GameTemps["ValeurAffichageReponse"] += 1



        if event.type == pygame.KEYDOWN:

            if Game["etat"] == "Playing":

                if event.key == pygame.K_BACKSPACE:
                    Game["textePlayer"] = Game["textePlayer"][:-1]


                elif event.key == pygame.K_RETURN:
                    if Game["motTraduit"].lower().replace("to ","").replace(" ","") != Game["textePlayer"].lower().replace("to ","").replace(" ","")   :
                        Game["wrongAnswer"] = "Faux"
                        Game["motAncien"] = Game["mot"]
                        Game["motTraduitAncien"] = Game["motTraduit"]
                    else:
                        Game["wrongAnswer"] = "Vrai"
                        AjouterCompteurDict(Game, Game["textePlayer"])

                    GenererMot(Game)
                    Game["textePlayer"] = ""

                else:
                    Game["wrongAnswer"] = "Pas trouvée"
                    Game["textePlayer"] += event.unicode

            if Game["etat"] == "TimePlaying":
                if event.key == pygame.K_BACKSPACE:
                    Game["textePlayer"] = Game["textePlayer"][:-1]

                elif event.key == pygame.K_RETURN:

                    if Game["motTraduit"].lower().replace("to ","").replace(" ","") == Game["textePlayer"].lower().replace("to ","").replace(" ","")  :
                        pygame.mixer.music.load("Sounds/Correct.mp3")
                        pygame.mixer.music.play(1)
                        GameTemps["ListeMotCorrecte"].append(Game["textePlayer"])

                    GameTemps["ListeMotTotale"].append(Game["motTraduit"])
                    GameTemps["ListeMotTotaleNonTraduit"].append(Game["mot"])
                    GenererMot(Game)
                    Game["textePlayer"] = ""

                else:
                    Game["wrongAnswer"] = "Pas trouvée"
                    Game["textePlayer"] += event.unicode


            Game["Ecran affiché"] = False




