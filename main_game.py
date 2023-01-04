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
                'This is new messages 2 ',
                'Check out this message! ',
                'This is new message',
                'This is new messages 2 '
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
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message < len(messages) - 1:
                    active_message += 1;
                    if (active_message % 2 == 0):
                        char1_var = "character/left2.png"
                    else:
                        char1_var = "character/front2.png"
                    done = False
                    message = messages[active_message]
                    counter = 0

        snip = font.render(message[0:counter // speed], True, 'white')
        screen.blit(snip, (10, 580))
        pygame.display.flip()
    pygame.quit()



def play():
    while True:
        phase1()


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