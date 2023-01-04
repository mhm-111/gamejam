import pygame, sys
from button import Button
import random
import math

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

##################################################


######################################

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def play():
    playstat = True
    running = True

    while playstat:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playstat = False
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        # Window set
        screen = pygame.display.set_mode((1280, 720))

        # Game over
        gameOver = pygame.font.Font("osthir_font2.ttf", 90)
        final_score = pygame.font.Font("osthir_font2.ttf", 50)
        backgroundImage = pygame.image.load("bg1.jpg")

        # creating player
        head = pygame.image.load("basket.png")
        headX = 400
        headY = 300
        head_changeX = 0
        head_changeY = 0

        # Enemey
        enemyImg = pygame.image.load("bomb.png")
        enemyX = random.randint(0, 750)
        enemyY = 0
        enemyY_change = 90
        enemyX_change = 0.4

        # fruit
        fruit = True
        fruitImg = []
        fruitX = []
        fruitY = []
        fruitX_change = []
        fruitY_change = []
        fruit_number = 8

        for i in range(fruit_number):
            fruitImg.append(pygame.image.load("apple.png"))
            fruitX.append(random.randint(10, 740))
            fruitY.append(random.randint(-1500, 0))
            fruitY_change.append(.15)

        # Enemy Come
        def enemy(x, y):
            screen.blit(enemyImg, (x, y))

        # player
        def show_block(x, y):
            screen.blit(head, (x, y))

        # Back ground Image
        backgroundImage_always = pygame.image.load("bg1.jpg")

        # fruit show
        def fruit(x, y, i):
            screen.blit(fruitImg[i], (x, y))

        # Collision
        def isCollide(eX, eY, pX, pY):
            distance = math.sqrt((math.pow(eX - pX, 2)) + (math.pow(eY - pY, 2)))
            if distance < 45:
                return True

        # score
        score = 0
        score_change = 5
        scoreText = pygame.font.Font("osthir_font.ttf", 40)

        # score show
        def score_show():
            score_text = scoreText.render("Score : " + str(score), True, (0, 0, 0))
            screen.blit(score_text, (10, 540))

        # score count
        def score_count(px, py, fx, fy):
            dist = math.sqrt((math.pow(px - fx, 2)) + math.pow(py - fy, 2))
            if dist < 45:
                return True

        # Boundary collision
        def boundary_collision():
            if headX > 735 or headX < 0 or headY > 535 or headY < 0:
                return True

        # game over
        def game_over():
            game_over_text = gameOver.render("GAME OVER BOSS", True, (255, 255, 255))
            final_score_text = final_score.render("Your Score : " + str(score), True, (255, 255, 255))
            screen.blit(game_over_text, (180, 250))
            screen.blit(final_score_text, (300, 350))

        game_run = True

        while running:
            if game_run:
                # screen.fill((0, 150, 150))
                screen.blit(backgroundImage_always, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_LEFT:
                        head_changeX = -.2

                    if event.key == pygame.K_RIGHT:
                        head_changeX = .2

                    if event.key == pygame.K_UP:
                        head_changeY = -.2

                    if event.key == pygame.K_DOWN:
                        head_changeY = .2
            # fruit
            if fruit:
                for i in range(fruit_number):
                    fruitY[i] += fruitY_change[i]
                    fruit(fruitX[i], fruitY[i], i)
                    if fruitY[i] > 1000:
                        fruitY[i] = random.randint(-1500, 0)
                    # score count
                    if score_count(headX, headY, fruitX[i], fruitY[i]):
                        score += score_change
                        fruitY[i] = random.randint(-1500, 0)

            # Game over
            if isCollide(enemyX, enemyY, headX, headY) or boundary_collision():
                screen.blit(backgroundImage, (0, 0))
                game_run = False
                # vanishing enemy after collision
                enemyY_change = 0
                enemyX_change = 0
                enemyY = -1000
                # vanishing player after collision
                headY = 1000
                head_changeX = 0
                head_changeY = 0
                # vanishing fruit
                fruit = False
                game_over()

            # moving snake
            headX += head_changeX
            headY += head_changeY

            # Moving Enemy
            enemyX += enemyX_change
            if enemyX > 770:
                enemyX_change = -.4
                enemyY += enemyY_change
            if enemyX < 1:
                enemyX_change = .4
                enemyY += enemyY_change
            if enemyY > 590:
                enemyY = random.randint(0, 250)
                enemyX_change += 0.05
            score_show()
            show_block(headX, headY)
            enemy(enemyX, enemyY)
            pygame.display.update()

        pygame.display.update()


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