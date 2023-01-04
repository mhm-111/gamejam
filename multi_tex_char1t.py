import pygame
pygame.init()
font = pygame.font.Font('osthir_font.ttf',24)
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

snip = font.render('',True, 'white')
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
    pygame.draw.rect(screen, 'black', [0,550,1275,150])
    if counter < speed*len(message):
        counter += 1
    elif counter >= speed*len(message):
        done = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and done and active_message < len(messages)-1:
                active_message +=1 ;
                if (active_message%2==0):
                    char1_var = "character/left2.png"
                else:
                    char1_var = "character/front2.png"
                done = False
                message = messages[active_message]
                counter = 0

    snip = font.render(message[0:counter//speed], True, 'white')
    screen.blit(snip, (10, 580))
    pygame.display.flip()
pygame.quit()