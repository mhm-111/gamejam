import pygame
pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('pygame button1')


font = pygame.font.Font('Georgia',40)
stat1 = "OFF"
v1 = 0
stat2 = "ON"
v2 = 1
stat3 = "ON"
v3 = 1
stat4 = "OFF"
v4 = 0

button1 = pygame.Rect(10, 200, 110, 60)
button2 = pygame.Rect(200, 200, 110, 60)
button3 = pygame.Rect(400, 200, 110, 60)
button4 = pygame.Rect(550, 200, 110, 60)



while True:
    win_bg = pygame.image.load("assets/Background.png")
    win_message = font.render("You won!", 480, 500)
    screen.fill('pink')
    if v1 == 1 and v2 == 1 and v3 == 1 and v4 == 1:
        screen.blit(win_bg, (0,0 ))
        screen.blit(win_message, (250, 460))
        pygame.display.update()
    for events in pygame.event.get():
        surf1 = font.render(stat1, True, 'white')
        surf2 = font.render(stat2, True, 'white')
        surf3 = font.render(stat3, True, 'white')
        surf4 = font.render(stat4, True, 'white')
        win_message = font.render("You Won !!", True, 'white')

        if events.type == pygame.QUIT:
            pygame.quit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(events.pos) and v1 == 0 :
                stat1 = 'ON'
                v1 = 1
                pygame.display.update()
            elif button1.collidepoint(events.pos) and v1 == 1 :
                stat1 = 'OFF'
                v1 = 0
                pygame.display.update()
            elif button2.collidepoint(events.pos) and v2 == 0 :
                stat2 = 'ON'
                v2 = 1
                pygame.display.update()
            elif button2.collidepoint(events.pos) and v2 == 1 :
                stat2 = 'OFF'
                v2 = 0
                pygame.display.update()

            elif button3.collidepoint(events.pos) and v3 == 0 :
                stat3 = 'ON'
                v3 = 1
                pygame.display.update()
            elif button3.collidepoint(events.pos) and v3 == 1 :
                stat3 = 'OFF'
                v3 = 0
                pygame.display.update()

            elif button4.collidepoint(events.pos) and v4 == 0 :
                stat4 = 'ON'
                v4 = 1
                pygame.display.update()
            elif button4.collidepoint(events.pos) and v4 == 1 :
                stat4 = 'OFF'
                v4 = 0
                pygame.display.update()



    pygame.draw.rect(screen, (110,110,110), button1)
    pygame.draw.rect(screen, (110,110,110), button2)
    pygame.draw.rect(screen, (110,110,110), button3)
    pygame.draw.rect(screen, (110,110,110), button4)
    screen.blit(surf1, (button1.x + 5, button1.y + 5))
    screen.blit(surf2, (button2.x + 5, button2.y + 5))
    screen.blit(surf3, (button3.x + 5, button3.y + 5))
    screen.blit(surf4, (button4.x + 5, button4.y + 5))
    pygame.display.update()