from player import Player
import pygame

class Game:
    # configs
    gameSpeed = 2

    # colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)

    def __init__(self, screenWidth = 800, screenHeight = 600) -> None:
        # Game init
        pygame.init()

        # set screen
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))

        # Change title and logo
        icon = pygame.image.load('assets/astronaut.png')
        pygame.display.set_caption("Space Invaders")
        pygame.display.set_icon(icon)

    def drawPlayer(self, player: Player):
        playerIcon = pygame.image.load('assets/spaceship.png')

        self.screen.blit(playerIcon, (player.positionX, player.positionY))

    def setScore(self, points):
        font = pygame.font.Font('assets/Eight-Bit Madness.ttf', 22)
        text = font.render(f"Score: {str(points)}", 1, self.white)
        position = text.get_rect(center=(self.screen.get_width() - 85, 15))
        self.screen.blit(text, position)


    def paintBackground(self):
        # paint the screen
        self.screen.fill(self.black)

    def refreshScreen(self):
        # Update the display
        pygame.display.update()
