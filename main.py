import pygame
from collections import namedtuple

# Coordinates
Coordinate = namedtuple('Coordinate', ['x', 'y'])

# Game init
pygame.init()

# configs
gameSpeed = 2
## create screen
# screenSize = Coordinate(x=1690, y=1470)
screenSize = Coordinate(x=800, y=600)
screen = pygame.display.set_mode(screenSize)

# colors
Color = namedtuple('Color', ['r', 'g', 'b'])
black = Color(r=0, g=0, b=0)
white = Color(r=255, g=255, b=255)
red = Color(r=255, g=0, b=0)

# Change title and logo
icon = pygame.image.load('assets/astronaut.png')
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(icon)

# Player
playerIcon = pygame.image.load('assets/spaceship.png')
pygame.display.set_icon(icon)
playerPositionX = (screen.get_width() // 2) - 32
playerPositionY = (screen.get_height()) - 132
playerPositionChangeX = 0
playerPositionChangeY = 0

def player(x, y):
    screen.blit(playerIcon, (x, y))

def setScore(points):
    font = pygame.font.Font('assets/Eight-Bit Madness.ttf', 22)
    text = font.render(f"Score: {str(points)}", 1, white)
    position = text.get_rect(center=(screen.get_width() - 85, 15))
    screen.blit(text, position)

def checkBoundaries(axis, position):
    if axis != 'x' or axis != 'y':
        return
    pygame.display.update()
    if axis == 'x':
        return position > 5 and position < screen.get_width()
    if axis == 'y':
        return position > 35 and position < screen.get_height()

# Game loop
running = True
while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerPositionChangeX = -gameSpeed

            if event.key == pygame.K_RIGHT:
                playerPositionChangeX = gameSpeed

            if event.key == pygame.K_UP:
                playerPositionChangeY = -gameSpeed

            if event.key == pygame.K_DOWN:
                playerPositionChangeY = gameSpeed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerPositionChangeX = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerPositionChangeY = 0

    # paint the screen
    screen.fill(black)

    # Draw the player
    playerPositionX += playerPositionChangeX
    playerPositionY += playerPositionChangeY

    if playerPositionX <= 0:
        playerPositionX = 0
    elif playerPositionX >= screen.get_width() - 64:
        playerPositionX = screen.get_width() - 64

    if playerPositionY <= 25:
        playerPositionY = 25
    elif playerPositionY >= screen.get_height() - 64:
        playerPositionY = screen.get_height() - 64

    player(playerPositionX, playerPositionY)

    # Draw the score
    setScore('00000000')

    # Update the display
    pygame.display.update()
