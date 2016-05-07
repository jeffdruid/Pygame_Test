import pygame
import random

pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("soundtrack.wav")


display_width = 800
display_height = 600

black = (0,0,0)
white = (216,191,216)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)


block_color = (53,115,255)


car_width = 75

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("race game by jeffcake")

clock = pygame.time.Clock()

carImg = pygame.image.load("car.png")
gameIcon = pygame.image.load("icon.png")
pygame.display.set_icon(gameIcon)

pause = False

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car (x, y):
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    largeText = pygame.font.Font("freesansbold.ttf", 75)
    Textsurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width / 2, display_height / 2))
    gameDisplay.blit(Textsurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Again!", 275, 400, 100, 50, green, bright_green, game_loop)
        button("Quit", 425, 400, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
  #  print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0]== 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textsSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textsSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused():

    pygame.mixer.music.pause()

    largeText = pygame.font.Font("freesansbold.ttf", 75)
    Textsurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2, display_height / 2))
    gameDisplay.blit(Textsurf, TextRect)



    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        button("Continue!", 275, 400, 100, 50, green, bright_green, unpause)
        button("Quit", 425, 400, 100, 50, red, bright_red, quitgame)



        pygame.display.update()
        clock.tick(15)


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf", 75)
        Textsurf, TextRect = text_objects("Jeffy Race Game", largeText)
        TextRect.center = ((display_width / 2, display_height / 2))
        gameDisplay.blit(Textsurf, TextRect)

        button("GO!", 275, 400, 100, 50, green, bright_green, game_loop)
        button("EXIT", 425, 400, 100, 50, red, bright_red, quitgame)



        pygame.display.update()
        clock.tick(15)



def game_loop():
    global pause

    pygame.mixer.music.play(-1)


    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -400
    thing_speed = 7
    thing_width = 75
    thing_height = 75

    dodged = 0

    gameExit = False


    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change =0


        x += x_change

        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        car(x, y)

        things_dodged(dodged)


        if x > display_width - car_width or x < 0:
           crash()


        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 0.25
            thing_width = random.randrange(80, 100)
            thing_height = random.randrange(80, 100)

        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or  x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                crash()




        pygame.display.update()
        clock.tick(60)

    print(event)


game_intro()
game_loop()
pygame.quit()
quit()
