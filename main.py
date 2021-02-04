import pygame

# Initialize the game
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 800))

# Create background
background = pygame.image.load("intbuilding7a.png")

# Title and Icon
pygame.display.set_caption("Danny's Video Game")
icon = pygame.image.load('dog.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))

# Game Loop
running = True
while running:

    # RGB Values for screen background
    screen.fill((64, 35, 82))


    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

    # Add Player Icon
    player()
    pygame.display.update()


