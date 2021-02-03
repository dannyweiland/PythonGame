import pygame

#Initialize the game
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800, 800))

#Create background
background = pygame.image.load("intbuilding7a.png")

#Title and Icon
pygame.display.set_caption("Danny's Video Game")
icon = pygame.image.load('dog.png')
pygame.display.set_icon(icon)

#Game Function
running = True
while running:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

    #RGB Values for screen background
    screen.fill((0, 150, 0))
    pygame.display.update()


