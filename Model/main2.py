import pygame
from credits import drawCredits
from credits import drawExplication
from main import playing
from game import Game
from main import gameOver
from utils_game import load_image
from utils_game import PATH
from background_anime import BackgroundAnime
import os
from boost import BubbleBoost


pygame.init()


Texty = pygame.font.Font('../Fonts/gumbonormal.ttf', 40)
Texty2 = pygame.font.Font('../Fonts/gumbonormal.ttf', 20)

TextyGrand = pygame.font.Font('../Fonts/gumbonormal.ttf', 80)

selector = 1
placement = 200
game = Game()
selectorLevels = 1
selectorMenu = 1
music_Menu = pygame.mixer.Sound('../Sounds/Otarie.wav')
music_bouton = pygame.mixer.Sound('../Sounds/bouton.wav')

imagesBackground = [load_image(PATH + "frame_00.png"), load_image(PATH + "frame_01.png"), load_image(PATH + "frame_02.png"),
                    load_image(PATH + "frame_03.png"), load_image(PATH + "frame_04.png"), load_image(PATH + "frame_05.png"),
                    load_image(PATH + "frame_06.png"), load_image(PATH + "frame_07.png"), load_image(PATH + "frame_08.png"),
                    load_image(PATH + "frame_09.png"), load_image(PATH + "frame_10.png"), load_image(PATH + "frame_11.png"),
                    load_image(PATH + "frame_12.png"), load_image(PATH + "frame_13.png"), load_image(PATH + "frame_14.png")]
background_anime = BackgroundAnime(imagesBackground)
spriteGroup = pygame.sprite.Group(background_anime)
clock = pygame.time.Clock()

if os.stat("../highscore.txt").st_size == 0:
    f = open('../highscore.txt','w')
    f.write('0')
    f.close()
if os.stat("../highscore2.txt").st_size == 0:
    f = open('../highscore2.txt','w')
    f.write('0')
    f.close()
if os.stat("../highscore3.txt").st_size == 0:
    f = open('../highscore3.txt','w')
    f.write('0')
    f.close()



def drawMenu():
    f = open('../name.txt', 'r')
    name = f.read()
    f.close()

    f2 = open('../name2.txt', 'r')
    name2 = f2.read()
    f2.close()

    f3 = open('../name3.txt', 'r')
    name3 = f3.read()
    f3.close()

    f = open('../highscore.txt', 'r')
    highscore = int(f.read())
    f.close()

    f2 = open('../highscore2.txt', 'r')
    highscore2 = int(f2.read())
    f2.close()

    f3 = open('../highscore3.txt', 'r')
    highscore3 = int(f3.read())
    f3.close()



    dt = clock.tick(60) / 1000
    #Generer la fenetre de notre jeu
    windowSize = (800, 600)
    origin = (0,0)
    global selectorMenu
    placement = 200
    pygame.display.set_caption('Bubble Escape')
    screen = pygame.display.set_mode(windowSize)
    rect = pygame.Rect(origin,windowSize)
    image = pygame.Surface(windowSize)
    textTitre = TextyGrand.render('Bubble Escape ', 0, (0, 102, 204))
    textStart = Texty.render('Start', 0, (0, 153, 255))
    textCredits = Texty.render('Credits', 0, (0, 153, 255))
    textExplication = Texty.render('Explication', 0, (0, 153, 255))
    textQuit = Texty.render('Quit ', 0, (255, 0, 0))
    textName = Texty.render(name,0,(0, 153, 255))
    textNameDeuxieme = Texty2.render(name2,0,(0, 153, 255))
    textNameTroisieme = Texty2.render(name3,0,(0, 153, 255))
    textHighscore = Texty.render("Highscore : "+str(highscore),0,(0, 153, 255))
    textDeuxiemeHighScore = Texty2.render("2eme : "+str(highscore2),0,(0, 153, 255))
    textTroisiemeHighscore = Texty2.render("3eme : "+str(highscore3),0,(0, 153, 255))


    imageFleche = pygame.image.load("../Images/bubble.png")
    imageFleche = pygame.transform.scale(imageFleche,(30,30))
    spriteGroup.update(dt)
    spriteGroup.draw(screen)
    screen.blit(textName,(20,10))
    screen.blit(textTitre, (40, 110))
    screen.blit(textStart, (300, 300))
    screen.blit(textCredits, (300, 350))
    screen.blit(textExplication, (300, 400))
    screen.blit(textQuit, (300, 450))
    screen.blit(textHighscore,(20,50))


    screen.blit(textNameDeuxieme,(20,350))
    screen.blit(textDeuxiemeHighScore, (20, 370))
    screen.blit(textNameTroisieme,(20,450))
    screen.blit(textTroisiemeHighscore,(20,470))

    if selectorMenu == 1:
        placement = 310
    elif selectorMenu == 2:
        placement = 360
    elif selectorMenu == 3:
        placement = 410
    elif selectorMenu == 4:
        placement = 460
    screen.blit(imageFleche,(260, placement))
    pygame.display.update()




def draw_levels():
    dt = clock.tick(60) / 1000
    Texty = pygame.font.Font('../Fonts/Polo Bubble.ttf', 50)
    placement = 200
    global selectorLevels
    windowSize = (800, 600)
    origin = (0, 0)
    pygame.display.set_caption('Levels')
    screen = pygame.display.set_mode(windowSize)
    rect = pygame.Rect(origin, windowSize)
    image = pygame.Surface(windowSize)
    # imagesBackground
    textLevelFacile = Texty.render('Easy ', 0, (0, 153, 255))
    textLevelNormal = Texty.render('Medium', 0, (0, 153, 255))
    textLevelPro = Texty.render('Pro', 0, (0, 153, 255))
    textLevelExpert = Texty.render('Nightmare', 0, (0, 153, 255))
    textLevelRetour= Texty.render('Back', 0, (58, 52, 235))

    imageFleche = pygame.image.load("../Images/bubble.png")
    imageFleche = pygame.transform.scale(imageFleche, (30, 30))
    spriteGroup.update(dt)
    spriteGroup.draw(screen)
    screen.blit(textLevelFacile, (300, 150))
    screen.blit(textLevelNormal, (300, 200))
    screen.blit(textLevelPro, (300, 250))
    screen.blit(textLevelExpert, (300, 300))
    screen.blit(textLevelRetour, (300, 350))

    if selectorLevels == 1:
        placement = 160
    elif selectorLevels == 2:
        placement = 210
    elif selectorLevels == 3:
        placement = 260
    elif selectorLevels == 4:
        placement = 310
    elif selectorLevels ==5:
        placement = 360
    screen.blit(imageFleche, (260, placement))
    pygame.display.update()




music_Menu.play(-1)

run = True
while run:
    drawMenu()
    for event in pygame.event.get(): ########boucle du menu
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                music_bouton.play()
                if selectorMenu != 1:
                    selectorMenu -= 1
            elif event.key == pygame.K_DOWN:
                music_bouton.play()
                if selectorMenu != 4:
                    selectorMenu += 1
            elif event.key == pygame.K_RETURN and selectorMenu == 1: #####On choisit de jouer => levels
                truuuue = True
                quitter = False
                while truuuue:
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        elif e.type == pygame.KEYDOWN:
                            if e.key == pygame.K_UP:
                                if selectorLevels != 1:
                                    selectorLevels -= 1
                            elif e.key == pygame.K_DOWN:
                                if selectorLevels != 5:
                                    selectorLevels += 1
                            elif e.key == pygame.K_RETURN and selectorLevels == 1: #on a choisit le niveau facile, tant que l'on joue rien sinon game over
                                music_Menu.stop()
                                difficulte = 1
                                res = playing(difficulte)
                                if not res: ##on arrive sur la page game over si jeu finit
                                    gameOver()

                                    break
                            #  ici direction draw_levels
                            elif e.key == pygame.K_RETURN and selectorLevels == 2:
                                music_Menu.stop()
                                difficulte= 2
                                res = playing(difficulte)
                                if not res: ##on arrive sur la page game over si jeu finit
                                    gameOver()

                                    break
                            elif e.key == pygame.K_RETURN and selectorLevels == 3:
                                music_Menu.stop()
                                difficulte = 3
                                res = playing(difficulte)
                                if not res: ##on arrive sur la page game over si jeu finit
                                    gameOver()
                                    break
                            elif e.key == pygame.K_RETURN and selectorLevels == 4:
                                music_Menu.stop()
                                difficulte = 5
                                res = playing(difficulte)
                                if not res: ##on arrive sur la page game over si jeu finit
                                    gameOver()
                                    break
                            elif e.key == pygame.K_RETURN and selectorLevels == 5:
                                music_Menu.stop()
                                quitter = True
                                break

                    draw_levels()
                    if quitter:
                        quitter = False
                        break

            elif event.key == pygame.K_RETURN and selectorMenu == 2: #bouton credits
                drawCredits()
            elif event.key == pygame.K_RETURN and selectorMenu == 3: #bouton credits
                drawExplication()
            elif event.key == pygame.K_RETURN and selectorMenu == 4: #bouton quit
                pygame.quit()
                exit()


