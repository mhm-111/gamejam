import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

######################### Phase-1 : Intro

def phase1():
    font = pygame.font.Font('osthir_font.ttf', 24)
    backgroundImage = pygame.image.load("newmedia/bg2_1200x700.jpg")
    char1_var = "character/front2.png"

    screen = pygame.display.set_mode([1280, 720])
    timer = pygame.time.Clock()

    messages = ['Check out this message! ',
                'This is new message',
                'let\'s start play',
                'ukh'
                ]

    snip = font.render('', True, 'white')
    counter = 0
    active_message = 0
    message = messages[active_message]
    speed = 3
    done = False

    run = True

    while run:

        charac1 = pygame.image.load(char1_var)
        screen.blit(backgroundImage, (0, 0))
        screen.blit(charac1, (600, 390))

        timer.tick(60)
        pygame.draw.rect(screen, 'black', [0, 550, 1275, 150])
        if counter < speed * len(message):
            counter += 1
        elif counter >= speed * len(message):
            done = True

        for event in pygame.event.get():
            if (active_message == len(messages)-1):
                return 0

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
                    active_message += 1



                    if (active_message % 2 == 0):
                        char1_var = "character/left2.png"
                    elif(active_message % 2 !=0 ):
                        char1_var = "character/front2.png"






                    message = messages[active_message]
                    counter = 0

        snip = font.render(message[0:counter // speed], True, 'white')
        screen.blit(snip, (10, 580))
        pygame.display.flip()

    pygame.quit()
###################################
########## phase-2

def phase2():
    screen = pygame.display.set_mode((1280, 720))
    font = pygame.font.Font('osthir_font2.ttf', 24)
    stat1 = "OFF"
    v1 = 0
    stat2 = "ON"
    v2 = 1
    stat3 = "ON"
    v3 = 1
    stat4 = "OFF"
    v4 = 0
    surf1 = font.render(stat1, True, 'white')
    surf2 = font.render(stat2, True, 'white')
    surf3 = font.render(stat3, True, 'white')
    surf4 = font.render(stat4, True, 'white')

    button1 = pygame.Rect(10, 200, 110, 60)
    button2 = pygame.Rect(200, 200, 110, 60)
    button3 = pygame.Rect(400, 200, 110, 60)
    button4 = pygame.Rect(550, 200, 110, 60)

    while True:
        win_bg = pygame.image.load("assets/Background.png")
        win_message = font.render("You Won !!", True, 'white')
        screen.fill('pink')
        if v1 == 1 and v2 == 1 and v3 == 1 and v4 == 1:
            screen.blit(win_bg, (0, 0))
            screen.blit(win_message, (250, 460))
            pygame.display.update()
        for events in pygame.event.get():
            surf1 = font.render(stat1, True, 'white')
            surf2 = font.render(stat2, True, 'white')
            surf3 = font.render(stat3, True, 'white')
            surf4 = font.render(stat4, True, 'white')


            if events.type == pygame.QUIT:
                pygame.quit()
            if events.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(events.pos) and v1 == 0:
                    stat1 = 'ON'
                    v1 = 1
                    pygame.display.update()
                elif button1.collidepoint(events.pos) and v1 == 1:
                    stat1 = 'OFF'
                    v1 = 0
                    pygame.display.update()
                elif button2.collidepoint(events.pos) and v2 == 0:
                    stat2 = 'ON'
                    v2 = 1
                    pygame.display.update()
                elif button2.collidepoint(events.pos) and v2 == 1:
                    stat2 = 'OFF'
                    v2 = 0
                    pygame.display.update()

                elif button3.collidepoint(events.pos) and v3 == 0:
                    stat3 = 'ON'
                    v3 = 1
                    pygame.display.update()
                elif button3.collidepoint(events.pos) and v3 == 1:
                    stat3 = 'OFF'
                    v3 = 0
                    pygame.display.update()

                elif button4.collidepoint(events.pos) and v4 == 0:
                    stat4 = 'ON'
                    v4 = 1
                    pygame.display.update()
                elif button4.collidepoint(events.pos) and v4 == 1:
                    stat4 = 'OFF'
                    v4 = 0
                    pygame.display.update()

        pygame.draw.rect(screen, (110, 110, 110), button1)
        pygame.draw.rect(screen, (110, 110, 110), button2)
        pygame.draw.rect(screen, (110, 110, 110), button3)
        pygame.draw.rect(screen, (110, 110, 110), button4)
        screen.blit(surf1, (button1.x + 5, button1.y + 5))
        screen.blit(surf2, (button2.x + 5, button2.y + 5))
        screen.blit(surf3, (button3.x + 5, button3.y + 5))
        screen.blit(surf4, (button4.x + 5, button4.y + 5))
        pygame.display.update()

########################################


def play():
    while True:
        phase1()
        phase2()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()