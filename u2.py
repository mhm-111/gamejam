import pygame.display


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
        screen = pygame.display.set_mode((790,450))

        # creating player
        head = pygame.image.load("newmedia/char1.png")
        headX = 400
        headY = 300
        head_changeX = 0
        head_changeY = 0

        # player
        def show_block(x, y):
            screen.blit(head, (x, y))

         # Back ground Image
        backgroundImage_always = pygame.image.load("newmedia/bg2.jpg")

        game_run = True

        while running:
            if game_run:
                # screen.fill((0, 150, 150))
                screen.blit(backgroundImage_always, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            show_block(headX, headY)
            pygame.display.update()
        pygame.display.update()