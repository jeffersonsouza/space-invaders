from game import Game
from player import Player
import pygame

# Game
game = Game()

# Player
player = Player((game.screen.get_width() // 2) - 32, (game.screen.get_height()) - 132)

# Game loop
running = True
while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.positionChangeX = -game.gameSpeed

            if event.key == pygame.K_RIGHT:
                player.positionChangeX = game.gameSpeed

            if event.key == pygame.K_UP:
                player.positionChangeY = -game.gameSpeed

            if event.key == pygame.K_DOWN:
                player.positionChangeY = game.gameSpeed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.positionChangeX = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.positionChangeY = 0

    # paint the screen
    game.paintBackground()

    # Draw the player
    player.positionX += player.positionChangeX
    player.positionY += player.positionChangeY

    if player.positionX <= 0:
        player.positionX = 0
    elif player.positionX >= game.screen.get_width() - 64:
        player.positionX = game.screen.get_width() - 64

    if player.positionY <= 25:
        player.positionY = 25
    elif player.positionY >= game.screen.get_height() - 64:
        player.positionY = game.screen.get_height() - 64

    game.drawPlayer(player)

    # Draw the score
    game.setScore('00000000')

    # Update the display
    game.refreshScreen()
